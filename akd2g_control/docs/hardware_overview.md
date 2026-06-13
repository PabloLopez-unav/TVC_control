# AKD2G — Hardware Overview

## Drive Variants

The AKD2G comes in two axis configurations and two voltage classes:

| Suffix | Meaning |
|--------|---------|
| **(S)** | Single axis drive |
| **(D)** | Dual axis drive (I1 = I2, equal current both axes) |
| **-6V** | 120/240V AC mains range |
| **-7V** | 240/480V AC mains range |

Your unit: **AKD2G dual-axis, CANopen fieldbus variant**

---

## Connector Map

This is the complete connector reference for the AKD2G-S series. All connectors are labelled on the drive.

| Connector | Function |
|-----------|----------|
| **X1** | Motor, Brake, Feedback — Axis 1 (single-cable or power only) |
| **X2** | Motor, Brake, Feedback — Axis 2 (dual-axis variant) |
| **X3** | Mains supply (AC), Regen resistor, DC-Bus link |
| **X10** | 24 VDC auxiliary logic supply |
| **X11** | Motion Bus port 1 (EtherCAT / fieldbus IN) |
| **X12** | Motion Bus port 2 (EtherCAT / fieldbus OUT, daisy-chain) |
| **X13** | CAN Bus — port 1 (optional) |
| **X14** | CAN Bus — port 2 (optional, daisy-chain) |
| **X20** | **Service / HMI — Ethernet port for PC, Workbench, Modbus TCP** |
| **X21** | Primary I/O and Feedback (analog in/out, digital I/O, encoder) |
| **X22** | Extended I/O, Emulated Encoder Output 2 (EEO2), Feedback |
| **X23** | Feedback 3, Emulated Encoder Output 1 (EEO1), I/O |
| **X41** | SFA Feedback Converter accessory, EEO3/EEO4 (optional) |

### The Three Visible Ethernet-Style Ports

| Physical Label | Connector ID | Protocol | Your Use |
|----------------|-------------|----------|----------|
| **Service / HM** | X20 | Ethernet TCP/IP | ✅ Laptop, Workbench, Python |
| **IN** | X13 or X11 | CANopen or EtherCAT | ❌ Not for laptop |
| **OUT** | X14 or X12 | CANopen or EtherCAT | ❌ Not for laptop |

**Always connect your laptop to the Service/HM (X20) port.**

---

## Power Inputs

| Supply | Connector | Spec |
|--------|-----------|------|
| Mains AC | X3 | 1-phase or 3-phase AC (120/240V for -6V, 240/480V for -7V) |
| Logic/Aux | X10 | 24 VDC (always required, keeps logic alive even if AC is off) |

> The 24V X10 supply must be present for the drive to power on its logic, communicate, and respond to Workbench or Python commands — even before enabling motors.

---

## LCD Display and Buttons (B1, B2)

The drive has a small LCD display and two push-buttons. Use these to:
- Read the drive's IP address
- Navigate fault codes
- Reset faults manually
- Configure basic network settings

---

## SD Card Slot

- Used for firmware updates and drive parameter backup/restore
- Parameters can be saved to SD card in Workbench and loaded onto a replacement drive

---

## Dual Axis — Axis Numbering

| Axis | Python Slave ID | Motor Connector |
|------|-----------------|-----------------|
| Axis 1 | `1` | X1 |
| Axis 2 | `2` | X2 |

Both axes share the same IP, Ethernet port, and Modbus TCP connection. They are addressed separately by slave ID in every Python/Modbus command.

---

## Safety — STO (Safe Torque Off)

The AKD2G includes a hardware **Safe Torque Off (STO)** function rated **SIL2 / PLd**. STO cuts motor power at the hardware level independently of software.

| Parameter | Description |
|-----------|-------------|
| `AXIS#.SAFE.STO.A` | STO input channel A for that axis |
| `AXIS#.SAFE.STO.B` | STO input channel B for that axis |
| `AXIS#.SAFE.STO.ACTIVE` | Read-only status: 1 = STO active (drive disabled by hardware) |
| `AXIS#.SAFE.STO.REPORTFAULT` | Whether STO activation raises a fault |

> ⚠️ If the motor does not enable and you've confirmed the software commands are correct, check that the STO inputs are properly wired and not tripped.

---

## Operating Voltage Safety

> ⚠️ Wait **at least 5 minutes** after removing mains power before touching any internal wiring. The DC bus capacitors retain dangerous voltage after power-off.

---

## Supported Software

- **Kollmorgen Workbench** — Windows 7 / 8 / 10
- Drive IP configured via LCD display or Workbench
- Firmware updates via SD card or Workbench
