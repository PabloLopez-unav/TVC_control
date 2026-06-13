# AKD2G — Workbench Setup Guide

## What is Workbench?

Kollmorgen Workbench is the PC software used to configure, tune, and monitor the AKD2G. It connects via the **Service/HM (X20) Ethernet port** and supports all AKD2G variants from a single application.

Download: https://www.kollmorgen.com/en-us/products/drives/servo/AKD2G/

---

## First-Time Connection

1. Plug laptop into **X20 (Service/HM)** port with an Ethernet cable
2. Set laptop Ethernet adapter to:
   - IP: `169.254.78.1`
   - Subnet: `255.255.0.0`
3. Open Workbench → click **Scan for Drives**
4. Drive should appear at `169.254.78.209`
5. Axis 1 and Axis 2 appear as sub-nodes — click either to configure

---

## Workbench Navigation Tree

The left-hand panel in Workbench is a tree. Key nodes:

```
Drive
├── Settings
│   ├── Motor           ← Motor selection, temperature sensor, Wake & Shake
│   ├── Feedback        ← Encoder type, resolution, direction
│   ├── Units           ← Set user units (mm, rpm, counts, etc.)
│   ├── Communication   ← Modbus TCP enable/disable, IP settings
│   └── Limits          ← Current, velocity, position limits
├── Axis 1
│   ├── Motor
│   ├── Feedback Devices
│   ├── Service Motion  ← Manual jog for testing
│   ├── Wake & Shake    ← Commutation alignment routine
│   └── Scope           ← Real-time signal plotting
├── Axis 2
│   └── (same as Axis 1)
├── Modbus View         ← Look up register addresses for any parameter
└── Terminal            ← Direct command line to drive
```

---

## Enabling Modbus TCP

**Drive → Settings → Communication → Modbus TCP**

- Enable: ✅
- Port: `502`
- Click **Store to Flash** (or **Save**) then reboot drive if prompted

---

## Modbus View — Finding Register Addresses

Use this when you need to control a specific parameter from Python:

1. **Drive → Modbus View**
2. Search for the parameter name (e.g., `PL.FB`, `VL.CMD`, `IL.CMD`)
3. Note the **Address** column — this is the Modbus holding register number
4. Use that address in `client.read_holding_registers(address=..., ...)`

---

## Motor Setup (per axis)

Navigate to **Axis# → Settings → Motor**:

1. Set `AUTOSET = OFF`
2. Click **Select Motor** → choose Motor Family → select Part #
3. Select the Feedback # for encoder used to commutate
4. Click OK

### Motor Temperature Sensor
**Axis# → Settings → Motor → Motor Temperature**
- `MOTOR.RTYPE = 0`: PTC thermistor (type "TR")
- `MOTOR.RTYPE = 5`: Thermal switch (type "TS")
- `MOTOR.RTYPE = 127`: No thermal sensor (bench testing)

---

## Feedback / Encoder Setup

**Axis# → Feedback Devices → Feedback #**

- Set feedback type (e.g., Incremental with Halls, SinCos, EnDat, etc.)
- For linear encoders: enter **Encoder Pitch in nanometers/line**
  - Formula: `Encoder Pitch (nm) = Scale (nm/count) * 4` (for quadrature)

### Testing Encoder Direction
- If position counts in wrong direction when motor moves forward:
  - Swap Sine+ / Sine− signals, or
  - Swap A / A\ signals on incremental encoder

---

## Units Setup

**Axis# → Settings → Units**

Recommended for linear motors:
- Position: `mm`
- Velocity: `mm/s`
- Acceleration: `mm/s²`

---

## Wake & Shake (Commutation Alignment)

Required for linear motors or when motor phase is unknown.

**Axis# → Settings → Motor → Wake and Shake**

1. Set `AXIS#.WS.IMAX` = motor continuous current rating
2. Set Wake & Shake mode to **2 — Auto Wake & Shake**
3. Click **Arm** (axis must be disabled first)
4. Enable the axis → W&S runs automatically
5. Status changes: Idle → Armed → Running → Successful (or Error)
6. For standard Kollmorgen DDL linear motors: `MOTOR.PHASE ≈ 120°`
7. Run W&S at several positions along the travel for best results

---

## Service Motion (Manual Jog Test)

Use this to verify the motor moves before writing any Python scripts.

**Axis# → Service Motion**

1. Select Mode: **Pulse** (for a timed burst) or **Continuous** (jog)
2. Enter a slow velocity (e.g., `10 mm/s`)
3. Set pulse duration (make sure it won't hit hard stops)
4. Enable the axis
5. Click **Start** — motor should move

> ⚠️ Always limit peak current before jogging a new setup.

---

## Homing

**Axis# → Home**

1. Disable axis
2. Move motor physically to desired home position
3. Set Operation Mode to **Position**
4. Home using **Current Position**, distance = `0`
5. Enable axis → click **Start**
6. Position feedback should read `0.000 mm` after homing

---

## Terminal — Direct Commands

**Drive → Terminal**

Useful commands:

| Command | Description |
|---------|-------------|
| `AXIS1.PL.FB` | Read Axis 1 position |
| `AXIS2.PL.FB` | Read Axis 2 position |
| `AXIS1.VL.FB` | Read Axis 1 velocity |
| `AXIS1.WS.IMAX` | Read/set Wake & Shake max current |
| `AXIS1.FB1.HALLSTATE` | Read Hall sensor state (binary: 001=U, 010=V, 100=W) |
| `MODBUS.LIST` | List all Modbus register mappings |
| `MODBUS.MAP` | Show parameter-to-register map |
| `DRV.FAULT` | Show current fault code |
| `DRV.FAULTHIST` | Show fault history |

---

## Fault Codes

If the drive faults (Status Word bit 3 set, `& 0x0008`):

1. Check the LCD display on the drive — fault code is shown
2. In Workbench: **Drive → Faults & Warnings**
3. In Terminal: type `DRV.FAULT`
4. Fix the root cause
5. Reset fault: Control Word `0x0080`, then re-run enable sequence
   - Or press B1/B2 buttons on drive to reset from hardware

### Common Faults

| Code | Cause | Fix |
|------|-------|-----|
| F128 | STO active (hardware safety input) | Check STO wiring, re-enable STO |
| F501 | Motor over-temperature | Check motor cooling, reduce duty cycle |
| F502 | Drive over-temperature | Check ambient temp, airflow |
| F201 | Feedback loss | Check encoder cable and connection |
| F101 | Over-voltage on DC bus | Check regen resistor wiring |
| F102 | Under-voltage on DC bus | Check mains wiring and fuses |

---

## Scope — Real-Time Plotting

**Axis# → Scope**

Use to plot position, velocity, current vs. time. Essential for tuning. Channels can be any drive parameter. Trigger on enable, fault, or manual.

---

## Saving Parameters

Always save after making changes:
- **File → Store Parameters to Drive Flash** — saves to drive non-volatile memory
- **File → Export Parameters** — saves to a `.AKD` file on your PC (good for backup)
- Parameters can also be saved to the SD card slot for drive replacement
