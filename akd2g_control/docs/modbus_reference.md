# AKD2G — Modbus TCP Reference

## Connection Details

| Parameter | Value |
|-----------|-------|
| Drive IP | `169.254.78.209` |
| Port | `502` |
| Protocol | Modbus TCP |
| Physical port on drive | X20 (Service/HM) |
| Axis 1 Slave ID | `1` |
| Axis 2 Slave ID | `2` |

---

## How Modbus Works on the AKD2G

- Uses **holding registers** (16-bit each) — coils and discrete inputs are NOT supported
- 32-bit values (position, velocity) span **two consecutive 16-bit registers** — always read `count=2`
- Each axis is a separate Modbus slave on the same TCP connection
- Register addresses follow the **CiA 402** (CANopen device profile for drives) object dictionary
- Workbench has a built-in **Modbus View** screen showing all parameter addresses — use it to look up any parameter's register address

---

## CiA 402 State Machine

The drive must follow this sequence before motion is possible:

```
Power On
   │
   ▼
Not Ready to Switch On  (automatic)
   │
   ▼
Switch On Disabled  (0x0040)
   │  Control Word = 0x0006 (Shutdown)
   ▼
Ready to Switch On  (0x0021)
   │  Control Word = 0x0007 (Switch On)
   ▼
Switched On  (0x0023)
   │  Control Word = 0x000F (Enable Operation)
   ▼
Operation Enabled  (0x0027 / 0x0037)  ← Motors can move here
```

To go back to safe state: Control Word = `0x0000` (Disable Voltage)
To quick-stop: Control Word = `0x0002`
To clear a fault: Control Word = `0x0080`, then re-run enable sequence

---

## Core Registers

### Control & Status

| Register | Name | R/W | Description |
|----------|------|-----|-------------|
| `0x6040` | Control Word | W | Drive state machine commands |
| `0x6041` | Status Word | R | Current drive state |
| `0x6060` | Modes of Operation | W | Set motion mode |
| `0x6061` | Modes of Operation Display | R | Confirm active mode |
| `0x605A` | Quick Stop Option Code | R/W | Behavior on quick stop |
| `0x605B` | Shutdown Option Code | R/W | Behavior on shutdown |

---

### Control Word (0x6040) Command Values

| Value | Command | When to Use |
|-------|---------|-------------|
| `0x0006` | Shutdown | Step 1 of enable sequence |
| `0x0007` | Switch On | Step 2 of enable sequence |
| `0x000F` | Enable Operation | Step 3 — drive is active |
| `0x001F` | Enable + New Setpoint | Trigger a new position move |
| `0x0000` | Disable Voltage | Safe power-down |
| `0x0002` | Quick Stop | Emergency stop |
| `0x0080` | Fault Reset | Clear a fault (fix cause first) |

---

### Status Word (0x6041) Interpretation

| Value | State | Meaning |
|-------|-------|---------|
| `0x0027` | Operation Enabled | ✅ Ready for motion |
| `0x0037` | Operation Enabled | ✅ Ready for motion |
| `0x0021` | Ready to Switch On | Enable sequence step 1 done |
| `0x0023` | Switched On | Enable sequence step 2 done |
| `0x0040` | Switch On Disabled | Drive not yet in enable sequence |
| `0x0240` | Fault | ❌ Check Workbench for fault code |
| `0x0250` | Fault | ❌ Check Workbench for fault code |

**Bit checks:**
- Bit 3 set (`status & 0x0008`): **Fault present**
- Bit 2 set (`status & 0x0004`): **Operation enabled**
- Bit 1 set (`status & 0x0002`): **Switched on**
- Bit 0 set (`status & 0x0001`): **Ready to switch on**

---

### Motion Modes (0x6060)

| Value | Mode | Use Case |
|-------|------|----------|
| `1` | Profile Position | Move to absolute or relative target position |
| `3` | Profile Velocity | Run at a set speed continuously |
| `4` | Torque | Apply a set torque/current |
| `6` | Homing | Run homing sequence |

---

## Velocity Mode Registers (Mode = 3)

| Register | Name | R/W | Notes |
|----------|------|-----|-------|
| `0x60FF` | Target Velocity | W | 32-bit — use 2 registers |
| `0x606C` | Actual Velocity | R | 32-bit — use 2 registers |
| `0x6083` | Profile Acceleration | W | Ramp-up rate |
| `0x6084` | Profile Deceleration | W | Ramp-down rate |

---

## Position Mode Registers (Mode = 1)

| Register | Name | R/W | Notes |
|----------|------|-----|-------|
| `0x607A` | Target Position | W | 32-bit — use 2 registers |
| `0x6064` | Actual Position | R | 32-bit — use 2 registers |
| `0x6081` | Profile Velocity | W | Max speed during move |
| `0x6083` | Profile Acceleration | W | Ramp-up rate |
| `0x6084` | Profile Deceleration | W | Ramp-down rate |
| `0x607D` | Software Position Limits | R/W | Min/max position limits |

To trigger a new position move, set bit 4 of the control word:
```python
client.write_register(0x6040, 0x001F, slave=slave_id)  # new setpoint
```

---

## Torque Mode Registers (Mode = 4)

| Register | Name | R/W | Notes |
|----------|------|-----|-------|
| `0x6071` | Target Torque | W | In units of 0.1% of rated torque |
| `0x6077` | Actual Torque | R | Current measured torque |
| `0x6072` | Max Torque | W | Torque limit |

---

## Homing Registers (Mode = 6)

| Register | Name | R/W | Notes |
|----------|------|-----|-------|
| `0x6098` | Homing Method | W | Method 1–35 (see manual) |
| `0x6099` | Homing Speeds | W | Speed during/after switch |
| `0x609A` | Homing Acceleration | W | Acceleration during homing |

To start homing: write `0x001F` to control word while in mode 6.

---

## AKD2G Special Modbus Parameters

Kollmorgen added drive-specific parameters accessible over Modbus for convenience. These go beyond the CiA 402 standard registers:

| Parameter Name | Description |
|----------------|-------------|
| `MODBUS.DRV` | Drive-level control shortcuts |
| `MODBUS.DRVSTAT` | Drive status summary register |
| `MODBUS.MOTOR` | Motor parameter shortcuts |
| `MODBUS.HOME` | Homing control shortcuts |
| `MODBUS.MT` | Motion tasking shortcuts |
| `MODBUS.DIO` | Digital I/O control |
| `MODBUS.DATA` | Generic parameter read/write by parameter ID |
| `MODBUS.MAP` | Read the parameter-to-register mapping table |
| `MODBUS.LIST` | List all mapped Modbus registers |

> To find the register address of any Workbench parameter: in Workbench go to **Drive → Modbus View** and search for the parameter name. The address shown is the Modbus holding register offset.

---

## Reading 32-bit Values

Position and velocity registers are 32-bit values split across two consecutive 16-bit registers:

```python
def read_32bit(client, address, slave_id):
    result = client.read_holding_registers(address=address, count=2, slave=slave_id)
    if result.isError():
        return None
    low, high = result.registers
    value = (high << 16) | low
    # Handle signed values
    if value >= 0x80000000:
        value -= 0x100000000
    return value
```

---

## Writing 32-bit Values

```python
def write_32bit(client, address, value, slave_id):
    low  = value & 0xFFFF
    high = (value >> 16) & 0xFFFF
    client.write_registers(address=address, values=[low, high], slave=slave_id)
```

---

## Supported Modbus Function Codes

| Code | Name | Support |
|------|------|---------|
| `0x03` | Read Holding Registers | ✅ |
| `0x06` | Write Single Register | ✅ (firmware ≥ 02-05-02-000) |
| `0x10` | Write Multiple Registers | ✅ |
| `0x01` | Read Coils | ❌ Not supported |
| `0x02` | Read Discrete Inputs | ❌ Not supported |

---

## Finding Register Addresses for Any Parameter

1. Open **Workbench**
2. Navigate to **Drive → Modbus View**
3. Search or scroll for the parameter (e.g., `PL.FB`, `VL.CMD`)
4. The **Address** column shows the Modbus holding register number
5. Use that address directly in Python

Alternatively, use the `MODBUS.LIST` terminal command in Workbench to dump the full mapping.
