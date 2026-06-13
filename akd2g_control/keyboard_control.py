"""
AKD2G Keyboard Control
-----------------------
W / S        : Axis 1 forward / reverse  (100 RPM)
Up / Down    : Axis 2 forward / reverse  (100 RPM)
Q            : stop both axes, disable, quit

Requirements: uv sync
Usage:        uv run python keyboard_control.py
"""

import struct
import time
from pynput import keyboard
from pymodbus.client import ModbusTcpClient

DRIVE_IP  = "169.254.78.209"
PORT      = 502
SLAVE_ID  = 1
SPEED_RPM = 100.0

AXES = {
    "Axis 1": {"en": 0,  "dis": 1,  "active": 4,  "faulted": 10, "vl_cmd": 64},
    "Axis 2": {"en": 62, "dis": 63, "active": 54, "faulted": 60, "vl_cmd": 66},
}

KEY_MAP = {
    "w":               ("Axis 1", +SPEED_RPM),
    "s":               ("Axis 1", -SPEED_RPM),
    keyboard.Key.up:   ("Axis 2", +SPEED_RPM),
    keyboard.Key.down: ("Axis 2", -SPEED_RPM),
}

velocities = {"Axis 1": 0.0, "Axis 2": 0.0}
running    = True


def write_float32(client, address, value):
    packed = struct.pack(">f", float(value))
    hi = (packed[0] << 8) | packed[1]
    lo = (packed[2] << 8) | packed[3]
    client.write_registers(address=address, values=[hi, lo], device_id=SLAVE_ID)


def read32(client, address):
    r = client.read_holding_registers(address=address, count=2, device_id=SLAVE_ID)
    if r.isError():
        return None
    return (r.registers[0] << 16) | r.registers[1]


def trigger(client, address):
    client.write_register(address=address, value=0, device_id=SLAVE_ID)
    time.sleep(0.05)
    client.write_register(address=address, value=1, device_id=SLAVE_ID)


def enable_axes(client):
    for name, regs in AXES.items():
        trigger(client, regs["en"])
        time.sleep(0.3)
        active = read32(client, regs["active"])
        print(f"  {name}: {'enabled' if active == 1 else f'NOT enabled (active={active})'}")


def stop_and_disable(client):
    for regs in AXES.values():
        write_float32(client, regs["vl_cmd"], 0.0)
    time.sleep(0.1)
    for regs in AXES.values():
        trigger(client, regs["dis"])


def resolve_key(key):
    try:
        return KEY_MAP.get(key.char)
    except AttributeError:
        return KEY_MAP.get(key)


def on_press(key):
    global running
    print(f"[key] {key}")  # debug — remove once working
    if hasattr(key, "char") and key.char == "q":
        running = False
        return False
    entry = resolve_key(key)
    if entry:
        axis, vel = entry
        velocities[axis] = vel


def on_release(key):
    entry = resolve_key(key)
    if entry:
        axis, _ = entry
        velocities[axis] = 0.0


def main():
    global running
    print(f"Connecting to AKD2G at {DRIVE_IP}:{PORT} ...")
    client = ModbusTcpClient(DRIVE_IP, port=PORT)
    if not client.connect():
        print("Connection failed.")
        return

    print("Enabling axes...")
    enable_axes(client)
    print("\nReady.  W/S=Axis1  Up/Down=Axis2  Q=quit\n")

    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()

    while running:
        for name, regs in AXES.items():
            write_float32(client, regs["vl_cmd"], velocities[name])
        time.sleep(0.05)  # 20 Hz

    print("\nStopping...")
    stop_and_disable(client)
    listener.stop()
    client.close()
    print("Done.")


if __name__ == "__main__":
    main()
