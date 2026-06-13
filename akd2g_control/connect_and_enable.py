"""
AKD2G Dual-Axis Drive - Connect, Enable & Status
-------------------------------------------------
Uses the Kollmorgen MODBUS.MAP parameter interface.
All registers are on Slave ID 1 (global map).
Axes are differentiated by register address, not slave ID.

Mode note:
    0x6060 = Modes of Operation
    1 = Profile Position
    3 = Profile Velocity
    4 = Torque

Register map (0-based pymodbus addr = Modbus register - 40001):
  Axis 1:
    40001 (addr  0) AXIS1.EN        ActionCommand — write 1 to enable
    40002 (addr  1) AXIS1.DIS       ActionCommand — write 1 to disable
    40005 (addr  4) AXIS1.ACTIVE    32-bit, 1 = enabled
    40007 (addr  6) AXIS1.MOTIONSTAT  32-bit status
    40011 (addr 10) AXIS1.FAULTED   32-bit, non-zero = fault
  Axis 2:
    40063 (addr 62) AXIS2.EN        ActionCommand — write 1 to enable
    40064 (addr 63) AXIS2.DIS       ActionCommand — write 1 to disable
    40055 (addr 54) AXIS2.ACTIVE    32-bit, 1 = enabled
    40057 (addr 56) AXIS2.MOTIONSTAT  32-bit status
    40061 (addr 60) AXIS2.FAULTED   32-bit, non-zero = fault

Requirements: uv sync
Usage:        uv run python connect_and_enable.py
"""

from pymodbus import ModbusTcpClient
import time

DRIVE_IP = "169.254.78.209"
PORT     = 502
SLAVE_ID = 1  # Global MODBUS.MAP — slave ID 1 for all access

AXES = {
    "Axis 1": {"en": 0,  "dis": 1,  "active": 4,  "motion": 6,  "faulted": 10, "dissources": 8},
    "Axis 2": {"en": 62, "dis": 63, "active": 54, "motion": 56, "faulted": 60, "dissources": 58},
}


def read32(client, address):
    r = client.read_holding_registers(address=address, count=2, device_id=SLAVE_ID)
    if r.isError():
        print(f"  [read error @ {address}] {r}")
        return None
    return (r.registers[0] << 16) | r.registers[1]


DISSOURCES_BITS = {
    0: "HW Enable input low",
    1: "Drive fault",
    2: "STO active",
    3: "Under-voltage",
    4: "Over-voltage",
    5: "Over-temperature",
    7: "Motor feedback error",
    9: "Software disabled",
    11: "Axis not homed",
}

EXPECTED_DISSOURCE_BITS = {9}


def dissources_reasons(dissources):
    return [desc for bit, desc in DISSOURCES_BITS.items() if dissources & (1 << bit)]


def blocking_dissources(dissources):
    return [desc for bit, desc in DISSOURCES_BITS.items() if bit not in EXPECTED_DISSOURCE_BITS and dissources & (1 << bit)]

def print_status(client, regs):
    active     = read32(client, regs["active"])
    faulted    = read32(client, regs["faulted"])
    motion     = read32(client, regs["motion"])
    dissources = read32(client, regs["dissources"])
    print(f"  Active:     {active}")
    print(f"  Faulted:    {faulted}")
    if motion is not None:
        print(f"  MotionStat: 0x{motion:08X}")
    if dissources is not None and dissources != 0:
        bits = dissources_reasons(dissources)
        print(f"  DisSources: 0x{dissources:08X} -> {', '.join(bits) if bits else 'unknown bits'}")


def can_enable_axis(client, name, regs):
    dissources = read32(client, regs["dissources"])
    faulted = read32(client, regs["faulted"])

    if faulted not in (None, 0):
        print(f"  Skipping {name}: faulted is non-zero ({faulted}). Clear the fault first.")
        return False

    if dissources is None:
        print(f"  Skipping {name}: unable to read disable sources.")
        return False

    reasons = blocking_dissources(dissources)
    if reasons:
        print(f"  Skipping {name}: blocking disable sources active -> {', '.join(reasons)}")
        return False

    return True


def trigger(client, address):
    """Trigger an ActionCommand: write 0 then 1 to guarantee rising edge."""
    r = client.write_register(address=address, value=0, device_id=SLAVE_ID)
    if r.isError(): print(f"  [write error @ {address}] {r}")
    time.sleep(0.1)
    r = client.write_register(address=address, value=1, device_id=SLAVE_ID)
    if r.isError(): print(f"  [write error @ {address}] {r}")


def enable_axis(client, name, regs):
    print(f"\n--- Enabling {name} ---")
    if not can_enable_axis(client, name, regs):
        print_status(client, regs)
        return
    trigger(client, regs["en"])
    time.sleep(0.5)
    print_status(client, regs)


def main():
    print(f"Connecting to AKD2G at {DRIVE_IP}:{PORT} ...")
    client = ModbusTcpClient(DRIVE_IP, port=PORT)

    if not client.connect():
        print("Connection failed. Check IP, subnet, and Modbus TCP setting in Workbench.")
        return
    
    print("Connected!\n")

    print("Suck it!")
    time.sleep(1)



    print("=== Initial Status ===")
    for name, regs in AXES.items():
        print(f"\n{name}:")
        print_status(client, regs)

    print("\n=== Enabling Both Axes ===")
    for name, regs in AXES.items():
        enable_axis(client, name, regs)

    client.close()
    print("\nDone.")


if __name__ == "__main__":
    main()
