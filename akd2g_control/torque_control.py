"""
AKD2G Velocity Control
-----------------------
W / S        : Axis 1 forward / reverse
Up / Down    : Axis 2 forward / reverse
Q            : stop, disable, quit

OPMODE = 1 (velocity). VL.CMDU written directly at 20 Hz.
Modbus float scaling: Modbus value = RPM × 1000.
No SM.MOVE — that runs the Workbench-programmed service motion, not our command.

Register map (0-based addr = Modbus addr - 40001):
  Axis 1: en=0  dis=1  active=4  dissrc=8  opmode=69  vl_cmd=73 (32-bit, 2 regs)
  Axis 2: en=62 dis=63 active=54 dissrc=58 opmode=71  vl_cmd=75 (32-bit, 2 regs)

Usage: uv run python torque_control.py
"""

import time
from pynput import keyboard
from pymodbus.client import ModbusTcpClient

DRIVE_IP = "169.254.78.209"
PORT     = 502
SLAVE_ID = 1

VELOCITY = 10.0   # RPM — raise once motion confirmed
VEL_MODE = 1

AXES = {
    "Axis 1": {"en": 0,  "dis": 1,  "active": 4,  "dissources": 8,  "opmode": 69, "vl_cmd": 73},
    "Axis 2": {"en": 62, "dis": 63, "active": 54, "dissources": 58, "opmode": 71, "vl_cmd": 75},
}

KEY_MAP = {
    "w":               ("Axis 1", +VELOCITY),
    "s":               ("Axis 1", -VELOCITY),
    keyboard.Key.up:   ("Axis 2", +VELOCITY),
    keyboard.Key.down: ("Axis 2", -VELOCITY),
}

commands = {"Axis 1": 0.0, "Axis 2": 0.0}
running  = True


def read32(client, address):
    r = client.read_holding_registers(address=address, count=2, device_id=SLAVE_ID)
    if r.isError():
        return None
    return (r.registers[0] << 16) | r.registers[1]


def write_cmd(client, address, rpm):
    """RPM × 1000 as signed 32-bit integer, big-endian word order."""
    raw = int(rpm * 1000) & 0xFFFFFFFF
    r = client.write_registers(address=address, values=[(raw >> 16) & 0xFFFF, raw & 0xFFFF], device_id=SLAVE_ID)
    if r.isError():
        print(f"  [vl_cmd error @ {address}] {r}")


def trigger(client, address):
    client.write_register(address=address, value=0, device_id=SLAVE_ID)
    time.sleep(0.05)
    client.write_register(address=address, value=1, device_id=SLAVE_ID)


def enable_axes(client):
    for name, regs in AXES.items():
        client.write_register(address=regs["opmode"], value=VEL_MODE, device_id=SLAVE_ID)
        time.sleep(0.05)
        trigger(client, regs["en"])
        time.sleep(0.3)
        active = read32(client, regs["active"])
        print(f"  {name}: {'enabled' if active == 1 else f'NOT enabled (active={active})'}")


def stop_and_disable(client):
    for regs in AXES.values():
        write_cmd(client, regs["vl_cmd"], 0.0)
    time.sleep(0.1)
    for name, regs in AXES.items():
        trigger(client, regs["dis"])


def resolve_key(key):
    try:
        return KEY_MAP.get(key.char)
    except AttributeError:
        return KEY_MAP.get(key)


def on_press(key):
    global running
    if hasattr(key, "char") and key.char == "q":
        running = False
        return False
    entry = resolve_key(key)
    if entry:
        axis, vel = entry
        commands[axis] = vel
        print(f"[key] {axis} -> {vel:+.0f} RPM")


def on_release(key):
    entry = resolve_key(key)
    if entry:
        axis, _ = entry
        commands[axis] = 0.0


def main():
    global running
    print(f"Connecting to AKD2G at {DRIVE_IP}:{PORT} ...")
    client = ModbusTcpClient(DRIVE_IP, port=PORT)
    if not client.connect():
        print("Connection failed.")
        return

    print("Enabling axes (velocity mode, OPMODE=1)...")
    enable_axes(client)
    print(f"\nReady.  W/S=Axis1  Up/Down=Axis2  Q=quit  (±{VELOCITY:.0f} RPM)\n")

    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()

    try:
        while running:
            for name, regs in AXES.items():
                write_cmd(client, regs["vl_cmd"], commands[name])
            time.sleep(0.05)
    finally:
        print("\nStopping...")
        stop_and_disable(client)
        listener.stop()
        client.close()
        print("Done.")


if __name__ == "__main__":
    main()
