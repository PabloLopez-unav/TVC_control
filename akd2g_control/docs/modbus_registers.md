# AKD2G — Modbus TCP Reference

## Connection

| Setting | Value |
|---------|-------|
| IP | 169.254.78.209 |
| Port | 502 |
| Slave ID | 1 (global map — all access via slave ID 1) |
| Library | pymodbus 3.13.0 |

> **Note:** pymodbus 3.13 renamed `slave=` to `device_id=` in all read/write calls.

---

## How Addressing Works

The AKD2G uses a **dynamic MODBUS.MAP** system — there are no fixed CiA 402 addresses.
Parameters are mapped to Modbus registers in Workbench Terminal using:

```
MODBUS.MAP 40001 AXIS1.EN
MODBUS.MAP 40063 AXIS2.EN
...
DRV.NVWRITE        ← saves to flash (MODBUS.SAVE does not exist)
```

View current map: `MODBUS.MAP` (no args)  
List all mappable parameters: `MODBUS.LIST`

Pymodbus address = Modbus register number − 40001 (0-based).

---

## Current Register Map

### Axis 1

| pymodbus addr | Modbus reg | Parameter | Type | R/W | Description |
|---------------|------------|-----------|------|-----|-------------|
| 0 | 40001 | AXIS1.EN | ActionCommand 16-bit | W | Write 0 then 1 to enable |
| 1 | 40002 | AXIS1.DIS | ActionCommand 16-bit | W | Write 0 then 1 to disable |
| 2–3 | 40003–40004 | AXIS1.VL.FBFILTER | Float 32-bit | R | Velocity feedback (filtered) |
| 4–5 | 40005–40006 | AXIS1.ACTIVE | Unsigned 32-bit | R | 1 = axis enabled |
| 6–7 | 40007–40008 | AXIS1.MOTIONSTAT | Unsigned 32-bit | R | Motion status word |
| 8–9 | 40009–40010 | AXIS1.DISSOURCES | Unsigned 32-bit | R | Disable reason bits (see below) |
| 10–11 | 40011–40012 | AXIS1.FAULTED | Unsigned 32-bit | R | Non-zero = fault active |
| 20–21 | 40021–40022 | AXIS1.MOTIONCONTROL | Unsigned 32-bit | R/W | Motion control word |
| 22–23 | 40023–40024 | AXIS1.MT.MOVE#0 | Float 32-bit | R/W | Motion task: move distance |
| 24–25 | 40025–40026 | AXIS1.MT.ACC#0 | Float 32-bit | R/W | Motion task: acceleration |
| 26–27 | 40027–40028 | AXIS1.MT.DEC#0 | Float 32-bit | R/W | Motion task: deceleration |
| 28–29 | 40029–40030 | AXIS1.MT.V#0 | Float 32-bit | R/W | Motion task: velocity |
| 30–31 | 40031–40032 | AXIS1.MT.P#0 | Float 32-bit | R/W | Motion task: position target |
| 32–33 | 40033–40034 | AXIS1.MT.CNTL#0 | Unsigned 32-bit | R/W | Motion task: control flags |

### Axis 2

| pymodbus addr | Modbus reg | Parameter | Type | R/W | Description |
|---------------|------------|-----------|------|-----|-------------|
| 50–51 | 40051–40052 | AXIS2.PL.FB | Float 32-bit | R | Position feedback |
| 52–53 | 40053–40054 | AXIS2.VL.FBFILTER | Float 32-bit | R | Velocity feedback (filtered) |
| 54–55 | 40055–40056 | AXIS2.ACTIVE | Unsigned 32-bit | R | 1 = axis enabled |
| 56–57 | 40057–40058 | AXIS2.MOTIONSTAT | Unsigned 32-bit | R | Motion status word |
| 58–59 | 40059–40060 | AXIS2.DISSOURCES | Unsigned 32-bit | R | Disable reason bits (see below) |
| 60–61 | 40061–40062 | AXIS2.FAULTED | Unsigned 32-bit | R | Non-zero = fault active |
| 62 | 40063 | AXIS2.EN | ActionCommand 16-bit | W | Write 0 then 1 to enable |
| 63 | 40064 | AXIS2.DIS | ActionCommand 16-bit | W | Write 0 then 1 to disable |
| 70–71 | 40071–40072 | AXIS2.MOTIONCONTROL | Unsigned 32-bit | R/W | Motion control word |
| 72–73 | 40073–40074 | AXIS2.MT.MOVE#0 | Float 32-bit | R/W | Motion task: move distance |
| 74–75 | 40075–40076 | AXIS2.MT.ACC#0 | Float 32-bit | R/W | Motion task: acceleration |
| 76–77 | 40077–40078 | AXIS2.MT.DEC#0 | Float 32-bit | R/W | Motion task: deceleration |
| 78–79 | 40079–40080 | AXIS2.MT.V#0 | Float 32-bit | R/W | Motion task: velocity |
| 80–81 | 40081–40082 | AXIS2.MT.P#0 | Float 32-bit | R/W | Motion task: position target |
| 82–83 | 40083–40084 | AXIS2.MT.CNTL#0 | Unsigned 32-bit | R/W | Motion task: control flags |

---

## AXIS.DISSOURCES Bit Definitions

| Bit | Hex | Meaning |
|-----|-----|---------|
| 0 | 0x0001 | Hardware enable input low (X21-A5 needs 24V) |
| 1 | 0x0002 | Drive fault |
| 2 | 0x0004 | STO active (X21-A11, X21-B11 need 24V) |
| 3 | 0x0008 | Under-voltage |
| 4 | 0x0010 | Over-voltage |
| 5 | 0x0020 | Over-temperature |
| 7 | 0x0080 | Motor feedback error |
| 9 | 0x0200 | Software disabled (EN not commanded) |
| 11 | 0x0800 | Axis not homed |

DISSOURCESMASK = 2623 (0x0A3F) — bits enforced on this drive: 0,1,2,3,4,5,9,11.

---

## ActionCommand Enable Sequence

Action commands trigger on a **rising edge from 0**. Always write 0 first:

```python
client.write_register(address=0, value=0, device_id=1)  # reset
time.sleep(0.1)
client.write_register(address=0, value=1, device_id=1)  # trigger EN
```

---

## Hardware Wiring Required to Enable

| Connector pin | Signal | Purpose |
|---------------|--------|---------|
| X21-B3 | 24VDC | I/O supply |
| X21-B4 | 0VDC | I/O ground |
| X21-A5 | 24VDC | Hardware enable input (both axes) |
| X21-A11 | 24VDC | STO channel 1 |
| X21-B11 | 24VDC | STO channel 2 |

---

## 32-bit Register Reads

All 32-bit parameters span two consecutive 16-bit registers.
High word is at the lower address:

```python
r = client.read_holding_registers(address=4, count=2, device_id=1)
value = (r.registers[0] << 16) | r.registers[1]
```

---

## Notes

- `AXIS.CANOPEN.CONTROLWORD` is **ReadOnly** — CiA 402 state machine cannot be driven directly over Modbus
- Use `AXIS1.EN` / `AXIS1.DIS` ActionCommands instead of writing 0x0006/0x0007/0x000F
- Registers 40001–40300 are the valid Modbus range on this drive
- The slave ID does not select the axis — axis is selected by register address
