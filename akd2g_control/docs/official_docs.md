# AKD2G — Official Documentation Links

## Kollmorgen Web Help (Online, JavaScript-rendered)

> Note: These pages require a browser with JavaScript — they cannot be scraped programmatically. Open them directly in Chrome/Edge.

| Resource | URL |
|----------|-----|
| AKD2G WorkBench Help (main) | https://webhelp.kollmorgen.com/AKD2G/English/Content/WorkBench%20Help/Welcome%20AKD2G.htm |
| About WorkBench | https://webhelp.kollmorgen.com/AKD2G/English/Content/AKD2G_User_Manual/Using_WorkBench.htm |
| WorkBench Navigation | https://webhelp.kollmorgen.com/akd2g/english/Content/AKD2G_User_Manual/WorkBench_Interface_Navigation.htm |
| Modbus View | https://webhelp.kollmorgen.com/akd2g/english/Content/AKD2G_User_Manual/ModbusView.htm |
| Modbus Commands | https://webhelp.kollmorgen.com/AKD2G/English/Content/AKD2G%20Modbus/Modbus_Commands.htm |
| MODBUS.MAP command | https://webhelp.kollmorgen.com/akd2g/english/content/AKD2G%20Commands/MODBUS/MODBUS.MAP.htm |
| MODBUS.LIST command | https://webhelp.kollmorgen.com/AKD2G/English/Content/AKD2G%20Commands/MODBUS/MODBUS.LIST.htm |

---

## Official PDF Manuals (Direct Download)

| Manual | URL |
|--------|-----|
| **AKD2G Modbus Communications Manual** (most relevant for Python control) | https://www.kollmorgen.com/sites/default/files/public_downloads/AKD2G%20Modbus%20Communications%20Manual%20EN%20REV%20A_0.pdf |
| AKD2G EtherCAT/CANopen Communications Manual | https://www.kollmorgen.com/sites/default/files/public_downloads/907-200004-00%20AKD2G%20EtherCAT_CANopen%20Communications%20Manual%20EN%20REV%20A.pdf |

---

## Kollmorgen Downloads Page

Full list of all AKD2G documentation, firmware, and software:

https://www.kollmorgen.com/en-us/developer-network/akd2g-downloads

---

## ManualsLib — AKD2G Manuals

Publicly accessible, no login required:

| Manual | URL |
|--------|-----|
| AKD2G System Configuration with Linear Motors (67 pages) | https://www.manualslib.com/manual/3483436/Kollmorgen-Akd2g.html |
| AKD2G-S Series Installation Manual (146 pages) | https://www.manualslib.com/manual/1550284/Kollmorgen-Akd2g-S-Series.html |
| AKD2G-S Series Product Safety Manual (76 pages) | https://www.manualslib.com/manual/1550283/Kollmorgen-Akd2g-S-Series.html |

---

## Kollmorgen Developer Network — Modbus TCP Articles

| Article | URL |
|---------|-----|
| Modbus TCP Landing Page | https://www.kollmorgen.com/en-us/developer-network/akd-modbus-tcp-landing-page |
| Special Modbus AKD Parameters | https://www.kollmorgen.com/en-us/developer-network/special-modbus-akd-parameters |
| Basic Position Move Using Modbus | https://www.kollmorgen.com/en-us/developer-network/akd-basic-position-move-using-modbus |
| Home AKD Drive Using Modbus TCP | https://www.kollmorgen.com/en-us/developer-network/home-akd-drive-using-modbus-tcp |

---

## What's in Each Manual

### AKD2G Modbus Communications Manual (PDF)
The most important reference for Python control. Contains:
- Complete Modbus TCP parameter register address table
- All special AKD Modbus parameters (MODBUS.DRV, MODBUS.DRVSTAT, etc.)
- Function code support table
- CiA 402 state machine over Modbus
- Example Modbus sequences for enable, velocity, position, homing

### AKD2G-S Series Installation Manual (146 pages)
Full hardware reference. Contains:
- All connector pinouts (X1–X41)
- Mains and 24V wiring diagrams
- Cable and wire cross-section requirements
- EMI shielding recommendations
- I/O connector technical data (analog, digital)
- STO (Safe Torque Off) wiring and parameters
- Fault codes and troubleshooting table
- Mechanical dimensions and mounting

### AKD2G System Configuration with Linear Motors (67 pages)
Step-by-step guide for DDL linear motor setup. Contains:
- System wiring diagrams (Heidenhain, Renishaw, incremental+halls)
- Feedback connector pinouts (X23, X41)
- Motor phase and Hall sensor alignment procedure
- Wake & Shake procedure
- Encoder resolution calculation
- Homing and motion tasking examples

---

## Installation Manual — Chapter Structure (Quick Reference)

| Chapter | Content |
|---------|---------|
| 2 | About the manual, symbols, abbreviations, standards |
| 3 | Product safety, shock hazard, emergency stop |
| 4 | Transport, storage, disposal |
| 5 | Package contents, nameplate, part number scheme |
| 6 | Technical data — electrical specs, LCD display, SD card, braking |
| 7 | Mechanical installation, dimensions |
| 8 | Electrical installation — all connectors, wiring, EMI, I/O |
| 9 | Setup procedure, Workbench installation, switch-on behavior, faults |
| 10 | Functional safety — STO wiring, SIL2/PLd, parameters |
| 11 | Approvals — UL, CE, RoHS, REACH |
