# AKD2G — Python Quick Start

## Requirements

```bash
uv sync
```

---

## Boilerplate — Connect to Both Axes

```python
from pymodbus.client import ModbusTcpClient

DRIVE_IP = "169.254.78.209"
PORT     = 502
AXIS1    = 1   # Slave ID for Axis 1
AXIS2    = 2   # Slave ID for Axis 2

client = ModbusTcpClient(DRIVE_IP, port=PORT)
client.connect()
```

---

## Read Status Word

```python
def read_status(client, slave_id):
    result = client.read_holding_registers(address=0x6041, count=1, slave=slave_id)
    return result.registers[0] if not result.isError() else None

print(hex(read_status(client, AXIS1)))  # e.g. 0x0027 = enabled
print(hex(read_status(client, AXIS2)))
```

---

## Enable an Axis (CiA 402 State Machine)

```python
import time

def enable_axis(client, slave_id):
    client.write_register(0x6040, 0x0006, slave=slave_id)  # Shutdown
    time.sleep(0.3)
    client.write_register(0x6040, 0x0007, slave=slave_id)  # Switch On
    time.sleep(0.3)
    client.write_register(0x6040, 0x000F, slave=slave_id)  # Enable Operation
    time.sleep(0.3)

enable_axis(client, AXIS1)
enable_axis(client, AXIS2)
```

---

## Disable an Axis Safely

```python
def disable_axis(client, slave_id):
    client.write_register(0x6040, 0x0000, slave=slave_id)
    time.sleep(0.2)
```

---

## Reset a Fault

```python
def reset_fault(client, slave_id):
    client.write_register(0x6040, 0x0080, slave=slave_id)
    time.sleep(0.3)
    # Then re-run the enable sequence
```

---

## Set Velocity Mode and Command a Speed

```python
# Set mode to Profile Velocity (mode 3)
client.write_register(0x6060, 3, slave=AXIS1)
time.sleep(0.1)

# Set target velocity (units = counts/sec — check Workbench for scaling)
client.write_register(0x60FF, 1000, slave=AXIS1)  # example: 1000 counts/sec
```

---

## Set Position Mode and Move to Target

```python
# Set mode to Profile Position (mode 1)
client.write_register(0x6060, 1, slave=AXIS1)
time.sleep(0.1)

# Set target position (32-bit value split across 2 registers)
target_pos = 5000
client.write_registers(0x607A, [target_pos & 0xFFFF, (target_pos >> 16) & 0xFFFF], slave=AXIS1)

# Trigger move: set bit 4 of control word
client.write_register(0x6040, 0x001F, slave=AXIS1)
```

---

## Read Actual Position (32-bit)

```python
def read_position(client, slave_id):
    result = client.read_holding_registers(address=0x6064, count=2, slave=slave_id)
    if result.isError():
        return None
    low, high = result.registers
    return (high << 16) | low

print(read_position(client, AXIS1))
print(read_position(client, AXIS2))
```

---

## Always Close Cleanly

```python
disable_axis(client, AXIS1)
disable_axis(client, AXIS2)
client.close()
```

---

## Current Scripts

| File                    | What it does                              |
|-------------------------|-------------------------------------------|
| `connect_and_enable.py` | Connects, reads status, enables both axes |

---

## Status Word Cheat Sheet

| Hex value | Meaning              |
|-----------|----------------------|
| `0x0027`  | Enabled ✓            |
| `0x0037`  | Enabled ✓            |
| `0x0021`  | Switched on          |
| `0x0240`  | Fault — check Workbench |
