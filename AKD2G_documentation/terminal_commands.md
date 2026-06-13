# AKD™

## Parameter and Command Reference Guide

Edition December 2009

Valid for Hardware Revision A

Original Document

Patents Pending

```
Keep all manuals as a product component
during the life span of the product.
Pass all manuals to future users/owners
of the product.
```

**Record of Document Revisions:**

```
Revision Remarks
12/2009 Launch version
```
**Hardware Revision (HR)**

```
Hardware Revision Firmware WorkBench Remarks
A M_01-01-00-000 1.1.0.11368 Launch
```
EnDat is a registered trademark of Dr. Johannes Heidenhain GmbH
EtherCAT is a registered trademark of EtherCAT Technology Group
HIPERFACE is a registered trademark of Max Stegmann GmbH
WINDOWS is a registered trademark of Microsoft Corporation
AKD is a registered trademark of Kollmorgen Corporation

**Current patents:**

US Patent 5,646,496 (used in control card R/D and 1 Vp-p feedback interface)
US Patent 5,162,798 (used in control card R/D)

US Patent 6,118,241 (used in control card simple dynamic braking)

**Technical changes which improve the performance of the device may be made without prior notice!**

Printed in the United States of America
This document is the intellectual property of Kollmorgen™. All rights reserved. No part of this work may be
reproduced in any form (by photocopying, microfilm or any other method) or stored, processed, copied or dis-
tributed by electronic means without the written permission of Kollmorgen™.

**Table of Revisions**

**Record of Document Revisions:**

```
ii Kollmorgen | November 2009
```

```
Revision Remarks
11/2009 Launch version
```
**Hardware Revision (HR)**

```
Hardware Revision Usable Firmware Usable Workbench Remarks
A M_01-00-00-000 1.0.0.11140 Launch editions
```
EnDat is a registered trademark of Dr. Johannes Heidenhain GmbH
EtherCAT is a registered trademark of EtherCAT Technology Group
HIPERFACE is a registered trademark of Max Stegmann GmbH
WINDOWS is a registered trademark of Microsoft Corporation
AKD is a registered trademark of Kollmorgen Corporation

**Current patents:**

US Patent 5,646,496 (used in control card R/D and 1 Vp-p feedback interface)

US Patent 5,162,798 (used in control card R/D)

US Patent 6,118,241 (used in control card simple dynamic braking)

**Technical changes which improve the performance of the device may be made without prior notice!**

Printed in the United States of America
This document is the intellectual property of Kollmorgen™. All rights reserved. No part of this work may be
reproduced in any form (by photocopying, microfilm or any other method) or stored, processed, copied or dis-
tributed by electronic means without the written permission of Kollmorgen™.

```
iii Kollmorgen | November 2009
```

## Table of Contents

```
AKD Parameter and Command Reference Guide |
```


AKD Parameter and Command Reference Guide |



AKD Parameter and Command Reference Guide |



AKD Parameter and Command Reference Guide |



AKD Parameter and Command Reference Guide |



AKD Parameter and Command Reference Guide |

- 1 About the Parameter and Command Reference Guide
   - 1.1 Parameter and Command Naming Conventions
   - 1.2 Summary of Parameters and Commands
- AIN Parameters
   - AIN.CUTOFF
   - AIN.DEADBAND
   - AIN.OFFSET
   - AIN.VALUE
   - AIN.ZERO
- AIO Parameters
   - AIO.ISCALE
   - AIO.PSCALE
   - AIO.VSCALE
- AOUT Parameters
   - AOUT.MODE
   - AOUT.OFFSET
   - AOUT.VALUE
   - AOUT.VALUEU
- BODE Parameters
   - BODE.EXCITEGAP
   - BODE.FREQ
   - BODE.IAMP
   - BODE.INJECTPOINT
   - BODE.MODE
   - BODE.PRBDEPTH
   - BODE.VAMP
- CAP Parameters
   - CAP0.EDGE, CAP1.EDGE
   - CAP0.EN, CAP1.EN
   - CAP0.EVENT, CAP1.EVENT
      - CAP0.FILTER, CAP1.FILTER
      - CAP0.MODE, CAP1.MODE
      - CAP0.PLFB, CAP1.PLFB
      - CAP0.PREEDGE, CAP1.PREEDGE
      - CAP0.PREFILTER, CAP1.PREFILTER
      - CAP0.PRESELECT, CAP1.PRESELECT
      - CAP0.STATE, CAP1.STATE
      - CAP0.T, CAP1.T
      - CAP0.TRIGGER, CAP1.TRIGGER
   - CS Parameters
      - CS.DEC
      - CS.STATE
      - CS.TMAX
      - CS.TO
      - CS.VTHRESH
   - DIN Parameters
      - DIN.DIPSWITCH
      - DIN.ROTARY
      - DIN.STATES
      - DIN1.INV TO DIN7.INV
      - DIN1.MODE TO DIN7.MODE
      - DIN1.PARAM TO DIN7.PARAM
      - DIN1.STATE to DIN7.STATE
   - DOUT Parameters
      - DOUT.CTRL
      - DOUT.RELAYMODE
      - DOUT.STATES
      - DOUTx.MODE
      - DOUT1.PARAM AND DOUT2.PARAM
      - DOUT1.STATE AND DOUT2.STATE
   - DRV Parameters and Commands
      - DRV.ACC
      - DRV.ACTIVE
- ii Kollmorgen | November AKD Parameter and Command Reference Guide |
- DRV.BLINKDISPLAY
- DRV.CLRFAULTHIST
- DRV.CLRFAULTS
- DRV.CMDSOURCE
- DRV.CRASHDUMP
- DRV.DBILIMIT
- DRV.DEC
- DRV.DIR
- DRV.DIS
- DRV.DISMODE
- DRV.DISSOURCES
- DRV.DISTO
- DRV.EMUEDIR
- DRV.EMUEMODE
- DRV.EMUEMTURN
- DRV.EMUERES
- DRV.EMUEZOFFSET
- DRV.EN
- DRV.ENDEFAULT
- DRV.FAULTHIST
- DRV.FAULTS
- DRV.HANDWHEEL
- DRV.HELP
- DRV.HELPALL
- DRV.ICONT
- DRV.INFO
- DRV.IPEAK
- DRV.IZERO
- DRV.LIST
- DRV.LOGICVOLTS
- DRV.MEMADDR
- DRV.MEMDATA
- DRV.MOTIONSTAT
      - Drive Name: DRV.NAME
      - DRV.NVLIST
      - DRV.NVLOAD
      - DRV.NVSAVE
      - DRV.ONTIME
      - DRV.OPMODE
      - DRV.READFORMAT
      - DRV.RSTVAR
      - DRV.RUNTIME
      - DRV.STOP
      - DRV.TEMPERATURES
      - DRV.VER
      - DRV.VERIMAGE
      - DRV.WARNINGS
      - DRV.ZERO
   - FB1 Parameters
      - FB1.ENCRES
      - FB1.HALLSTATE
      - FB1.IDENTIFIED
      - FB1.INITSIGNED
      - FB1.MECHPOS
      - FB1.MEMVER
      - FB1.OFFSET
      - FB1.ORIGIN
      - FB1.PFIND
      - FB1.PFINDCMDU
      - FB1.POLES
      - FB1.PSCALE
      - FB1.RESKTR
      - FB1.RESREFPHASE
      - FB1.SELECT
      - FB1.TRACKINGCALC
   - FBUS Parameters
- iv Kollmorgen | November AKD Parameter and Command Reference Guide |
   - FBUS.PARAM1 TO FBUS.PARAM20
   - FBUS.PLLTHRESH
   - FBUS.SAMPLEPERIOD
   - FBUS.SYNCACT
   - FBUS.SYNCDIST
   - FBUS.SYNCWND
   - FBUS.TYPE
- GEAR Parameters
   - GEAR.ACCMAX
   - GEAR.DECMAX
   - GEAR.IN
   - GEAR.MODE
   - GEAR.MOVE
   - GEAR.OUT
   - GEAR.VMAX
- HOME Parameters
   - HOME.ACC
   - HOME.DEC
   - HOME.DIR
   - HOME.DIST
   - HOME.FEEDRATE
   - HOME.IPEAK
   - HOME.MODE
   - HOME.MOVE
   - HOME.P
   - HOME.PERRTHRESH
   - HOME.SET
   - HOME.V
- HWLS Parameters
   - HWLS.NEGSTATE
   - HWLS.POSSTATE
- IL Parameters
   - IL.BUSFF
      - IL.CMD
      - IL.CMDU
      - IL.DIFOLD
      - IL.FB
      - IL.FF
      - IL.FOLDFTHRESH
      - IL.FOLDFTHRESHU
      - IL.FOLDWTHRESH
      - IL.FRICTION
      - IL.IFOLD
      - IL.KACCFF
      - IL.KBUSFF
      - IL.KP
      - IL.KPDRATIO
      - IL.KVFF
      - IL.LIMITN
      - IL.LIMITP
      - IL.MFOLDD
      - IL.MFOLDR
      - IL.MFOLDT
      - IL.MIFOLD
      - IL.OFFSET
      - IL.VCMD
      - IL.VUFB
      - IL.VVFB
   - MOTOR Parameters
      - MOTOR.AUTOSET
      - MOTOR.BRAKE
      - MOTOR.BRAKERLS
      - MOTOR.BRAKESTATE
      - MOTOR.CTF0
      - MOTOR.ICONT
      - MOTOR.IDDATAVALID
- vi Kollmorgen | November AKD Parameter and Command Reference Guide |
   - MOTOR.INERTIA
   - MOTOR.IPEAK
   - MOTOR.KT
   - MOTOR.LQLL
   - MOTOR.NAME
   - MOTOR.PHASE
   - MOTOR.PITCH
   - MOTOR.POLES
   - MOTOR.R
   - MOTOR.RTYPE
   - MOTOR.TBRAKEAPP
   - MOTOR.TBRAKERLS
   - MOTOR.TEMP
   - MOTOR.TEMPFAULT
   - MOTOR.TEMPWARN
   - MOTOR.TYPE
   - MOTOR.VMAX
   - MOTOR.VOLTMAX
- MT Parameters and Commands
   - MT.ACC
   - MT.CLEAR
   - MT.CNTL
   - MT.CONTINUE
   - MT.DEC
   - MT.EMERGMT
   - MT.LIST
   - MT.LOAD
   - MT.MOVE
   - MT.MTNEXT
   - MT.NUM
   - MT.P
   - MT.PARAMS
   - MT.SET
      - MT.TNEXT
      - MT.TNUM
      - MT.TPOSWND
      - MT.TVELWND
      - MT.V
      - MT.VCMD
   - PL Parameters
      - PL.CMD
      - PL.ERR
      - PL.ERRFTHRESH
      - PL.ERRWTHRESH
      - PL.FB
      - PL.FBSOURCE
      - PL.INTINMAX
      - PL.INTOUTMAX
      - PL.KI
      - PL.KP
   - PLS Parameters and Commands
      - PLS.CLR
      - PLS.EN
      - PLS.MODE
      - PLS.P01 TO PLS.P16
      - PLS.POLARITY
      - PLS.STATE
   - REC Parameters and Commands
      - REC.ACTIVE
      - REC.CH1 to REC.CH6
      - REC.DONE
      - REC.GAP
      - REC.NUMPOINTS
      - REC.OFF
      - REC.RECPRMLIST
      - REC.RETRIEVE
- viii Kollmorgen | November AKD Parameter and Command Reference Guide |
   - REC.RETRIEVEDATA
   - REC.RETRIEVEHDR
   - REC.RETRIEVESIZE
   - REC.STOPTYPE
   - REC.TRIG
   - REC.TRIGparam
   - REC.TRIGPOS
   - REC.TRIGPRMLIST
   - REC.TRIGSLOPE
   - REC.TRIGTYPE
   - REC.TRIGVAL
- REGEN Parameters
   - REGEN.POWER
   - REGEN.REXT
   - REGEN.TEXT
   - 1.3 Regen Resistor Type
   - Parameter: REGEN.TYPE
   - REGEN.WATTEXT
- SM Parameters
   - SM.ACCTYPE
   - SM.I1
   - SM.I2
   - SM.MODE
   - SM.MOVE
   - SM.T1
   - SM.T2
   - SM.V1
   - SM.V2
   - SM.VPM1
   - SM.VPM2
- 2 STO Parameters
   - STO.STATE
- SWLS Parameters
      - SWLS.EN
      - SWLS.LIMIT0
      - SWLS.LIMIT1
      - SWLS.STATE
   - UNIT Parameters
      - UNIT.ACCLINEAR
      - UNIT.ACCROTARY
      - UNIT.LABEL
      - UNIT.PIN
      - UNIT.PLINEAR
      - UNIT.POUT
      - UNIT.PROTARY
      - UNIT.VLINEAR
      - UNIT.VROTARY
   - VBUS Parameters
      - VBUS.OVFTHRESH
      - VBUS.OVFWTHRESH
      - VBUS.RMSLIMIT
      - VBUS.UVFTHRESH
      - VBUS.UVMODE
      - VBUS.UVWTHRESH
      - Measured Bus Voltage: VBUS.VALUE
   - VL Parameters
      - VL.ARPF1 TO VL.ARPF4
      - VL.ARPQ1 TO VL.ARPQ4
      - VL.ARTYPE1 TO VL.ARTYPE4
      - VL.ARZF1 TO VL.ARZF4
      - VL.ARZQ1 TO VL.ARZQ4
      - VL.BUSFF
      - VL.CMD
      - VL.CMDU
      - VL.ERR
      - VL.FB
- x Kollmorgen | November AKD Parameter and Command Reference Guide |
- VL.FBFILTER
- VL.FBSOURCE
- VL.FF
- VL.GENMODE
- VL.KBUSFF
- VL.KI
- VL.KP
- VL.KVFF
- VL.LIMITN
- VL.LIMITP
- VL.LMJR
- VL.THRESH


This page intentionally left blank.


## 1 About the Parameter and Command Reference Guide

This reference guide provides descriptive information about each parameter and command used in the AKD
firmware. Parameters and commands are used to configure the drive or to return status information from the
drive via the WorkBench terminal screen. The use of parameters and commands to perform various drive func-
tions is detailed in Section [link] of the AKD User Guide.

For each parameter or command, this guide presents the following table of information, followed by a descrip-
tion of the command and examples as appropriate.

**XXX.XXX (Parameter or Command Name)**

```
General Information
```
```
Type
```
```
One of four types:
 Command: Action or W/O command.
 NV Parameter: R/W and stored in nonvolatile (NV) memory
 R/W Parameter: Can be either read from or written to the drive.
 R/O Parameter. Can only be read from the drive
Description Brief description of the parameter or command.
Units Appropriate units (see Table of Units [link] unit descriptions)
Range Permissible range; multiple ranges are sometimes present.
Default Value Determined at setup process time or motor ID; otherwise set to 0.010.
Data Type Integer, Boolean, Float, or String
See Also Links to related information such as other parameters, block diagrams,schematics, or other sections of the product manual.
```
```
Start Version The minimum firmware version number required to use the parameter orcommand
```
```
Fieldbus Information
EtherCAT COE & CANOpen
Index/Subindex or
Parameter Number
```
```
1 four-digit hex number/1 two-digit
hex number.
Data Type See DS301 list.
PDO Mappable Yes or no.
```
```
Start Version
```
```
The minimum firmware version
number required to use the param-
eter or command.
```
Additional data types may include:

```
Type Description
Error Illegal type=
b Boolean
U8 8 x unsigned numbers
```
```
AKD Parameter and Command Reference Guide | 1 About the Parameter and Command Reference Guide
```

AKD Parameter and Command Reference Guide | 1 About the Parameter and Command Reference Guide

```
Type Description
S8 8 x signed numbers
U16 16 x unsigned numbers
S16 16 x signed numbers
U32 32 x unsigned numbers
S32 32 x signed numbers
U64 64 x unsigned numbers
S64 64 x signed numbers
```

### 1.1 Parameter and Command Naming Conventions

```
Abbreviation Term
ACC Acceleration
APP Apply
CLR Clear
CS Controlled Stop
I Current
D Current D component
DEC Deceleration
DIR Direction
DIS Disable
DIST Distance
EMUE Emulated encoder
EN Enable
ERR Error
F Fault
FB Feedback
FF Feedforward
K Gain
INT Integrator
LIM Limit
L Loop
MAX Maximum
MIN Minimum
N Negative
NV Nonvolatile
P Position,Proportional, Positive
RLS Release
R Resistance
STATE Status, State, Stat
THRESH Threshold
T Time
TMAX Timeout
U User
V Velocity, Volt
W Warning
```
### 1.2 Summary of Parameters and Commands

This table lists all valid commands and parameters, with a brief description for each. The parameter name and
description are linked to the parameter tables.

```
Parameter or Command Type Description
Analog Input (AIN)
```
```
AKD Parameter and Command Reference Guide | 1 About the Parameter and Command Reference Guide
```

AKD Parameter and Command Reference Guide | 1 About the Parameter and Command Reference Guide

```
Parameter or Command Type Description
AIN.CUTOFF NV
Sets the analog input low-pass filter cutoff
frequency.
AIN.DEADBAND NV Sets the analog input signal deadband.
AIN.OFFSET NV Sets the analog input offset.
AIN.VALUE R/O Reads the value of the analog input signal.
AIN.ZERO Command Zeroes the analog input signal.
Analog Current Output (AIO)
AIO.ISCALE NV Sets current scale factor.
AIO.VSCALE NV Sets velocity scale factor.
"AIO.PSCALE" (page 22) NV Sets position scale factor.
Analog Output (AOUT)
AOUT.MODE NV Sets the analog output mode.
"AOUT.OFFSET" (page 27) NV "Sets the analog input offset." (page 27)
AOUT.VALUE NV Reads the analog output value.
"AOUT.VALUEU" (page 29) R/W Sets the analog output value.
Bode plot (BODE)
BODE.EXCITEGAP R/W Controls how often the excitation is updated.
BODE.FREQ R/W Sets the frequency of the sine excitation source.
BODE.IAMP R/W
Sets current command value used during the
Bode procedure.
BODE.INJECTPOINT R/W
Sets whether the excitation uses current or veloc-
ity excitation type.
BODE.MODE R/W Sets the mode of the excitation.
BODE.PRBDEPTH R/W Sets the length of the PRB signal before itrepeats.
```
```
BODE.VAMP R/W Sets the amplitude of the excitation when invelocity mode.
Capture (CAP)
CAP0.EN, CAP1.EN R/W " Enables or disables the related capture engine."
(page 41)
CAP0.FILTER, CAP1.FILTER R/W "Controls the precondition logic." (page 42)
CAP0.MODE, CAP1.MODE NV Selects the captured value.
CAP0.PLFB, CAP1.PLFB R/O Setscapturedposition value.
CAP0.PREFILTER, CAP1.P-
REFILTER R/W Sets the filter for the precondition input source.
CAP0.PRESELECT, CAP1.PRE-
SELECT R/W Sets the precondition trigger.
CAP0.STATE, CAP1.STATE R/O Indicates whether or not trigger source was cap-tured.
```
```
CAP0.T, CAP1.T R/O Reads time capture (if time capture was con-figured).
CAP0.TRIGGER,
CAP1.TRIGGER R/W
```
```
Specifies the trigger source for the position cap-
ture.
Controlled Stop (CS)
```

```
Parameter or Command Type Description
```
CS.DEC NV
Sets the deceleration value for the controlled
stop process.

CS.STATE NV
Returns the internal status of the controlled stop
process.

CS.TMAX R/O
Sets the time-out value for the drive to disable if
velocity is not within CS.VTHRESH.

CS.TO NV
Sets the time value for the drive velocity to be
within CS.VTHRESH.

CS.VTHRESH NV
Sets the velocity threshold for the controlled
stop.
**Digital Input (DIN)**
DIN.DIPSWITCH R/O Reads the DIP switch positions.
DIN.ROTARY R/O Reads the rotary knob value.
DIN.STATES R/O Reads the digital input states.

DIN1.INV TO DIN7.INV R/W Setstheindicatedthepolarityofadigitalinputmode.

DIN1.MODE TO DIN7.MODE NV Sets the digital input modes.

DIN1.PARAM TO DIN7.PARAM R/W Setsavalueusedasan extraparameterfordig-italinputsnodes.

DIN1.STATE to DIN7.STATE R/O Reads a specific digital input state.
**Digital Output (DOUT)**

DOUT.CTRL NV Sets the source of digital outputs (firmware or
fieldbus).
DOUT.RELAYMODE R/W Indicates faults relay mode.
DOUT.STATES R/O Reads the state of the two digital outputs.
DOUTx.MODE NV Sets the digital output mode.
DOUT1.PARAM AND
DOUT2.PARAM
NV Sets extra parameters for the digital outputs.

DOUT1.STATE AND
DOUT2.STATE
R/O Reads the digital output state.
**Drive (DRV)**

DRV.ACC NV Describes the acceleration ramp for the velocity
central loop.
DRV.ACTIVE R/O Reads the enable status of an axis.
DRV.BLINKDISPLAY Command Causes the display to blink for 10 seconds.
DRV.BURNINOFFT (Password
Protected) R/W Sets the burn-in test mode OFF time.
DRV.CLRFAULTHIST Command Clears the fault history log in the NV.
DRV.CLRFAULTS Command Tries to clear all active faults in the drive.

DRV.CMDSOURCE NV Sets the command source (service, fieldbus,
analog input, gearing, digital, or Bode).

"DRV.CRASHDUMP" (page 86) Command Retrieves diagnostic information after the drive
crashes.

"DRV.DBILIMIT" (page 87) NV Sets the maximum amplitude of the current for
dynamic braking.

```
AKD Parameter and Command Reference Guide | 1 About the Parameter and Command Reference Guide
```

AKD Parameter and Command Reference Guide | 1 About the Parameter and Command Reference Guide

```
Parameter or Command Type Description
DRV.DEC NV Sets the deceleration value for the velocity loop.
"DRV.DIR" (page 90) R/W Changes drive direction.
DRV.DIS Command Disables the axis (software).
"DRV.DISMODE" (page 93) NV Sets disable type to either dynamic brake or
immediate disable.
DRV.DISSOURCES R/O Returns the possible reason for a drive disable.
"DRV.DISTO" (page 95) R/W Sets the emergency timeout
DRV.DOWNLOAD Command Starts a new FW/FPGA download.
DRV.EMUEDIR R/W Sets the direction of the emulated encoder output
(EEO) signal.
DRV.EMUEMODE R/W Sets the mode of the emulated encoder output
(EEO) connector.
```
```
"DRV.EMUEMTURN" (page 98) R/W
```
```
Defines the location of the index pulse on the
EEO (emulated encoder output) when DRV.EMU-
EMODE=2.
DRV.EMUERES R/W Sets the resolution of the EEO (emulatedencoder output).
```
```
DRV.EMUEZOFFSET R/W Sets the resolution of the EEO (emulatedencoder output).
DRV.EN Command Enables the axis (software).
DRV.ENDEFAULT R/W Sets the default state of the software enable
DRV.FAULTHIST R/O Reads the last 10 faults from NV memory.
DRV.FAULTS R/O Reads the active faults.
DRV.FLASHREAD R/O Reads a value from the serial flash.
DRV.HANDWHEEL R/O Reads the EEO input value.
DRV.HELP R/O Reads the minimum, maximum, and default
values for a specific parameter or command.
```
```
DRV.HELPALL R/O
```
```
Retrieves the minimum, maximum, default, and
actual values for all available parameters and
commands.
DRV.ICONT R/O Reads the continuous rated current value.
DRV.INFO R/O Reads general information about the drive.
DRV.IPEAK R/O Reads the peak rated current value.
DRV.IZERO R/W Sets the current that will be used during theDRV.ZERO procedure.
```
```
DRV.LIST R/O Reads the list of available parameters and com-mands.
DRV.LOGICVOLTS Reads the logic voltages.
DRIVE NAME: DRV.NAME NV Sets and reads the name of the drive.
DRV.NVLIST R/O Lists the NV parameters and values from the
RAM.
DRV.NVLOAD W/O
"Loads all data from the NV memory of the drive
into the RAM parameters." (page 119)
DRV.NVSAVE CommandSavesthedriveparametersfrom theRAMtotheNV.
```

```
Parameter or Command Type Description
```
DRV.ONTIME R/O
Returns how long the drive has been running
since last power up.

DRV.OPMODE NV
Sets the operation mode (current, velocity, or
position).

DRV.READFORMAT R/W
Sets the value returned to either decimal or hex-
adecimal.

DRV.RSTVAR Command
Sets default values in the drive without re-booting
the drive and without resetting the NV memory.

DRV.RUNTIME R/O
Returns how long the drive has been running
since first activated.
DRV.STOP Command This command stops all drive motion.
DRV.VER R/O Reads the drive version.
DRV.VERIMAGE R/O Returns the version data from each image.
DRV.TEMPERATURES R/O Reads the temperature of drive components.

"DRV.ZERO" (page 131) R/W
Sets the zero mode. The procedure is activated
when the drive is enabled.
**Feedback (FB1)**
FB1.ENCRES NV Sets the resolution of the motor encoder.
FB1.HALLSTATE R/O Reads the resolution of the motor encoder.

FB1.IDENTIFIED R/O Reads the type of feedback device used by the
drive/motor.

FB1.INITSIGNED NV Setsinitialfeedbackvalueassignedorunsigned.

FB1.LDLL R/O Reads the motor line-to-line inductance from theFPGA.

##### FB1.LQLL R/O

Reads the motor line-to-line inductance in the
back emf axis (q axis) from the SFD memory
from the FPGA.
FB1.MECHPOS R/O Reads the mechanical position.
FB1.MEMVER R/O Returns the memory feedback version.
FB1.MNUM R/O Returns the motor name/number.
FB1.MPHASE NV Set or get the commutation angle offset.
FB1.OFFSET NV Sets position feedback offset.
FB1.POLES R/O Reads the number of feedback poles.
FB1.OFFSET NV Sets position feedback offset.
FB1.POLES R/O Reads the number of feedback poles.
FB1.SELECT NV Sets user entered type or identified type (–1).
**Fieldbus (FBUS)**
FBUS.PARAM1TO
FBUS.PARAM20
NV Set fieldbus specific meanings.

FBUS.PLLTHRESH NV Sets number of successful synchronized cycles
needed to lock the PLL.
FBUS.SAMPLEPERIOD NV Sets fieldbus sample period.

FBUS.SYNCACT R/O Reads actual distance from the desired sync dis-
tance.

```
AKD Parameter and Command Reference Guide | 1 About the Parameter and Command Reference Guide
```

AKD Parameter and Command Reference Guide | 1 About the Parameter and Command Reference Guide

```
Parameter or Command Type Description
FBUS.SYNCDIST NV Sets time target for synchronization.
FBUS.SYNCWND NV Sets symmetrically arranged window around thedesired sync distance.
FBUS.TYPE R/O Shows the active fieldbus type.
Gearing (GEAR)
GEAR.ACCMAX R/W Sets the maximum allowed acceleration value.
GEAR.DECMAX R/W Sets the maximum allowed deceleration value
GEAR.IN R/W Sets the denominator of the electronic gearingratio.
GEAR.MODE R/W Selects electronic gearing mode.
GEAR.MOVE Command Starts the electronic gearing.
GEAR.OUT R/W Sets the numerator of the electronic gearing ratio
GEAR.VMAX R/W Maximum allowed velocity value
Homing (HOME)
HOME.ACC R/W Sets homing acceleration.
HOME.DEC R/W Sets homing deceleration.
HOME.DIR NV Sets homing direction.
HOME.DIST R/W Sets homing distance.
HOME.FEEDRATE R/W Sets homing velocity factor.
HOME.IPEAK R/W Sets the current limit during homing procedure to
a mechanical stop
HOME.MODE R/W Selects the homing mode.
HOME.MOVE Command Starts a homing procedure.
HOME.P R/W Sets home position.
HOME.PERRTHRESH R/W Position lag threshold.
HOME.SET Command Immediately sets the home position.
HOME.V R/W Sets homing velocity.
Hardware Limit Switch (HWLS)
HWLS.NEGSTATE R/O Reads the status of the negative hardware limit
switch.
HWLS.POSSTATE R/O Reads the status of the positive hardware limit
switch.
Current Loop (IL)
IL.BUSFF R/O Displaysthecurrent feedforwardvalueinjectedbythefieldbus
```
```
IL.CMD R/O Reads the value of the q-component current con-troller inside the FPGA.
IL.CMDU R/W Sets the user current command.
IL.DCMD R/O Reads the value of the d-component current con-
troller inside the FPGA.
IL.DCMD (Password Protected) R/O Reads the value of the d-component current con-
troller inside the FPGA.
IL.DCMDU R/W User d-component current command.
```

**Parameter or Command Type Description**
IL.DEADBAND (Password Pro-
tected) R/O Dead-time of two IGBTs in series connection.
IL.DFB R/O Actual value of the d-component current.

IL.DFOLDD (Password Protected) R/O Reads the motor foldback maximum time atmotor peak current.

IL.DFOLDR (Password Protected) R/O Reads the motor foldback recovery time.

IL.DFOLDT R/O Reads the motor foldback time constant of the
exponential current drop (foldback).
IL.DIFOLD R/O Reads the drive foldback current limit.

IL.DLIMITN R/W Negative user (application) d-component current
limit.

IL.DLIMITP R/W Positive user (application) d-component current
limit.

IL.FB R/O Reads the actual value of the d-component cur-
rent.
IL.FOLDFTHRESH NV IL.FOLDFTHRESH
IL.FOLDWTHRESH NV Sets the foldback warning level.
IL.IFOLD R/O Reads the overall foldback current limit.

IL.INTEN NV Enables/Disables the integrator part of the PI-
loop.
IL.IUOFFSET (Password Pro-
tected)
R/W Offset, which is added to the sigma-delta meas-
ured current value in the u-winding.

IL.IUFB R/O Sigma/Delta measured current in the u-winding
of the motor.

IL.IVFB* R/W Sigma/Delta measured current in the u-winding
of the motor.

IL.IVOFFSET* R/W Offset added to the sigma-delta measured cur-
rent value in the v-winding.

IL.KP NV Sets the proportional gain of the q-component of
the PI regulator.
IL.KPDRATIO NV IL.KPDRATIO
IL.LIMITN NV Sets the negative user (application) current limit.
IL.LIMITP NV Sets the positive user (application) current limit.

IL.MFOLDD NV Sets the motor foldback maximum time at motorpeak current.

IL.MFOLDR R/O Sets the motor foldback recovery time.

IL.MFOLDT NV Sets the motor foldback time constant of the
exponential current drop (foldback).
IL.MIFOLD R/O Sets the motor foldback current limit.
IL.PWMFREQ* NV PWM frequency of the IGBTs.
IL.VDCMD R/O Output of the d-component PI-regulator.
IL.VCMD R/O Sets the output of the q-component PI regulator.

IL.VUFB R/O Reads the measured voltage on the u-winding of
the motor.

```
AKD Parameter and Command Reference Guide | 1 About the Parameter and Command Reference Guide
```

AKD Parameter and Command Reference Guide | 1 About the Parameter and Command Reference Guide

```
Parameter or Command Type Description
IL.VVFB R/O
Reads the measured voltage on the v-winding of
the motor.
IL.DLIMITN R/W
Negative user (application) d-component current
limit.
IL.DLIMITP R/W
Positive user (application) d-component current
limit.
```
```
IL.FB R/O Reads the actual value of the d-component cur-
rent.
```
```
Motor (MOTOR) Parameters
MOTOR.BRAKE NV Sets the presence or absence of a motor brake.
MOTOR.TBRAKEAPP NV The delay time used for applying the motor brake.
MOTOR.TBRAKERLS NV
The delay time used for releasing the motor
brake.
MOTOR.ICONT NV Sets the motor continuous current.
MOTOR.INERTIA NV Sets the motor inertia.
MOTOR.IPEAK NV Sets the motor peak current.
MOTOR.KT NV Sets the torque constant of the motor.
MOTOR.LQLL NV Sets the line-to-line motor Lq.
MOTOR.VMAX NV Sets the maximum motor speed.
MOTOR.NAME NV Sets the motor name.
MOTOR.PHASE NV Sets the motor phase.
MOTOR.PITCH NV Sets the motor pitch.
MOTOR.POLES NV Sets the number of motor poles.
MOTOR.R NV Sets the stator winding resistance phase-phase
in ohms.
MOTOR.TEMP R/O Reads the motor temperature represented as the
resistance of the motor PTC.
MOTOR.TEMPFAULT NV Sets the motor temperature fault level.
MOTOR.TEMPWARN NV Sets the motor temperature warning level.
MOTOR.TYPE NV Sets the motor type.
MOTOR.VOLTMAX NV Sets the motor maximum voltage.
Motion Task (MT)
MT.ACC R/W Specifies motion task acceleration.
MT.CLEAR Command Clears motion tasks from the drive.
MT.CNTL R/W Sets motion task control word.
MT.CONTINUE Command Continues a stopped motion task.
MT.DEC R/W Motion task deceleration.
MT.EMERGMT R/W
Selects a motion task to be triggered after an
emergency stop procedure.
MT.MTNEXT R/W Specifies following motion task number.
MT.TNEXT R/W Specifies following motion task time.
MT.LIST Command Lists all initialized motion tasks in the drive.
```

MT.LOAD Command Reads/loads a motion task number from thedrive.

MT.MOVE Command Starts a motion task.
MT.NUM R/W Motion task number.
MT.PARAMS Command Shows a motion task.
MT.P R/W Motion task position.
MT.SET Command Sets the motion task in the drive.
MT.TNUM R/W Motion task customer table number.
MT.V R/W Motion task velocity.
**Position Loop (PL)**

PL.CMD NV Reads the position command directly from theentry to the position loop.

PL.ERR NV Returns the position following an error.
PL.ERRFTHRESH Sets the maximum position error.
PL.ERRWTHRESH Sets the position error warning level.
PL.FB R/O Reads the position feedback value.
PL.FBSOURCE Sets the feedback source for the position loop.

PL.INTINMAX NV Limits the input of the position loop integrator by
setting the input saturation.

PL.INTOUTMAX NV Limits the output of the position loop integrator by
setting the output saturation.
PL.KD NV The derivative gain of the position loop.
PL.KI NV Sets the integral gain of the position loop.

PL.KP NV
Sets the proportional gain of the position regulator
PID loop.
**Position Register Switches (PLS)**
PLS.CLR Defines which position register to clear.
PLS.EN Enables the position registers.
PLS.MODE Selects position register mode.
PLS.POLARITY Sets the polarity of the position registers.
PLS.P01 TO PLS.P16 Position register compare value.
PLS.STATE Reads the status of the position registers.
**Recorder (REC)**
REC.ACTIVE R/O Indicates if data recording is in progress (active).
REC.CH1 to REC.CH6 R/W Sets recording channels 1 to 6.

REC.DONE R/O Checks whether or not the recorder has finished
recording.
REC.GAP R/W Specifies the gap between consecutive samples.
REC.NUMPOINTS R/W Sets the number of points to record.
REC.OFF R/W Turns the recorder OFF.

REC.RETRIEVE R/O Transfers all the recorded data to the com-munication channel.

REC.STOPTYPE R/W Sets the recorder stop type.
REC.TRIG Command Triggers the recorder.
REC.TRIGSLOPE R/W Sets the trigger slope.

```
AKD Parameter and Command Reference Guide | 1 About the Parameter and Command Reference Guide
```

AKD Parameter and Command Reference Guide | 1 About the Parameter and Command Reference Guide

```
REC.TRIGTYPE R/W Sets the trigger type.
REC.TRIGVAL R/W Sets the trigger value.
Regen Resistor (REGEN)
REGEN.IMPEXT NV
Sets the external user defined regen resistor ther-
mal impedance.
REGEN.IMPEXTHLF NV
he external user defined regen resistor’s thermal
impedance.
REGEN.REXT NV
Sets the external, user-defined regen resistor
resistance.
PARAMETER: REGEN.TYPE NV Sets the regen resistor type.
REC.TRIGPOS R/W Sets the position in the recording buffer in whichto set the trigger.
VBUS.UVFTHRESH R/O Reads the under voltage fault level.
VBUS.OVFTHRESH R/O Reads the over voltage fault level.
MEASURED BUS VOLTAGE:
VBUS.VALUE
R/O Reads DC bus voltage.
Units (UNIT)
UNIT.ACCLINEAR NV Sets the linear acceleration/deceleration units.
UNIT.ACCROTARY NV Sets the rotary acceleration/deceleration units.
UNIT.LABEL NV Sets user-defined name for user-defined position
units.
UNIT.PIN NV Sets gear IN for the unit conversion.
UNIT.PLINEAR NV Sets the linear position units.
UNIT.POUT NV Sets gear out for the unit conversion.
UNIT.PROTARY NV Sets the position units when the motor type(MOTOR.TYPE) is rotary.
UNIT.VLINEAR NV Sets the linear velocity units.
UNIT.VROTARY NV Sets the velocity units when the motor type
(MOTOR.TYPE) is rotary.
Bus voltage (VBUS)
VBUS.OVFTHRESH R/O Reads the over voltage fault level.
"VBUS.OVFWTHRESH" (page
338) N/V Sets voltage level for over voltage warning.
"VBUS.RMSLIMIT" (page 339) Reads the limit for the bus capacitors load.
"VBUS.UVFTHRESH" (page 340) R/O Reads the under voltage fault level.
"VBUS.UVMODE" (page 341) Indicates undervoltage (UV) mode.
"VBUS.UVWTHRESH" (page 342) NV Sets voltage level for undervoltage warning.
"Measured Bus Voltage:
VBUS.VALUE" (page 343) R/O Reads DC bus voltage.
Velocity Loop (VL)
```
```
VL.ARPF1 TO VL.ARPF4 R/W
```
```
Sets the natural frequency of the pole (denom-
inator) of anti-resonance (AR) filters 1, 2, 3, and
4.
VL.ARPQ1 TO VL.ARPQ4 R/W
Sets the Q of the pole (denominator) of anti-res-
onance (AR) filter 1.
```

VL.ARTYPE1 TO VL.ARTYPE4 NV Indicates the method used to calculate BiQuad
coefficients.

VL.ARZF1 TO VL.ARZF4 R/W Sets the natural frequency of the zero (numer-
ator) of anti-resonance (AR)filter 1.

VL.ARZQ1 TO VL.ARZQ4 R/W Sets the Q of the zero (numerator) of anti-res-
onance filter #1.

VL.BUSFF R/O Displays the velocity loop feedforward value
injected by the field-bus
VL.CMD R/O Reads the actual velocity command.
VL.CMDU R/W Sets the user velocity command.
VL.ERR R/O Sets the velocity error.
VL.FB R/O Reads the velocity feedback.
VL.FBFILTER Filters VL.FB value.
VL.FBSOURCE Sets feedback source for the velocity loop.

VL.FF
Displays the velocity loop overall feedforward
value.

VL.GENMODE NV
Selects mode of velocity generation (Observer,
d/dt).

VL.KBUSFF
Sets the velocity loop acceleration feedforward
gain value.

VL.KI NV
Sets the velocity loop integral gain for the PI con-
troller.

VL.KP NV
Sets velocity loop proportional gain for the PI con-
troller.
VL.KVFF R/W Velocity loop velocity feedforward gain value
VL.LIMITN NV Sets the velocity lower limit.
VL.LIMITP NV Sets the velocity high limit.

VL.LMJR Sets the ratio of the estimated load moment of
inertia relative to the motor moment of inertia.
VL.THRESH NV Sets the over speed fault value.

```
AKD Parameter and Command Reference Guide | 1 About the Parameter and Command Reference Guide
```

This page intentionally left blank.


## AIN Parameters

This section describes the analog input (AIN) parameters. AIN parameters function as shown in the block dia-
gram below:

Analog Input Block Diagram


AKD Parameter and Command Reference Guide | AIN Parameters

### AIN.CUTOFF

```
General Information
Type NV Parameter
Description Sets the analog input low-pass filter cutoff frequency.
Units Hz
Range 0 to 10,000 Hz
Default Value 5,000 Hz
Data Type Float
See Also Analog Input Block Diagram
Start Version M_0-0-15
```
#### Description

```
AIN.CUTOFF sets the break frequency in Hz for two cascaded single-pole low-pass filters on the hardware
command input. Since the two poles are cascaded at the same frequency, the -3 dB frequency is 0.64*A-
IN.CUTOFF in hertz and the 10% to 90% step response rise time is 0.53/AIN.CUTOFF in seconds.
Suggested operating values are as follows:
 Analog torque opmode: 5 kHz
 Analog velocity opmode: 2.5 kHz
 General purpose analog input high resolution: 500 Hz
See the Velocity Controller Environment Block Diagram for the drive controller environment.
```

### AIN.DEADBAND

```
General Information
Type NV Parameter
Description Sets the analog input signal deadband.
Units V
Range 0 to 12.5 V
Default Value 0 V
Data Type Float
See Also Analog Input Block Diagram
Start Version M_0-0-15
```
#### Description

AIN.DEADBAND sets the deadband of the analog input signal. If the absolute value of the analog input signal
is less than the AIN.DEADBAND value, then no analog command signal is generated.

```
AKD Parameter and Command Reference Guide | AIN Parameters
```

AKD Parameter and Command Reference Guide | AIN Parameters

### AIN.OFFSET

```
General Information
Type NV Parameter
Description Sets the analog input offset.
Units V
Range –10 to +10 V
Default Value 0 V
Data Type Float
See Also Analog Input Block Diagram, AIN.ZERO
Start Version M_0-0-15
```
#### Description

```
AIN.OFFSET sets the analog offset, which is added to the analog input command to the drive. This value
compensates for the analog input signal (AIN.VALUE) offset or drift.
```

### AIN.VALUE

```
General Information
Type R/O Parameter
Description Reads the value of the analog input signal.
Units V
Range -12.5 to +12.5 V
Default Value N/A
Data Type Float
See Also AIN.OFFSET, AIN.ZERO, Analog Input Block Diagram
Start Version M_0-0-15
```
#### Description

AIN.VALUEreadstheanaloginputvalueafterthevalueisfiltered (asshownintheAnalogInputBlockDiagram).

```
AKD Parameter and Command Reference Guide | AIN Parameters
```

AKD Parameter and Command Reference Guide | AIN Parameters

### AIN.ZERO

```
General Information
Type Command
Description Zeroes the analog input signal.
Units N/A
Range N/A
Default Value N/A
Data Type N/A
See Also AIN.VALUE, AIN.OFFSET
Start Version M_0-0-50-0
```
#### Description

```
AIN.ZERO causes the drive to zero the analog input signal (AIN.VALUE). You may need to execute this com-
mand more than once to achieve zero offset, and AIN.OFFSET is modified in this process.
```

## AIO Parameters

### AIO.ISCALE

```
General Information
Type NV Parameter
Description Sets current scale factor.
Units A/V
Range 0.001 to 22.4 A/V
Default Value 0.001 A/V
Data Type Float
See Also Analog Input Block Diagram
Start Version M_0-0-15
```
#### Description

AIO.ISCALE sets the analog current scale factor that scales:

```
 The analog input (AIN.VALUE) for DRV.OPMODE = 0 (analog torque mode), DRV.CMDSOURCE = 3
(analog)
 The analog output (AOUT.VALUE) for AOUT.MODE = 5 or 6. The value entered is the motor current
per 1 V of analog input or output. This value may be either higher or lower than 100%, but the actual
analog I/O will be limited by the application current limit (IL.LIMITN and IL.LIMITP).
```

AKD Parameter and Command Reference Guide | AIO Parameters

### AIO.PSCALE

```
General Information
Type NV Parameter
Description Sets position scale factor.
```
```
Units
```
```
Depends on UNIT.PROTARY or UNIT.PLINEAR
Rotary: counts/V,rad/V, deg/V, (PIN/POUT)/V, counts 16 bit/V
Linear: counts/V, mm/V, um/V, (PIN/POUT)/V, counts 16 bit/V
```
```
Range
```
```
Rotary:
1 to 9,223,372,036,854,775 counts/V
0 to 13,493,026.816 rad/V
0 to773,094,113.280 deg/V
0 to 10,737,418.240 (PIN/POUT)/V
0 to 140,737,488,355.327 counts 16 bit/V
Linear:
1 to 9,223,372,036,854,775 counts/V
0 to 2147483.648 mm/V
0 to 2147483648.000 um/V
0 to 10737418.240 (PIN/POUT)/V
0 to 140737488355.327 counts 16 bit/V
```
```
Default Value
```
```
Rotary:
1 counts/V
0 rad/V
0 deg/V
0 (PIN/POUT)/V
0 counts 16 bit/V
Linear:
1 count/V
0 rad/V
0 deg/V
0 (PIN/POUT)/V
0 counts16 bit/V
Data Type Float
See Also Analog Input Block Diagram
Start Version M_00-00-56-000
```
#### Description

```
AIO.PSCALE is an analog position scale factor that scales:
```
1. The analog input (AIN.VALUE) for DRV.OPMODE = 2 , DRV.CMDSOURCE = 3 (analog position mode)
2. The analog output (AOUT.VALUE) for AOUT.MODE = 6, or 7. (actual position or position error) per 10 V of
analog input or output.


### AIO.VSCALE

```
General Information
Type NV Parameter
Description Sets velocity scale factor.
```
```
Units
```
```
Depends on UNIT.VROTARY or UNIT.ACCLINEAR
Rotary: rpm/V, rps/V, (deg/s)/V, [(PIN/POUT)/s]/V, (rad/s)/V
Linear: counts/s/V, (mm/s)/V, (um/s)/V, [(PIN/POUT)/s]/V
```
```
Range
```
```
Rotary:
0.060 to 60,000 rpm/V
0.001 to 1,000 rps/V
0.359 to 360,000 (deg/s)/V
0.005 to 5,000 [(PIN/POUT)/s]/V
0.006 to 6,283.186 (rad/s)/V
Linear:
0.001 to 1.000 counts/s/V
0.001*MOTOR.PITCH to 1,000.000*MOTOR.PITCH (mm/s)/V
0.998*MOTOR.PITCH to 1,000,000.000*MOTOR.PITCH (um/s)/V
0.005 to 5,000 [(PIN/POUT)/s]/V
```
```
Default Value
```
```
Rotary:
0.060 rpm/V
0.001 rps/V
0.359 (deg/s)/V
0.005 [(PIN/POUT)/s]/V
0.006 (rad/s)/V
Linear:
0.001 counts/s/V
0.001*MOTOR.PITCH (mm/s)/V
0.998*MOTOR.PITCH (um/s)/V
0.005 to 5,000 [(PIN/POUT)/s]/V
Data Type Float
See Also Analog Input Block Diagram
Start Version M_0-0-15
```
#### Description

AIO.VSCALE is an analog velocity scale factor that scales:

1. The analog input (AIN.VALUE) for DRV.OPMODE = 2 (analog velocity mode)
2. The analog output (AOUT.VALUE) for AOUT.MODE = 1, 3, or 7. The value entered is the motor veloc-
    ity per 10 V of analog input or output. This value may be either higher or lower than the application
    velocity limit (VL.LIMITP or VL.LIMITN), but the actual analog I/O will be limited by VL.LIMITP or VL.LI-
    MITN.

```
AKD Parameter and Command Reference Guide | AIO Parameters
```

This page intentionally left blank.


## AOUT Parameters

### AOUT.MODE

```
General Information
Type NV Parameter
Description Sets the analog output mode.
Units N/A
Range 0 to 9
Default Value 0
Data Type Integer
See Also N/A
Start Version M_0-0-15
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 3470h/1
Data Type Integer 8
PDO Mappable N/A
Start Version M_00-00-62-000
```
#### Description

AOUT.MODE sets the analog output functionality.

```
AOUTx.MODE Description
0 User variable. The analog output signal is determined by the user (usingAOUT.VALUEU).
1 Actual velocity. The analog signal describes the current velocity value.
2 Velocity error. The analog signal describes the velocity error value.
3 Velocity command. The analog signal describes the velocity command value.
4 Actual current. The analog signal describes the actual current value.
5 Current command. The analog signal describes the current command value.
6 Actual position. The analog signal describes the current position value.
7 Position error. The analog signal describes the position error value.
8 Triangle wave. The analog signal is a triangle wave (sawtooth pattern).
9 Debug mode. In this mode the user can define a drive variable to monitor viathe analog output (AOUT.VALUEU).
```
#### Example

Using the command AOUT.VALUEU, you can implement a voltage output. As an example:

-->AOUT.MODE 0

-->AOUT.VALUEU 5

```
AKD Parameter and Command Reference Guide | AOUT Parameters
```

AKD Parameter and Command Reference Guide | AOUT Parameters

##### -->AOUT.VALUEU 4.33


### AOUT.OFFSET

```
General Information
Type NV Parameter
Description Sets the analog input offset.
Units V
Range -10 to +10 V
Default Value 0 V
Data Type Float
See Also N/A
Start Version M_00-00-65-000
```
#### Description

This parameter sets the analog input offset.

```
AKD Parameter and Command Reference Guide | AOUT Parameters
```

AKD Parameter and Command Reference Guide | AOUT Parameters

### AOUT.VALUE

```
General Information
Type N/V Parameter
Description Reads the analog output value.
Units V
Range –10 to +10 V
Default Value 0
Data Type Float
See Also N/A
Start Version M_0-0-15
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 3470h/2
Data Type Integer 16
PDO Mappable N/A
Start Version
```
#### Description

```
AOUT.VALUE reads the analog output value. This parameter can also be used to set the value of the analog
output when AOUT.MODE = 0 (analog output signal is determined by the user).
```

### AOUT.VALUEU

```
General Information
Type R/W parameter
Description Sets the analog output value.
Units V
Range –10 to +10 V
Default Value 0
Data Type Float
See Also N/A
Start Version M_00-00-50-000
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 3470h/3
Data Type Integer 16
PDO Mappable Yes
Start Version M_00-00-62-000
```
#### Description

AOUT.VALUEU reads/writes the analog output value whenAOUT.MODE= 0 (analog output signal is deter-
mined by the user).

```
AKD Parameter and Command Reference Guide | AOUT Parameters
```

AKD Parameter and Command Reference Guide | BODE Parameters

## BODE Parameters


### BODE.EXCITEGAP

```
General Information
Type R/W Parameter
Description Controls how often the excitation is updated.
Units Drive samples
Range 1 to 255 drive samples
Default Value 2 drive samples
Data Type N/A
See Also BODE.MODE
Start Version M_0-0-30
```
#### Description

BODE.EXCITEGAP controls how often the excitation is updated. The excitation is updated every n drive sam-
ples, where n is BODE.EXCITEGAP. For example, if BODE.EXCITEGAP = 2, then the excitation is updated
every 1 / (2 * 16000 Hz) = 1 / 8000 Hz = 0.000125 sec. When measuring a system, update the excitation only
as often as the data is recorded.

#### Example

Set excitation update rate to 8,000 Hz:

-->BODE.EXCITEGAP 2

Set excitation update rate to 4,000 Hz:

-->BODE.EXCITEGAP 4

Get excitation update rate (already set to 8000 Hz)

-->BODE.EXCITEGAP 2

```
AKD Parameter and Command Reference Guide | BODE Parameters
```

AKD Parameter and Command Reference Guide | BODE Parameters

### BODE.FREQ

```
General Information
Type R/W Parameter
Description Sets the frequency of the sine excitation source.
Units Hz
Range 0 to 8,000 Hz
Default Value 0 Hz
Data Type Float
See Also BODE.MODE BODE.INJECTPOINT, BODE.IAMP, BODE.VAMP
Start Version M_0-0-30
```
#### Description

```
BODE.FREQ sets the frequency of the sine excitation source in Hz. The sine excitation source is used to
take frequency response measurements of a system.
```
#### Example

```
Setting up a sine excitation source of 0.2 A at 50 Hz:
-->BODE.INJECTPOINT 1
-->BODE.IAMP 0.2
-->BODE.FREQ 50.0
-->BODE.MODE 2
```

### BODE.IAMP

```
General Information
Type R/W Parameter
Description Sets current command value used during the Bode procedure.
Units A
Range +/- Combined drive and motor current limit
Default Value 0.2 A
Data Type Float
See Also BODE.INJECTPOINT, BODE.FREQ
Start Version M_0-0-30
```
#### Description

BODE.IAMP sets the amplitude of the excitation when in current mode as set in BODE.INJECTPOINT.
When using BODE.MODE = 1 and BODE.INJECTPOINT = 1, this parameter will determine the level of noise
injected to commanded current value.

#### Example

Set the excitation current to 0.2 A

-->BODE.IAMP 0.2

Get the excitation current (already set to 0.2 A)

-->BODE.IAMP 0.200 [A]

```
AKD Parameter and Command Reference Guide | BODE Parameters
```

AKD Parameter and Command Reference Guide | BODE Parameters

### BODE.INJECTPOINT

```
General Information
Type R/W Parameter
Description Sets whether the excitation uses current or velocity excitation type.
Units N/A
Range 0 to 2
Default Value 0
Data Type Integer
See Also BODE.IAMP, BODE.MODE, BODE.VAMP
Start Version M_0-0-30
```
#### Description

```
BODE.INJECTPOINT sets whether the excitation uses current or velocity excitation type.
BODE.INJECTPOINT Description
0 None
1 Current
2 Velocity
```
#### Example

```
Set BODE.INJECTPOINT to current:
-->BODE.INJECTPOINT 1
Get BODE.INJECTPOINT (already set to current)
-->BODE.INJECTPOINT
1
```

### BODE.MODE

```
General Information
Type R/W Parameter
Description Sets the mode of the excitation.
Units N/A
Range 0 to 4
Default Value 0
Data Type Integer
See Also BODE.INJECTPOINTBODE.VAMP
Start Version M_0-0-30
```
#### Description

BODE.MODE sets the mode of the excitation.. The excitation can be set to the modes shown in the table
below. BODE.MODE is always set to **None** when Ethernet communication is disconnected. The peak ampli-
tude of the excitation is set by either BODE.IAMP or BODE.VAMP (depending on BODE.INJECTPOINT).

```
BODE.MODE Description Comments
0 None Turns all excitation off
```
##### 1 PRB

```
Uses Pseudo Random Binary (PRB)excitation. PRB is a
signal that is always +/- peak amplitude, varying only in
phase.
PRB excitation results in a flat excitation frequency spec-
trum. PRB results in a high peak excitation amplitude,
which can help minimize friction in a frequency response
test.
PRB excitation repeats every (2^BODE.PRBDEPTH) /
BODE.EXCITEGAP drive samples. This repetition can be
used to see through the effects of friction.
2 Sine Uses Sine excitation
3 Noise Uses Random Noise excitation. Noise is a random number
generator that varys between +/- peak amplitude.
4 Offset Sets a torque offset equal to BODE.IAMP
```
#### Example

Set BODE.MODE to PRB:

-->BODE.MODE 1

Get BODE.MODE (already set to PRB):

-->BODE.MODE

1

**PRB excitation:**

```
AKD Parameter and Command Reference Guide | BODE Parameters
```

AKD Parameter and Command Reference Guide | BODE Parameters

```
Sine excitation:
```

**Noise excitation:**

```
AKD Parameter and Command Reference Guide | BODE Parameters
```

AKD Parameter and Command Reference Guide | BODE Parameters

### BODE.PRBDEPTH

```
General Information
Type R/W Parameter
Description Sets the length of the PRB signal before it repeats.
Units NA
Range 4 to 19
Default Value 19
Data Type Integer
See Also BODE.MODE, BODE.INJECTPOINT, BODE.IAMP, BODE.VAMP
Start Version M_0-0-30
```
#### Description

```
BODE.PRBDEPTH sets the length of the PRB signal before it repeats. This applies only when BODE.MODE
= PRB. The PRB excitation will repeat after (2^BODE.PRBDEPTH) / BODE.EXCITEGAP drive samples.
```
#### Example

```
Set BODE.PRBDEPTH to 19:
-->BODE.PRBDEPTH 19
```
```
Get BODE.PRBDEPTH (already set to 19):
-->BODE.PRBDEPTH
19
```

### BODE.VAMP

```
General Information
Type R/W Parameter
Description Sets the amplitude of the excitation when in velocity mode.
Units rpm
Range 0 to maximum motor speed
Default Value 0
Data Type Float
See Also BODE.MODE, BODE.INJECTPOINT
Start Version M_0-0-30
```
#### Description

BODE.VAMP sets the amplitude of the excitation when in velocity mode as set in BODE.INJECTPOINT.

#### Example

Set the excitation velocity to 100 RPM

-->BODE.VAMP 100

Get the excitation velocity(already set to 100 RPM)

-->BODE.VAMP

100.000 [rpm]

```
AKD Parameter and Command Reference Guide | BODE Parameters
```

AKD Parameter and Command Reference Guide | CAP Parameters

## CAP Parameters

### CAP0.EDGE, CAP1.EDGE

```
General Information
Type R/W Parameter
Description Selects the capture edge.
Units N/A
Range 1 to 3
Default Value 1
Data Type U8
See Also CAP0.PREEDGE, CAP1.PREEDGE
Start Version M_0-0-50-0
```
#### Description

```
The filtered trigger source is monitored for rising edge, falling edge, or both edges. The event mode logic may
ignore the precondition edge detection; however, the trigger always uses edge detection.
The precondition logic has an identical feature controlled by CAP0.PREEDGE, CAP1.PREEDGE.
```
```
Value Description
0 Reserved
1 Rising edge
2 Falling edge
3 Both edges
```

### CAP0.EN, CAP1.EN

```
General Information
Type R/W Parameter
Description Enables or disables the related capture engine.
Units N/A
Range 0 to 1
Default Value 0
Data Type Boolean
See Also N/A
Start Version M_0-0-50-0
```
#### Description

This parameter enables or disables the related capture engine. After each successful capture event, this
parameter is reset to 0 and must be activated again for the next capture. Also note that CAP0.PLFB,
CAP1.PLFB is set to 0 when this parameter is set to 1.

0 = Disable

1 = Enable

```
AKD Parameter and Command Reference Guide | CAP Parameters
```

AKD Parameter and Command Reference Guide | CAP Parameters

### CAP0.EVENT, CAP1.EVENT

```
General Information
Type R/W Parameter
Description Controls the precondition logic.
Units N/A
Range 0 to 3
Default Value 0
Data Type U8
See Also N/A
Start Version M_0-0-50-0
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 3460h/5, 3460h/6
Data Type Unsigned 8
PDO Mappable N/A
Start Version M_00-00-62-000
```
#### Description

```
The event mode controls use of the precondition logic. The four event modes are listed below.
```
```
Event Description
0 Trigger Event = Trigger edge (ignore precondition)
1 Trigger Event = Trigger edge after precondition edge
2 Trigger Event = Trigger edge while precondition = 1
3 Trigger Event = Trigger edge while precondition = 0
```
#### Example

```
Event 0
The following diagram shows an example of Event = 0 (trigger on edge, trigger edge = rising). In this mode, the
precondition logic is ignored.
```

Figure 1: Trigger Edge Mode

**Events 2 and 3 (Trigger edge while precondition = 0 or 1)**

In these events, the precondition logic samples the current (post-filter) state of the selected precondition
source input. The capture engine looks for a trigger edge while the precondition input is at a “1” or “0” state.

Figure 2: Trigger edge WHILE precondition edge

**Event 1 (Trigger edge after precondition)**

In this event, each trigger event requires Enable=1, a new precondition edge, followed by a new trigger edge.
The sequence requirements are shown in the figure below.

```
AKD Parameter and Command Reference Guide | CAP Parameters
```

AKD Parameter and Command Reference Guide | CAP Parameters

```
Figure 3: Trigger edge after precondition edge
Note: If the precondition and trigger edges occur at the same time, it is not a valid trigger event. A subsequent
trigger edge must occur after the precondition edge. The same time resolves to a single 40 ns clock tick in the
trigger event logic (after the optional filter function as well as any sensor, cable, or noise delays).
```

#### CAP0.FILTER, CAP1.FILTER

```
General Information
Type R/W Parameter
Description Sets the filter for the capture source input.
Units N/A
Range 0 to 2
Default Value 0
Data Type U8
See Also CAP0.PREFILTER, CAP1.PREFILTER
Start Version M_0-0-50-0
```
#### Description

Anoptional glitchfilter maybe usedto debouncethe inputtrigger signals.By defaultthe filteris disabled.A 0.6
μsfilter maybe selectedfor fastsignals suchas RS422,or fastopto. A40 μsfilter maybe selectedfor slow
optoinputs. Exactvalues foreach filtermode arelisted below (the preconditionlogic hasan identicalfilter).

```
Filter Mode (if no
glitch)
```
```
Trigger Filter (filter
clock enable
period)
```
```
Filter Delay
```
```
Min
(μs)
```
```
Typical
(μs)
Max (μs) (μs)
off 0 N/A N/A N/A N/A
(default) 0 0 0 N/A N/A
fast 1 0.56 0.6 0.64 0.80
slow 2 35.84 38.4 40.96 5.12
```
The filter uses seven stages of delay when enabled. An input glitch restarts the filter delay. The clock enable
period for the seven stage filter is set to 0.080 us for the fast filter, 5.12 us for the slow filter. The filter delay for
a clean input edge is therefore an average of 7.5 periods (+/-0.5 period for worst case).

```
AKD Parameter and Command Reference Guide | CAP Parameters
```

AKD Parameter and Command Reference Guide | CAP Parameters

#### CAP0.MODE, CAP1.MODE

```
General Information
Type NV Parameter
Description Selects the captured value.
Units N/A
Range 0 to 3
Default Value 0
Data Type U8
See Also N/A
Start Version M_00-00-51-000
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 3460h/3, 3460h/4
Data Type Unsigned 8
PDO Mappable N/A
Start Version M_00-00-62-000
```
#### Description

```
Mode 0 is the standard position capture which stores PL.FB. Data can be retrieved with CAP0.PLFB,
CAP1.PLFB.
Mode 1 is the drive internal time capture. Data can be retrieved with CAP0.T, CAP1.T.
Mode 2 is the KMS EtherCAT distributed clock time (DCT) capture. Instead of using a position value, the
DCT is calculated. There is no user parameter to retrieve the captured DCT.
Mode3isthecaptureofprimaryencodersignal.Itisusedtohomeontoafeedbackindex.Mode3setsotherparam-
etersneededforthismode.Theseparameterscanbechangedafterwards,butthispracticeisnotrecommended.
```

#### CAP0.PLFB, CAP1.PLFB

```
General Information
Type R/O Parameter
Description Sets captured position value.
```
```
Units
```
```
Depends on UNIT.VROTARY or UNIT.VLINEAR
Rotary: counts, rad, deg, PIN/POUT, counts 16 bit
Linear: counts, mm, μm, PIN/POUT, counts 16 bit
Range Full range of a signed 64 bit variable
Default Value 0
Data Type S64
See Also UNIT.PROTARY, UNIT.PLINEAR
Start Version M_0-0-51-0-0
```
#### Description

This parameter sets the captured position value scaled to actual set units. See UNIT.PROTARY or
UNIT.PIN for these units.

```
AKD Parameter and Command Reference Guide | CAP Parameters
```

AKD Parameter and Command Reference Guide | CAP Parameters

#### CAP0.PREEDGE, CAP1.PREEDGE

```
General Information
Type R/W Parameter
Description Selects the capture precondition edge.
Units N/A
Range 1 to 3
Default Value 1
Data Type U8
See Also CAP0.EDGE, CAP1.EDGE
Start Version M_0-0-50-0
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 3460h/7, 3460h/8
Data Type Unsigned 8
PDO Mappable N/A
Start Version M_00-00-62-000
```
#### Description

```
The precondition edge is monitored for rising edge, falling edge, or both. The event mode logic may ignore the
precondition edge detection (trigger always uses edge detection).
The filtered trigger source has an identical feature controlled by CAP0.EDGE, CAP1.EDGE.
```
```
Value Description
0 Reserved
1 Rising edge
2 Falling edge
3 Both edges
```

#### CAP0.PREFILTER, CAP1.PREFILTER

```
General Information
Type R/W Parameter
Description Sets the filter for the precondition input source.
Units N/A
Range 0 to 2
Default Value 0
Data Type U8
See Also CAP0.FILTER, CAP1.FILTER
Start Version M_0-0-50-0
```
#### Description

You can use an optional glitch filter to debounce the input trigger signals. By default the filter is disabled. A 0.6
us filter may be selected for fast signals such as RS422, or fast opto. A 40 us filter may be selected for slow
opto inputs. Exact values for each filter mode are listed below.

```
Filter (if no
glitch)
```
```
Trigger Filter (filter clock enable
period)
Filter Delay (us)
Min TypMax
off 0 N/A N/A N/A N/A
(default) 0 0 0 N/A N/A
fast 1 0.56 0.6 0.64 0.80
slow 2 35.8438.440.96 5.12
```
The filter uses seven stages of delay when enabled. An input glitch restarts the filter delay. The clock enable
period for the seven-stage filter is set to 0.080 us for the fast filter, 5.12 us for the slow filter. The filter delay for
a clean input edge is therefore an average of 7.5 periods (+/- 0.5 period for worst case).

```
AKD Parameter and Command Reference Guide | CAP Parameters
```

AKD Parameter and Command Reference Guide | CAP Parameters

#### CAP0.PRESELECT, CAP1.PRESELECT

```
General Information
Type R/W Parameter
Description Sets the precondition trigger.
Units N/A
Range 0 to 11
Default Value 0
Data Type U8
See Also CAP0.TRIGGER, CAP1.TRIGGER
Start Version M_0-0-50-0
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 3460h/9, 3460h/10
Data Type Unsigned 8
PDO Mappable N/A
Start Version M_00-00-62-000
```
#### Description

```
This parameter specifies the input signal for the precondition trigger.
Trigger Source Input Name
0 General Input 1
1 General Input 2
2 General Input 3
3 General Input 4
4 General Input 5
5 General Input 6
6 General Input 7
7 RS485 Input 1
8 RS485 Input 2
9 RS485 Input 3
10 Primary Index
11 Tertiary Index
```

#### CAP0.STATE, CAP1.STATE

```
General Information
Type R/O Parameter
Description Indicates whether or not trigger source was captured.
Units N/A
Range 0 to 1
Default Value 0
Data Type Boolean
See Also N/A
Start Version M_0-0-50-0
```
#### Description

When enabling the capture (CAP0.EN, CAP1.EN), this parameter is set to 0 until the next event is captured.
0 = Not captured

1 = Captured

```
AKD Parameter and Command Reference Guide | CAP Parameters
```

AKD Parameter and Command Reference Guide | CAP Parameters

#### CAP0.T, CAP1.T

```
General Information
Type R/O Parameter
Description Reads time capture (if time capture was configured).
Units ns
Range N/A
Default Value N/A
Data Type U32
See Also CAP0.MODE, CAP1.MODE
Start Version M_0-0-50-0
```
#### Description

```
If time capture was configured, the captured time is stored in this parameter. The reference time is the occur-
rence of the last MTS signal (recurring every 62.5 μs), so this is a purely drive internal time.
```

#### CAP0.TRIGGER, CAP1.TRIGGER

```
General Information
Type R/W Parameter
Description Specifies the trigger source for the position capture.
Units N/A
Range 0 to 11
Default Value 0
Data Type U8
See Also CAP0.PRESELECT, CAP1.PRESELECT
Start Version M_0-0-50-0
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 3460h/1, 3460h/2
Data Type Unsigned 8
PDO Mappable N/A
Start Version M_00-00-62-000
```
#### Description

This parameter specifies the trigger source (capture input signal).

```
Trigger Source Input Name
0 General Input 1
1 General Input 2
2 General Input 3
3 General Input 4
4 General Input 5
5 General Input 6
6 General Input 7
7 RS485 Input 1
8 RS485 Input 2
9 RS485 Input 3
10 Primary Index
11 Tertiary Index
```
```
AKD Parameter and Command Reference Guide | CAP Parameters
```

AKD Parameter and Command Reference Guide | CS Parameters

### CS Parameters

```
Controlled stop (CS) parameters set the values for the controlled stop process.
```
#### CS.DEC

```
General Information
Type NV Parameter
Description Sets the deceleration value for the controlled stop process.
```
```
Units
```
```
Depends on UNIT.ACCROTARY or UNIT.ACCLINEAR
Rotary: rps/s, rpm/s, deg/s^2 , (PIN/POUT)/s^2 , rad/s^2
Linear: counts/s^2 , mm/s^2 , μm/s^2 , (PIN/POUT)/s^2
```
```
Range
```
```
Rotary:
0.031 to 833,333.333 rps/s
1.860 to 50,000,000.000 rpm/s
11.158 to 300,000,000.000 deg/s^2
0.155 to 4,166,666.752 (PIN/POUT)/s^2
0.195 to 5,235,987.968 rad/s^2
Linear:
0.000 to 833.333 Counts/s^2
0.031*MOTOR.PITCH to 833333.333*MOTOR.PITCH mm/s^2
30.994*MOTOR.PITCH to 833333333.333*MOTOR.PITCH μm/s^2
0.155 to 4,166,666.667 (PIN/POUT)/s^2
```
```
Default Value
```
```
Rotary:
50.000 rps/s
3000.000 rpm/s
18,000.000 deg/s^2
250.000 (PIN/POUT)/s^2
314.159 rad/s^2
Linear:
0.050 Counts/s^2
50.000*MOTOR.PITCH mm/s^2
50000.000*MOTOR.PITCH μm/s^2
250.000 (PIN/POUT)/s^2
Data Type Float
See Also CS.VTHRESH, CS.TO, CS.STATE
Start Version M_0-0-50-0
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 3440h/1
Data Type Unsigned 32
```

```
Fieldbus Information
PDO Mappable N/A
Start Version M_00-00-62-000
```
#### Description

This parameter sets the deceleration value for the controlled stop process.

See DRV.DISMODEfor more information about the controlled stop process.

```
AKD Parameter and Command Reference Guide | CS Parameters
```

AKD Parameter and Command Reference Guide | CS Parameters

#### CS.STATE

```
General Information
Type R/O Parameter
Description Returns the internal status of the controlled stop process.
Units N/A
Range N/A
Default Value N/A
Data Type N/A
See Also CS.DEC, CS.VTHRESH, CS.TO
Start Version M_0-0-50-0
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 3441h/0
Data Type Unsigned 8
PDO Mappable N/A
Start Version M_00-00-62-000
```
#### Description

```
CS.STATE returns the internal state machine value of the controlled stop. See DRV.DISMODEfor more infor-
mation about the controlled stop process.
```

#### CS.TMAX

```
General Information
Type NV Parameter
Description
Sets the time-out value for the drive to disable if velocity is not within
CS.VTHRESH.
Units ms
Range 1 to 30,000 ms
Default Value 1,000 ms
Data Type Integer
See Also CS.DEC, CS.VTHRESH, CS.TOCS.STATE
Start Version M_0-0-50-0
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 36DCh/0
Data Type Integer 32
PDO Mappable N/A
Start Version M_00-00-62-000
```
#### Description

CS.TMAX is the time-out value for the drive to disable if velocity is not within CS.VTHRESH. See DRV.DI-
SMODEfor more information about the controlled stop process.

#### Example

##### CS.TMAX 1000.

```
AKD Parameter and Command Reference Guide | CS Parameters
```

AKD Parameter and Command Reference Guide | CS Parameters

#### CS.TO

```
General Information
Type NV Parameter
Description Sets the time value for the drive velocity to be within CS.VTHRESH.
Units ms
Range 1 to 30,000 ms
Default Value 6 ms
Data Type Integer
See Also CS.DEC, CS.VTHRESH, CS.STATE
Start Version M_0-0-50-0
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 3440h/3
Data Type Unsigned 32
PDO Mappable N/A
Start Version M_00-00-62-000
```
#### Description

```
CS.TO is the time value for the drive velocity to be within CS.VTHRESH before the drive disables. See
DRV.DISMODEfor more information about the controlled stop process.
```
#### Example

##### CS.TO 100

#### CS.VTHRESH

```
General Information
Type NV Parameter
Description Sets the velocity threshold for the controlled stop.
Units rpm, rps, deg/s, (PIN/POUT)/s
Range 0.001 to 200.000 rpm
Default Value 120 rpm
Data Type Float
See Also CS.DEC, CS.TO, CS.STATE
Start Version M-0-0-50-0
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 3440h/2
Data Type Unsigned 32
PDO Mappable No
Start Version M_00-00-62-000
```

#### Description

CS.VTHRESH is the velocity threshold for the controlled stop algorithm. See DRV.DISMODEfor more infor-
mation about the controlled stop process.

#### Example

##### CS.VTHRESH 100

```
AKD Parameter and Command Reference Guide | CS Parameters
```

This page intentionally left blank.


### DIN Parameters

#### DIN.DIPSWITCH

```
General Information
Type R/O Parameter
Description Reads the DIP switch positions.
Units N/A
Range 0 to 15
Default Value N/A
Data Type Integer
See Also N/A
Start Version M_0-0-15
```
#### Description

DIN.DIPSWITCH reads the four DIP switch positions.

#### DIN.ROTARY

```
General Information
Type R/O Parameter
Description Reads the rotary knob value.
Units N/A
Range 0 to 99
Default Value N/A
Data Type Integer
See Also N/A
Start Version M_0-0-15
```
#### Description

DIN.ROTARY reads the rotary knob value.

```
AKD Parameter and Command Reference Guide | DIN Parameters
```

AKD Parameter and Command Reference Guide | DIN Parameters


#### DIN.STATES

```
General Information
Type R/O Parameter
Description Reads the digital input states.
Units N/A
Range 0000000 to 1111111
Default Value N/A
Data Type String
See Also N/A
Start Version M_0-0-15
```
#### Description

DIN.STATES reads the states of the seven digital inputs. The leftmost bit represents digital input 1 (DIN1)
and the rightmost bit represents digital input 7 (DIN7).

```
AKD Parameter and Command Reference Guide | DIN Parameters
```

AKD Parameter and Command Reference Guide | DIN Parameters

#### DIN1.INV TO DIN7.INV

```
General Information
Type R/W Parameter
Description Sets the indicated the polarity of a digital input mode.
Units N/A
Range 0 to 1
Default Value 0
Data Type Boolean
See Also N/A
Start Version M_00-00-51-000
```
#### Description

```
Sets the indicated the polarity of a digital input mode.
```
#### Example

```
DIN1.INV = 0 : Input is active high.
DIN1.INV = 1 : Input is active low.
```

#### DIN1.MODE TO DIN7.MODE

```
General Information
Type R/W Parameter
Description Sets the digital input modes.
Units N/A
Range 0 to 20
Default Value 0
Data Type Integer
See Also N/A
Start Version M_0-0-15
```
```
Fieldbus Information
EtherCAT COE & CANopen
```
```
Index/Subindex or
Parameter Number
```
```
DIN1.MODE: 3562h/0
DIN2.MODE: 3565h/0
DIN3.MODE: 3568h/0
DIN4.MODE: 356Bh/0
DIN5.MODE: 36F6h/0
DIN6.MODE: 36F9h/0
DIN7.MODE: 36FCh/0
Data Type Integer 32 (all)
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

DIN1.MODEtoDIN7.MODEparameterssetthefunctionalityofthedigitalinputs1through7.Digitalinputsand
correspondingX7andX8pinconnectorsaredescribedintheAKD InstallationManual,section8.16.4,Digital
Inputs.Thetablebelow summarizesthedigitalinputmodes;detaileddescriptionsofeachmodefollow thetable.

```
DINx.MODE Description
0 No function; off
1 Fault reset
2 Start motion task (use DINx.PARAM for this
task)
3 Motion task select bit
4 Motion task start selected
5 Start home
6 Start jog
7 Switch opmode
8 Zero latch
9 Reserved
10 Control fault relay
11 Home reference
13 Emergency stop
```
```
AKD Parameter and Command Reference Guide | DIN Parameters
```

AKD Parameter and Command Reference Guide | DIN Parameters

```
DINx.MODE Description
15 Quick stop
16 Activate electronic gearing
17 Activate electronic gear position shift
18 Positive limit switch
19 Negative limit switch
20 Brake release
```
```
Mode 0: Off
This mode is the non-use state. The AKD defaults to this setting.
Mode 1: Fault Reset
This mode is used to clear the drive faults. A change in state causes the drive to reset faults. This mode will
only correct non-fatal faults (see fault chart). Upon a rising edge a command, which is similar to
DRV.CLRFAULTS, is issued and faults are cleared
Mode 2: Start Motion Task
This mode is used to start motion task number X. This input will trigger a motion task number as defined in the
extra parameter field for this input.
X = the value of the associated input parameter.
It is assumed that motion task number X exists.
Example :
-->DIN1.MODE 2 - sets the input mode mode to be Start Motion Task
-->DIN1.PARAM 1 - sets the Motion Task to start to be 1
-->MT.LIST - make sure that Motion Task 1 does exist
1 0.000 [Counts] 1000.000 [rpm] 0 1001.358 [rpm/s] 1001.358 [rpm/s] 0 0 0 [ms]
<Create a rising edge of the input>
<Motion Task 1 executed>
Mode 3: Motion Task Select Bit
Thismode isused toselect themotion tasksthat arestored inthe drive(numbers 1to 127)or thereference trav-
erse/homing(0). Themotion tasknumber ispresented externallyat thedigital inputs.The motiontask setby
thismode willbe executedwhen digitalinput assignedto mode4 (motiontask startselected) getsa risingedge.
Example
Assume:
DIN1.MODE = DIN2.MODE
DIN3.MODE =3
The state of input 1 and 3 are 1
The state of input 2 is 0
that motion task 5 (2^0+2^2) will be executed.
Mode 4: Motion Task Start Selected
```

This mode is used to start the motion task that is stored in the servo amplifier, by giving the motion task
number. This input utilizes a secondary variable for the motion task number to be started with the Input trigger.
The secondary variable is set by mode 3 (Motion task select bit).
Motion task number “0” initiates homing/reference traverse. A rising edge starts the motion task and a falling
edge cancels the motion task.

**Mode 5: Start Motion Task Home**

This mode is used to start the homing motion task on the rising edge. The falling edge has no effect on this
input mode of operation.

**Mode 6: Start Jog**

This mode is used to start a jog move. This input mode utilizes a secondary variable for the jog’s velocity. The
jog will start upon a rising edge. A falling edge stops the jog.

**Mode 7: Switch Opmode**

This mode is used to switch between two pre-defined drive operation modes (current, velocity, position). This
input mode utilizes a secondary variable used to set the predefined opmodes to switch between the modes.

The secondary variable holds the value of 2 opmodes.
The tens digit holds the opmode to switch to upon falling edge.

The units digit holds the opmode to switch to upon rising edge.

For example:

```
If you need the opmode on falling edge to be 1 and the opmode on rising edge to be 2, then you
would set DINx.PARAM 12.
```
DINx.PARAM is shown in Workbench in the **Digital Inputs and Outputs** screen as the parameter "Param"
just to the right of the **Mode** combination box.

**Mode 8 – Zero Latch**

This mode is used to define the current drive position as the zero pulse for the drive EEO and sets the incre-
mental encoder zero pulse offset. The current position, depending on the incremental encoder resolution that
is set, is calculated at the rising edge and stored as an offset. An automatic save is then generated. This func-
tion is used to perform an automatic setting of the zero pulse in one turn of the motor.

**Mode 9: Reserved**

**Mode 10: Control Fault Relay**

This mode is used to create an external fault.

Input state is 0 – drive regular behavior

Input state is 1 – “Fault 245 – external fault” is issued.

**Mode 11: Home reference**

This mode is used to receive a physical home reference switch located on the machine to use for the different
Home Types.

**Mode 12: Position Latch**

The input latches the actual current position. The position can then be read in a stored variable.
The stored variable can be read by issuing the command CAP0.PLFB. (The command CAP0.EN 1 must be
issued prior to this)

```
AKD Parameter and Command Reference Guide | DIN Parameters
```

AKD Parameter and Command Reference Guide | DIN Parameters

```
Mode 13: Emergency Stop
This mode is used to stop the motor using the deceleration variable ramp. If zero velocity is reached, the
power stage is then disabled. Also see CS.XXX commands.
Mode 14: Reserved
Mode 15: Quick Stop
This mode is used to stop the motor. It is equivalent to issuing a DRV.STOP command.
Mode 16: Activate Electronic Gearing
This mode starts/activates an electronic gearing procedure upon a rising edge.
Mode 17: Activate Electronic Gear Position Shift
This mode is used to add a difference velocity to the gearing upon a rising edge. The velocity to add is set by a
secondary variable. The secondary variable is set by DINx.PARAM.
Mode 18: Positive Limit Switch
This mode will cause the input to operate as the CW limit switch. If the CW limit switch input is triggered
(goes low), the CW (positive) direction motion will then be stopped.
Mode 19: Negative Limit Switch
This mode will cause the input to operate as the CCW limit switch. If the CCW limit switch input is triggered
(goes low), the CCW (negative) direction motion will then be stopped.
Mode 20: Brake Release
This mode is used to lift the brake when the drive is not active.
Input = 0: the drive controls the brake (regular drives behavior)
Input = 1: the user controls the brake (lift or close using commands)
```

#### DIN1.PARAM TO DIN7.PARAM

```
General Information
Type R/W Parameter
Description Sets a value used as an extra parameter for digital inputs nodes.
Units N/A
Range -9,223,372,036,854,775,000 to +9,223,372,036,854,775,000
Default Value 0
Data Type Float
See Also N/A
Start Version M_0-0-50-0
```
#### Description

This parameter sets a value that is used as an extra parameter for digital inputs nodes.

#### Example

The digital input mode "Start motion task" is used to start a motion task. This mode uses an extra parameter
as the ID of the motion task to be started.

```
AKD Parameter and Command Reference Guide | DIN Parameters
```

AKD Parameter and Command Reference Guide | DIN Parameters

#### DIN1.STATE to DIN7.STATE

```
General Information
Type R/O Parameter
Description Reads a specific digital input state.
Units N/A
Range 0 to 1
Default Value N/A
Data Type Boolean
See Also N/A
Start Version M_0-0-15
```
#### Description

```
DIN1.STATE to DIN7.STATE reads the state of one digital input according to the number identified in the
command.
```

### DOUT Parameters

#### DOUT.CTRL

```
General Information
Type NV Parameter
Description Sets the source of digital outputs (firmware or fieldbus).
Units N/A
Range 0 to 1
Default Value 0
Data Type Boolean
See Also N/A
Start Version M_0-0-15
```
#### Description

DOUT.CTRL sets the source of the digital outputs:

0 = Firmware controlled

1 = Fieldbus controlled

```
AKD Parameter and Command Reference Guide | DOUT Parameters
```

AKD Parameter and Command Reference Guide | DOUT Parameters

#### DOUT.RELAYMODE

```
General Information
Type R/W Parameter
Description Indicates faults relay mode.
Units N/A
Range 0 to 1
Default Value 0
Data Type Boolean
See Also N/A
Start Version M_00-00-51-000
```
#### Description

```
DOUT.RELAYMODE indicates the faults relay mode as follows:
If DOUT.RELAYMODE= 0 and faults exist, then the relay is open.
If DOUT.RELAYMODE= 0 and faults do not exist - relay closed.
```
```
If DOUT.RELAYMODE = 1 and the drive is disabled, then the relay is open.
If DOUT.RELAYMODE = 1 and the drive is enabled, then the relay is closed.
```

#### DOUT.STATES

```
General Information
Type R/O Parameter
Description Reads the state of the two digital outputs.
Units N/A
Range 0 to 11
Default Value N/A
Data Type String
See Also N/A
Start Version M_0-0-15
```
#### Description

DOUT.STATES reads the states of the two digital outputs. The rightmost bit represents DOUT2 and the left-
most bit represents DOUT1.

```
AKD Parameter and Command Reference Guide | DOUT Parameters
```

AKD Parameter and Command Reference Guide | DOUT Parameters

#### DOUTx.MODE

```
General Information
Type NV Parameter
Description Sets the digital output mode.
Units N/A
Range 0 to 11
Default Value 0
Data Type Integer
See Also N/A
Start Version M_0-0-15
```
#### Description

```
DOUTx.MODE sets the functionality of the digital outputs. The table below summarizes the digital output
modes; detailed descriptions of each mode follow the table.
```
```
DOUTx.MODE Description
0 User (default = 0)
2 Software limit switch reached
3 Move complete
4 In position
5 Position greater than x
6 Position less than x
7 Drive produced warning
8 Drive enabled
10 Motor brake
11 Drive produced fault
12 Absolute velocity greater than x
13 Absolute velocity less than x
```
```
Mode 0: User
The output state is decided by user or fieldbus.
Mode 1: Reserved
Mode 2: Software limit
This output mode produces a high signal if a software limit-switch is reached. A move or motion task in the
opposite direction resets the output.
Mode 3: Move complete
This output mode produces a high signal if a position move is completed.
Mode 4: In position
This output mode produces a high signal when the absolute value of the position error in less than a variable x.
Use DOUTx.PARAM to set x.
Mode 5: Position greater than x
```

This output mode produces a high-signal if a position value exceeds the variable x.

Use DOUTx.PARAM to set x.

**Mode 6: Position less than x**

This output mode produces a high signal if a position value is less than the variable x. Use DOUTx.PARAM to
set x.

**Mode 7: Warning**

The output mode produces a high signal if the drive has a warning.

**Mode 8: Enable**

The output mode produces a high signal if the drive is enabled.

**Mode 9: Reserved**

**Mode 10: Motor Brake**

The output mode produces a high signal if a brake is disengaged. The output mode produces a low if a brake is
engaged.

**Mode 11: Drive Faults**

The output mode produces a high signal if the drive has a fault.

```
AKD Parameter and Command Reference Guide | DOUT Parameters
```

AKD Parameter and Command Reference Guide | DOUT Parameters

#### DOUT1.PARAM AND DOUT2.PARAM

```
General Information
Type NV Parameter
Description Sets extra parameters for the digital outputs.
Units N/A
Range –9,223,372,036,854,775,808 to +9,223,372,036,854,775,807
Default Value 0
Data Type Integer
See Also N/A
Start Version M_0-0-15
```
#### Description

```
DOUT1.PARAM and DOUT2.PARAM set the extra parameter needed for the digital outputs calculations,
respectively.
```

#### DOUT1.STATE AND DOUT2.STATE

```
General Information
Type R/O Parameter
Description Reads the digital output state.
Units N/A
Range 0 to 1
Default Value N/A
Data Type Boolean
See Also N/A
Start Version M_0-0-15
```
#### Description

DOUT1.STATEandDOUT2.STATEreadthestateofonedigitaloutputaccordingtothevaluestatedinthecom-
mand.Theseparameterscanalsobeusedtosetavalueofonedigitaloutput(onlyiftheoutputmodeisidle).

```
AKD Parameter and Command Reference Guide | DOUT Parameters
```

This page intentionally left blank.


### DRV Parameters and Commands

#### DRV.ACC

```
General Information
Type NV Parameter
Description Describes the acceleration ramp for the velocity loop.
```
```
Units
```
```
Depends on UNIT.ACCROTARY or UNIT.ACCLINEAR
Rotary: rps/s, rpm/s, deg/s², (PIN/POUT)/s² , rad/s²
Linear: counts/s² , mm/s² , μm/s² , (PIN/POUT)/s²
```
```
Range
```
```
Rotary:
0.031 to 833333.333 rps/s
1.860 to 50000000.000 rpm/s
11.158 to 300000000.000 deg/s²
0.155 to 4166666.752 (PIN/POUT)/s²
0.195 to 5235987.968 rad/s²
Linear:
0.000 to 833.333 counts/s²
0.031*MOTOR.PITCH to 833333.333*MOTOR.PITCH mm/s²
30.994*MOTOR.PITCH to 833333333.333*MOTOR.PITCH μm/s²
0.155 to 4166666.667 (PIN/POUT)/s²
```
```
Default Value
```
```
Rotary:
50.000 rps/s
3000.000 rpm/s
18,000.000 deg/s²
250.000 (PIN/POUT)/s²
314.159 rad/s²
Linear:
0.050 counts/s²
1.000*MOTOR.PITCH mm/s²
1000.000*MOTOR.PITCH μm/s²
250.000 (PIN/POUT)/s²
Data Type Float
See Also DRV.DEC, UNIT.ACCLINEAR, UNIT.ACCROTARY
Start Version M_0-0-15
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 3501h/0
Data Type Integer 32
```
```
AKD Parameter and Command Reference Guide | DRV Parameters and Commands
```

AKD Parameter and Command Reference Guide | DRV Parameters and Commands

```
Fieldbus Information
PDO Mappable N/A
Start Version M_00-00-62-000
```
#### Description

```
Describes the acceleration ramp for the velocity central loop.
```

#### DRV.ACTIVE

```
General Information
Type R/O Parameter
Description Reads the enable status of an axis.
Units N/A
Range 0 to 1
Default Value N/A
Data Type Boolean
See Also DRV.EN,DRV.DISSOURCES
Start Version M_0-0-15
```
#### Description

DRV.ACTIVE reads the enable status of an axis.
0 = Axis disabled

1 = Axis enabled.

If an axis is not enabled (DRV.ACTIVE is 0), but DRV.EN is 1 and the hardware enable is high, read the value
of DRV.DISSOURCES to query the reason that the drive is not enabled.

```
AKD Parameter and Command Reference Guide | DRV Parameters and Commands
```

AKD Parameter and Command Reference Guide | DRV Parameters and Commands

## DRV.BLINKDISPLAY

```
General Information
Type Command
Description Causes the display to blink for 10 seconds.
Units N/A
Range N/A
Default Value N/A
Data Type N/A
See Also N/A
Start Version M_0-0-15
```
#### Description

```
DRV.BLINKDISPLAY causes the drive display located on the front of the drive to blink for 10 seconds.
This command allows the user to identify the drive that is currently communicating with WorkBench.
```

## DRV.CLRFAULTHIST

```
General Information
Type Command
Description Clears the fault history log in the NV.
Units N/A
Range N/A
Default Value N/A
Data Type N/A
See Also DRV.FAULTHIST
Start Version M_0-0-15
```
#### Description

DRV.CLRFAULTHIST clears the fault history from the nonvolatile memory of the drive.
This command erases all faults returned by DRV.FAULTHIST.

```
AKD Parameter and Command Reference Guide | DRV Parameters and Commands
```

AKD Parameter and Command Reference Guide | DRV Parameters and Commands

## DRV.CLRFAULTS

```
General Information
Type Command
Description Tries to clear all active faults in the drive.
Units N/A
Range N/A
Default Value N/A
Data Type N/A
See Also DRV.FAULTS, DRV.EN, DRV.DIS
Start Version M_0-0-15
```
#### Description

```
DRV.CLRFAULTS tries to clear all active faults in the drive. If the command succeeds, then the reply to
DRV.FAULTS states that no faults exist. If the command fails, then the fault condition is still present.
When a fault occurs, the fault is registered in the drive fault handler. DRV.CLRFAULTS clears the fault from
the drive fault handler. However, if the fault still exists in the system, DRV.CLRFAULTS fails and the fault is
re-registered in the fault handler.
Note that executing a drive disable (DRV.DIS) followed by a drive enable (DRV.EN) has the same effect as
executing DRV.CLRFAULTS.
```

## DRV.CMDSOURCE

```
General Information
Type NV Parameter
Description
Sets the command source (service, fieldbus, analog input, gearing, digital,
or Bode).
Units N/A
Range 0 to 3
Default Value 0
Data Type Integer
See Also DRV.OPMODE
Start Version M_0-0-15
```
#### Description

DRV.CMDSOURCE specifies the source of the command to the drive. DRV.OPMODE sets the operation
mode to the relevant control loop.

The DRV.CMDSOURCE values can be set as follows:

```
Value Description
0 TCP/IP command
1 Fieldbus command
2 Gearing command
3 Analog command
4 Digital command
5 Sine-sweep Bode plot command
```
#### Example

To set the command source to the TCP/IP channel and the operation mode to velocity:

```
-->DRV.CMDSOURCE 0
-->DRV.OPMODE 1
```
```
AKD Parameter and Command Reference Guide | DRV Parameters and Commands
```

AKD Parameter and Command Reference Guide | DRV Parameters and Commands

## DRV.CRASHDUMP

```
General Information
Type Command
Description Retrieves diagnostic information after the drive crashes.
Units N/A
Range N/A
Default Value N/A
Data Type N/A
See Also N/A
Start Version M_0-0-50-0
```
#### Description

```
Drivesrarely crash,but ifa crashoccurs, informationthat canhelp diagnosethe causeof acrash issaved to
thenonvolatile (NV)memory withinthe drive.After thedrive isrestarted, youcan usethe DRV.CRASHDUMP
commandto retrievethis diagnosticinformation, whichcan beemailed toKollmorgen forfurther support.
If the drive crashes (display flashes an F and three bars), it saves the diagnostic information to a specific
block of the drive NV memory. The DRV.CRASHDUMP command then prints the diagnostic information from
this NV memory block. Subsequent crash conditions will overwrite the NV memory block. Since the NV mem-
ory block is overwritten, but never erased, the DRV.CRASHDUMP command always shows the diagnostic
information for the most recent crash.
```

## DRV.DBILIMIT

```
General Information
Type NV Parameter
Description Sets the maximum amplitude of the current for dynamic braking.
Units Arms
Range 0 to 2 Arms
Default Value 1 Arms
Data Type Float
See Also DRV.DISMODE
Start Version M-0-0-50
```
#### Description

This parameter sets the maximum amplitude of the current for dynamic braking.

#### Example

Setting DRV.DBILIMIT to 2 limits the dynamic brake current to 2 Arms.

```
AKD Parameter and Command Reference Guide | DRV Parameters and Commands
```

AKD Parameter and Command Reference Guide | DRV Parameters and Commands

## DRV.DEC

```
General Information
Type NV Parameter
Description Sets the deceleration value for the velocity loop.
```
```
Units
```
```
Depends on UNIT.ACCROTARY or UNIT.ACCLINEAR
Rotary: rps/s, rpm/s, deg/s², (PIN/POUT)/s², rad/s²
Linear: counts/s², mm/s², μm/s², (PIN/POUT)/s²
```
```
Range
```
```
Rotary:
0.031 to 833,333.333 rps/s
1.860 to 50,000,000.000 rpm/s
11.158 to 300,000,000.000 deg/s²
0.155 to 4,166,666.752 (PIN/POUT)/s²
0.195 to 5,235,987.968 rad/s²
Linear:
0.000 to 833.333 counts/s²
0.031*MOTOR.PITCH to 833,333.333*MOTOR.PITCH mm/s²
30.994*MOTOR.PITCH to 833,333,333.333*MOTOR.PITCH μm/s²
0.155 to 4,166,666.667 (PIN/POUT)/s²
```
```
Default Value
```
```
Rotary:
50.000 rps/s
3,000.000 rpm/s
18,000.000 deg/s²
250.000 (PIN/POUT)/s²
314.159 rad/s²
Linear:
0.050 counts/s²
1.000*MOTOR.PITCH mm/s²
1,000.000*MOTOR.PITCH μm/s²
250.000 (PIN/POUT)/s²
Data Type Float
See Also DRV.ACC, UNIT.ACCROTARY, UNIT.ACCLINEAR, DRV.OPMODE
Start Version M_0-0-15
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 3522h/0
Data Type Integer 32
PDO Mappable N/A
Start Version M_00-00-62-000
```
#### Description

```
DRV.DEC sets the deceleration value for the velocity loop command (VL.CMDU) and for the analog
```

velocity command (AIN.VALUE). The operation mode (DRV.OPMODE) must be set to velocity mode for this
command to function.

```
AKD Parameter and Command Reference Guide | DRV Parameters and Commands
```

AKD Parameter and Command Reference Guide | DRV Parameters and Commands

## DRV.DIR

```
General Information
Type R/W Parameter
Description Changes drive direction.
Units N/A
Range 0 to 1
Default Value 0
Data Type Integer
See Also N/A
Start Version M_0-0-38
```
```
Fieldbus Information
EtherCAT COE & CANOpen
Index/Subindex or
Parameter Number 352Ah/0
Data Type Integer 32
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

```
DRV.DIR changes the direction of the motor by changing the algebraic sign of the current command and posi-
tion feedback value according to the figure below.
Note the following when using DRV.DIR:
 You can only change the DRV.DIR command when the drive is disabled.
 The drive status changes to "Axis not homed" as soon as the DRV.DIR parameter changes value (see
DRV.MOTIONSTAT).
 You must verify the settings of the hardware limit switches. If necessary, switch the CW and CCW
hardware limit switches by swapping the wires at the digital inputs.
```

AKD Parameter and Command Reference Guide | DRV Parameters and Commands


AKD Parameter and Command Reference Guide | DRV Parameters and Commands

## DRV.DIS

```
General Information
Type Command
Description Disables the axis (software).
Units N/A
Range N/A
Default Value Analog drive software enabled. All other types of drive software disabled.
Data Type N/A
```
```
See Also
```
##### DRV.EN, DRV.DISSOURCES, DRV.ACTIVE, DRV.DISMODE,

##### DRV.DISTO

```
Start Version M_0-0-15
```
#### Description

```
DRV.DIS issues a software disable to the drive. The method how the drive will be disabled, immediately or
with a ramp down first is controlled by DRV.DISMODE!
By querying the value of DRV.ACTIVE, you can check whether the drive is currently enabled or disabled.
ByqueryingthevalueofDRV.DISINPUTS,youcancheckwhetherthesoftwareenablebitishigh(softwareenabled
was issued by executing DRV.EN) or the software enable bit is low (software disable was issued by execut-
ing DRV.DIS)
If DRV.DIS is commanded the emergency timeout is started. If the drive does not disable or activate
dynamic brake within DRV.DISTO, the fault F703 is reported.
```

## DRV.DISMODE

```
General Information
Type NV Parameter
Description Sets disable type to either dynamic brake or immediate disable.
Units NA
Range 0 to 3
Default Value 0
Data Type Integer
See Also DRV.DBILIMIT ,DRV.DISTO, CS.VTHRESH
Start Version M-0-0-50
```
#### Description

Sets the drive reaction a DRV.DIS command.

#### Example

DRV.DISMODE 0 - Disable axis immediately.

**Be careful with vertical loads**

DRV.DISMODE 1 - Use dynamic brake to ramp down. PWM stays active afterwards.

DRV.DISMODE 2 - Use active disable to ramp down and then disable the drive.

DRV.DISMODE 3 - Use active disable to ramp down and use dynamic brake afterwards. PWM stays ena-
bled.

In all cases described above, if a brake is configured (MOTOR.BRAKE), the brake closes if VL.FB drops
below CS.VTHRESH.

For more information about active disable, please consult the CS.x parameters.

```
AKD Parameter and Command Reference Guide | DRV Parameters and Commands
```

AKD Parameter and Command Reference Guide | DRV Parameters and Commands

## DRV.DISSOURCES

```
General Information
Type R/O Parameter
Description Returns the possible reason for a drive disable.
Units N/A
Range N/A
Default Value N/A
Data Type N/A
See Also DRV.ACTIVE, DRV.FAULTS, DRV.EN, DRV.DIS
Start Version M_0-0-15
```
#### Description

```
DRV.DISSOURCES is a bitwise parameter that returns the status of possible causes of a drive disable. If
this parameter is 0, then the drive is enabled, but the software is disabled.
The return value specific bits are as follows:
```
```
Bit Status and Response
0 Software disable (execute DRV.EN to issue software enable)
1 Fault exists (read DRV.FAULTS to get the active faults)
2 Hardware disable (remote enable input is low)
3 In-rush disable (the in-rush relay is opened)
4 Initialization disable (the drive did not finish the initialization process)
5 Controlled stop disable from a digital input.
```

## DRV.DISTO

```
General Information
Type R/W Parameter
Description Sets the emergency timeout
Units ms
Range 500 to 120,000 ms
Default Value 1,000 ms
Data Type U32
See Also DRV.DIS, DRV.DISMODE
Start Version M-0-0-55
```
#### Description

This timer starts when DRV.DIS is issued (regardless of the DRV.DIS origin). After this timeout elapses, the
actual state of the drive is compared to the DRV.DISMODE setting. If the actual state does not match the
DRV.DISMODE setting, a fault is reported and the hardware immediately executes the DRV.DISMODE set-
ting (for instance, disable or activate dynamic brake).

```
AKD Parameter and Command Reference Guide | DRV Parameters and Commands
```

AKD Parameter and Command Reference Guide | DRV Parameters and Commands

## DRV.EMUEDIR

```
General Information
Type R/W Parameter
Description Sets the direction of the emulated encoder output (EEO) signal.
Units N/A
Range 0 to 1
Default Value 0
Data Type N/A
See Also DRV.EMUEMODE
Start Version M_0-0-59
```
#### Description

```
Allows the user to change the direction of the emulated encoder output. DRV.DIR has also an affect on the
this direction (it is XORed with this parameter).
```

## DRV.EMUEMODE

```
General Information
Type R/W Parameter
Description Sets the mode of the emulated encoder output (EEO) connector.
Units N/A
Range 0 to 5
Default Value 0
Data Type Integer
See Also DRV.EMUERES, DRV.EMUEZOFFSET, DRV.EMUEMTURN
Start Version M_0-0-50-0
```
#### Description

This parameter sets the EEO connector to act as either an input or output as follows:

```
Setting Function
0 EEO connector is not operative.
1 Output, with once per rev index pulse.
2 Output, with absolute index pulse.
3 Input, A/B signals.
4 Input, step and direction signals.
5 Input, up-down signals.
```
```
AKD Parameter and Command Reference Guide | DRV Parameters and Commands
```

AKD Parameter and Command Reference Guide | DRV Parameters and Commands

## DRV.EMUEMTURN

```
General Information
Type R/W Parameter
Description
Defines the location of the index pulse on the EEO (emulated encoder out-
put) when DRV.EMUEMODE=2.
Units counts
Range 0 to 4,294,967,295
Default Value 0
Data Type Integer
See Also DRV.EMUEMODE, DRV.EMUERES
Start Version M_0-0-50-0
```
#### Description

```
If the EEO mode with absolute index is selected (DRV.EMUEMODE=2), the index will be output when the
feedback position (in counts) matches this parameter.
```

## DRV.EMUERES

```
General Information
Type R/W Parameter
Description Sets the resolution of the EEO (emulated encoder output).
Units Lines per revolution
Range 0 to 65,535 lines per revolution
Default Value 0 lines per revolution
Data Type Integer
See Also DRV.EMUEMODE
Start Version M_0-0-50-0
```
#### Description

This parameter sets the EEO resolution. DRV.EMUERES also defines how many lines are output for 1 rev-
olution of the primary feedback (when this port is configured as an output), or how many lines will be con-
sidered a full revolution of the handwheel (when this port is configured as an input).

```
AKD Parameter and Command Reference Guide | DRV Parameters and Commands
```

AKD Parameter and Command Reference Guide | DRV Parameters and Commands

## DRV.EMUEZOFFSET

```
General Information
Type R/W Parameter
Description
Sets the location of the EEO (emulated encoder output) index pulse (when
DRV.EMUEMODE=1).
Units 1/65536 rev
Range 0 to 65535 rev
Default Value 0 rev
Data Type Integer
See Also DRV.EMUEMODE, DRV.EMUEMTURN
Start Version M_0-0-50-0
```
#### Description

```
When EEO multiturn is selected (DRV.EMUEMODE=1), this parameter sets a position of the EEO index.
When the primary feedback position (within a revolution) equals this value, an index pulse will output.
```

## DRV.EN

```
General Information
Type Command
Description Enables the axis (software).
Units N/A
Range N/A
```
```
Default Value
```
```
Analog drive software is enabled.
All other types of drive software are disabled.
Data Type N/A
See Also DRV.DIS, DRV.DISSOURCES DRV.ACTIVE
Start Version M_0-0-15
```
#### Description

DRV.EN issues a software enable to the drive. You can query the value of DRV.ACTIVE to check whether
the drive is currently enabled or disabled.

You can also query the value of DRV.DISSOURCES to check whether the software enable bit is high (soft-
ware enabled was issued by executing DRV.EN) or the software enable bit is low (software disable was
issued by executing DRV.DIS). If the drive software enable bit is low and DRV.EN is executed, then drive
faults are automatically cleared during the software enable process.

```
AKD Parameter and Command Reference Guide | DRV Parameters and Commands
```

AKD Parameter and Command Reference Guide | DRV Parameters and Commands

## DRV.ENDEFAULT

```
General Information
Type R/W Parameter
Description Sets the default state of the software enable
Units N/A
Range 0-SWEN=0 to 1-SWEN=1
Default Value 0
Data Type Boolean
See Also N/A
Start Version M-0-30-00
```
#### Description

```
DRV.ENDEFAULT sets the default state of the software enable.
```

## DRV.FAULTHIST

```
General Information
Type R/O Parameter
Description Reads the last 10 faults from NV memory.
Units N/A
Range N/A
Default Value N/A
Data Type N/A
See Also DRV.FAULTS, DRV.CLRFAULTHIST
Start Version M_0-0-15
```
#### Description

DRV.FAULTHISTORY returns the last 10 faults that occurred in the drive. The faults are shown with their
fault number (which matches the one displayed on the drive display) and a time stamp that indicates when
they last occurred.

Issue a DRV.CLRFAULTHIST to clear this fault log.

```
AKD Parameter and Command Reference Guide | DRV Parameters and Commands
```

AKD Parameter and Command Reference Guide | DRV Parameters and Commands

## DRV.FAULTS

```
General Information
Type R/O Parameter
Description Reads the active faults.
Units N/A
Range N/A
Default Value N/A
Data Type N/A
See Also DRV.CLRFAULTS, DRV.FAULTHIST, DRV.CLRFAULTHIST
Start Version M_0-0-15
```
#### Description

```
DRV.FAULTS returns a list of all currently active faults in the system, preceded by their fault number which
matches the number displayed on the drive display.
To clear the faults, either issue a DRV.CLRFAULTS or issue a DRV.DIS followed by DRV.EN.
If no active faults are in the system, then after executing DRV.CLRFAULTS the value read by DRV.FAULTS
is "No faults active".
```
#### Example

##### -->DRV.FAULTS

```
502: Bus under voltage.
-->
```

## DRV.HANDWHEEL

```
General Information
Type R/O Parameter
Description Reads the EEO input value.
Units 1/4,294,967,296 rev
Range 0 to 4,294,967,295 rev
Default Value 0 rev
Data Type Integer
See Also DRV.EMUERES, DRV.EMUEMODE
Start Version M_0-0-50-0
```
#### Description

When the EEO is selected as an input (DRV.EMUEMODE=3,4,5), this parameter reads the EEO value
(where 4,294,967,296 is a full revolution, then the value rolls over). DRV.EMUERES defines the how many
counts constitute a revolution on the EEO.

```
AKD Parameter and Command Reference Guide | DRV Parameters and Commands
```

AKD Parameter and Command Reference Guide | DRV Parameters and Commands

## DRV.HELP

```
General Information
Type R/O Parameter
Description
Reads the minimum, maximum, and default values for a specific param-
eter or command.
Units N/A
Range N/A
Default Value N/A
Data Type N/A
See Also N/A
Start Version M_0-0-15
```
#### Description

```
This parameter returns more information about a specific parameter or command.
In most cases, except special parameters, this command tells you the minimum, maximum, default, and
actual value of a parameter. Exceptions are commands that do not have these values (such as DRV.EN) or
information commands (such as DRV.VER).
```

## DRV.HELPALL

```
General Information
Type R/O Parameter
Description
Retrieves the minimum, maximum, default, and actual values for all avail-
able parameters and commands.
Units N/A
Range N/A
Default Value N/A
Data Type N/A
See Also N/A
Start Version M_0_0_38
```
#### Description

```
This parameter retrieves all information about all parameters and commands in the firmware. In most cases,
DRV.HELPALL returns the minimum, maximum, default, and actual value for each parameter and command.
Exceptions include parameters and commands that do not have these values (such as DRV.EN) or pure
INFO commands (such as DRV.VER).
```
```
AKD Parameter and Command Reference Guide | DRV Parameters and Commands
```

AKD Parameter and Command Reference Guide | DRV Parameters and Commands

## DRV.ICONT

```
General Information
Type R/O Parameter
Description Reads the continuous rated current value.
Units A
Range N/A
Default Value N/A
Data Type Float
See Also DRV.IPEAK
Start Version M_0-0-15
```
#### Description

```
DRV.ICONT returns the drive continuous rated current in amperes.
The value of the continuous current is read automatically on drive boot from the power EEPROM of the drive.
This value cannot be modified.
```

## DRV.INFO

```
General Information
Type R/O Parameter
Description Reads general information about the drive.
Units N/A
Range N/A
Default Value N/A
Data Type String
See Also N/A
Start Version M_0-0-15
```
#### Description

DRV.INFO returns general information about the drive.

#### Example

```
Danaher Motion - Digital Servo Drive
----------------------------------------------------------------------
Drive mode : AKD-B00606-NAAN-0000
Continuous current : 12.000 A
Peak current: 30.000 A
Mac address: 00.23.1B.00.00.16
FPGA size: 1600
Fieldbus type: Analog
Power type : MV - Medium Voltage
Product serial number: 16777215
Product manufacturing date code : 65535
Power board serial number : 0
Power board manufacturing date code: 0
Control board serial number: 0
Control board manufacturing date code: 0
Option board serial number: 0
Option board manufacturing date code: 0
```
```
AKD Parameter and Command Reference Guide | DRV Parameters and Commands
```

AKD Parameter and Command Reference Guide | DRV Parameters and Commands

## DRV.IPEAK

```
General Information
Type R/O Parameter
Description Reads the peak rated current value.
Units A
Range N/A
Default Value N/A
Data Type Float
See Also DRV.ICONT
Start Version M_0-0-15
```
#### Description

```
DRV.IPEAK returns the drive peak rated current in amperes.
The value of the peak current is read automatically on drive boot from the power EEPROM of the drive. This
value cannot be modified.
```

## DRV.IZERO

```
General Information
Type R/W Parameter
Description Sets the current that will be used during the DRV.ZERO procedure.
Units A
Range Drive peak current to 0 A
Default Value 0 A
Data Type Float
See Also DRV.ZERO
Start Version M_0-0-50-0
```
#### Description

This parameter sets the current that is used during the DRV.ZERO procedure.

```
AKD Parameter and Command Reference Guide | DRV Parameters and Commands
```

AKD Parameter and Command Reference Guide | DRV Parameters and Commands

## DRV.LIST

```
General Information
Type R/O Parameter
Description Reads the list of available parameters and commands.
Units N/A
Range N/A
Default Value N/A
Data Type String
See Also N/A
Start Version M_0-0-15
```
#### Description

```
DRV.LIST reads the list of available commands and parameters from the drive.
To filter this list, enter DRV.LIST followed by the prefix of the commands and parameters that you wish
to display.
```
#### Example

```
Return a list of all available commands in the system:
-->DRV.LIST
Return all commands with the prefix DRV:
-->DRV.LIST DRV
```
## DRV.LOGICVOLTS

```
General Information
Type R/O Parameter
Description Reads the logic voltages.
Units mv , Ω
Range N/A
Default Value N/A
Data Type String
See Also N/A
Start Version M_0-0-15
```
#### Description

```
DRV.LOGICVOLTS reads the logic voltages data of 1.2 V, 2.5 V, 3.3 V, 5 V, 12 V, –12 V, and 3.3 AV.
```
#### Example

```
Below is an example of the output for this command:
ch0 = 1.2V : 1211 mv
ch1 = 2.5V :2488 mv
ch2 = 3.3V :3274 mv
```

ch3 = 5V :4950 mv

ch4 = 12V :11892 mv

ch5 = -12V :-11912 mv

ch6 = 3.3AV :3300 mv

ch7 = R ohm :100000 ohm

```
AKD Parameter and Command Reference Guide | DRV Parameters and Commands
```

AKD Parameter and Command Reference Guide | DRV Parameters and Commands

## DRV.MEMADDR

```
General Information
Type R/W Parameter
Description Sets the read and write address.
Units N/A
Range N/A
Default Value 1.U8
Data Type N/A
See Also DRV.MEMDATA
Start Version M_0-0-14
```
#### Description

```
DRV.MEMADDR sets the address that is used by DRV.MEMDATA. The input can be either an internal
parameter of the drive or any direct address from the DSP address space (SDRAM, internal RAM, or asyn-
chronous memory). The input value can be either decimal or hexadecimal with 0x prefix.
Type extension can be one of the following:
U8,S8,U16,S16,U32,S32,U64,S64.
```
#### Examples

```
Setting to an internal parameter:
-->DRV.MEMADDR CCommandHandler.Debug1
Setting to an internal address:
-->DRV.MEMADDR 0xffabcde.u16
```

## DRV.MEMDATA

```
General Information
Type R/W Parameter
Description Sets or reads a value from an internal address.
Units N/A
Range N/A
Default Value N/A
Data Type N/A
See Also DRV.MEMADDR
Start Version M_0-0-14
```
#### Description

DRV.MEMDATA reads a value from the address that was set by DRV.MEMADDR or writes a value to this
address. The input value can be either decimal or hexadecimal with 0x prefix.

#### Examples

Read a value from internal address:

```
-->DRV.MEMDATA 01
```
Write a hexadecimal value to an internal address:

```
-->DRV.MEMADDR 0x01
```
```
AKD Parameter and Command Reference Guide | DRV Parameters and Commands
```

AKD Parameter and Command Reference Guide | DRV Parameters and Commands

## DRV.MOTIONSTAT

```
General Information
Type R/O Parameter
Description Reads the motion status of the drive.
Units N/A
Range 0 to 4,294,967,295
Default Value N/A
Data Type Integer
See Also N/A
Start Version M_0-0-15
```
#### Description

```
This command indicates the current status of the drive internal motion (see table below).
Bit Significance Description
0 0x00000001 Motion task is active (high active)
1 0x00000002 Home position found /reference point set (high active)
2 0x00000004 Homing finished (high active)
3 0x00000008 Homing active (high active)
4 0x00000010 Homing error condition has occurred (high active)*
5 0x00000020 Slave in electronic gearing mode synchronized (high active)
6 0x00000040 Electronic gearing is active (high active)
7 0x00000080 Emergency stop procedure in progress (high active)
8 0x00000100 Emergency stop procedure has an error (high active)
9 0x00000200 Service motion active (high active)
10 0x00000400 A motion task could not be activated /invalid MT (high active)**
11 0x00000800
Motion task target position has been reached. See also
MT.TPOSWND (high active).
12 0x00001000
Motion task target velocity has been reached. See also
MT.TVELWND (high active).
13 0x00002000 The bode plot procedure within the drive is active (high active).
```
```
14 0x00004000
```
```
The target position of a motion task has been crossed. This sit-
uation occurs for motion tasks with a change on the fly when trig-
gering the DRV.STOP command just before the reaching the
target velocity of the current active motion task. The ramp-down
procedure with the motion task deceleration ramp causes the tar-
get position to be crossed (high active).
* A possible error condition for homing to a reference switch could be that no reference switch was found
between two hardware limit switches.
** A possible error condition for an invalid motion task could be that a motion task tried to trigger automatically
following motion task that has never been initialized (called an "empty motion" task).
```

#### Drive Name: DRV.NAME

```
General Information
Type NV Parameter
Description Sets and reads the name of the drive.
Units N/A
Range N/A
Default Value No-Name
Data Type String
See Also N/A
Start Version M_0-0-15
```
#### Description

You can assign a unique name to any AKD drive. This name is one way to identify the drive in a multiple drive
network (for instance, in a TCP/IP network on which multiple drives reside).

From the terminal screen, DRV.NAME returns the name of the drive as ASCII characters.

```
AKD Parameter and Command Reference Guide | DRV Parameters and Commands
```

AKD Parameter and Command Reference Guide | DRV Parameters and Commands

#### DRV.NVLIST

```
General Information
Type R/O Parameter
Description Lists the NV parameters and values from the RAM.
Units N/A
Range N/A
Default Value N/A
Data Type N/A
See Also N/A
Start Version M_0-0-15
```
#### Description

```
DRV.NVLIST lists all the drive parameters that reside in NV memory.
The list includes each parameter name, followed by its current value from the RAM.
```

#### DRV.NVLOAD

```
General Information
Type W/O Parameter
Description Loads all data from the NV memory of the drive into the RAM parameters.
Units N/A
Range N/A
Default Value N/A
Data Type N/A
See Also DRV.NVLOAD DRV.NVLIST
Start Version M_00-00-62-000
```
#### Description

DRV.NVLOAD loads all data from the NV memory of the drive into the RAM parameters.

```
AKD Parameter and Command Reference Guide | DRV Parameters and Commands
```

AKD Parameter and Command Reference Guide | DRV Parameters and Commands

#### DRV.NVSAVE

```
General Information
Type Command
Description Saves the drive parameters from the RAM to the NV.
Units N/A
Range N/A
Default Value N/A
Data Type N/A
See Also DRV.RSTVAR
Start Version M_0-0-15
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 1010h/1
Data Type Unsigned 32
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

```
DRV.NVSAVE saves the current drive parameter values from the RAM to the NV memory.
The drive parameters that were saved to the NV are read from the NV on the next drive boot, causing the
values to be automatically set to the saved values on every drive boot.
ExecutingDRV.RSTVAR doesnotmodifythevaluesoftheNV,butinsteadsetsthedrivevaluesinRAMtotheir
defaults.
```

#### DRV.ONTIME

```
General Information
Type R/O Parameter
Description Returns how long the drive has been running since last power up.
Units Days:Hours:Minutes:Seconds
Range N/A
Default Value N/A
Data Type String
See Also Returns how long the drive has been running since first activated.
Start Version M_0-0-59
```
#### Description

Returns how long the drive has been running since last power up.

```
AKD Parameter and Command Reference Guide | DRV Parameters and Commands
```

AKD Parameter and Command Reference Guide | DRV Parameters and Commands

#### DRV.OPMODE

```
General Information
Type NV Parameter
Description Sets the operation mode (current, velocity, or position).
Units N/A
Range 0 to 2
Default Value 0
Data Type Integer
See Also DRV.CMDSOURCE
Start Version M_0-0-15
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 35B4h/0
Data Type Integer 32
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

```
DRV.OPMODE specifies the operation mode of the drive.
The operation mode values can be set as follows:
Mode Description
0 Current (torque) operation mode
1 Velocity operation mode
2 Position operation mode
You must also use DRV.CMDSOURCE to set the source of the command to the drive.
```
#### Example

```
Set the source of the command to a TCP/IP channel and the desired operation mode to velocity:
-->DRV.CMDSOURCE 0
-->DRV.OPMODE 1
```

#### DRV.READFORMAT

```
General Information
Type R/W Parameter
Description Sets the value returned to either decimal or hexadecimal.
Units N/A
Range 10 or 16
Default Value 10
Data Type Integer
See Also N/A
Start Version M_0-0-15
```
#### Description

DRV.READFORMAT sets the return values type to either decimal or hexadecimal.

```
Format Description
10 Sets the read values to decimal format
16 Sets the read values to hexadecimal format
```
```
AKD Parameter and Command Reference Guide | DRV Parameters and Commands
```

AKD Parameter and Command Reference Guide | DRV Parameters and Commands

#### DRV.RSTVAR

```
General Information
Type Command
Description
Sets default values in the drive without re-booting the drive and without
resetting the NV memory.
Units N/A
Range N/A
Default Value N/A
Data Type N/A
See Also
Start Version M_0-0-15
```
#### Description

```
DRV.RSTVAR causesthedrivetoreturntothedefaultvalueswithouttheneedtore-bootthedrivefirstandwith-
outresettingtheNVmemory.UseDRV.RSTVAR toreturntothedefaultsettingsandrecoveraworkingdrive.
```

#### DRV.RUNTIME

```
General Information
Type R/O Parameter
Description Returns how long the drive has been running since first activated.
Units Days:Hours:Minutes:Seconds
Range N/A
Default Value N/A
Data Type String
See Also N/A
Start Version M_0-0-15
```
#### Description

DRV.RUNTIME returns how long the drive has been running since first activated. This is not only the current
session but the total amount of time from all sessions.

```
AKD Parameter and Command Reference Guide | DRV Parameters and Commands
```

AKD Parameter and Command Reference Guide | DRV Parameters and Commands

#### DRV.STOP

```
General Information
Type Command
Description This command stops all drive motion.
Units N/A
Range N/A
Default Value N/A
Data Type N/A
See Also N/A
Start Version M_0-0-15
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 35FEh/0
Data Type Integer 32
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

```
This command stops all drive motion.
```

#### DRV.TEMPERATURES

```
General Information
Type R/O Parameter
Description Reads the temperature of drive components.
Units °C
Range 55 to 125 °C
Default Value N/A
Data Type String
See Also N/A
Start Version M_0-0-15
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 3413h/0
Data Type Unsigned 16
PDO Mappable No
Start Version
```
#### Description

DRV.TEMPERATURES reads the temperature in different parts of the drive (power and control boards). The
temperature is read from temperature sensors located in the drive.

#### Example

Below is an example of the output for this command :

```
Control Temperature: 39 °C
Power1 Temperature: 31 °C
Power2 Temperature: Sensor does not exist.
Power3 Temperature: Sensor does not exist.
```
```
AKD Parameter and Command Reference Guide | DRV Parameters and Commands
```

AKD Parameter and Command Reference Guide | DRV Parameters and Commands

#### DRV.VER

```
General Information
Type R/O Parameter
Description Reads the drive version.
Units N/A
Range N/A
Default Value N/A
Data Type String
See Also N/A
Start Version M_0-0-15
```
#### Description

```
DRV.VER reads both FPGA and firmware versions.
The version data presented is hard coded in the firmware code.
```
#### Example

```
Below is an example of the output for this command:
Danaher Motion - Digital Servo Drive
-------------------------------------
FPGA version : FP0004_0001_00_07
Firmware Version : M_0-0-15_T_2009-01-19_10-36-28_IR
```

#### DRV.VERIMAGE

```
General Information
Type R/O Parameter
Description Returns the version data from each image.
Units N/A
Range N/A
Default Value N/A
Data Type String
See Also N/A
Start Version M_0-0-15
```
#### Description

DRV.VERIMAGE reads the versions of the different images in the drive. This parameter returns the version
data from each image .i00 file.

#### Example

Below is an example of the output for this parameter:

```
Danaher Motion - Digital Servo Drive
------------------------------------
Resident Firmware: R_0-0-11
Operational Firmware: M_0-0-15
Resident FPGA: FPB004_0001_00_07
Operational FPGA : FP0004_0001_00_07
```
```
AKD Parameter and Command Reference Guide | DRV Parameters and Commands
```

AKD Parameter and Command Reference Guide | DRV Parameters and Commands

#### DRV.WARNINGS

```
General Information
Type R/O Parameter
Description Reads the active warnings.
Units N/A
Range N/A
Default Value N/A
Data Type N/A
See Also N/A
Start Version M_0-0-50-0
```
#### Description

```
DRV.WARNINGS returns a list of all currently active warnings in the system.
```

#### DRV.ZERO

```
General Information
Type R/W Parameter
Description Sets the zero mode. The procedure is activated when the drive is enabled.
Units N/A
Range 0,1
Default Value 0
Data Type Integer
See Also DRV.IZERO
Start Version M_0-0-50-0
```
#### Description

The zero procedure is a sequence in which phase commutation is initialized. During this procedure, the motor
is held at a certain known electrical position (by applying a current defined by DRV.IZERO). After the motor
rests at this position, the commutation angle is calculated and set automatically.

```
AKD Parameter and Command Reference Guide | DRV Parameters and Commands
```

AKD Parameter and Command Reference Guide | FB1 Parameters

### FB1 Parameters

#### FB1.ENCRES

```
General Information
Type NV Parameter
Description Sets the resolution of the motor encoder.
Units Encoder counts
Range 0 to 2^32 -1
Default Value 1,024
Data Type Integer
See Also N/A
Start Version M_0-0-14
```
#### Description

```
This parameter sets or gets the resolution of the motor encoder (encoder feedback systems only) in number of
counts per revolution for a rotary motor and the number of encoder pitches per motor pole pitch for a linear
motor. The number of encoder counts per revolution is obtained by multiplying the motor catalog resolution in
units of PPR by four. For example, for a 1024 PPR resolution motor, the number of encoder counts per rev-
olution is 1024*4 = 4096. For this motor FB1.ENCRES must be set to 4096.
For linear motors, the value of FB1.ENCRES is set to the number of encoder pitches per motor pole pitch. For
a motor with 32 mm pole pitch, and a 40 μm encoder pitch, the value for FB1.ENCRES should be set to 32
mm/40 μm = 800.
```

#### FB1.HALLSTATE

```
General Information
Type R/O Parameter
Description Reads the resolution of the motor encoder.
Units Binary
Range 0 0 0 to 1 1 1
Default Value N/A
Data Type String
See Also N/A
Start Version M_0-0-14
```
#### Description

FB1.HALLSTATE reads the Hall switch values (encoder feedback only).

```
AKD Parameter and Command Reference Guide | FB1 Parameters
```

AKD Parameter and Command Reference Guide | FB1 Parameters

#### FB1.IDENTIFIED

```
General Information
Type R/O Parameter
Description Reads the type of feedback device used by the drive/motor.
Units N/A
Range N/A
Default Value N/A
Data Type Integer
See Also FB1.SELECT
Start Version M_0-0-15
```
#### Description

```
This parameter is set according to FB1.SELECT on drive power up if FB1.SELECT is not –1; otherwise the
parameter value is read from the drive memory.
Feedback Type Description
0 Unknown
10 Incremental encoder with A/B Quad, Marker pulse & Halls
20 Sine encoder , with marker pulse & Halls
30 EnDat 2.1 with Sine Cosine
31 EnDat 2.2
32 BiSS with Sine Cosine
33 HIPERFACE
40 Resolver
41 SFD
```

#### FB1.INITSIGNED

```
General Information
Type NV Parameter
Description Sets initial feedback value as signed or unsigned.
Units N/A
Range 0 to 1
Default Value 0
Data Type Integer
See Also FB1.ORIGIN
Start Version M-0-0-51
```
#### Description

This parameter sets whether the initial value of the feedback read from the feedback device will be set as a
signed or as an unsigned value

The drive internal process for the feedback initialization is as follows:

1. Reads the position feedback.
2. Adds the origin to the feedback.
3. Determines modulo from Step 2 by the actual feedback bits.
4. Sets the position feedback sign according to FB1.INITSIGNED.

```
Value Functionality
0 Set as unsigned
1 Set as signed
```
#### Example

##### FB1.INITSIGNED 1

```
AKD Parameter and Command Reference Guide | FB1 Parameters
```

AKD Parameter and Command Reference Guide | FB1 Parameters

#### FB1.MECHPOS

```
General Information
Type R/O Parameter
Description Reads the mechanical position.
Units counts
Range 0 to 4,294,967,295 counts
Default Value N/A
Data Type Integer
See Also N/A
Start Version M_0-0-15
```
#### Description

```
FB1.MECHPOS reads the mechanical angle which is equal to the lower 32 bits in the 64-bit position feedback
word.
```

#### FB1.MEMVER

```
General Information
Type R/O Parameter
Description Returns the memory feedback version.
Units N/A
Range N/A
Default Value N/A
Data Type Integer
See Also N/A
Start Version M_0-0-15
```
#### Description

FB1.MEMVER returns the memory feedback version (only applicable for feedbacks with memory).

```
AKD Parameter and Command Reference Guide | FB1 Parameters
```

AKD Parameter and Command Reference Guide | FB1 Parameters

#### FB1.OFFSET

```
General Information
Type NV Parameter
Description Sets position feedback offset.
```
```
Units
```
```
Depends on UNIT.ACCROTARY or UNIT.PLINEAR
Rotary: counts, rad, deg, PIN/POUT, counts 16 bit
Linear: counts, mm, μm, PIN/POUT, counts 16 bit
```
```
Range
```
```
Rotary:
-5,123,372,000,000,005.000 to 5,123,372,000,000,005.000 counts
-7495.067 to 7495.067 rad
-429,436.096 to 429,436.096 deg
-5,964.390 to 5,964.390 [PIN/POUT]
-78,176,452.637 to 78,176,452.636 counts 16 bit
Linear:
-5,123,372,000,000,005.000 to 5,123,372,000,000,005.000 counts
-1192.878*MOTOR.PITCH to 1192.878*MOTOR.PITCH mm
-1192877.952*MOTOR.PITCH to 1192877.952*MOTOR.PITCH μm
-5964.390 to 5964.390 PIN/POUT
-78176452.637 to 78176452.636 counts 16 bit
Default Value 0
Data Type Float
See Also PL.FB
Start Version M_0-0-15
```
#### Description

```
FB1.OFFSET is a value added to the position feedback (PL.FB).
```
#### Example

```
If PL.FB is 10 deg and FB1.OFFSET is set to –10 deg, then the next read of PL.FB will return ~0 deg.
```

#### FB1.ORIGIN

```
General Information
Type NV Parameter
Description Adds to the initial feedback position.
```
```
Units
```
```
Depends on UNIT.ACCROTARY or UNIT.ACCLINEAR
Rotary: counts, rad, deg, PIN/POUT, counts 16 Bit
Linear: counts, mm, μm, PIN/POUT, counts 16 Bit
```
```
Range
```
```
Rotary:
0.000 to 5,123,372,000,000.000 counts
0.000 to 7,495.067 rad
0.000 to 429,436.096 deg
0.000 to 5,964.390 PIN/POUT
0.000 to 78,176,452.636 counts16 Bit
Linear:
0.000 to 5,123,372,000,000.000 Counts
0.000 to 1,192.878 mm
0.000 to 1,192,877.952 μm
0.000 to 5,964.390 PIN/POUT
0.000 to 78,176,452.636 counts16 Bit
Default Value 0 counts
Data Type Float
See Also FB1.INITSIGNED
Start Version M-0-0-51
```
#### Description

FB1.ORIGIN is a value that is added to the feedback device position. Initial value and modulo are determined
from the number of bits of the feedback:

Initial position value = ( <feedback from device> + FB1.ORIGIN ) modulo <number of feedback bits>

The number of feedback bits is set according to the feedback type. For memory feedbacks it is the number of
feedback bits; for none memory it is always single turn.

The drive internal process for the feedback initialization is as follows:

1. Reads the position feedback.
2. Adds the origin to the feedback.
3. Determines modulo from Step 2 by the actual feedback bits.
4. Sets the position feedback sign according to FB1.INITSIGNED.

#### Example

This example uses UNIT.PROTARY set to 2 (degrees)

It also assumes that the AKD is connected to a single turn feedback device with memory.

FB1.ORIGIN is set to 22 and saved into NV memory.

```
AKD Parameter and Command Reference Guide | FB1 Parameters
```

AKD Parameter and Command Reference Guide | FB1 Parameters

```
Drive boots and reads from feedback device position 340 degrees. According to the description section
above, calculation will be:
(340 + 22) modulo 360 = 2 degrees.
Therefore the initial feedback value will be set to 2 degrees.
```

#### FB1.PFIND

```
General Information
Type R/W Parameter
Description
A procedure that allows the user to find the commutation angle for encoder
feedback, which has no halls.
Units NA
Range 0, 1
Default Value 0
Data Type Integer
See Also FB1.PFINDCMDU
Start Version M_0-0-53
```
#### Description

A procedure that allows the user to find the commutation angle for encoder feedback (which has no Halls).

```
AKD Parameter and Command Reference Guide | FB1 Parameters
```

AKD Parameter and Command Reference Guide | FB1 Parameters

#### FB1.PFINDCMDU

```
General Information
Type R/W Parameter
Description Current value used during the phase finding procedure (PFB.PFIND=1)
Units A
Range 0 to DRV.IPEAK
Default Value 0
Data Type Float
See Also PFB.PFIND
Start Version M_0-0-53
```
#### Description

```
FB1.PFINDCMDU sets the current value used during the phase finding procedure.
```

#### FB1.POLES

```
General Information
Type R/O Parameter
Description Reads the number of feedback poles.
Units N/A
Range 2 to 128
Default Value 2
Data Type Integer
See Also MOTOR.POLES
Start Version M_0-0-15
```
#### Description

FB1.POLES sets the number of individual poles in the feedback device. This variable is used for the com-
mutation function, as well as for velocity feedback scaling, and represents the number of individual poles (not
pole pairs). The division value of motor poles (MOTOR.POLES) and feedback poles (FB1.POLES) must be an
integer when moving drive to enable, otherwise a fault is issued.

```
AKD Parameter and Command Reference Guide | FB1 Parameters
```

AKD Parameter and Command Reference Guide | FB1 Parameters

#### FB1.PSCALE

```
General Information
Type R/W Parameter
Description Sets position scaling value.
Units N/A
Range 0 to 32
Default Value 20
Data Type Integer
See Also N/A
Start Version M_00-00-51-000
```
#### Description

```
This parameter converts a 64-bit position value into a 32-bit position value. This parameter mostly affects posi-
tion values (which are transferred via a fieldbus system), since not all fieldbus systems are capable of trans-
ferring 64-bit variables.
FB1.PSCALE determines the number of bits for a 32-bit position, which represent the mechanical angle.
Thus, for FB1.PSCALE 32 bits are used to display the number of turns.
```
#### Example

```
The drive always works internally with 64-bit position values. The drive internal 64-bit actual position should
contain the following value:
0x0000.0023.1234.ABCD
The lower 32 bits represent the mechanical angle of the feedback. The upper 32 bits represent the number of
turns.
FB1.PSCALE = 20
The 32-bit position is: 0x0231234A
```
##### FB1.PSCALE = 16

```
The 32-bit position is: 0x00231234
```

#### FB1.RESKTR

```
General Information
Type NV Parameter
Description Sets the resolver nominal transformation ratio.
Units N/A
Range 0.001 to 50.000
Default Value 0.5
Data Type Float
See Also N/A
Start Version M-0-0-50
```
#### Description

Thisparametersetsthe resolvernominaltransformationratio.Itaffectstheresolverexcitationoutputamplitude.
The value can be obtained from the resolver data sheet.

#### Example

##### FB1.RESKTR 0.5

```
AKD Parameter and Command Reference Guide | FB1 Parameters
```

AKD Parameter and Command Reference Guide | FB1 Parameters

#### FB1.RESREFPHASE

```
General Information
Type NV Parameter
Description Sets the electrical degrees of phase lag in the resolver.
Units electrical degrees
Range -180 to 180°
Default Value -2°
Data Type Float
See Also N/A
Start Version M-0-0-50-0
```
#### Description

```
This parameter sets the electrical degrees of phase lag in the resolver.
See the motor resolver datasheet for the value for this parameter.
```
#### Example

##### FB1.RESREFPHASE -2


#### FB1.SELECT

```
General Information
Type NV Parameter
Description Sets user entered type or identified type (–1).
Units N/A
Range –1, 10, 20, 30, 31, 32, 40, 41
Default Value –1
Data Type Integer
See Also FB1.IDENTIFIED
Start Version M_0-0-15
```
#### Description

FB1.SELECT sets the feedback type manually (see FB1.IDENTIFIED) or allows the drive to automatically
identify the feedback type on power up.

**FB1.SELECT Input Values**

```
Input
Value Description
```
##### –1

```
The drive automatically identifies the type of feedback as part of the power up process.
Setting this value does not modify FB1.IDENTIFIED, unless it is saved in the NV mem-
ory for the next power up. If a feedback with memory is connected to the drive, the
value of FB1.IDENTIFIED is set automatically to the feedback identified and all param-
eters read from the feedback are set according to the values read from the feedback. If
no feedback is connected or a feedback with no memory is connected, the value of
FB1.IDENTIFIED is set to 0 (no feedback identified) and all values normally read from
the feedback are read from NV memory (if stored in NV) otherwise they are set to the
default values.
```
```
10
```
```
Manually sets the type to incremental encoder. This input sets the value of FB1.ID-
ENTIFIED to 10. If the feedback setting fails, FB1.IDENTIFIED is automatically set to
0 (no feedback identified).
```
```
20
```
```
Manually sets the type to sine encoder. This input sets the value of FB1.IDENTIFIED
to 20. If the feedback setting fails, FB1.IDENTIFIED is automatically set to 0 (no feed-
back identified).
```
```
30
```
```
Manually sets the type to Endat 2.1. This input sets the value of FB1.IDENTIFIED to
```
30. If the feedback setting fails, FB1.IDENTIFIED is automatically set to 0 (no feed-
back identified).

```
31
```
```
Manually sets the type to Endat 2.2. This input sets the value of FB1.IDENTIFIED to
```
31. If the feedback setting fails, FB1.IDENTIFIED is automatically set to 0 (no feed-
back identified).

```
32
```
```
Manually sets the type to BiSS. This input sets the value of FB1.IDENTIFIED to 32. If
the feedback setting fails, FB1.IDENTIFIED is automatically set to 0 (no feedback iden-
tified).
```
```
33
```
```
Manually sets the type to Hyperface. This input sets the value of FB1.IDENTIFIED to
```
33. If the feedback setting fails, FB1.IDENTIFIED is automatically set to 0 (no feed-
back identified).

```
AKD Parameter and Command Reference Guide | FB1 Parameters
```

AKD Parameter and Command Reference Guide | FB1 Parameters

```
Input
Value
Description
```
##### 40

```
Manually sets the type to resolver. This input sets the value of FB1.IDENTIFIED to 40.
If the feedback setting fails, FB1.IDENTIFIED is automatically set to 0 (no feedback
identified).
```
```
41
```
```
Manually sets the type to SFD. This input sets the value of FB1.IDENTIFIED to 41. If
the feedback setting fails, FB1.IDENTIFIED is automatically set to 0 (no feedback iden-
tified).
```
```
FB1.SELECT Feedback Types
```
```
Type Description
0 Unknown
10 Incremental encoder with A/B Quad,
marker pulse & Hall
20 Sine Encoder , with marker pulse & Hall
30 EnDat 2.1 with Sine Cosine
31 EnDat 2.2
32 BiSS with Sine Cosine
33 HIPERFACE
40 Resolver
41 SFD
```

#### FB1.TRACKINGCALC

```
General Information
Type NV Parameter
Description Controls tracking calibration algorithm.
Units N/A
Range 0 to 1
Default Value 0
Data Type Integer
See Also N/A
Start Version M-0-0-50
```
#### Description

This parameter turns the tracking calibration algorithm on or off for sine-cosine or resolver.

```
Value Functionality
0 Tracking calibration isoff
```
```
1 Tracking calibration ison
```
#### Example

##### FB1.TRACKINGCALC 1

```
AKD Parameter and Command Reference Guide | FB1 Parameters
```

AKD Parameter and Command Reference Guide | FBUS Parameters

### FBUS Parameters

### FBUS.PARAM1 TO FBUS.PARAM20

```
General Information
Type NV Parameter
Description Set fieldbus specific meanings.
Units N/A
Range 0 to 2^31
Default Value 0
Data Type Integer, U32
See Also CANopen Communication Manual, EtherCAT Communication Manual
Start Version M_0-0-33
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number
```
```
FBUS.PARAM1 to
FBUS.PARAM10: 0x36E5 sub 0 to
0x36EE sub 0
Data Type Unsigned 32
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

```
These parameters set the fieldbus baud rate.
FBUS.PARAM01 sets the baud rate: Supported baud rates are 125, 250, 500 and 1000 kBaud.
FBUS.PARAM02 switches the phase locked loop (PLL) for synchronized use: 0 = OFF, 1 = ON
FBUS.PARAM04 switches the surveillance of SYNC-signals: 0 = OFF, 1 = ON
FBUS.PARAM03, FBUS.PARAM05 - FBUS.PARAM10 are reserved.
```
```
FBUS.PARAM04 Additional Notes
Fieldbus Parameter 4 enables (1) or disables(0) the synchronization supervision of the CANOpen or Ether-
CAT fieldbus.
Default values:
 CANOpen: disabled (0)
 EtherCAT: enabled (1)
The surveillance is active, when
 Parameter 4 = 1
 The first CANOpen Sync message or first EtherCAT frame was received.
```

When more than three CANOpen sync messages or seven EtherCAT frames were not received, AND the
drive is enabled, the fault "Sync lost" (FAULT_CMDH_FIELDBUS_SYNC_LOST = 125) occurs.

```
AKD Parameter and Command Reference Guide | FBUS Parameters
```

AKD Parameter and Command Reference Guide | FBUS Parameters

### FBUS.PLLTHRESH

```
General Information
Type NV Parameter
Description Sets number of successful synchronized cycles needed to lock the PLL.
Units N/A
Range 0 to 10,000
Default Value 0
Data Type Integer, U32
See Also Appendix B: Fieldbus Manuals
Start Version M_0-0-33
```
#### Description

```
This parameter sets number of successful synchronized cycles needed to lock the PLL.
```

### FBUS.SAMPLEPERIOD

```
General Information
Type NV Parameter
Description Sets fieldbus sample period.
Units Whole multiples of MTS 62.5 μs
Range 1 to 128 and value must be a power of 2
Default Value 32 = 2 ms
Data Type U8
See Also Appendix B: Fieldbus Manuals
Start Version M_0-0-33
```
```
Fieldbus Information
EtherCAT COE & CANOpen
Index/Subindex or
Parameter Number 60C2h/0
Data Type Unsigned 8
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

This parameter sets the fieldbus cycle time. It is normally written in the startup phase of the field busses via
the object 60C2 subindex 1 (interpolation time units) and 2 (interpolation time index), where the index stands
for a power of 10 seconds (for instance, -3 stands for milliseconds) and the units are the counts of these units.

```
AKD Parameter and Command Reference Guide | FBUS Parameters
```

AKD Parameter and Command Reference Guide | FBUS Parameters

### FBUS.SYNCACT

```
General Information
Type R/O Parameter
Description Reads actual distance from the desired sync distance.
Units ns
Range
Default Value
Data Type Integer, U32
See Also Appendix B: Fieldbus Manuals
Start Version M_0-0-33
```
#### Description

```
This parameter reads actual distance from the desired sync distance.
```

### FBUS.SYNCDIST

```
General Information
Type NV Parameter
Description Sets time target for synchronization.
Units ns
Range 0 to 250,000
Default Value 100,000
Data Type Integer, U32
See Also Appendix B: Fieldbus Manuals
Start Version M_0-0-33
```
#### Description

This parameter sets time target for synchronization.

```
AKD Parameter and Command Reference Guide | FBUS Parameters
```

AKD Parameter and Command Reference Guide | FBUS Parameters

### FBUS.SYNCWND

```
General Information
Type NV Parameter
Description Sets symmetrically arranged window around the desired sync distance.
Units ns
Range 0 to 1,000,000
Default Value 50,000
Data Type Integer, U2
See Also Appendix B: Fieldbus Manuals
Start Version M_0-0-33
```
#### Description

```
This parameter sets symmetrically arranged window around the desired sync distance.
```

### FBUS.TYPE

```
General Information
Type R/O Parameter
Description Shows the active fieldbus type.
Units N/A
Range 0 to 3
Default Value 0
Data Type U8
See Also Appendix B: Fieldbus Manuals
Start Version M_0-0-33
```
#### Description

0 = No fieldbus available
1 = SynqNet

2 = CANopen

3 = EtherCAT

```
AKD Parameter and Command Reference Guide | FBUS Parameters
```

AKD Parameter and Command Reference Guide | GEAR Parameters

## GEAR Parameters

### GEAR.ACCMAX

```
General Information
Type R/W Parameter
Description Sets the maximum allowed acceleration value.
```
```
Units
```
```
Depends on UNIT.ACCROTARY or UNIT.ACCLINEAR
Rotary: rps/s, rpm/s, deg/s^2 , (PIN/POUT)/s^2 , rad/s^2
Linear: counts/s^2 , mm/s^2 , μm/s^2 , (PIN/POUT)/s^2
```
```
Range
```
```
Rotary:
0.031 to 833,333.333 rps/s
1.860 to 50,000,000.000 rpm/s
11.158 to 300,000,000.000 deg/s^2
0.155 to 4,166,666.752 (PIN/POUT)/s^2
0.195 to 5,235,987.968 rad/s^2
Linear:
0.000 to 833.333 counts/s^2
0.031*MOTOR.PITCH to 833,333.333*MOTOR.PITCH mm/s^2
30.994*MOTOR.PITCH to 83,3333,333.333*MOTOR.PITCH μm/s^2
0.155 to 4,166,666.667 (PIN/POUT)/s^2
```
```
Default Value
```
```
Rotary:
50.000 rps/s
3,000.000 rpm/s
18,000.000 deg/s^2
250.000 (PIN/POUT)/s^2
314.159 rad/s^2
Linear:
0.050 Counts/s^2
1.000*MOTOR.PITCH mm/s^2
1000.000*MOTOR.PITCH μm/s^2
250.000 (PIN/POUT)/s^2
Data Type Float
See Also UNIT.ACCROTARY, UNIT.ACCLINEAR, GEAR.DECMAX
Start Version M_0-0-50-0
```
#### Description


This parameter limits the acceleration of the slave to a numerical higher value.

```
AKD Parameter and Command Reference Guide | GEAR Parameters
```

AKD Parameter and Command Reference Guide | GEAR Parameters

### GEAR.DECMAX

```
General Information
Type R/W Parameter
Description Sets the maximum allowed deceleration value
```
```
Units
```
```
Depends on UNIT.ACCROTARY or UNIT.ACCLINEAR
Rotary: rps/s, rpm/s, deg/s^2 , (PIN/POUT)/s^2 , rad/s^2
Linear: counts/s^2 , mm/s^2 , μm/s^2 , (PIN/POUT)/s^2
```
```
Range
```
```
Rotary:
0.031 to 833,333.333 rps/s
1.860 to 50,000,000.000 rpm/s
11.158 to 300,000,000.000 deg/s^2
0.155 to 4,166,666.752 (PIN/POUT)/s^2
0.195 to 5,235,987.968 rad/s^2
Linear:
0.000 to 833.333 c/s^2
0.031*MOTOR.PITCH to 833,333.333*MOTOR.PITCH mm/s^2
30.994*MOTOR.PITCH to 833,333,333.333*MOTOR.PITCH μm/s^2
0.155 to 4,166,666.667 (PIN/POUT)/s^2
```
```
Default Value
```
```
Rotary:
50.000 rps/s
3,000.000 rpm/s
18,000.000 deg/s^2
250.000 (PIN/POUT)/s^2
314.159 rad/s^2
Linear:
0.050 counts/s^2
1.000*MOTOR.PITCH mm/s^2
1,000.000*MOTOR.PITCH μm/s^2
250.000 (PIN/POUT)/s^2
Data Type Float
See Also UNIT.ACCROTARY, UNIT.ACCLINEAR, GEAR.ACCMAX
Start Version M_0-0-50-0
```
#### Description

```
This parameter limits the deceleration of the slave to a numerical higher value.
```

### GEAR.IN

```
General Information
Type R/W Parameter
Description Sets the denominator of the electronic gearing ratio.
Units N/A
Range 1 to 65,535
Default Value 1
Data Type Integer
See Also N/A
Start Version M_0-0-50-0
```
#### Description

Thisparametersetsthedenominatorofthegearratiofortheelectronicgearingmode.Thegearratioisusedin
ordertoincreaseanddecreasetheslavevelocity.Theslavevelocitycanbecalculatedbythefollowingformula:

Slave velocity = Master velocity * GEAR.OUT/GEAR.IN

Be sure that you set the external master source number of signals per revolution correctly. Also, select the
gear ratio so that the maximum electronic gearing velocity (GEAR.VELMAX) is not exceeded.

Master velocitymax * GEAR.OUT/GEAR.IN < GEAR.VELMAX

```
AKD Parameter and Command Reference Guide | GEAR Parameters
```

AKD Parameter and Command Reference Guide | GEAR Parameters

### GEAR.MODE

```
General Information
Type R/W Parameter
Description Selects electronic gearing mode.
Units N/A
Range 0 to 1
Default Value N/A
Data Type Integer
See Also N/A
Start Version M_0-0-50-0
```
#### Description

```
This parameter selects the electronic gearing mode at the beginning of the electronic gearing procedure.
```

### GEAR.MOVE

```
General Information
Type Command
Description Starts the electronic gearing.
Units N/A
Range N/A
Default Value N/A
Data Type N/A
See Also N/A
Start Version M_0-0-50-0
```
#### Description

The command GEAR.MOVE starts the electronic gearing procedure according to the selected electronic gear-
ing mode. The electronic gearing process can be stopped using the DRV.STOP command.

```
AKD Parameter and Command Reference Guide | GEAR Parameters
```

AKD Parameter and Command Reference Guide | GEAR Parameters

### GEAR.OUT

```
General Information
Type R/W Parameter
Description Sets the numerator of the electronic gearing ratio
Units N/A
Range -32,768 to +32,767
Default Value 1
Data Type Integer
See Also N/A
Start Version M_0-0-50-0
```
#### Description

```
This parameter is the numerator of the gear ratio for the electronic gearing mode. The gear ratio is used in order
to increase/decrease the slave velocity. The slave velocity can be calculated by the following formula:
Slave velocity = Master velocity * GEAR.OUT/GEAR.IN
```
```
Make sure that the external master source has been set properly. Also, be certain to select a gear ratio such
that the maximum electronic gearing velocity (GEAR.VELMAX) will not be exceeded.
Master velocitymax * GEAR.OUT/GEAR.IN < GEAR.VELMAX
```

### GEAR.VMAX

```
General Information
Type R/W Parameter
Description Maximum allowed velocity value
```
```
Units
```
```
Depends on UNIT.ACCROTARY or UNIT.ACCLINEAR
Rotary: rpm, rps, deg/s, (PIN/POUT)/s, rad/s
Linear: counts/s, mm/s, μm/s, (PIN/POUT)/s
```
```
Range
```
```
Rotary:
0.001 to 12,000.000 rpm
0.001 to 200.000 rps
0.001 to 72,000.000 deg/s
0.001 to 1,000.000 (PIN/POUT)/s
0.001 to 1256.637 rad/s
Linear:
0.001 to 0.200 counts/s
0.001*MOTOR.PITCH to 200.000*MOTOR.PITCH mm/s
0.004*MOTOR.PITCH to 200,000.000*MOTOR.PITCH μm/sec
0.001 to 1,000.000 (PIN/POUT)/s
```
```
Default Value
```
```
Rotary:
12,000.000 rpm
200.000 rps
17,999.998 deg/s
250.000 (PIN/POUT)/s
1,256.637 rad/s
Linear:
0.050 Counts/s
50.000*MOTOR.PITCH mm/s
49,999.996*MOTOR.PITCH μm/sec
250.000 (PIN/POUT)/s
Data Type Float
See Also N/A
Start Version M_0-0-50-0
```
#### Description

This parameter limits the maximum velocity of the slave drive.

```
AKD Parameter and Command Reference Guide | GEAR Parameters
```

This page intentionally left blank.


## HOME Parameters

### HOME.ACC

```
General Information
Type R/W Parameter
Description Sets homing acceleration.
```
```
Units
```
```
Depends on UNIT.ACCROTARY or UNIT.ACCLINEAR
Rotary: rps/s, rpm/s, deg/s^2 , (PIN/POUT)/s^2 , rad/s^2
Linear: counts/s^2 , mm/s^2 , μm/s^2 , (PIN/POUT)/s^2
```
```
Range
```
```
Rotary:
0.031 to 833,333.333 rps/s
1.860 to 50,000,000.000 rpm/s
11.158 to 300,000,000.000 deg/s^2
0.155 to 4,166,666.752 (PIN/POUT)/s^2
0.195 to 5,235,987.968 rad/s^2
Linear:
0.000 to 833.333 counts/s^2
0.031*MOTOR.PITCH to 833,333.333*MOTOR.PITCH mm/s^2
30.994*MOTOR.PITCH to 833,333,333.333*MOTOR.PITCH μm/s^2
0.155 to 4,166,666.667 (PIN/POUT)/s^2
```
```
Default Value
```
```
Rotary:
50.000 rps/s
3,000.000 rpm/s
18,000.000 deg/s^2
250.000 (PIN/POUT)/s^2
314.159 rad/s^2
Linear:
0.050 counts/s^2
1.000*MOTOR.PITCH mm/s^2
1,000.000*MOTOR.PITCH μm/s^2
250.000 (PIN/POUT)/s^2
Data Type Float
See Also UNIT.ACCROTARY, UNIT.ACCLINEAR
Start Version M_0-0-50-0
```
```
AKD Parameter and Command Reference Guide | HOME Parameters
```

AKD Parameter and Command Reference Guide | HOME Parameters

```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 3502h/0
Data Type Integer 32
PDO Mappable N/A
Start Version
```
#### Description

```
This parameter determines the acceleration of the motor during the homing procedure.
```

### HOME.DEC

```
General Information
Type R/W Parameter
Description Sets homing deceleration.
```
```
Units
```
```
Depends on UNIT.ACCROTARY or UNIT.ACCLINEARUNIT.A-
CCLINEAR
Rotary: rps/s, rpm/s, deg/s^2 , (PIN/POUT)/s^2 , rad/s^2
Linear: counts/s^2 , mm/s^2 , μm/s^2 , (PIN/POUT)/s^2
```
```
Range
```
```
Rotary:
0.031 to 833,333.333 rps/s
1.860 to 50,000,000.000 rpm/s
11.158 to 300,000,000.000 deg/s^2
0.155 to 4,166,666.752 (PIN/POUT)/s^2
0.195 to 5,235,987.968 rad/s^2
Linear:
0.000 to 833.333 counts/s^2
0.031*MOTOR.PITCH to 833,333.333*MOTOR.PITCH mm/s^2
30.994*MOTOR.PITCH to 833,333,333.333*MOTOR.PITCH μm/s^2
0.155 to 4,166,666.667 (PIN/POUT)/s^2
```
```
Default Value
```
```
Rotary:
50.000 rps/s
3,000.000 rpm/s
18,000.000 deg/s^2
250.000 (PIN/POUT)/s^2
314.159 rad/s^2
Linear:
0.050 counts/s^2
1.000*MOTOR.PITCH mm/s^2
1000.000*MOTOR.PITCH μm/s^2
250.000 (PIN/POUT)/s^2
Data Type Float
See Also UNIT.ACCROTARY, UNIT.ACCLINEAR
Start Version M_0-0-50-0
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 3524h/0
Data Type Integer 32
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

```
AKD Parameter and Command Reference Guide | HOME Parameters
```

AKD Parameter and Command Reference Guide | HOME Parameters

```
This parameter sets the deceleration of the motor during the homing procedure.
```

### HOME.DIR

```
General Information
Type NV Parameter
Description Sets homing direction.
Units N/A
Range 0 to 1
Default Value 1
Data Type Integer
See Also N/A
Start Version M_0-0-50-0
```
#### Description

This parameter determines the direction in which the motor should start to move during a homing procedure.

0 = Movement in negative direction.

1 = Movement in positive direction.

```
AKD Parameter and Command Reference Guide | HOME Parameters
```

AKD Parameter and Command Reference Guide | HOME Parameters

### HOME.DIST

```
General Information
Type R/W Parameter
Description Sets homing distance.
```
```
Units
```
```
Depends on UNIT.PROTARY or UNIT.PLINEARUNIT.ACCLINEAR
Rotary: counts, rad, deg, PIN/POUT, counts 16 bit
Linear: counts, mm, μm, PIN/POUT, counts 16 bit
Range N/A
Default Value 0
Data Type Float
See Also N/A
Start Version M_0-0-50-0
```
#### Description

```
This parameter takes effect only after the homing procedure is complete (see the HOME.MODE description).
HOME.DIST specifies an additional movement after the homing procedure is complete. The drive uses the
homing acceleration, deceleration, and velocity parameters for this movement. This parameter can be used to
let the motor move away from the home position by the value of HOME.DIST.
A value not equal to 0 triggers an additional movement of the selected homing distance after the general hom-
ing procedure. A value of 0 for HOME.DIST causes no additional movement.
```

### HOME.FEEDRATE

```
General Information
Type R/W Parameter
Description Sets homing velocity factor.
Units %
Range 0 to 100%
Default Value 50%
Data Type Integer
See Also N/A
Start Version M_0-0-50-0
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 6099h/2
Data Type Unsigned 32
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

This parameter is used in order to reduce the velocity during the index search (index = zero-pulse of a feed-
back device). This parameter determines the percentage of the homing velocity (HOME.V) that should be
used during the index-search.

```
AKD Parameter and Command Reference Guide | HOME Parameters
```

AKD Parameter and Command Reference Guide | HOME Parameters

### HOME.IPEAK

```
General Information
Type R/W Parameter
Description Sets the current limit during homing procedure to a mechanical stop
Units A
Range ± Drive peak current A
Default Value [(1/120) * DRV.IPEAK] A
Data Type Float
See Also HOME.MODE
Start Version M_00-00-62
```
#### Description

```
This parameter sets the intermediate current limit during a homing procedure to a mechanical stop
(HOME.MODE 8, 9 or 10). The current-controller limit (IL.LIMITP and IL.LIMITN) is set to ±HOME.IPEAK
while the homing procedures are active.
HOME.IPEAK is active as soon as the homing procedure starts and remains active until the home position is
found. Previous current limit settings are re-activated before the motor covers the homing distance
(HOME.DIST ≠ 0).
```

### HOME.MODE

```
General Information
Type R/W Parameter
Description Selects the homing mode.
Units N/A
Range 0 to 10
Default Value 0
Data Type Integer
See Also N/A
Start Version M_0-0-50-0
```
#### Description

HOME.MODE specifies the homing procedure of the drive. There are 10 homing modes available in the drive.

**Homing mode 0 (set immediately the home position):**

The actual- and the command position of the drive will be immediately be set to the HOME.P value.

**Homing mode 1 (homing to hardware limit switches):**

This homing mode starts a motion to a positive or negative hardware limit switch. The sequence of this hom-
ing mode is as follows:

1. The motor starts to move according to the HOME.DIR setting.
2. The motor stops as soon as the hardware limit switch has been detected and changes afterwards the
    direction of the movement.
3. The home position has been found as soon as the hardware limit switch is not active any more. The
    actual- and the command position of the drive will immediately be set to the HOME.P value and the
    motor ramps down to velocity 0.

**Homing mode 2 (homing to hardware limit switch with movement to zero-angle):**

This homing mode starts a motion to a positive or negative hardware limit switch. The home position is
located at the mechanical zero-angle of the feedback. The sequence of this homing mode is as follows:

1. The motor starts to move according to the HOME.DIR setting.
2. The motor stops as soon as the hardware limit switch has been detected and changes afterwards the
    direction of the movement.
3. The home position has been found as soon as the hardware limit switch is not active any more. The
    actual- and the command position of the drive will immediately be set to the HOME.P value plus dis-
    tance to the mechanical zero angle of the feedback device according to the current direction.
4. The motor decelerates until velocity 0 has been reached.
5. The motor moves to the home position (HOME.P), which is located at the mechanical zero-angle of the
    feedback.

**Homing mode 3 (homing to hardware limit switch with index detection):**

This mode is not implemented yet.

This homing mode starts a motion to a positive or negative hardware limit switch. The home position is
located at the point where the index signal (the zero-pulse signal of a feedback device) has been detected by
the drive. The sequence of this homing mode is as follows:

```
AKD Parameter and Command Reference Guide | HOME Parameters
```

AKD Parameter and Command Reference Guide | HOME Parameters

1. The motor starts to move according to the HOME.DIR setting.
2. The motor stops as soon as the hardware limit switch has been detected and changes afterwards the
    direction of the movement.
3. The motor ramps down to a reduced velocity as soon as the hardware limit switch is not active any
    more (please refer also to HOME.FEEDRATE). The Drive is searching for the index-signal during this
    time. The home-position has been found as soon as the index-signal has been detected by the Drive.
4. The actual- and the command position of the Drive will be set to the HOME.P value as soon as the
    index-signal was found and the Drive ramps down to velocity 0.
**Homing mode 4 (homing to a home-switch):**
This homing mode starts a motion until a digital input, which is assigned to act as a home-switch, has been
activated.
The home-switch must be activated according to the setting of the HOME.DIR setting. The home position is
found as soon as the home-switch was activated during a motion in direction of the HOME.DIR setting.
The sequence of this homing mode is as follows:
1) The motor starts to move according to the HOME.DIR setting.
2) The home position has been found as soon as the home-switch becomes active during a motion in direction
of the HOME.DIR setting. The actual- and the command position of the Drive will immediately be set to the
HOME.P value and the motor ramps down to velocity 0.
Remarks:
The hardware limit switches are monitored during the whole homing procedure. The Drive behaves as follows
in case that a hardware limit switch is active before the home-switch has been activated:
a) The motor changes the direction until the home switch is crossed.
b)Themotorrampsdowntovelocity0andchangesafterwardsthedirectionagainaftercrossingthehome-switch.
c) The home-switch will now be activated according to the HOME.DIR setting and the home-position has
been found. The actual- and the command position of the Drive will immediately be set to the HOME.P value
and the motor ramps down to velocity 0.
**Homing mode 5 (homing to a home-switch with movement to zero-angle):**
This homing mode starts a motion until a digital input, which is assigned to act as a home-switch, has been
activated. The motor moves afterwards to the mechanical zero-angle of the feedback.
The home-switch must be activated according to the setting of the HOME.DIR setting. The home position is
found as soon as the home-switch was activated during a motion in direction of the HOME.DIR setting.
The sequence of this homing mode is as follows:
1. The motor starts to move according to the HOME.DIR setting.
2. The home position has been found as soon as the home-switch becomes active during a motion in
direction of the HOME.DIR setting. The actual- and the command position of the drive will immediately
be set to the HOME.P value plus distance to the mechanical zero angle of the feedback device accord-
ing to the current direction.
3. The motor decelerates until velocity 0 has been reached.
4. The motor moves to the home position (HOME.P), which is located at the mechanical zero-angle of the
feedback.
Remarks:
The hardware limit switches are monitored during the whole homing procedure. The drive behaves as follows
in case that a hardware limit switch is active before the home-switch has been activated:


1. The motor changes the direction until the home switch is crossed.
2. The motor ramps down to velocity 0 and changes afterwards the direction again after crossing the
    home-switch.
3. The home-switch will now be activated according to the HOME.DIR setting and the home-position has
    been found. The actual- and the command position of the drive will immediately be set to the HOME.P
    value plus distance to the mechanical zero angle of the feedback device according to the current direc-
    tion.
4. The motor decelerates until velocity 0 has been reached.
5. The motor moves to the home position (HOME.P), which is located at the mechanical zero-angle of the
    feedback.

**Homing mode 6 (homing to a home-switch with index detection):**

This mode is not implemented yet.

This homing mode starts a motion until a digital input, which is assigned to act as a home-switch, has been
activated. The motor moves afterwards with a reduced velocity HOME.FEEDRATE until the index signal (the
zero-pulse signal of a feedback device) has been detected by the drive.
The home-switch must be activated according to the setting of the HOME.DIR setting.

The sequence of this homing mode is as follows:

1. The motor starts to move according to the HOME.DIR command.
2. The motor decelerates to a reduced velocity according to the HOME.FEEDRATE setting as soon as
    the home-switch becomes active during a motion in direction of the HOME.DIR setting.
3. The actual- and the command position of the drive will immediately be set to the HOME.P value as
    soon as the index-signal has been detected. The motor decelerates until velocity 0 has been reached.

Remarks:
The hardware limit switches are monitored during the whole homing procedure. The Drive behaves as follows
in case that a hardware limit switch is active before the home-switch has been activated:

a) The motor changes the direction until the home-switch is crossed.

b)Themotorrampsdowntovelocity0andchangesafterwardsthedirectionagainaftercrossingthehome-switch.
c) The home-switch will now be activated according to the HOME.DIR command. The motor decelerates to a
reduced velocity according to the HOME.FEEDRATE setting as soon as the home-switch becomes active.

d) The actual- and the command position of the drive will immediately be set to the HOME.P value as soon as
the index-signal has been detected. The motor decelerates until velocity 0 has been reached.

**Homing mode 7 (homing to the mechanical zero-angle of the feedback):**

Thishomingmodestartsamotiontothemechanicalzero-angleofthefeedbackindirectionoftheHOME.DIRsetting.

The sequence of this homing mode is as follows:

1. The home-position is immediately found by the drive. The actual and the command position of the drive
    are set to the HOME.P value plus distance to the mechanical zero angle of the feedback device accord-
    ing to the HOME.DIR setting.
2. The motor moves to the home position (HOME.P), which is located at the mechanical zero-angle of the
    feedback

**Homing mode 8 (homing to a mechanical stop):**

This homing mode starts a motion to a mechanical stop. A mechanical stop is detected as soon as the abso-
lute value of the position error (PL.ERR) is larger than the HOME.PERRTHRESH setting. During this homing
method the current command value is limited to the TBD value.

```
AKD Parameter and Command Reference Guide | HOME Parameters
```

AKD Parameter and Command Reference Guide | HOME Parameters

```
The sequence of this homing mode is as follows:
1) The motor starts to move according to the HOME.DIR command.
2)Theactual-andthecommandpositionoftheDrivewillimmediatelybesettotheHOME.Pvalueassoonasthe
absolutevalueofPL.ERR islargerthantheHOME.PERRTHRESHsetting.Thehomingisimmediatelyfinished.
Remark:
It must be ensured that the current limitation (TBD) has been set to a reasonable value in order to prevent the
machine from too much mechanical force when moving against a mechanical stop.
Homing mode 9 (homing to a mechanical stop plus movement to the mechanical zero-angle of the
feedback):
This homing mode starts a motion to a mechanical stop. A mechanical stop is detected as soon as the abso-
lute value of the position error (PL.ERR) is larger than the HOME.PERRTHRESH setting. During this homing
method the current command value is limited to the TBD value. The motor moves afterwards in the opposite
direction to the zero-angle of the feedback.
The sequence of this homing mode is as follows:
1) The motor starts to move according to the HOME.DIR command.
2) The actual- and the command position of the Drive will immediately be set to the HOME.P value plus dis-
tance to the mechanical zero angle of the feedback device according to opposite direction of DRV.DIR as
soon as the absolute value of PL.ERR is larger than the HOME.PERRTHRESH setting.
3) The motor starts now moving to the opposite direction of the DRV.DIR setting until the home position
(HOME.P) has been reached, which is located at the mechanical zero-angle of the feedback.
Remark:
It must be ensured that the current limitation (TBD) has been set to a reasonable value in order to prevent the
machine from too much mechanical force when moving against a mechanical stop.
Homing mode 10 (homing to a mechanical stop plus with index detection):
This mode is not implemented yet.
This homing mode starts a motion to a mechanical stop. A mechanical stop is detected as soon as the abso-
lute value of the position error (PL.ERR) is larger than the HOME.PERRTHRESH setting. During this homing
method the current command value is limited to the TBD value. The motor moves afterwards with a reduced
velocity (HOME.FEEDRATE) until the index signal (the zero-pulse signal of a feedback device) has been
detected by the Drive.
The sequence of this homing mode is as follows:
1) The motor starts to move according to the HOME.DIR command.
2) The motor changes the direction with a reduced velocity (HOME.FEEDRATE) as soon as the absolute
value of PL.ERR is larger than the HOME.PERRTHRESH setting.
3) The actual- and the command position of the Drive will immediately be set to the HOME.P value as soon as
the index-signal has been detected. The motor decelerates until velocity 0 has been reached.
Remark:
It must be ensured that the current limitation (TBD) has been set to a reasonable value in order to prevent the
machine from too much mechanical force when moving against a mechanical stop.
```

### HOME.MOVE

```
General Information
Type Command
Description Starts a homing procedure.
Units N/A
Range N/A
Default Value N/A
Data Type N/A
See Also N/A
Start Version M_0-0-38
```
#### Description

The HOME.MOVE command starts a homing procedure. The DRV.OPMODE must be set to 2 (closed posi-
tion loop) and DRV.CMDSOURCE must be set to 0 (TCP/IP command).

```
AKD Parameter and Command Reference Guide | HOME Parameters
```

AKD Parameter and Command Reference Guide | HOME Parameters

### HOME.P

```
General Information
Type R/W Parameter
Description Sets home position.
```
```
Units
```
```
Depends on UNIT.PROTARY or UNIT.PLINEAR
Rotary: counts, rad, deg, PIN/POUT, counts 16 bit
Linear: counts, mm, μm, PIN/POUT, counts 16 bit
Range N/A
Default Value 0
Data Type Float
See Also N/A
Start Version M_0-0-50-0
```
#### Description

```
This parameter sets the home position. The command and actual position of the drive will be set to this value
as soon as a homing event occurs. The homing events differ in each homing mode.
```

### HOME.PERRTHRESH

```
General Information
Type R/W Parameter
Description Position lag threshold.
```
```
Units
```
```
Depends on UNIT.PROTARY or UNIT.PLINEAR
Rotary: counts, rad, deg, PIN/POUT, Countes16 bit
Linear: counts, mm, μm, PIN/POUT, Counts16 bit
Range N/A
Default Value N/A
Data Type Float
See Also N/A
Start Version M_0-0-50-0
```
#### Description

This parameter is used for the homing modes against a mechanical stop (HOME.MODE = 8, 9, and 10). The
absolute value of the following error (PL.ERR) is compared with HOME.PERRTHRESH in order to detect a
mechanical stop.

```
AKD Parameter and Command Reference Guide | HOME Parameters
```

AKD Parameter and Command Reference Guide | HOME Parameters

### HOME.SET

```
General Information
Type Command
Description Immediately sets the home position.
Units N/A
Range N/A
Default Value N/A
Data Type N/A
See Also N/A
Start Version M_0-0-38
```
```
Fieldbus Information
EtherCAT COE & CANOpen
Index/Subindex or
Parameter Number 35F0h/0
Data Type Integer 32
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

```
The HOME.SET command immediately homes the drive. The drive can be homed in an enabled or disabled
state. Motion in the current mode of operation (DRV.OPMODE=0) or velocity mode of operation (DRV.O-
PMODE=1) is not affected by the HOME.SET command. Motion in the position mode of operation (DRV.O-
PMODE=2) is immediately aborted when the HOME.SET command is issued.
```

### HOME.V

```
General Information
Type R/W Parameter
Description Sets homing velocity.
```
```
Units
```
```
Depends on UNIT.VROTARY or UNIT.VLINEAR
Rotary: rpm, rps, deg/s, (PIN/POUT)/s, rad/s
Linear: counts/s, mm/s, μm/s, (PIN/POUT)/s
```
```
Range
```
```
Rotary:
0.001 to 12,000.000 rpm
0.001 to 200.000 rps
0.001 to 72,000.000 deg/s
0.001 to 1,000.000 (PIN/POUT)/s
0.001 to 1,256.637 rad/s
Linear:
0.001 to 0.200 counts/s
0.001*MOTOR.PITCH to 200.000*MOTOR.PITCH mm/s
0.004*MOTOR.PITCH to 200,000.000*MOTOR.PITCH μm/sec
0.001 to 1,000.000 (PIN/POUT)/s
```
```
Default Value
```
```
Rotary:
12,000.000 rpm
200.000 rps
17,999.998 deg/s
250.000 (PIN/POUT)/s
1,256.637 rad/s
Linear:
0.050 counts/s
1.000*MOTOR.PITCH mm/s
999.998*MOTOR.PITCH μm/sec
250.000 (PIN/POUT)/s
Data Type Float
See Also N/A
Start Version M_0-0-50-0
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 6099h/1
Data Type Unsigned 32
PDO Mappable N/A
Start Version M_00-00-62-000
```
#### Description

This parameter sets the velocity of the motor during the homing procedure.

```
AKD Parameter and Command Reference Guide | HOME Parameters
```

AKD Parameter and Command Reference Guide | HWLS Parameters

## HWLS Parameters


### HWLS.NEGSTATE

```
General Information
Type R/O Parameter
Description Reads the status of the negative hardware limit switch.
Units 0 to 1
Range N/A
Default Value Boolean
Data Type HWLS.POSSTATE
See Also N/A
Start Version M_00-00-62-000
```
#### Description

HWLS.NEGSTATE reads the status of the negative HW limit switch as follows:
0 = low

1 = high

```
AKD Parameter and Command Reference Guide | HWLS Parameters
```

AKD Parameter and Command Reference Guide | HWLS Parameters

### HWLS.POSSTATE

```
General Information
Type R/O Parameter
Description Reads the status of the positive hardware limit switch.
Units N/A
Range 0 to 1
Default Value N/A
Data Type Boolean
See Also HWLS.NEGSTATE
Start Version M_00-00-62-000
```
#### Description

```
HWLS.POSSTATE reads the status of the positive hardware limit switch as follows:
0 = low
1 = high
```

## IL Parameters

### IL.BUSFF

```
General Information
Type R/O Parameter
Description Displays the current feedforward value injected by the fieldbus
Units A
Range N/A
Default Value N/A
Data Type Float
See Also IL.KBUSFF
Start Version M_0-0-32
```
#### Description

This parameter displays the current feedforward value injected by the fieldbus

```
AKD Parameter and Command Reference Guide | IL Parameters
```

AKD Parameter and Command Reference Guide | IL Parameters

#### IL.CMD

```
General Information
Type R/O Parameter
Description Reads the value of the q-component current controller inside the FPGA.
Units Arms
Range ± Drive peak current
Default Value N/A
Data Type Float
See Also DRV.IPEAK
Start Version M_0-0-15
```
#### Description

```
IL.CMD displays the q-component current command value of the current loop after any limitation (such as a
parameter setting or I^2 t calculation).
```

#### IL.CMDU

```
General Information
Type R/W Parameter
Description Sets the user current command.
Units A
Range ± Drive peak current
Default Value 0 A
Data Type Float
See Also DRV.IPEAK, DRV.OPMODE,DRV.CMDSOURCE
Start Version M_0-0-15
```
#### Description

This parameter sets the user current command value.
The current command value, which is provided to the current loop (IL.CMD), can be limited further using a
parameter setting or I^2 t calculation.

```
AKD Parameter and Command Reference Guide | IL Parameters
```

AKD Parameter and Command Reference Guide | IL Parameters

#### IL.DIFOLD

```
General Information
Type R/O Parameter
Description Reads the drive foldback current limit.
Units A
Range 0 to 2,147,483.647 A
Default Value N/A
Data Type Float
See Also Foldback
Start Version M_0-0-15
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 3559h/0
Data Type Integer 32
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

```
IL.DIFOLD is the output of the drive foldback algorithm. It is an artificial current, which can be higher or lower
than the drive peak current. When IL.DIFOLD is lower than the existing current limit (such as IL.LIMITP), it
becomes the active current limit.
IL.DIFOLD decreases when the actual current is higher than drive continuous current and increases (up to a
certain level) when the actual current is lower than drive continuous current.
```

#### IL.FB

```
General Information
Type R/O Parameter
Description Reads the actual value of the d-component current.
Units Arms
Range ± Drive peak current
Default Value N/A
Data Type Float
See Also N/A
Start Version M_0-0-15
```
#### Description

This parameter reads the measured, de-rotated actual current value of the motor.

```
AKD Parameter and Command Reference Guide | IL Parameters
```

AKD Parameter and Command Reference Guide | IL Parameters

#### IL.FF

```
General Information
Type R/O Parameter
Description Displays the current loop overall feedforward value
Units A
Range NA
Default Value NA
Data Type Float
See Also IL.KBUSFF, IL.KVFF, IL.OFFSET, IL.FRICTION, IL.KACCFF
Start Version M_0-0-32
```
#### Description

```
This parameter displays the current loop overall feedforward value.
```

#### IL.FOLDFTHRESH

```
General Information
Type R/O Parameter
Description Sets the foldback fault level.
Units Arms
Range 0 to 500 Arms
Default Value Drive peak current
Data Type Float
See Also Foldback
Start Version M_0-0-15
```
```
Fieldbus Information
EtherCAT COE and CANopen
Index/Subindex or
Parameter Number 3420h/0
Data Type Unsigned 16
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

IL.FOLDFTHRESH is the fault level of the current foldback algorithm. If IL.IFOLD drops below the value for
IL.FOLDFTHRESH, then a fault is generated and the drive is disabled.
To avoid reaching the current foldback fault level, set IL.FOLDFTHRESH well below the continuous current
value for both the drive and the motor or set the IL.FOLDFTHRESH value to zero.

```
AKD Parameter and Command Reference Guide | IL Parameters
```

AKD Parameter and Command Reference Guide | IL Parameters

#### IL.FOLDFTHRESHU

```
General Information
Type NV Parameter
Description Sets the user value for the foldback fault level.
Units Arms
Range 0 to 500 Arms
Default Value Drive peak current
Data Type Float
See Also IL.FOLDFTHRESH, Foldback
Start Version M_00-00-55-000
```
#### Description

```
IL.FOLDFTHRESHU is the fault level of the current foldback algorithm. The value of IL.FOLDFTHRESH is
the minimum of DRV.IPEAK, MOTOR.IPEAK, and IL.FOLDFTHRESH.
```

#### IL.FOLDWTHRESH

```
General Information
Type NV Parameter
Description Sets the foldback warning level.
Units Arms
Range 0 to 500 Arms
Default Value 0 A
Data Type Float
See Also Foldback
Start Version M_0-0-15
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 355Ah/0
Data Type Integer 32
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

IL.FOLDWTHRESH is the warning level of the current foldback algorithm. When IL.IFOLD drops **below**
IL.FOLDWTHRESH a warning is generated.
To ensure that the current foldback warning level is never reached, IL.FOLDWTHRESH should be set well
below the continuous current value for both the drive and the motor. You can also set the IL.FOLDFTHRESH
value to zero.

```
AKD Parameter and Command Reference Guide | IL Parameters
```

AKD Parameter and Command Reference Guide | IL Parameters

#### IL.FRICTION

```
General Information
Type R/W Parameter
Description Sets friction compensation value.
Units A
Range 0 to IL.LIMITP
Default Value 0
Data Type Float
See Also IL.FF
Start Version M_0-0-32
```
```
Fieldbus Information
EtherCAT COE & CANOpen
Index/Subindex or
Parameter Number 3422h/0
Data Type
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

```
Position command derivative sign is multiplied by this value to be injected to the current command.
```

#### IL.IFOLD

```
General Information
Type R/O Parameter
Description Reads the overall foldback current limit.
Units A
Range 0 to 2,147,483.647 A
Default Value N/A
Data Type Float
See Also Foldback
Start Version M_0-0-15
```
#### Description

Two current foldback algorithms run in parallel in the drive: the drive foldback algorithm and the motor foldback
algorithm. Each algorithm uses different sets of parameters.

Each algorithm has its own foldback current limit, IL.DIFOLD and IL.MIFOLD. The overall foldback current
limit is the minimum of the two at any given moment.

IL.IFOLD = min (IL.DIFOLD, IL.MIFOLD).
IL.DIFOLD is an artificial current, which can be higher or lower than the drive or motor peak current. When
IL.IFOLD becomes lower than the existing current limit (e.g. IL.LIMITP), it becomes the active current limit.

```
AKD Parameter and Command Reference Guide | IL Parameters
```

AKD Parameter and Command Reference Guide | IL Parameters

#### IL.KACCFF

```
General Information
Type R/W Parameter
Description Sets current loop acceleration feedforward gain value
Units NA
Range 0.0 to 2.0
Default Value 0.0
Data Type Float
See Also IL.FF
Start Version M_0-0-32
```
#### Description

```
This value sets the gain for the acceleration feedforward (a scaled second derivative of the position command
is added to the current command value).
This parameter is valid only in the position mode (DRV.OPMODE = 2).
```

#### IL.KBUSFF

```
General Information
Type RW
Description Current loops fieldbus injected feed-forward gain
Units NA
Range 0 to 2
Default Value NA
Data Type Float
See Also IL.FF, IL.BUSFF
Start Version M_0-0-32
```
#### Description

This parameter scales the feedforward term added by the fieldbus to the current command. The nominal feed-
forward value can be multiplied by this gain value.

This parameter is only used in the position mode (DRV.OPMODE = 2).

```
AKD Parameter and Command Reference Guide | IL Parameters
```

AKD Parameter and Command Reference Guide | IL Parameters

#### IL.KP

```
General Information
Type NV Parameter
Description Sets the proportional gain of the q-component of the PI regulator.
Units V/A
Range 0 to 2,000 V/A
Default Value Read from the motor or, if no memory, 50 V/A
Data Type Float
See Also N/A
Start Version M_0-0-15
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 3598h/0
Data Type Integer 32
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

```
IL.KP is used to modify the proportional gain of the PI-loop that controls the q-component of the current.
```

#### IL.KPDRATIO

```
General Information
Type NV Parameter
Description
Sets the proportional gain of the d-component current PI-regulator as a per-
centage of IL.KP
Units N/A
Range 0 to 100
Default Value 1
Data Type Float
See Also IL.KP
Start Version M_0-0-15
```
#### Description

This parameter allows the user to modify the proportional gain of the PI-loop, which controls the d-component
of the current.

```
AKD Parameter and Command Reference Guide | IL Parameters
```

AKD Parameter and Command Reference Guide | IL Parameters

#### IL.KVFF

```
General Information
Type R/W
Description Current loops velocity feed-forward gain
Units NA
Range 0 to 2
Default Value 0
Data Type Float
See Also IL.FF
Start Version M_0-0-32
```
#### Description

```
This parameter sets the gain for the velocity loop feedforward. The nominal feedforward value can be mul-
tiplied by this gain value.
This parameter is only used in position mode (DRV.OPMODE = 2).
```

#### IL.LIMITN

```
General Information
Type NV Parameter
Description Sets the negative user (application) current limit.
Units A
Range Negative drive peak current to 0 A
Default Value Negative drive peak current
Data Type Float
See Also IL.LIMITP
Start Version M_0-0-15
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 356Fh/0
Data Type Integer 32
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

This parameter sets the negative user limitation of the q-component current command value. The real current
command value can furthermore be limited by additional settings or calculations, such as an I^2 t calculation or
motor peak current.

```
AKD Parameter and Command Reference Guide | IL Parameters
```

AKD Parameter and Command Reference Guide | IL Parameters

#### IL.LIMITP

```
General Information
Type NV Parameter
Description Sets the positive user (application) current limit.
Units A
Range 0 A to drive peak current
Default Value Drive peak current
Data Type Float
See Also IL.LIMITN
Start Version M_0-0-15
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 356Eh/0
Data Type Integer 32
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

```
This parameter sets the positive user limitation of the q-component current command value. The real current
command value can furthermore be limited by some additional settings or calculations such as I^2 t calculation
and motor peak current.
```

#### IL.MFOLDD

```
General Information
Type R/O Parameter
Description Sets the motor foldback maximum time at motor peak current.
Units s
Range 0.1 to 2400 s
Default Value 10 s
Data Type Float
See Also Foldback
Start Version M_0-0-15
```
#### Description

IL.MFOLDD sets the maximum time allowed for the motor to remain at peak current before starting to fold
towards the motor continuous current. When at motor peak current, IL.MFOLDD is the amount of time before
the foldback algorithm starts to reduce the current.

```
AKD Parameter and Command Reference Guide | IL Parameters
```

AKD Parameter and Command Reference Guide | IL Parameters

#### IL.MFOLDR

```
General Information
Type R/O Parameter
Description Sets the motor foldback recovery time.
Units s
Range 0.1 to 65,535 s
Default Value Calculated from other foldback parameters.
Data Type Float
See Also Foldback
Start Version M_0-0-15
```
#### Description

```
IL.MFOLDR sets the recovery time for the motor foldback algorithm. If 0 current is applied for at least the
recovery time duration, it is possible to apply motor peak current for the duration of IL.MFOLDD time.
The IL.MFOLDR value is automatically calculated from other foldback parameters.
```

#### IL.MFOLDT

```
General Information
Type R/O Parameter
Description
Sets the motor foldback time constant of the exponential current drop (fold-
back).
Units s
Range 0.1 to 2,400 s
Default Value 10 s
Data Type Float
See Also Foldback
Start Version M_0-0-15
```
#### Description

IL.MFOLDT sets the time constant of the exponential drop (foldback) of the current towards motor continuous
current.

```
AKD Parameter and Command Reference Guide | IL Parameters
```

AKD Parameter and Command Reference Guide | IL Parameters

#### IL.MIFOLD

```
General Information
Type R/O Parameter
Description Sets the motor foldback current limit.
Units A
Range 0 to 2147483.647 A
Default Value N/A
Data Type Float
See Also Foldback
Start Version M_0-0-15
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 35A4h/0
Data Type Integer 32
PDO Mappable N/A
Start Version M_00-00-62-000
```
#### Description

```
IL.MIFOLD sets the output of the motor foldback algorithm. It is an artificial current, which can be higher or
lower than the motor peak current. When IL.MIFOLD becomes lower than the existing current limit
(IL.LIMITP) it becomes the active current limit.
IL.MIFOLD decreases when the actual current is higher than motor continuous current and increases (up to a
certain level) when the actual current is lower than the motor continuous current.
```

#### IL.OFFSET

```
General Information
Type RW
Description A constant current command added to compensate for gravity.
Units A
Range IL.LIMITN to IL.LIMITP
Default Value 0
Data Type Float
See Also IL.FF
Start Version M_0-0-32
```
```
Fieldbus Information
EtherCAT COE & CANOpen
Index/Subindex or
Parameter Number 3423h/0
Data Type
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

This value will be added to the overall current loop feedforward value.

```
AKD Parameter and Command Reference Guide | IL Parameters
```

AKD Parameter and Command Reference Guide | IL Parameters

#### IL.VCMD

```
General Information
Type R/O Parameter
Description Sets the output of the q-component PI regulator.
Units Vrms
Range 0 Vrms to bus voltage
Default Value N/A
Data Type Integer
See Also IL.VDCMD
Start Version M_0-0-15
```
#### Description

```
Sets the output of the current loop that controls the q-component of the current.
```

#### IL.VUFB

```
General Information
Type R/O Parameter
Description Reads the measured voltage on the u-winding of the motor.
Units V
Range –1200*VBusScale to +1200*VBusScale
Default Value N/A
Data Type Integer
See Also IL.VVFB
Start Version M_0-0-15
```
#### Description

The range for this parameter depends on whether the drive model is an MV/240 Vac or an HV/480 Vac.
The VBusScale parameter sets the drive model:

MV/240 Vac: VBusScale = 1

HV/480 Vac: VBusScale = 2

VBusScale must be used for multiple parameter ranges that are model dependent, such as IL.KP.

```
AKD Parameter and Command Reference Guide | IL Parameters
```

AKD Parameter and Command Reference Guide | IL Parameters

#### IL.VVFB

```
General Information
Type R/O Parameter
Description Reads the measured voltage on the v-winding of the motor.
Units V
Range –1200*VBusScale to +1200*VBusScale
Default Value N/A
Data Type Integer
See Also IL.VUFB
Start Version M_0-0-15
```
#### Description

```
The range for this parameter depends on whether the drive model is an MV/240 Vac or an HV/480 Vac.
The VBusScale parameter sets the drive model:
MV/240 Vac: VBusScale = 1
HV/480 Vac: VBusScale = 2
VBusScale needs to be used for multiple parameter ranges that are model dependent such as IL.KP.
```

### MOTOR Parameters

```
AKD Parameter and Command Reference Guide | MOTOR Parameters
```

AKD Parameter and Command Reference Guide | MOTOR Parameters

#### MOTOR.AUTOSET

```
General Information
Type NV Parameter
Description Determines which drive parameters are calculated automatically.
Units N/A
Range 0 to 1
Default Value 0
Data Type Boolean
See Also N/A
Start Version M_00-00-58-000
```
#### Description

```
This parameter determines whether or not certain drive parameters (for example, IL.KP or MOTOR.POLES)
are calculated automatically. A value of 1 causes the parameters to be automatically calculated from the
motor ID data (read from memory-supporting feedback devices, such as SFD, Endat, and BISS). Auto-
matically calculated parameters are read-only. A value of 0 disables the automatic calculation and you must
set the parameters manually. Manually set parameters are read-write.
```
#### MOTOR.BRAKE

```
General Information
Type NV Parameter
Description Sets the presence or absence of a motor brake.
Units N/A
Range 0 to 1
Default Value 0
Data Type Boolean
See Also N/A
Start Version M_0-0-15
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number
3587h/0
Data Type Integer 32
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

```
The MOTOR.BRAKE parameter notifies the firmware whether a brake exists or not. It does not enable or dis-
able the brake. If a brake is found to be present, the firmware considers hardware indications regarding the
brake circuits (open circuit, short circuit, etc). If a brake does not exist, then the firmware ignores the hardware
indications since they are irrelevant.
```

```
Value Status
0 Motor brake does not exist.
1 Motor brake exists and brake hardware circuitry checks are enabled.
```
Enabling the MOTOR.BRAKE (value set to 1) when no motor brake exists creates a fault.

The motor brake is polled every 16 ms.

```
AKD Parameter and Command Reference Guide | MOTOR Parameters
```

AKD Parameter and Command Reference Guide | MOTOR Parameters

#### MOTOR.BRAKERLS

```
General Information
Type Command
Description Allows a user to release the motor brake.
Units N/A
Range 0 to 1
Default Value 0
Data Type Integer
See Also N/A
Start Version M_0-0-41
```
#### Description

```
This command allows a user to release motor brake although the brake should be engaged.
0 = Drive controls the brake.
1 = Brake is released.
```
```
Note: There is a digital input mode used for the same purpose. The two mechanisms are independent.
```

#### MOTOR.BRAKESTATE

```
General Information
Type R/O Parameter
Description Reads the actual status of the motor brake.
Units N/A
Range
Brake closed or not present.
Brake opened.
Default Value Brake closed or not present.
Data Type String
See Also N/A
Start Version M_0-0-42
```
#### Description

This parameter eads the actual status of the motor brake and can an only show two states:
1) Brake closed or not present

2) Brake open

```
AKD Parameter and Command Reference Guide | MOTOR Parameters
```

AKD Parameter and Command Reference Guide | MOTOR Parameters

#### MOTOR.CTF0

```
General Information
Type NV Parameter
Description Sets the thermal constant of the motor coil.
Units mHz
Range 0.265 to 16,000 mHz
Default Value 10 mHz
Data Type Float
See Also N/A
Start Version M_00-00-62-000
```
#### Description

```
This parameter is used to configure the thermal constant of the motor coil, which is the break frequency of a
single-pole low-pass filter model of the thermal dynamics of the motor coil.
This parameter, together with MOTOR.IPEAK and MOTOR.ICONT, determine the motor foldback param-
eters IL.MFOLDD,IL.MFOLDT, and IL.MFOLDR.
```

#### MOTOR.ICONT

```
General Information
Type NV Parameter
Description Sets the motor continuous current.
Units mA
Range 100 to 500,000 mA
Default Value 1,000 mA
Data Type Float
See Also N/A
Start Version M_0-0-15
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 358Eh/0
Data Type Integer 32
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

This parameter is used to configure the motor continuous current.

#### MOTOR.IDDATAVALID

```
General Information
Type
Description Reports the status of the motor memory.
Units
Range
Default Value
Data Type
See Also
Start Version
```
#### Description

MOTOR.IDDATAVALID reports the status of the motor memory status.
The valid values for this keyword are the following:

```
Value Description
0 Error in identification
1 Success in identification
2 Identification in process
3 Identification not started yet
4 Success recognizing feedback, but failed to varify OEM
data integrity
```
```
AKD Parameter and Command Reference Guide | MOTOR Parameters
```

AKD Parameter and Command Reference Guide | MOTOR Parameters


### MOTOR.INERTIA

```
General Information
Type NV Parameter
Description Sets the motor inertia.
```
```
Units
kgcm² for rotary motors
kg for linear motors
Range 1 to 200,000 kgcm² or kg
Default Value 100 kgcm² or kg
Data Type Float
See Also N/A
Start Version M_0-0-15
```
#### Description

This parameter sets the motor inertia.

```
AKD Parameter and Command Reference Guide | MOTOR Parameters
```

AKD Parameter and Command Reference Guide | MOTOR Parameters

### MOTOR.IPEAK

```
General Information
Type NV Parameter
Description Sets the motor peak current.
Units mA
Range 200 to 1,000,000 mA
Default Value 2,000 mA
Data Type Float
See Also N/A
Start Version M_0-0-15
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 358Fh/0
Data Type Integer 32
PDO Mappable N/A
Start Version M_00-00-62-000
```
#### Description

```
This parameter is used to configure the motor peak current.
```

### MOTOR.KT

```
General Information
Type NV Parameter
Description Sets the torque constant of the motor.
Units Nm/A
Range 0.001 to 65 Nm/A
Default Value 0.1 Nm/A
Data Type Float
See Also N/A
Start Version M_0-0-15
```
#### Description

This parameter is the torque constant of the motor in Nm/A.

The value can be online checked according to the following equation:

Kt = 60 *√3 * Ui/( 2 * π* n)

Ui = induced voltage of the motor
n = actual rotor velocity

```
AKD Parameter and Command Reference Guide | MOTOR Parameters
```

AKD Parameter and Command Reference Guide | MOTOR Parameters

### MOTOR.LQLL

```
General Information
Type NV Parameter
Description Sets the line-to-line motor Lq.
Units mH
Range 1 to 2^32 mH
Default Value 17,000 mH
Data Type Float
See Also N/A
Start Version M_0-0-15
```
#### Description

```
This parameter is used to configure the motor line-to-line inductance.
```

### MOTOR.NAME

```
General Information
Type NV Parameter
Description Sets the motor name.
Units N/A
Range 11 chars
Default Value N/A
Data Type String
See Also N/A
Start Version M_0-0-15
```
#### Description

This parameter is used to set the motor name.

```
AKD Parameter and Command Reference Guide | MOTOR Parameters
```

AKD Parameter and Command Reference Guide | MOTOR Parameters

### MOTOR.PHASE

```
General Information
Type NV Parameter
Description Sets the motor phase.
Units Electrical degrees
Range 0 to 360°
Default Value 0°
Data Type Integer
See Also N/A
Start Version M_0-0-15
```
#### Description

```
This parameter sets the motor phase.
```

### MOTOR.PITCH

```
General Information
Type NV Parameter
Description Sets the motor pitch.
Units μm
Range 1,000 to 1,000,000 μm
Default Value 1,000 μm
Data Type Integer
See Also N/A
Start Version M_0-0-15
```
#### Description

This parameter defines the pole-to-pair pitch for the linear motor in micrometers.

```
AKD Parameter and Command Reference Guide | MOTOR Parameters
```

AKD Parameter and Command Reference Guide | MOTOR Parameters

### MOTOR.POLES

```
General Information
Type NV Parameter
Description Sets the number of motor poles.
Units N/A
Range 0 to 128
Default Value 6
Data Type Integer
See Also FB1.POLES
Start Version M_0-0-15
```
#### Description

```
MOTOR.POLES sets the number of motor poles. This command is used for commutation control and rep-
resents the number of individual magnetic poles of the motor (not pole pairs). The division value of motor poles
(MOTOR.POLES) and feedback poles (FB1.POLES) must be an integer when setting drive to enable, other-
wise a fault is issued.
```

### MOTOR.R

```
General Information
Type NV Parameter
Description Sets the stator winding resistance phase-phase in ohms.
Units Ω
Range 0.001 to 650 Ω
Default Value 10 Ω
Data Type Float
See Also N/A
Start Version M_0-0-15; Units changed in M_00-00-66-000
```
#### Description

MOTOR.R sets the stator winding resistance phase-to-phase in ohms.

```
AKD Parameter and Command Reference Guide | MOTOR Parameters
```

AKD Parameter and Command Reference Guide | MOTOR Parameters

### MOTOR.RTYPE

```
General Information
Type NV Parameter
Description Defines the type of thermal resistor inside the motor.
Units N/A
Range 0 to 1
Default Value 0
Data Type Boolean
See Also N/A
Start Version M_0-0-63
```
#### Description

```
This parameter defines the type of thermal resistor used inside of the motor to measures motor temperature.
0 = PTC
1 = NTC
```

### MOTOR.TBRAKEAPP

```
General Information
Type NV Parameter
Description The delay time used for applying the motor brake.
Units 16 ms cycles
Range 0 to 1,000 16 ms cycles
Default Value 5 16 ms cycles
Data Type Integer
See Also N/A
Start Version M_0-0-15
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 366Fh/0
Data Type Integer 32
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

This parameter is used to configure the mechanical delay when applying the motor brake. Because this action
occurs once every 16 ms, the unit is a multiple of 16 ms cycles.

```
AKD Parameter and Command Reference Guide | MOTOR Parameters
```

AKD Parameter and Command Reference Guide | MOTOR Parameters

### MOTOR.TBRAKERLS

```
General Information
Type NV Parameter
Description The delay time used for releasing the motor brake.
Units 16 ms cycles
Range 0 to 1,000 16 ms cycles
Default Value 5 16 ms cycles
Data Type Integer
See Also N/A
Start Version M_0-0-15
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 366Eh/0
Data Type Integer 32
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

```
This parameter is used to configure the mechanical delay when releasing the motor brake. Because this
action occurs once every 16 ms, the unit is a multiple of 16 ms cycles.
```

### MOTOR.TEMP

```
General Information
Type R/O Parameter
Description
Reads the motor temperature represented as the resistance of the motor
PTC.
Units Ω
Range 0 to 2^32 Ω
Default Value N/A
Data Type Integer
See Also N/A
Start Version M_0-0-15
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 3612h/0
Data Type Integer 32
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

This parameter is used to get the motor temperature which is represented as the resistance of the motor PTC.

```
AKD Parameter and Command Reference Guide | MOTOR Parameters
```

AKD Parameter and Command Reference Guide | MOTOR Parameters

### MOTOR.TEMPFAULT

```
General Information
Type NV Parameter
Description Sets the motor temperature fault level.
Units Ω
Range 0 to 2,000,000,000 Ω
Default Value 0 Ω = switched off
Data Type Integer
See Also MOTOR.TEMP
Start Version M_0-0-15
```
#### Description

```
ThisparameterisusedtoconfigurethemotortemperaturefaultlevelasaresistancethresholdofthemotorPTC.
A zero value prevents any warning from being created.
```

### MOTOR.TEMPWARN

```
General Information
Type NV Parameter
Description Sets the motor temperature warning level.
Units Ω
Range 0 to 2,000,000,000 Ω
Default Value 0 Ω = switched off
Data Type Integer
See Also MOTOR.TEMP
Start Version M_0-0-15
```
#### Description

This parameter is used to configure the motor temperature warning level as a resistance threshold of the motor
PTC.

A zero value prevents any warning from being created.

```
AKD Parameter and Command Reference Guide | MOTOR Parameters
```

AKD Parameter and Command Reference Guide | MOTOR Parameters

### MOTOR.TYPE

```
General Information
Type NV Parameter
Description Sets the motor type.
Units N/A
Range 0 to 1
Default Value 0
Data Type Integer
See Also N/A
Start Version M_0-0-15
```
#### Description

```
MOTOR.TYPE sets the drive control algorithms to different motor types as follows:
0: Rotary motor
1: Linear motor
```

### MOTOR.VMAX

```
General Information
Type NV Parameter
Description Sets the maximum motor speed.
Units rpm
Range 100 to 40,000 rpm
Default Value 3,000 rpm
Data Type Integer
See Also N/A
Start Version M_0-0-15
```
#### Description

This parameter is used to configure the maximum speed of the motor.

```
AKD Parameter and Command Reference Guide | MOTOR Parameters
```

AKD Parameter and Command Reference Guide | MOTOR Parameters

### MOTOR.VOLTMAX

```
General Information
Type NV Parameter
Description Sets the motor maximum voltage.
Units Vrms
Range 110 to 900 Vrms
Default Value 230 Vrms
Data Type Integer
See Also N/A
Start Version M_0-0-15
```
#### Description

```
This parameter sets the maximum permissible motor voltage. For instance, if a motor that is rated for a 400 V
supply is connected to the drive, then the MOTOR.VOLTMAX setting is 400. This value also sets regen and
over voltage thresholds in the drive to acceptable values for the motor so that the motor windings are not dam-
aged.
```

## MT Parameters and Commands

### MT.ACC

```
General Information
Type R/W Parameter
Description Specifies motion task acceleration.
```
```
Units
```
```
Depends on UNIT.ACCROTARY or UNIT.ACCLINEAR
Rotary: rps/s, rpm/s, deg/s², (PIN/POUT)/s², rad/s²
Linear: counts/s², mm/s², μm/s², (PIN/POUT)/s²
```
```
Range
```
```
Rotary:
0.031 to 833,333.333 rps/s
1.860 to 50,000,000.000 rpm/s
11.158 to 300,000,000.000 deg/s²
0.155 to 4,166,666.752 (PIN/POUT)/s²
0.195 to 5,235,987.968 rad/s²
Linear:
0.000 to 833.333 counts/s²
0.031*MOTOR.PITCH to 833,333.333*MOTOR.PITCH mm/s²
30.994*MOTOR.PITCH to 833,333,333.333*MOTOR.PITCHμm/s²
0.155 to 4,166,666.667 (PIN/POUT)/s²
```
```
Default Value
```
```
Rotary:
50.000 rps/s
3,000.000 rpm/s
18,000.000 deg/s²
250.000 (PIN/POUT)/s²
314.159 rad/s²
Linear:
0.050 counts/s²
1.000*MOTOR.PITCH mm/s²
1000.000*MOTOR.PITCH μm/s²
250.000 (PIN/POUT)/s²
Data Type Float
See Also
```
##### MT.NUM , MT.P, MT.V, MT.CNTL, MT.DEC, MT.TNUM, MT.MTNEXT ,

##### MT.TNEXT, MT.SET , MT.LOAD

```
Start Version M_0-0-17
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number
6083h/0
```
```
AKD Parameter and Command Reference Guide | MT Parameters and Commands
```

AKD Parameter and Command Reference Guide | MT Parameters and Commands

```
Fieldbus Information
Data Type Unsigned 32
PDO Mappable Yes
Start Version M_00-00-62-000
```
#### Description

```
MT.ACC specifies the motion task acceleration and is used by the MT.SET and MT.LOAD command. This
parameter is a temporary value, since a motion task is only set after a MT.SET command. The motion task
acceleration is further limited by the maximum allowed acceleration DRV.ACC
A value of 0 for MT.ACC should not be used when setting a motion task via MT.SET because this value
causes a validity check of the MT.SET command to fail.
A value of 0 for MT.ACC after an MT.LOAD command displays an empty (not initialized) motion task.
```

### MT.CLEAR

```
General Information
Type Command
Description Clears motion tasks from the drive.
Units N/A
Range N/A
Default Value N/A
Data Type N/A
See Also MT.NUM , MT.P, MT.V, MT.CNTL, MT.ACC,MT.DEC, MT.TNUM,MT.MTNEXT , MT.TNEXT, MT.SET , MT.LOAD
Start Version M_0-0-17
```
#### Description

MT.CLEAR clears a motion task from the drive. This command needs one argument in order to clear a motion
task. A motion task consists of the following parameters: MT.NUM , MT.P, MT.V, MT.CNTL,
MT.ACC,MT.DEC, MT.TNUM, MT.MTNEXT , MT.TNEXT

A value of –1 clears all motion tasks in the drive (MT.CLEAR –1).

#### Example

MT.CLEAR 5: Clear motion task number 5.

After performing a command such as MT.PARAMS 5, the drive displays the following:

```
5 0.000 Counts 0.000 rpm 0 0.000 rpm/s 0.000 rpm/s 0 0
0 ms
```
A value of 0 for velocity, acceleration, or deceleration displays motion task as uninitialized.

```
AKD Parameter and Command Reference Guide | MT Parameters and Commands
```

AKD Parameter and Command Reference Guide | MT Parameters and Commands

### MT.CNTL

```
General Information
Type R/W Parameter
Description Sets motion task control word.
Units N/A
Range 0 to 4,294,967,295
Default Value 0
Data Type Integer
See Also MT.NUM , MT.P, MT.V, MT.ACCMT.V, MT.DEC, MT.TNUM,MT.MTNEXT MT.MTNEXT , MT.SET , MT.LOAD
Start Version M_0-0-17
```
```
Fieldbus Information
EtherCAT COE & CANOpen
Index/Subindex or
Parameter Number 35B9h/0
Data Type Integer 32
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

```
MT.CNTL specifies the motion task control word, which is used by the MT.SET and MT.LOAD commands.
The control word describes the behavior of the motion task. This parameter is a temporary value, since a
motion task is only set after an MT.SET command is issued.
Since this parameter is read bitwise, it can combine multiple functions into a single word. The meaning of
each bit is described in the tables below.
Table 1: Motion Task (MT) Bit Descriptions
```
```
Bit Meaning Description
0 0x00001
See Table 2: MT Type.
1 0x00002
2 0x00004
3 0x00008
```
```
4 0x00010
```
```
If this bit is 0, then the next MT is not executed.
If this bit is 1, then the next MT is executed.
```
```
5 0x00020
```
```
See Table 3: Next MT Start Type.
```
```
6 0x00040
7 0x00080
8 0x00100
9 0x00200
10 0x00400
See Table 4: MT Acceleration Type.
11 0x00800
```
```
12 0x01000
```
```
Activates the override functionality for a trapezoidal MT.
If this bit is 1, a motion task with override functionality must be activated
(see bit 5).
```

**Table 2: MT Type**

```
Bits 3, 2, 1, 0 Description
0000 Absolute MT. The target position is defined by the MT.P value.
1000 Absolute MT. The target position is defined by an external source, such as an
analog input.
0001 Relative MT. The target position is defined as:
Target position = PL.CMD + MT.P
0011 Relative MT. The target position is defined as:
Target position = Target position of the last motion task + MT.P
```
##### 0101

```
Relative MT. The target position is defined as:
Target position = External start position + MT.P
The ‘external start position’ can be generated by a latched position,
analog input, and other sources.
0111 Relative MT. The target position is defined as:Target position = PL.FB + MT.P
```
**Table 3: Next MT Start Type**

```
Bits 9, 8, 7, 6, 5 Description
00000
Switches over to next MT after stopping. After an MT ends, the next MT starts
immediately.
00001
Switches over to next MT after stopping and delay. After an MT ends, the MT
following time (MT.TNEXTelapse in order to start the next MT.
```
```
00010
```
```
Switches over to next MT after stopping and external event. After an MT ends,
an external event (such as a high digital input) must occur in order to start the
next MT.
```
```
00011
```
```
Switches over to next MT after stopping, delay, and external event. After an
MT ends, the MT.TNEXTmust elapse and an external event (such as a high
digital input) must occur in order to start the next MT.
```
```
00111
```
```
Switches over to next MT after stopping, then delay or external event. After an
MT ends, the MT.TNEXT must elapse or an external event (such as a high dig-
ital input) must occur in order to start the next MT.
```
##### 10000

```
Switches over to the next MT at present MT speed (change on the fly). After
reaching the target position of an MT, the next MT starts. The drive then accel-
erates with the adjusted acceleration ramp of this next MT to the target veloc-
ity of this next MT. The MT.TNEXT setting is ignored.
```
##### 11000

```
Switches over to the next MT at next MT speed (change on the fly).When the
target position of an MT is reached, the drive has already accelerated with the
acceleration ramp of the next MT to the target velocity of the next MT. Thus,
the drive begins the next MT at the next MT target velocity. The MT.TNEXT
setting is ignored if adjusted.
```
**Table 4: MT Acceleration Type**

```
AKD Parameter and Command Reference Guide | MT Parameters and Commands
```

AKD Parameter and Command Reference Guide | MT Parameters and Commands

```
Bits 11, 10 Description
00 Trapezoidal acceleration and deceleration.
```

### MT.CONTINUE

```
General Information
Type Command
Description Continues a stopped motion task.
Units N/A
Range N/A
Default Value 0
Data Type N/A
See Also MT.NUM , MT.P, MT.V, MT.CNTL, MT.ACCMT.V, MT.DEC,MT.TNUM, MT.MTNEXT MT.MTNEXT , MT.SET , MT.LOAD
Start Version M_0-0-17
```
#### Description

MT.CONTINUE continues a motion task that has been stopped by the DRV.STOP command.

```
AKD Parameter and Command Reference Guide | MT Parameters and Commands
```

AKD Parameter and Command Reference Guide | MT Parameters and Commands

### MT.DEC

```
General Information
Type R/W Parameter
Description Motion task deceleration.
```
```
Units
```
```
Depends on UNIT.ACCROTARY or UNIT.ACCLINEAR
Rotary: rps/s, rpm/s, deg/s², (PIN/POUT)/s², rad/s²
Linear: counts/s², mm/s², μm/s², (PIN/POUT)/s²
```
```
Range
```
```
Rotary:
0.031 to 833333.333 rps/s
1.860 to 50000000.000 rpm/s
11.158 to 300000000.000 deg/s²
0.155 to 4166666.752 (PIN/POUT)/s²
0.195 to 5235987.968 rad/s²
Linear:
0.000 to 833.333 counts/s²
0.031*MOTOR.PITCH to 833333.333*MOTOR.PITCH mm/s²
30.994*MOTOR.PITCH to 833333333.333*MOTOR.PITCH μm/s²
0.155 to 4166666.667 (PIN/POUT)/s²
```
```
Default Value
```
```
Rotary:
50.000 rps/s
3000.000 rpm/s
18,000.000 deg/s²
250.000 (PIN/POUT)/s²
314.159 rad/s²
Linear:
0.050 counts/s²
1.000*MOTOR.PITCH mm/s²
1000.000*MOTOR.PITCH μm/s²
250.000 (PIN/POUT)/s²
Data Type Float
See Also MT.ACC, MT.NUM , MT.P, MT.V, MT.CNTL, MT.TNUM, MT.MTNEXT, MT.TNEXT, MT.SET , MT.LOAD
Start Version M_0-0-17
```
```
Fieldbus Information
EtherCAT COE & CANOpen
Index/Subindex or
Parameter Number 6084h/0
Data Type Unsigned 32
PDO Mappable Yes
Start Version M_00-00-62-000
```
#### Description


MT.DEC specifies the motion task deceleration and is used by the MT.SET and MT.LOAD commands. This
parameter is a temporary value, since a motion task is only set after an MT.SET command is issued. The
motion task deceleration is further limited by the maximum allowed acceleration, DRV.DEC.
A value of 0 for MT.DEC should not be used when setting a motion task via MT.SET because this value
causes a validity check of the MT.SET command to fail.

A value of 0 for MT.DEC after an MT.LOAD command displays an empty (not initialized) motion task.

```
AKD Parameter and Command Reference Guide | MT Parameters and Commands
```

AKD Parameter and Command Reference Guide | MT Parameters and Commands

### MT.EMERGMT

```
General Information
Type R/W Parameter
Description Selects a motion task to be triggered after an emergency stop procedure.
Units N/A
Range 1 to 128
Default Value 0
Data Type N/A
See Also MT.NUM , MT.P, MT.V, MT.CNTL, MT.ACC, MT.DEC, MT.TNUM,MT.MTNEXT , MT.TNEXT, MT.SET , MT.LOAD
Start Version M_0-0-17
```
#### Description

```
MT.EMERGMT selects the motion task to be triggered after an emergency stop procedure.
A value of –1 shows that no motion task must be started after a ramp-down procedure in a closed position loop
mode of operation.
```

### MT.LIST

```
General Information
Type Command
Description Lists all initialized motion tasks in the drive.
Units N/A
Range 0
Default Value N/A
Data Type
```
##### MT.NUM , MT.P, MT.V, MT.CNTL, MT.ACC, MT.DEC, MT.TNUM,

##### MT.MTNEXT , MT.TNEXT, MT.SET , MT.LOAD

```
See Also M_0-0-17
Start Version N/A
```
#### Description

MT.LIST reads every initialized motion task from the drive. A motion task consists of the following param-
eters: MT.NUM , MT.P, MT.V, MT.CNTL, MT.ACC, MT.DEC, MT.TNUM, MT.MTNEXT , and MT.TNEXT.

A motion task is considered as initialized as soon as MT.V, MT.ACC, and MT.DEC of that specific motion
task have values not equal to 0.

```
AKD Parameter and Command Reference Guide | MT Parameters and Commands
```

AKD Parameter and Command Reference Guide | MT Parameters and Commands

### MT.LOAD

```
General Information
Type Command
Description Reads/loads a motion task number from the drive.
Units N/A
Range N/A
Default Value 0
Data Type N/A
See Also MT.NUM , MT.P, MT.V, MT.CNTL, MT.ACC, MT.DEC, MT.TNUM,MT.MTNEXT , MT.TNEXT, MT.SET
Start Version M_0-0-17
```
#### Description

```
MT.LOAD reads out a motion task number MT.NUM from the drive. A motion task consists of the following
parameters: MT.NUM, MT.P, MT.V, MT.CNTL, MT.ACC, MT.DEC, MT.TNUM, MT.MTNEXT , MT.TNEXT.
These parameters belong to the motion task number MT.NUM and are refreshed by MT.LOAD.
```

### MT.MOVE

```
General Information
Type Command
Description Starts a motion task.
Units N/A
Range N/A
Default Value 0
Data Type N/A
See Also MT.NUM , MT.P, MT.V, MT.CNTL, MT.ACC, MT.DEC, MT.TNUM,MT.MTNEXT , MT.TNEXT, MT.SET , MT.LOAD
Start Version M_0-0-17
```
#### Description

MT.MOVE starts a motion task. This command needs one argument in order to start a motion task. The drive
must be homed, otherwise the motion task will not start (see also HOME commands).

#### Example

MT.MOVE 3 -> Start motion task number 3.

```
AKD Parameter and Command Reference Guide | MT Parameters and Commands
```

AKD Parameter and Command Reference Guide | MT Parameters and Commands

### MT.MTNEXT

```
General Information
Type R/W Parameter
Description Specifies following motion task number.
Units N/A
Range 0 to 128
Default Value 0
Data Type Integer
See Also MT.NUM , MT.P, MT.V, MT.CNTL, MT.ACC, MT.DEC, MT.TNUM,MT.TNEXT, MT.SET , MT.LOAD
Start Version M_0-0-17
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 35BCh/0
Data Type Integer 32
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

```
MT.MTNEXT specifies the number of the following motion task and is used by the MT.SET and MT.LOAD
command. This parameter is a temporary value. A motion task is only set after an MT.SET command.
The motion task control word can be selected so that a following motion task is executed after a first motion
task. This parameter displays which motion task should be started after the first motion task.
```

### MT.NUM

```
General Information
Type R/W Parameter
Description Motion task number.
Units N/A
Range 0 to 128
Default Value 0
Data Type Integer
See Also MT.P, MT.V, MT.CNTL, MT.ACC, MT.DEC, MT.TNUM, MT.MTNEXT ,MT.TNEXT, MT.SET , MT.LOAD
Start Version M_0-0-17
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 365Bh/0
Data Type Integer 32
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

MT.NUM specifies the motion task number, which is used by the MT.SET and MT.LOAD commands. This
parameter is a temporary value. A motion task is only set after an MT.SET command is issued.

```
AKD Parameter and Command Reference Guide | MT Parameters and Commands
```

AKD Parameter and Command Reference Guide | MT Parameters and Commands

### MT.P

```
General Information
Type R/W Parameter
Description Motion task position.
Units Depends on UNIT.PROTARY or UNIT.PLINEAR
Range N/A
Default Value 0
Data Type Float
See Also MT.NUM , MT.V, MT.CNTL, MT.ACC, MT.DEC, MT.TNUM,MT.MTNEXT , MT.TNEXT, MT.SET , MT.LOAD
Start Version M_0-0-17
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number
607Ah/0
Data Type Integer 32
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

```
MT.P specifies the motion task position, which is used by the MT.SET and MT.LOAD command. Depending
on the motion task control word (MT.CNTL), the MT.P command can either be the target position of the
motion task or a relative distance. This parameter is a temporary value. A motion task is only set after an
MT.SET command.
```

### MT.PARAMS

```
General Information
Type Command
Description Shows a motion task.
Units N/A
Range N/A
Default Value 0
Data Type N/A
See Also MT.NUM , MT.P, MT.V, MT.CNTL, MT.ACC, MT.DEC, MT.TNUM,MT.MTNEXT , MT.TNEXT, MT.SET , MT.LOAD
Start Version M_0-0-17
```
#### Description

MT.PARAMS displays a motion task. This command needs one argument in order to show a motion task. If
you enter MT.PARAMS without an argument, the drive returns the current or last active motion task.

#### Example

##### MT.PARAMS 5

The drive responds as follows:

```
7 5222.000 Counts 135.000 rpm 1 550.746 rpm/s 654.458 rpm/s
0 0 0 ms
```
```
AKD Parameter and Command Reference Guide | MT Parameters and Commands
```

AKD Parameter and Command Reference Guide | MT Parameters and Commands

### MT.SET

```
General Information
Type Command
Description Sets the motion task in the drive.
Units N/A
Range N/A
Default Value 0
Data Type N/A
See Also MT.NUM , MT.P, MT.V, MT.CNTL, MT.ACC, MT.DEC, MT.TNUM,MT.MTNEXT , MT.TNEXT, MT.LOAD
Start Version M_0-0-17
```
#### Description

```
MT.SET sends a motion task to the drive. A motion task consists of the following parameters: MT.NUM ,
MT.P, MT.V, MT.CNTL, MT.ACC, MT.DEC, MT.TNUM, MT.MTNEXT , and MT.TNEXT.
Themotiontasknumber(MT.NUM)withtheparametersaboveissenttothedriveonlyaftertheMT.SETcommand.
```

#### MT.TNEXT

```
General Information
Type R/W Parameter
Description Specifies following motion task time.
Units ms
Range 0 to 65,535 ms
Default Value 0 ms
Data Type Integer
See Also MT.NUM , MT.P, MT.V, MT.CNTL, MT.ACC, MT.DEC, MT.TNUM,MT.MTNEXT , MT.SET , MT.LOAD
Start Version M_0-0-17
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number
35BDh/0
Data Type Integer 32
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

MT.TNEXTspecifies the time that must elapse before starting a following motion task. This value is used by
the MT.SET and MT.LOAD command. This parameter is a temporary value. A motion task is only set after
an MT.SET command.

The motion task control word can be selected so that a following motion task is executed after a first motion
task and this additional delay time.

```
AKD Parameter and Command Reference Guide | MT Parameters and Commands
```

AKD Parameter and Command Reference Guide | MT Parameters and Commands

#### MT.TNUM

```
General Information
Type R/W Parameter
Description Motion task customer table number.
Units N/A
Range 0 to 7
Default Value 0
Data Type Integer
See Also MT.NUM , MT.P, MT.V, MT.CNTL, MT.ACC, MT.DEC, MT.MTNEXT ,MT.TNEXT, MT.SET , MT.LOAD
Start Version M_0-0-17
```
#### Description

```
MT.TNUM specifies the customer profile table and is used by the MT.SET and MT.LOAD command. This
parameter is a temporary value. A motion task is only set after an MT.SET command.
The drive can have up to eight customer specific profile tables. The drive performs an S-curve acceleration
with these profile tables. The shapes of these tables have an impact on the shape of the motion task accel-
eration and deceleration. The motion task control word specifies if a customer profile table is used or not.
```

#### MT.TPOSWND

```
General Information
Type R/W Parameter
Description Motion task target position window.
```
```
Units
```
```
Depends on UNIT.PROTARY or UNIT.PLINEAR
Rotary: counts, rad, deg, PIN/POUT, counts 16 bit
Linear: counts, mm, μm, PIN/POUT, counts 16 bit
Range N/A
Default Value 0.5 rev
Data Type Float
See Also DRV.MOTIONSTAT
Start Version M_0-0-32
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 35C6h/0
Data Type Integer 32
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

Within DRV.MOTIONSTAT, MT.TPOSWND is used to indicate that the target position of a motion task has
been reached. DRV.MOTIONSTAT displays a "Target Position Reached" bit as soon as the following state-
ment becomes true:

abs(actual_position – target_position) < MT.TPOSWND

```
AKD Parameter and Command Reference Guide | MT Parameters and Commands
```

AKD Parameter and Command Reference Guide | MT Parameters and Commands

#### MT.TVELWND

```
General Information
Type R/W Parameter
Description Motion task target velocity window
```
```
Units
```
```
Depends on UNIT.VROTARY or UNIT.VLINEAR
Rotary: rpm, rps, deg/s, (PIN/POUT)/s, rad/s
Linear: Counts/s, mm/s, μm/s, (PIN/POUT)/s
```
```
Range
```
```
Rotary:
0.000 to 12000.000 rpm
0.000 to 200.000 rps
0.000 to 72000.000 deg/s
0.000 to 1000.000 (PIN/POUT)/s
0.000 to 1256.637 rad/s
Linear:
0.000 to 0.200 counts/s
0.000 to 200.000*MOTOR.PITCH mm/s
0.000 to 200,000.000*MOTOR.PITCH μm/sec
0.000 to 1000.000 (PIN/POUT)/s
```
```
Default Value
```
```
Rotary:
60.000 rpm
1.000 rps
359.999 deg/s
5.000 (PIN/POUT)/s
6.283 rad/s
Linear:
0.001 Counts/s
1.000*MOTOR.PITCH mm/s
999.998*MOTOR.PITCH μm/sec
5.000 (PIN/POUT)/s
Data Type Float
See Also DRV.MOTIONSTAT
Start Version M_0-0-32
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 3856h/0
Data Type Integer 32
PDO Mappable No
Start Version M_00-00-62-000
```

#### Description

Within DRV.MOTIONSTAT, MT.TVELWND is used to indicate that the target velocity of a motion task has
been reached. DRV.MOTIONSTAT displays a "Target Velocity Reached" bit as soon as the following state-
ment becomes true:

(target velocity – MT.TVELWND) < actual velocity < (target velocity + MT)

#### MT.V

```
General Information
Type R/W Parameter
Description Motion task velocity.
```
```
Units
```
```
Depends on UNIT.VROTARY or UNIT.VLINEAR
Rotary: rpm, rps, deg/s, (PIN/POUT)/s, rad/s
Linear: counts/s, mm/s, μm/s, (PIN/POUT)/s
```
```
Range
```
```
Rotary:
0.000 to 12,000.000 rpm
0.000 to 200.000 rps
0.000 to 72,000.000 deg/s
0.000 to 1,000.000 (PIN/POUT)/s
0.000 to 1,256.637 rad/s
Linear:
0.000 to 0.200 Counts/s
0.000 to 200.000*MOTOR.PITCH mm/s
0.000 to 200,000.000*MOTOR.PITCH μm/sec
0.000 to 1000.000 (PIN/POUT)/s
Default Value 0
Data Type Float
See Also
```
##### MT.NUM , MT.P, MT.CNTL, MT.ACC, MT.DEC, MT.TNUM,

##### MT.MTNEXT , MT.TNEXT, MT.SET , MT.LOAD

```
Start Version M_0-0-17
```
```
Fieldbus Information
EtherCAT COE & CANOpen
Index/Subindex or
Parameter Number
6081h/0
Data Type Unsigned 32
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

MT.V specifies the motion task velocity, which is used by the MT.SET and MT.LOAD command. This param-
eter is a temporary value. A motion task is only set after an MT.SET command. The motion task velocity is
furthermore limited by VL.LIMITP or VL.LIMITN depending on the direction of the motion task.

```
AKD Parameter and Command Reference Guide | MT Parameters and Commands
```

AKD Parameter and Command Reference Guide | MT Parameters and Commands

```
A value of 0 should not be used when setting a motion task via MT.SET because this value causes a validity
check of the MT.SET command to fail.
A value of 0 after an MT.LOAD command displays an empty (not initialized) motion task.
```

#### MT.VCMD

```
General Information
Type R/O Parameter
Description Derivative of PL.CMD.
Units Depends on UNIT.VROTARY or UNIT.VLINEAR
Range N/A
Default Value N/A
Data Type Float
See Also N/A
Start Version M_00-00-63-000
```
#### Description

MT.VCMD returns the derivative of the position loop trajectory (PL.CMD), which is therefore a velocity.
MT.VCMD is updated while the drive is in DRV.OPMODE 2 and is processing the following motion types:

```
 Motion tasking
 Homing
 Electronic gearing
 Service motion
 External trajectory coming from a fieldbus
 External trajectory calculated from an analog input signal
```
```
AKD Parameter and Command Reference Guide | MT Parameters and Commands
```

This page intentionally left blank.


### PL Parameters

#### PL.CMD

```
General Information
Type NV Parameter
Description Reads the position command directly from the entry to the position loop.
```
```
Units
```
```
Depends on UNIT.PROTARY or UNIT.PLINEARUNIT.ACCLINEAR
Rotary: counts, rad, deg, (PIN/POUT), counts 16 Bit
Linear: counts, mm, μm, (PIN/POUT), counts 16 Bit
Range N/A
Default Value N/A
Data Type Float
See Also PL.FB
Start Version M_0-0-15
```
#### Description

PL.CMD returns the position command as it is received in the position loop entry.

```
AKD Parameter and Command Reference Guide | PL Parameters
```

AKD Parameter and Command Reference Guide | PL Parameters

#### PL.ERR

```
General Information
Type NV Parameter
Description Returns the position following an error.
Units counts, rad, deg, (PIN/POUT)
Range N/A
Default Value N/A
Data Type Float
See Also PL.FB
Start Version M_0-0-15
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 60F4h/0
Data Type Integer 32
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

```
PL.ERR returns the position following an error.
```

#### PL.ERRFTHRESH

```
General Information
Type NV Parameter
Description Sets the maximum position error.
```
```
Units
```
```
Depends on UNIT.ACCROTARY or UNIT.ACCLINEAR
Rotary: counts, rad, deg, (PIN/POUT), counts 16 Bit
Linear: counts, mm, μm, (PIN/POUT), counts 16 Bit
```
```
Range
```
```
Rotary:
0.000 to 5,123,372,000,000,005.000 counts
0.000 to 7,495,067.136 rad
0.000 to 429,436,076.032 deg
0.000 to 5,964,389.888 (PIN/POUT)
0.000 to 78,176,452,636.718 counts 16 Bit
Linear:
0.000 to 5,123,372,000,000,005.000 counts
0.000 to 1,192,877.952*MOTOR.PITCH mm
0.000 to 1,192,878,014.464*MOTOR.PITCH μm
0.000 to 5,964,389.888 (PIN/POUT)
0.000 to 78,176,452,636.718 counts 16 Bit
Default Value 0.000
Data Type Float
See Also PL.ERR
Start Version M_0_0_33
```
```
Fieldbus Information
EtherCAT COE & CANOpen
Index/Subindex or
Parameter Number 35C7h/0
Data Type Integer 32
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

Thisparameter setsthe maximumposition error.If theposition errorPL.ERR islarger thanPL.ERRFTHRESH
thedrive generatesa fault.If PL.ERRFTHRESH is setto 0,the maximumposition erroris ignored.

#### Example

Set position rotary units to 2 (degrees). Setting PL.ERRFTHRESH to 1000 states that is the position error is
larger than 1000 degrees, the drive will generate a fault.

UNIT.PROTARY 2

PL.ERRFTHRESH 1000

```
AKD Parameter and Command Reference Guide | PL Parameters
```

AKD Parameter and Command Reference Guide | PL Parameters

#### PL.ERRWTHRESH

```
General Information
Type NV Parameter
Description Sets the position error warning level.
```
```
Units
```
```
Depends on UNIT.PROTARY or UNIT.PLINEARUNIT.ACCLINEAR
Rotary: counts, rad, deg, (PIN/POUT), counts 16 Bit
Linear: counts, mm, μm, (PIN/POUT), counts 16 Bit
```
```
Range
```
```
Rotary:
0.000 to 5,123,372,000,000,005.000 counts
0.000 to 7,495,067.136 rad
0.000 to 429,436,076.032 deg
0.000 to 5,964,389.888 (PIN/POUT)
0.000 to 78,176,452,636.718 counts 16 Bit
Linear:
0.000 to 5,123,372,000,000,005.000 counts
0.000 to 1,192,877.952*MOTOR.PITCH mm
0.000 to 1,192,878,014.464*MOTOR.PITCH μm
0.000 to 5,964,389.888 (PIN/POUT)
0.000 to 78,176,452,636.718 counts 16 Bit
Default Value 0.000 deg
Data Type Float
See Also PL.ERR
Start Version M_0-0-51
```
#### Description

```
Ifthisvalueisnotequal0andthepositionerrorPL.ERR islargerthanthisvalue,thedrivewillgenerateawarning.
If PL.ERRWTHRESH is set to 0 the warning is not issued.
```
#### Example

```
Set position rotary units to 2 degrees. If you set PL.ERRWTHRESH to 100 and the position error is larger
than 100 degrees, then the drive will generate a warning.
UNIT.PROTARY 2
PL.ERRWTHRESH 100
```

#### PL.FB

```
General Information
Type R/O Parameter
Description Reads the position feedback value.
```
```
Units
```
```
Depends on UNIT.PROTARY or UNIT.PLINEARUNIT.ACCLINEAR
Rotary: counts, rad, deg, (PIN/POUT), counts 16 Bit
Linear: counts, mm, μm, (PIN/POUT), counts16 bit
Range N/A
Default Value N/A
Data Type Float
See Also FB1.OFFSET
Start Version M_0-0-15
```
#### Description

PL.FB returns the position feedback value.

Note that this value is not the pure feedback value read from the feedback device, but also includes the value
of the FB1.OFFSET and an internal offset set automatically by the FW when a homing switch is actuated.

```
AKD Parameter and Command Reference Guide | PL Parameters
```

AKD Parameter and Command Reference Guide | PL Parameters

#### PL.FBSOURCE

```
General Information
Type NV Parameter
Description Sets the feedback source for the position loop.
Units N/A
Range 0 to 1
Default Value 0
Data Type Boolean
See Also VL.FBSOURCE
Start Version M_00-00-51-000
```
#### Description

```
This parameter determines the feedback source to be used by the position loop. A value of 0 selects the pri-
mary feedback, 1 selects the secondary feedback.
```

#### PL.INTINMAX

```
General Information
Type NV Parameter
Description
Limits the input of the position loop integrator by setting the input sat-
uration.
```
```
Units
```
```
Depends on UNIT.PROTARY or UNIT.PLINEAR
Rotary: counts, rad, deg, (PIN/POUT), counts 16 Bit
Linear: counts, mm, μm, (PIN/POUT), counts16 Bit
```
```
Range
```
```
Rotary:
0.000 to 18,446,744,073,709.000 counts
0.000 to 26,986.052 rad
0.000 to 1,546,188.288 deg
0.000 to 21,474.836 (PIN/POUT)
0.000 to 281,474,976.710 counts 16 Bit
Linear:
0.000 to 18,446,744,073,709.000 counts
0.000 to 4,294.968*MOTOR.PITCH mm
0.000 to 4,294,967.296*MOTOR.PITCH μm
0.000 to 21,474.836 (PIN/POUT)
0.000 to 281,474,976.710 counts 16 Bit
```
```
Default Value
```
```
Rotary:
5,000,000.000 counts
0.007 rad
0.419 deg
0.006 (PIN/POUT)
76.293 counts 16 Bit
Linear:
5,000,000.000 counts
4,294.968*MOTOR.PITCH mm
4,294,967.296*MOTOR.PITCH μm
0.006 (PIN/POUT)
76.293 counts 16 Bit
Data Type Float
See Also PL.FB
Start Version M_0-0-15
```
#### Description

```
AKD Parameter and Command Reference Guide | PL Parameters
```

AKD Parameter and Command Reference Guide | PL Parameters

```
PL.INTINMAX limits the input of the position loop integrator by setting the input saturation. When used in con-
cert with PL.INSATOUT, this variable allows you to make the position loop integrator effective near the target
position. Far from the target position, however,the integrator is not dominant in the loop dynamics.
```

#### PL.INTOUTMAX

```
General Information
Type NV Parameter
Description
Limits the output of the position loop integrator by setting the output sat-
uration.
```
```
Units
```
```
Depends on UNIT.PROTARY or UNIT.PLINEAR
Rotary: counts, rad, deg, (PIN/POUT), counts 16 Bit
Linear: counts, mm, μm, (PIN/POUT), counts 16 Bit
```
```
Range
```
```
Rotary:
0.000 to 18,446,744,073,709.000 counts
0.000 to 26,986.052 rad
0.000 to 1,546,188.288 deg
0.000 to 21,474.836 (PIN/POUT)
0.000 to 281,474,976.710 counts16 bit
Linear:
0.000 to 18,446,744,073,709.000 counts
0.000 to 4,294.968*MOTOR.PITCH mm
0.000 to 4,294,967.296*MOTOR.PITCH μm
0.000 to 21,474.836 (PIN/POUT)
0.000 to 281,474,976.710 counts16 bit
```
```
Default Value
```
```
Rotary:
5,000,000.000 counts
0.007 rad
0.419 deg
0.006 (PIN/POUT)
76.293 counts 16 Bit
Linear:
5,000,000.000 counts
4,294.968*MOTOR.PITCH mm
4,294,967.296*MOTOR.PITCH μm
0.006 (PIN/POUT)
76.293 counts16 bit
Data Type Float
See Also PL.INTINMAX
Start Version M_0-0-14
```
#### Description

```
AKD Parameter and Command Reference Guide | PL Parameters
```

AKD Parameter and Command Reference Guide | PL Parameters

```
PL.INTOUTMAX limits the output of the position loop integrator by setting the output saturation.
WhenusedinconcertwithPL.INTINMAX,thisvariableallowsyoutomakethepositionloopintegratoreffective
nearthetargetposition.Farfromthetargetposition,however,theintegratorisnotdominantintheloopdynamics.
```

#### PL.KI

```
General Information
Type NV Parameter
Description Sets the integral gain of the position loop.
Units kHz
Range 0 to 2,147,483.008 kHz
Default Value 0 kHz
Data Type Float
See Also PL.KP, PL.KD
Start Version M_0-0-15
```
#### Description

PL.KI sets the integral gain of the position regulator PID loop.

```
AKD Parameter and Command Reference Guide | PL Parameters
```

AKD Parameter and Command Reference Guide | PL Parameters

#### PL.KP

```
General Information
Type NV Parameter
Description Sets the proportional gain of the position regulator PID loop.
Units (rev/s)/rev
Range 0 to 2,147,483.008 (rev/s)/rev
Default Value 100 rps/rev
Data Type Float
See Also PL.KI, PL.KD
Start Version M_0-0-15
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 3542h/0
Data Type Integer 32
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

```
PL.KP sets the proportional gain of the position regulator PID loop.
```

### PLS Parameters and Commands

#### PLS.CLR

```
General Information
Type W/O Parameter
Description Defines which position register to clear.
Units N/A
Range 0 to 65,535
Default Value 0
Data Type U16
See Also N/A
Start Version M_0-0-50-0
```
#### Description

This parameter clears bits inside of PLS.STATE.

#### Example

If PLS.CLR Bit 0=1, then Bit 0 in PLS.STATE is set to 0.

If PLS.CLR Bit 15=1, then Bit 15 in PLS.STATE is set to 0.

```
AKD Parameter and Command Reference Guide | PLS Parameters and Commands
```

AKD Parameter and Command Reference Guide | PLS Parameters and Commands

#### PLS.EN

```
General Information
Type R/W Parameter
Description Enables the position registers.
Units N/A
Range 0 to 65,535
Default Value 0
Data Type U16
See Also N/A
Start Version M_0-0-50-0
```
#### Description

```
This parameter enables the position register switches.
```
#### Example

```
Bit 0 = 0: Disable PLS.P01
Bit 0 = 1: Enable PLS.P01
```
```
Bit15 = 0: Disable PLS.P16
Bit15 = 1: Enable PLS.P16
```

#### PLS.MODE

```
General Information
Type NV Parameter
Description Selects position register mode.
Units N/A
Range 0 to 65,535
Default Value 0
Data Type U16
See Also N/A
Start Version M_0-0-50-0
```
#### Description

This variable is responsible for selecting the functionality of the position register switches.

#### Example

PLS.MODE 0: PLS.P01 is triggered once.

PLS.MODE 1: PLS.P01 is monitored continuously.

Bit15 = 0: PLS.P16 is triggered once.

Bit15 = 1: PLS.P16 is monitored continuously.

```
AKD Parameter and Command Reference Guide | PLS Parameters and Commands
```

AKD Parameter and Command Reference Guide | PLS Parameters and Commands

#### PLS.P01 TO PLS.P16

```
General Information
Type NV Parameter
Description Position register compare value.
Units Position units
Range -5,188,146,770,730,811 to 5,188,146,770,729,811
Default Value 0
Data Type S64
See Also UNIT.PROTARY, UNIT.PLINEAR
Start Version M_0-0-50-0
```
#### Description

```
These parameters contain the compare register value for the position register switches.
```

#### PLS.POLARITY

```
General Information
Type NV Parameter
Description Sets the polarity of the position registers.
Units N/A
Range 0 to 65,536
Default Value 0
Data Type U16
See Also N/A
Start Version M_0-0-50-0
```
#### Description

This parameter selects the polarity of the position register switches.

#### Example

Bit 0 = 0: PLS.P01 is active if PL.FB > PLS.P01.

Bit 0 = 1: PLS.P01 is active if PL.FB < PLS.P01.

Bit15 = 0: PLS.P16 is active if PL.FB > PLS.P16.

Bit15 = 1: PLS.P16 is active if PL.FB < PLS.P16.

```
AKD Parameter and Command Reference Guide | PLS Parameters and Commands
```

AKD Parameter and Command Reference Guide | PLS Parameters and Commands

#### PLS.STATE

```
General Information
Type R/O Parameter
Description Reads the status of the position registers.
Units N/A
Range N/A
Default Value N/A
Data Type U16
See Also N/A
Start Version M_0-0-50-0
```
#### Description

```
This parameter reads the status word of the position register switches. The status word indicates the result of
the compare between the position register switch compare register and the actual position of the position loop.
```
#### Example

```
Bit 0 = 0: PLS.P01 is not active.
Bit 0 = 1: PLS.P01 is active.
```
```
Bit 15 = 0: PLS.P16 is not active.
Bit 15 = 1: PLS.P16 is active.
```

### REC Parameters and Commands

#### REC.ACTIVE

```
General Information
Type R/O Parameter
Description Indicates if data recording is in progress (active).
Units N/A
Range 0 to 1
Default Value N/A
Data Type Boolean
See Also REC.DONE, REC.OFF
Start Version M_0-0-16
```
#### Description

REC.ACTIVE indicates whether or not data recording is in progress. This action means that the trigger was
met and the recorder is recording all data.

```
AKD Parameter and Command Reference Guide | REC Parameters and Commands
```

AKD Parameter and Command Reference Guide | REC Parameters and Commands

#### REC.CH1 to REC.CH6

```
General Information
Type R/W Parameter
Description Sets recording channels 1 to 6.
Units N/A
Range N/A
```
```
Default Value
```
##### CH1 = IL.FB

##### CH2 = IL.CMD

##### CH3 = VL.FB

```
CH4 = Empty
CH5 = Empty
CH6 = Empty
Data Type String
See Also REC.TRIG
Start Version M_0-0-16
```
#### Description

```
REC.CHx specifies the recording channels.
There are 3 options to set the recording channels values:
 Set 0, CLR, or CLEAR. This setting clears the recording channel.
 Set one of the recordable commands. The list of recordable commands can be obtain by executing
REC.RECPRMLIST.
 Set an internal value or variable of the drive (same as for DRV.MEMADDR input).
```

#### REC.DONE

```
General Information
Type R/O Parameter
Description Checks whether or not the recorder has finished recording.
Units N/A
Range 0 to 1
Default Value N/A
Data Type Boolean
See Also REC.ACTIVE, REC.OFF
Start Version M_0-0-14
```
#### Description

REC.DONE indicates that the recorder has finished recording.
This value is reset to 0 when the recorder trigger is set.

This value is reset by the system when the recording has finished or when REC.OFF is executed.

```
AKD Parameter and Command Reference Guide | REC Parameters and Commands
```

AKD Parameter and Command Reference Guide | REC Parameters and Commands

#### REC.GAP

```
General Information
Type R/W Parameter
Description Specifies the gap between consecutive samples.
Units N/A
Range 1 to 65,535
Default Value 1
Data Type Integer
See Also REC.TRIG
Start Version M_0-0-16
```
#### Description

```
REC.GAP specifies the gap between consecutive samples. The recording base rate is 16 kHz, thus a gap of
1 means that a sample is recorded every 62.5 us.
```

#### REC.NUMPOINTS

```
General Information
Type R/W Parameter
Description Sets the number of points to record.
Units N/A
Range 1 to 65,535
Default Value 1,000
Data Type Integer
See Also REC.TRIG
Start Version M_0-0-16
```
#### Description

REC.NUMPOINTS specifies the number of points (samples) to record.

```
AKD Parameter and Command Reference Guide | REC Parameters and Commands
```

AKD Parameter and Command Reference Guide | REC Parameters and Commands

#### REC.OFF

```
General Information
Type R/W Parameter
Description Turns the recorder OFF.
Units N/A
Range N/A
Default Value N/A
Data Type N/A
See Also REC.ACTIVE, REC.DONE, REC.READY
Start Version M_0-0-15
```
#### Description

```
REC.OFF turns the recorder off. In order to set the recorder again, the recorder must first be armed and then a
trigger set.
```

#### REC.RECPRMLIST

```
General Information
Type R/O Parameter
Description Reads the list of recordable parameters.
Units N/A
Range N/A
Default Value N/A
Data Type N/A
See Also REC.CH1 to REC.CH6
Start Version M_0-0-50-0
```
#### Description

This command returns the list of recordable parameters. You can use recordable parameter as an input to any
of the recording channels.

Note that an internal address or a registered variable can be used as input to any of the channels in addition to
the list.

```
AKD Parameter and Command Reference Guide | REC Parameters and Commands
```

AKD Parameter and Command Reference Guide | REC Parameters and Commands

#### REC.RETRIEVE

```
General Information
Type R/O Parameter
Description Transfers all the recorded data to the communication channel.
Units N/A
Range N/A
Default Value N/A
Data Type String
See Also N/A
Start Version M_0-0-14
```
#### Description

```
REC.RETRIEVE causes the drive to transfer all the recorded data to the communication channel.
```
#### Example

```
Thefollowingformatistheretrievereplyformat(forN samples,Gsamplegap,andMparameters,whereM<=6):
Recording
<N>,<G>
<parameter name 1> ... <parameter name M>
Value11 ... Value1M
Value N1 ... ValueNM
```

### REC.RETRIEVEDATA

```
General Information
Type R/W Parameter
Description Retrieves the recorded data without the header.
Units N/A
Range N/A
Default Value N/A
Data Type N/A
See Also REC.RETRIEVE, REC.RETRIEVEHDR, REC.RETRIEVESIZE
Start Version M_0-0-50-0
```
#### Description

REC.RETRIEVEDATA retrieves a section of recorded data according to REC.RETRIEVESIZE from the
received index; if no index is received, the drive retrieves the data from next section. An index is supplied to
enable multiple retrieves and to give better control on the buffer in case of overflow. If no index or a negative
value is present, then the index is ignored.

WorkBench uses this parameter to retrieve the data continuously for RT recoding.
The size of the data returned by this command depends on the number set by REC.RETRIEVESIZE.

Use REC.RETRIEVE for complete recording information view.

Notes:

```
 If REC.RETRIEVESIZE is larger than the buffer size, then it simply returns the whole buffer (no error).
 If the index is received, the data will be continuously returned starting from the given index (default
starting index is 0).
 If the index is out of the bounds of the buffer, then it will be ignored.
 If recorder is active and REC.STOPTYPE==0, then this parameter returns an error.
 If REC.STOPTYPE==1, then this parameter returns the next section of data in the buffer (even if it
reached the end of the buffer, it will return to the beginning of the buffer and add the data from index 0.)
 If REC.STOPTYPE==1 and the retrieve is too slow (gets overrun by the recorder), an overflow error
message is returned instead of the retrieved data.
 If REC.STOPTYPE==0 and no index is received, continuously send the sections of data until the end
of the buffer is reached. Then, return to the beginning of buffer and continue.
 A new REC.TRIG command automatically sets the index to 0.
```
#### Example

The following example retrieves data from index 100 in the size of 10 (hence places 100 to 109 in the buffer)

```
REC.NUMPOINTS 1000
REC.RETRIVESIZE 10
REC.TRIG
REC.RETRIEVEDATA 100
```
```
AKD Parameter and Command Reference Guide | REC Parameters and Commands
```

AKD Parameter and Command Reference Guide | REC Parameters and Commands

### REC.RETRIEVEHDR

```
General Information
Type R/O Parameter
Description Retrieves the recorded header without the data.
Units N/A
Range N/A
Default Value N/A
Data Type N/A
See Also REC.RETRIEVE, REC.RETRIEVEDATA
Start Version M_0-0-50-0
```
#### Description

```
This command retrieves the recorded header without the data of the recording.
WorkBenchusesthisparametertoretrievetheheaderoncebeforecontinuouslyreadingthedataforRTrecoding.
Use REC.RETRIEVE for complete recording information view.
```
#### Example

##### REC.RETRIEVEHDR


### REC.RETRIEVESIZE

```
General Information
Type R/W Parameter
Description Sets the number of samples that REC.RETRIEVEDATA returns.
Units recorder samples
Range 0 to 65,535 recorder samples
Default Value 1,000 recorder samples
Data Type Integer
See Also REC.RETRIEVEDATA, REC.RETRIEVEHDR
Start Version M_0-0-50-0
```
#### Description

This parameter sets the number of samples that REC.RETRIEVEDATA returns.
WorkBench also uses this parameter to set the number of samples returned when retrieving the data con-
tinuously for RT recoding.

Use REC.RETRIEVE for the complete recording information view.

#### Example

##### REC.RETRIVESIZE 2000

```
AKD Parameter and Command Reference Guide | REC Parameters and Commands
```

AKD Parameter and Command Reference Guide | REC Parameters and Commands

### REC.STOPTYPE

```
General Information
Type R/W
Description Sets the recorder stop type.
Units N/A
Range 0 or 1
Default Value 0
Data Type Integer
See Also REC.RETRIEVEDATA, REC.RETRIEVESIZE
Start Version M_0-0-50-0-0
```
#### Description

```
This parameter sets the stop type for the recording.
0 = Recorder runs, continuously filling the recording circular buffer.
1 = Recorder fills in the buffer once.
To stop RT recording, execute REC.OFF.
```
#### Example

##### REC.STOPTYPE


### REC.TRIG

```
General Information
Type Command
Description Triggers the recorder.
Units N/A
Range N/A
Default Value N/A
Data Type N/A
See Also REC.RETRIEVE, REC.OFF
Start Version M_0-0-16
```
#### Description

REC.TRIG starts the trigger and effectively starts recording values while waiting for the trigger to occur.
REC.TRIG sets the value of REC.DONE to 0.

After calling REC.TRIG, the data that was recorded by previous recording is deleted and cannot be retrieved.

No REC parameters can be set after a call to REC.TRIG until the recorder has finished or until REC.OFF is
executed.

```
AKD Parameter and Command Reference Guide | REC Parameters and Commands
```

AKD Parameter and Command Reference Guide | REC Parameters and Commands

### REC.TRIGparam

```
General Information
Type R/W Parameter
Description Sets the parameter that triggers the recorder.
Units N/A
Range N/A
Default Value IL.FB
Data Type String
See Also REC.TRIG
Start Version M_0-0-14
```
#### Description

```
REC.TRIGPARAM sets the parameter on which the recorder triggers.
This parameter is only used when REC.TRIGTYPE = 2.
Input values are:
```
1. One of the set drive parameters list that can be set as a trigger. The available parameters for trigger are:
PL.ERR, PL.CMD, PL.FB, VL.CMD, VL.FB, IL.CMD, and IL.FB.
2. Internal value or variable of the drive (same as for DRV.MEMADDR input).


### REC.TRIGPOS

```
General Information
Type R/W Parameter
Description Sets the position in the recording buffer in which to set the trigger.
Units %
Range 1 to 100%
Default Value 10%
Data Type Integer
See Also REC.TRIG, REC.NUMPOINTS
Start Version M_0-0-16
```
#### Description

REC.TRIGPOS sets the position in the recording buffer in which to set the trigger. The recording buffer size is
defined by REC.NUMPOINTS.

The input value is a percentage of the buffer (that is, a value of 10 means saving 10% of the buffer data before
the trigger occurs and 90% after it occurs).

This parameter is only used when REC.TRIGTYPE = 0.

```
AKD Parameter and Command Reference Guide | REC Parameters and Commands
```

AKD Parameter and Command Reference Guide | REC Parameters and Commands

### REC.TRIGPRMLIST

```
General Information
Type R/O Parameter
Description Reads the list of possible trigger parameters.
Units N/A
Range N/A
Default Value N/A
Data Type N/A
See Also REC.TRIGPARAM
Start Version M_0-0-50-0
```
#### Description

```
This command returns the list of trigger parameters. Each one of those parameters can serve as the trigger
parameter (input to REC.TRIGPARAM).
Note that an internal address or a registered variable can be used as input to REC.TRIGPARAM in addition to
the list that this parameter returns.
```
#### Example

##### REC.TRIGPRMLIST


### REC.TRIGSLOPE

```
General Information
Type R/W Parameter
Description Sets the trigger slope.
```
```
Units
0 = Negative
1 = Positive
Range 0 to 1
Default Value 0
Data Type Boolean
See Also REC.TRIG, REC.NUMPOINTS
Start Version M_0-0-16
```
#### Description

REC.TRIGSLOPE sets the recorder trigger slope.
This parameter is only used when REC.TRIGTYPE = 2.

```
AKD Parameter and Command Reference Guide | REC Parameters and Commands
```

AKD Parameter and Command Reference Guide | REC Parameters and Commands

### REC.TRIGTYPE

```
General Information
Type R/W Parameter
Description Sets the trigger type.
```
```
Units
```
```
0 = immediate
1 = command
2 = parameter
Range 0 to 2
Default Value 0
Data Type Integer
See Also REC.TRIG, REC.TRIGPARAM, REC.TRIGVAL, REC.TRIGSLOPEREC.TRIGPOS
Start Version M_0-0-16
```
#### Description

```
REC.TRIGTYPE sets the type of trigger.
Input values are as follows:
```
```
Value Description
0 Recording starts immediately
1
Recording starts on the next command executed through the TCP/IP. The
trigger location in the buffer is set according to REC.TRIGPOS.
2
Recording starts per the values of REC.TRIGPARAM, REC.TRIGVAL,
REC.TRIGSLOPE, and REC.TRIGPOS.
```

### REC.TRIGVAL

```
General Information
Type R/W Parameter
Description Sets the trigger value.
Units The units of the parameter are chosen according to the unit type.
Range 0 to 2
Default Value 0
Data Type Integer
See Also REC.TRIG, REC.TRIGPARAM, REC.TRIGVAL, REC.TRIGSLOPE,REC.TRIGPOS
Start Version M_0-0-16
```
#### Description

REC.TRIGVAL is the value that must be met by REC.TRIGPARAM for the trigger to occur.

Note that the units of this parameter are set according to the units of REC.TRIGPARAM.

```
AKD Parameter and Command Reference Guide | REC Parameters and Commands
```

AKD Parameter and Command Reference Guide | REGEN Parameters

## REGEN Parameters

### REGEN.POWER

```
General Information
Type R/O parameter
Description
Units Watt
Range N/A
Default Value N/A
Data Type Integer
See Also N/A
Start Version M_00-00-52-000
```
#### Description

```
Gets regen resistor's calcultaed power. ( (V^2 / R) * DutyCycle )
```

### REGEN.REXT

```
General Information
Type NV Parameter
Description Sets the external, user-defined regen resistor resistance.
Units Ω
Range 0 to 255 Ω
Default Value 0 Ω
Data Type Integer
See Also N/A
Start Version M_0-0-15
```
#### Description

REGEN.REXT sets the external user-defined regen resistor resistance. This variable is needed for the regen
resistor temperature estimation algorithm.

```
AKD Parameter and Command Reference Guide | REGEN Parameters
```

AKD Parameter and Command Reference Guide | REGEN Parameters

### REGEN.TEXT

```
General Information
Type R/W Parameter
Description External regen resistor thermal protection time constant.
Units s
Range 0.1 to 1,200 s
Default Value 100 s
Data Type Float
See Also REGEN.WATTEXT, REGEN.REXT
Start Version
```
#### Description

```
REGEN.TEXT is a thermal time constant used to protect an external regeneration (braking) resistor from over-
heating and failing. It is the time-to-fault when input power steps from 0 to 150% of REGEN.WATTEXT. The
drive's regen resistor protection algorithm continuously calculates the power dissipated in the resistor and
processes that power value through a single pole low pass filter to model the resistor's thermal inertia. When
the filtered regen power on the output of the filter exceeds REGEN.WATTEXT, a fault occurs. REGEN.TEXT
sets the time constant of this thermal inertia filter.
REGEN.TEXT can often be found directly on power resistor data sheets. Just look for the peak overload
curve and find the safe allowed time to be at 150% of the resistor's continuous power rating. Another way
power resistors peak overload capability is often specified is by giving the energy rating in joules of the
resistor. If you have the energy rating E then:
```
```
REGEN.TEXT = (1.1)*((joule limit)/REGEN.WATTEXT)
```
#### Example:

```
The external regen resistor is rated for 250 W continuous, is 33 ohm, and has a joule rating of 500 joules. To
use this resistor, the drive settings become:
REGEN.TYPE = -1 (External Regen)
REGEN.REXT = 33
REGEN.WATTEXT = 250
```
```
REGEN.TEXT = (1.1)*(500 j)/(250 W) = 2.2 sec
```
### 1.3 Regen Resistor Type


### Parameter: REGEN.TYPE

```
General Information
Type NV Parameter
Function Sets the regen resistor type.
WorkBench Location
(Screen/Dialog Box) Power/Regen Resistor Type
Units N/A
Range –1 to 0
Default Value 0
Data Type Integer
See Also N/A
Start Version M_0-0-15
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 3412h/0
Data Type Integer 8
PDO Mappable N/A
Start Version
```
#### Description

You can specify a user-defined external regen resistor, select an internal regen resistor, or choose from a list
of predefined regen resistors. The values for REGEN.TYPE are shown below:

```
Type Description
–1 External user-defined regen resistor
0 Internal regen resistor
```
If you specify a user-defined regen resistor, then you must also define this resistor's resistance
(REGEN.REXT), heatup time (REGEN.REXT), and power (REGEN.WATTEXT).

For more information on regen resistors, see Regeneration and Sizing a Regen Resistor.

```
AKD Parameter and Command Reference Guide | REGEN Parameters
```

AKD Parameter and Command Reference Guide | REGEN Parameters

### REGEN.WATTEXT

```
General Information
Type R/W parameter
Description
Units W
Range 0 to 62,000 W
Default Value 1000 W
Data Type Integer
See Also N/A
Start Version M_00-00-53-000
```
#### Description

```
Gets/Sets the regen resistor's power fault level for an external regen resistor (when REGEN.TYPE = -1)
Above this fault level regen resistor's PWM wil be 0 and a fault will be issued.
```

## SM Parameters

### SM.ACCTYPE

```
General Information
Type R/W Parameter
Description Sets the service motion acceleration and deceleration type.
Units N/A
Range 0 to 8
Default Value 0
Data Type Float
See Also
```
##### SM.I1, SM.I2, SM.MODE, SM.MOVE, SM.T1, SM.T2, SM.V1, SM.V2,

##### SM.VPM1, SM.VPM2

```
Start Version M_0-0-16
```
#### Description

The SM.ACCTYPE parameter describes the behavior of the acceleration ramp for the service motion modes 4
and 5 (see SM.MODE for details regarding these modes).

Values:

0 = Trapezoidal acceleration/deceleration

1 through 8 = Acceleration according to customer profile tables 1 through 8 (as available)

```
AKD Parameter and Command Reference Guide | SM Parameters
```

AKD Parameter and Command Reference Guide | SM Parameters

### SM.I1

```
General Information
Type R/W Parameter
Description Sets service motion current 1.
Units A
Range –Drive peak current to +Drive peak current
Default Value 0.025∙Drive peak current
Data Type Float
See Also SM.ACCTYPE, SM.I2, SM.MODE, SM.MOVE, SM.T1, SM.T2, SM.V1,SM.V2, SM.VPM1, SM.VPM2
Start Version M_0-0-16
```
#### Description

```
SM.I1 defines the current that is used in service motion modes 0 and 1 (see SM.MODE).
```

### SM.I2

```
General Information
Type R/W Parameter
Description Sets service motion current 2.
Units –Drive peak current to +Drive peak current
Range 0.025∙Drive peak current
Default Value Float
Data Type
```
##### SM.ACCTYPE, SM.I1, SM.MODE, SM.MOVE, SM.T1, SM.T2, SM.V1,

##### SM.V2, SM.VPM1, SM.VPM2

```
See Also M_0-0-16
Start Version –Drive peak current to +Drive peak current
```
#### Description

SM.I2 defines the current that is used in service motion mode 1 (see SM.MODE).

```
AKD Parameter and Command Reference Guide | SM Parameters
```

AKD Parameter and Command Reference Guide | SM Parameters

### SM.MODE

```
General Information
Type R/W Paramete
Description Sets service motion mode.
Units N/A
Range 0 to 5
Default Value 4
Data Type Integer
See Also SM.ACCTYPE, SM.I1, SM.I2, SM.MOVE, SM.T1 SM.T2, SM.V1,SM.V2, SM.VPM1, SM.VPM2
Start Version M_0-0-16
```
#### Description

```
SM.MODE defines the mode of service motion for each loop. Two types of service motion are available :
```
1. A constant motion in one direction (endless or for a certain amount of time).
2. An alternating motion.
The six possible modes are described in the following table:

```
SM.MODE Description Requirements
```
##### 0

```
Constant motion in closed current loop
mode of operation. The drive generates a
constant current command value (SM.I1)
for a certain amount of time (if SM.T1>0)
or endless (if SM.T1=0). The service
motion can be stopped by using the
DRV.STOP command.
```
##### DRV.OPMODE = 0

##### DRV.CMDSOURCE = 0

##### 1

```
Alternating motion in closed current loop
mode of operation. The drive generates a
current command value (SM.I1) for a cer-
tain amount of time (SM.T1). Afterwards
the drive generates a current command
value (SM.I2) for another certain amount
of time (SM.T2). This sequence is
repeated as long as a DRV.STOP com-
mand occurs.
```
##### DRV.OPMODE = 0

##### DRV.CMDSOURCE = 0

##### SM.T1 > 0

##### 2

```
Constant motion in closed velocity loop
mode of operation. The drive generates a
constant velocity command value
(SM.V1) for a certain amount of time (if
SM.T1>0) or endless (if SM.T1=0). The
service motion can be stopped by using
the DRV.STOP command.
```
##### DRV.OPMODE = 1

##### DRV.CMDSOURCE = 0


```
SM.MODE Description Requirements
```
##### 3

```
Alternating motion in closed velocity loop
mode of operation. The drive generates a
velocity command value (SM.V1) for a cer-
tain amount of time (SM.T1). Afterwards
the drive generates a velocity command
value (SM.V2) for another certain amount
of time (SM.T2). This sequence is
repeated as long as a DRV.STOP com-
mand occurs.
```
##### DRV.OPMODE = 1

##### DRV.CMDSOURCE = 0

##### SM.T1 > 0

##### 4

```
Constant motion in closed position loop
mode of operation. The drive generates a
trajectory for the position loop by reaching
a constant velocity command value
(SM.VPM1) for a certain amount of time (if
SM.T1>0) or endless (if SM.T1=0). The
service motion can be stopped by using
the DRV.STOP command.
```
##### DRV.OPMODE = 2

##### DRV.CMDSOURCE = 0

##### 5

```
Alternating motion in closed position loop
mode of operation. The drive generates a
trajectory for the position loop by reaching
a constant a velocity command value
(SM.VPM1) for a certain amount of time
(SM.T1). Afterwards the drive generates a
trajectory for the position loop by reaching
a constant velocity command value
(SM.VPM2) for another certain amount of
time (SM.T2). This sequence is repeated
as long as a DRV.STOP command
occurs.
```
##### DRV.OPMODE = 2

##### DRV.CMDSOURCE = 0

##### SM.T1 > 0

#### Ramps

The drive uses DRV.ACC and DRV.DEC for the ramps in service motion modes 2, 3, 4, and 5. The drive
does not generate any ramps in service motion modes 0 and 1.

#### Service Motion Mode 1

```
AKD Parameter and Command Reference Guide | SM Parameters
```

AKD Parameter and Command Reference Guide | SM Parameters

#### Service Motion Mode 3

```
SM.T1 or SM.T2 contains the deceleration phase from SM.V1 or SM.V2 to 0 in service motion mode 3.
```
#### Service Motion Mode 5


The deceleration process from SM.VPM1 or SM.VPM2 to 0 is is not included in SM.T1 and SM.T2, respec-
tively. SM.T1 and SM.T2 start as soon as the command value has reached velocity 0.

```
AKD Parameter and Command Reference Guide | SM Parameters
```

AKD Parameter and Command Reference Guide | SM Parameters

### SM.MOVE

```
General Information
Type Command
Description Starts the service motion.
Units N/A
Range N/A
Default Value N/A
Data Type N/A
See Also SM.MODE
Start Version M_0-0-16
```
#### Description

```
This command starts the service motion that has been selected by the SM.MODE parameter.
```

### SM.T1

```
General Information
Type R/W Parameter
Description Sets service motion time 1.
Units ms
Range 0 to 65,535 ms
Default Value 500 ms
Data Type Integer
See Also SM.ACCTYPE, SM.I1, SM.I2, SM.MODE, SM.MOVE, SM.T2, SM.V1,SM.V2, SM.VPM1, SM.VPM2
Start Version M_0-0-16
```
#### Description

SM.T1 defines the time of the service motion that is used in all service motion modes (see SM.MODE). For an
alternating service motion mode, SM.T1 may not be set to 0.

```
AKD Parameter and Command Reference Guide | SM Parameters
```

AKD Parameter and Command Reference Guide | SM Parameters

### SM.T2

```
General Information
Type R/W Parameter
Description Sets service motion time 2
Units ms
Range 1 to 65,535 ms
Default Value 500 ms
Data Type Integer
See Also SM.ACCTYPE, SM.I1, SM.I2, SM.MODE, SM.MOVE, SM.T1, SM.V1,SM.V2, SM.VPM1, SM.VPM2
Start Version M_0-0-16
```
#### Description

```
SM.T2 defines the time of the service motion that is used in service motion modes 1, 3, and 5 (see
SM.MODE).
```

### SM.V1

```
General Information
Type R/W Parameter
Description Sets service motion velocity 1.
```
```
Units
```
```
Depends on UNIT.ACCROTARY or UNIT.ACCLINEAR
Rotary: rpm, rps, deg/s, (PIN/POUT)/s, rad/s
Linear: Counts/s, mm/s, μm/s, (PIN/POUT)/s
```
```
Range
```
```
Rotary:
-12,000.000 to 12,000.000 rpm
-200.000 to 200.000 rps
-72,000.000 to 72,000.000 deg/s
-1,000.000 to 1,000.000 (PIN/POUT)/s
-1,256.637 to 1,256.637 rad/s
Linear:
-0.200 to 0.200 Counts/s
-200.000*MOTOR.PITCH to 200.000*MOTOR.PITCH mm/s
-200,000.000*MOTOR.PITCH to 200,000.000*MOTOR.PITCH μm/s
-1,000.000 to 1,000.000 (PIN/POUT)/s
```
```
Default Value
```
```
Rotary:
60.000 rpm
1.000 rps
359.999 deg/s
5.000 (PIN/POUT)/s
6.283 rad/s
Linear:
0.001 Counts/s
1.000*MOTOR.PITCH mm/s
999.998*MOTOR.PITCH μm/sec
5.000 (PIN/POUT)/s
Data Type Float
See Also
```
##### SM.ACCTYPE, SM.I1, SM.I2, SM.MODE, SM.MOVE, SM.T1, SM.T2,

##### SM.V2, SM.VPM1, SM.VPM2

```
Start Version M_0-0-16
```
#### Description

SM.V1 defines the velocity that is used in service motion modes 2 and 3 (see SM.MODE) in the closed veloc-
ity mode of operation.

```
AKD Parameter and Command Reference Guide | SM Parameters
```

AKD Parameter and Command Reference Guide | SM Parameters

### SM.V2

```
General Information
Type R/W Parameter
Description Sets service motion velocity 2.
```
```
Units
```
```
Depends on UNIT.ACCROTARY or UNIT.ACCLINEAR
Rotary: rpm, rps, deg/s, (PIN/POUT)/s, rad/s
Linear: counts/s, mm/s, μm/s, (PIN/POUT)/s
```
```
Range
```
```
Rotary:
-12,000.000 to 12,000.000 rpm
-200.000 to 200.000 rps
-72,000.000 to 72,000.000 deg/s
-1,000.000 to 1,000.000 (PIN/POUT)/s
-1,256.637 to 1,256.637 rad/s
Linear:
-0.200 to 0.200 counts/s
-200.000*MOTOR.PITCH to 200.000*MOTOR.PITCH mm/s
-200,000.000*MOTOR.PITCH to 200,000.000*MOTOR.PITCH μm/s
-1,000.000 to 1,000.000 (PIN/POUT)/s
```
```
Default Value
```
```
Rotary:
-60.000 rpm
-1.000 rps
-359.999 deg/s
-5.000 (PIN/POUT)/s
-6.283 rad/s
Linear:
-0.001 counts/s
-1.000*MOTOR.PITCH mm/s
-999.998*MOTOR.PITCH μm/sec
-5.000 (PIN/POUT)/s
Data Type Float
See Also SM.ACCTYPE, SM.I1, SM.I2, SM.MODE, SM.MOVE, SM.T1, SM.T2,SM.V1, SM.VPM1, SM.VPM2
Start Version M_0-0-16
```
#### Description

```
SM.V2 defines the velocity that is used in service motion mode 3 (see SM.MODE) in the closed velocity
mode of operation.
```

### SM.VPM1

```
General Information
Type R/W Parameter
Description Sets service motion velocity 2 in position mode of operation.
```
```
Units
```
```
Depends on UNIT.ACCROTARY or UNIT.ACCLINEAR
Rotary: rpm, rps, deg/s, (PIN/POUT)/s, rad/s
Linear: counts/s, mm/s, μm/s, (PIN/POUT)/s
```
```
Range
```
```
Rotary:
-12,000.000 to 12,000.000 rpm
-200.000 to 200.000 rps
-72,000.000 to 72,000.000 deg/s
-1,000.000 to 1,000.000 (PIN/POUT)/s
-1,256.637 to 1,256.637 rad/s
Linear:
-0.200 to 0.200 counts/s
-200.000*MOTOR.PITCH to 200.000*MOTOR.PITCH mm/s
-200,000.000*MOTOR.PITCH to 200,000.000*MOTOR.PITCH μm/s
-1000.000 to 1000.000 (PIN/POUT)/s
```
```
Default Value
```
```
Rotary:
60.000 rpm
1.000 rps
359.999 deg/s
5.000 (PIN/POUT)/s
6.283 rad/s
Linear:
0.001 Counts/s
1.000*MOTOR.PITCH mm/s
999.998*MOTOR.PITCH μm/s
5.000 (PIN/POUT)/s
Data Type Float
See Also SM.ACCTYPE, SM.I1, SM.I2, SM.MODE, SM.MOVE, SM.T1, SM.T2,
SM.V1, SM.V2, SM.VPM2
Start Version M_0-0-16
```
#### Description

SM.VPM1 defines the velocity that is used in service motion mode 4 and 5 (see SM.MODE) in the closed posi-
tion mode of operation.

```
AKD Parameter and Command Reference Guide | SM Parameters
```

AKD Parameter and Command Reference Guide | SM Parameters

### SM.VPM2

```
General Information
Type R/W Parameter
Description Sets service motion velocity 2 in position mode of operation.
```
```
Units
```
```
Depends on UNIT.ACCROTARY or UNIT.ACCLINEAR
Rotary: rpm, rps, deg/s, (PIN/POUT)/s, rad/s
Linear: counts/s, mm/s, μm/s, (PIN/POUT)/s
```
```
Range
```
```
Rotary:
-12,000.000 to 12,000.000 rpm
-200.000 to 200.000 rps
-72,000.000 to 72,000.000 deg/s
-1,000.000 to 1,000.000 (PIN/POUT)/s
-1,256.637 to 1,256.637 rad/s
Linear:
-0.200 to 0.200 counts/s
-200.000*MOTOR.PITCH to 200.000*MOTOR.PITCH mm/s
-200,000.000*MOTOR.PITCH to 200,000.000*MOTOR.PITCH μm/s
-1,000.000 to 1,000.000 (PIN/POUT)/s
```
```
Default Value
```
```
Rotary:
-60.000 rpm
-1.000 rps
-359.999 deg/s
-5.000 (PIN/POUT)/s
-6.283 rad/s
Linear:
-0.001 counts/s
-1.000*MOTOR.PITCH mm/s
-999.998*MOTOR.PITCH μm/s
-5.000 (PIN/POUT)/s
Data Type Float
See Also SM.ACCTYPE, SM.I1, SM.I2, SM.MODE, SM.MOVE, SM.T1, SM.T2,SM.V1, SM.V2, SM.VPM1
Start Version M_0-0-16
```
#### Description

```
SM.VPM2 defines the velocity that is used in service motion mode 5 (see SM.MODE) in the closed position
mode of operation.
```

## 2 STO Parameters

```
AKD Parameter and Command Reference Guide | 2 STO Parameters
```

AKD Parameter and Command Reference Guide | 2 STO Parameters

### STO.STATE

```
General Information
Type R/O Parameter
Description Returns the status of the safe torque off.
Units N/A
Range 0 to 1
Default Value none
Data Type Integer
See Also N/A
Start Version M_00-00-56-000
```
#### Description

```
STO.STATE returns the status of the safe torque off.
1 - Safe torque on (no safe torque off fault).
0 - Safe torque off (safe torque off fault ).
```

## SWLS Parameters

#### SWLS.EN

```
General Information
Type NV Parameter
Description Position software emergency stop switch enable
Units N/A
Range 0 to 3
Default Value 0
Data Type U8
See Also N/A
Start Version M_0-0-50-0
```
#### Description

This parameter enables the software emergency stop switches. The software limit switches are only active if
the axis is homed. For more information about homing, please refer to the HOME and DRV.MOTIONSTAT
parameters.

#### Example

Bit 0 = 0: Disable SWLS.LIMIT0

Bit 0 = 1: Enable SWLS.LIMIT0

Bit 1 = 0: Disable SWLS.LIMIT1

Bit 1 = 1: Enable SWLS.LIMIT1

```
AKD Parameter and Command Reference Guide | SWLS Parameters
```

AKD Parameter and Command Reference Guide | SWLS Parameters

#### SWLS.LIMIT0

```
General Information
Type NV Parameter
Description Sets the position software emergency stop switch 0
Units Position units
Range -9,007,199,254,740,992 to 9,007,199,254,740,991
Default Value 0
Data Type S64
See Also UNIT.PROTARY, UNIT.PLINEAR
Start Version M_0-0-50-0
```
#### Description

```
This parameter sets the compare register for the software emergency stop switch 0. This can be either the
lower or the upper software limit switch register, depending on SWLS.LIMIT1. The software limit switches are
only active if the axis is homed. For more information about homing, please refer to the HOME and DRV.M-
OTIONSTAT parameters.
```

#### SWLS.LIMIT1

```
General Information
Type NV Parameter
Description Position software emergency stop switch 1
Units Position units
Range -9,007,199,254,740,992 to 9,007,199,254,740,991
Default Value 68,719,476,736
Data Type S64
See Also UNIT.PROTARY, UNIT.PLINEAR
Start Version M_0-0-50-0
```
#### Description

This parameter sets the compare register for the software emergency stop switch 1. This value can be either
the lower or the upper software limit switch register, depending on SWLS.LIMIT0. The software limit switches
are only active if the axis is homed. For more information about homing, please refer to the HOME and DRV.M-
OTIONSTAT parameters.

```
AKD Parameter and Command Reference Guide | SWLS Parameters
```

AKD Parameter and Command Reference Guide | SWLS Parameters

#### SWLS.STATE

```
General Information
Type R/O Parameter
Description Actual status of SW limit switches.
Units N/A
Range 0 to 3
Default Value 0
Data Type U8
See Also N/A
Start Version M_0-0-50-0
```
#### Description

```
This parameter reads the status word of the software emergency stop switches. The status word indicates
the result of the compare between the software emergency stop switch compare register and the actual posi-
tion of the position loop.
```
#### Example

```
Bit 0 = 0: SWLS.LIMIT0 is not active.
Bit 0 = 1: SWLS.LIMIT0 is active.
Bit 1 = 0: SWLS.LIMIT1 is not active.
Bit 1 = 1: SWLS.LIMIT1 is active.
Bits 2 to 7 are currently not in use.
```

### UNIT Parameters

#### UNIT.ACCLINEAR

```
General Information
Type NV Parameter
Description Sets the linear acceleration/deceleration units.
Units N/A
Range 0 to 3
Default Value 0
Data Type Integer
See Also DRV.ACC, DRV.DEC, MOTOR.TYPE
Start Version M_0-0-15
```
#### Description

UNIT.ACCLINEAR sets the units type for the acceleration and deceleration parameters, when the motor type
(MOTOR.TYPE) is linear.

UNIT.ACCLINEAR Types

```
Type Description
0 [PIN/POUT]/s^2
1 millimeters per second squared (mm/s^2 )
2 micrometers per second squared (μm/s^2 )
3 Feedback counts/s^2
```
```
AKD Parameter and Command Reference Guide | UNIT Parameters
```

AKD Parameter and Command Reference Guide | UNIT Parameters

#### UNIT.ACCROTARY

```
General Information
Type NV Parameter
Description Sets the rotary acceleration/deceleration units.
Units rpm/s, rps/s, deg/s^2 , [PIN/POUT]/s^2
Range 0 to 3
Default Value 0 rpm/s
Data Type Integer
See Also DRV.ACC, "DRV.DEC" (page 88), MOTOR.TYPE
Start Version M_0-0-15
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 3659h/0
Data Type Integer 32
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

```
UNIT.ACCROTARY sets the acceleration/deceleration units when the motor type (MOTOR.TYPE) is rotary.
UNIT.ACCROTARY Types
```
```
Type Description
0 rpm/s
1 rps/s
2 deg/s^2
3 (PIN/POUT)/s^2
```

#### UNIT.LABEL

```
General Information
Type NV Parameter
Description Sets user-defined name for user-defined position units.
Units N/A
Range Maximum 16 characters, no spaces
Default Value PIN/POUT
Data Type String
See Also UNIT.PLINEAR, UNIT.POUT
Start Version M_0-0-50-0
```
#### Description

If you define a special position unit with UNIT.PLINEAR and UNIT.POUT, then you can give this unit a
descriptive name. You can name the unit anything you wish, as long as the name is limited to 16 characters
and includes no spaces. This name is shown in derived units as velocity and acceleration.

This parameter is descriptive only and does not influence drive internal functions in any way.

```
AKD Parameter and Command Reference Guide | UNIT Parameters
```

AKD Parameter and Command Reference Guide | UNIT Parameters

#### UNIT.PIN

```
General Information
Type NV Parameter
Description Sets gear IN for the unit conversion.
Units User units
Range 0 to 65,535
Default Value 100
Data Type Integer
See Also UNIT.POUT
Start Version M_0-0-15
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 35CAh/0
Data Type Integer 32
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

```
UNIT.PIN is used in conjunction with UNIT.POUT to set application specific units. This parameter is used as
follows in the drive unit conversion:
 For position, this parameter sets the units as [PIN/POUT]/rev.
 For velocity, this parameter sets the units as [PIN/POUT]/s.
 For acceleration/deceleration, this parameter sets the units as [PIN/POUT]/s^2.
```

#### UNIT.PLINEAR

```
General Information
Type NV Parameter
Description Sets the linear position units.
Units N/A
Range 0 to 4
Default Value 0
Data Type Integer
See Also PL.FB, PL.CMD, MOTOR.TYPE
Start Version M_0-0-15
```
#### Description

UNIT.PLINEAR sets theunits typefor theposition parameterswhen themotor type(MOTOR.TYPE) islinear.

**UNIT.PLINEAR Types**

```
Type Description
0 Counts (32 bit)
1 Millimeters (mm)
2 Micrometers (μm)
3 (PLINEAR/POUT) per revolution
4 Counts (16 Bit)
```
```
AKD Parameter and Command Reference Guide | UNIT Parameters
```

AKD Parameter and Command Reference Guide | UNIT Parameters

#### UNIT.POUT

```
General Information
Type NV Parameter
Description Sets gear out for the unit conversion.
Units User units.
Range 0 to 65,535
Default Value 100
Data Type Integer
See Also UNIT.PLINEAR
Start Version M_0-0-15
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 35CBh/0
Data Type Integer 32
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

```
UNIT.POUT is used in conjunction with UNIT.PLINEAR to set application specific units in
UNIT.POUT. This parameter is used as follows in the drive unit conversion:
 For position, this parameter sets the units as [PIN/POUT]/rev.
 For velocity, this parameter sets the units as [PIN/POUT]/s.
 For acceleration/deceleration, this parameter sets the units as [PIN/POUT]/s^2.
```

#### UNIT.PROTARY

```
General Information
Type NV Parameter
Description Sets the position units when the motor type (MOTOR.TYPE) is rotary.
Units feedback counts, rad, deg, [PIN/POUT]
Range 0 to 3
Default Value 0 feedback counts
Data Type Integer
See Also PL.FB, PL.CMD, MOTOR.TYPE
Start Version M_0-0-15
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 3660h/0
Data Type Integer 32
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

UNIT.PROTARY sets the position units when the motor type (MOTOR.TYPE) is rotary.

**UNIT.PROTARY Types**

```
Type Description
0 counts
1 radians
2 degrees
3 [PIN/POUT]
```
```
AKD Parameter and Command Reference Guide | UNIT Parameters
```

AKD Parameter and Command Reference Guide | UNIT Parameters

#### UNIT.VLINEAR

```
General Information
Type NV Parameter
Description Sets the linear velocity units.
Units N/A
Range 0 to 3
Default Value 0
Data Type Integer
See Also VL.FB, VL.CMDU, VL.CMD, MOTOR.TYPE
Start Version M_0-0-15
```
#### Description

```
UNIT.VLINEAR sets theunits typefor thevelocity parameterswhen themotor type(MOTOR.TYPE) islinear.
UNIT.VLINEAR Types
```
```
Type Description
0 (PIN/POUT) per second
1 Micrometers per second
2 Millimeters per second
3 Counts per second
```

#### UNIT.VROTARY

```
General Information
Type NV Parameter
Description Sets the velocity units when the motor type (MOTOR.TYPE) is rotary.
Units rpm, rps, deg/s, (PIN/POUT)/s
Range 0 to 3
Default Value 0 rpm
Data Type Integer
See Also VL.FB, VL.CMDU, VL.CMD, MOTOR.TYPE
Start Version M_0-0-15
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 365Fh/0
Data Type Integer 32
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

UNIT.VROTARY sets the velocity units when the motor type (MOTOR.TYPE) is rotary.

**UNIT.VROTARY Types**

```
Type Description
0 rpm
1 rps
2 deg/s
3 (PIN/POUT)/s
```
```
AKD Parameter and Command Reference Guide | UNIT Parameters
```

AKD Parameter and Command Reference Guide | VBUS Parameters

### VBUS Parameters


#### VBUS.OVFTHRESH

```
General Information
Type R/O Parameter
Description Reads the over voltage fault level.
Units V
Range 0 to 900 V
Default Value N/A
Data Type Integer
See Also VBUS.UVFTHRESH
Start Version M_0-0-15
```
#### Description

VBUS.OVFTHRESH reads the over voltage fault level for the DC bus.

This value is read from the drive EEPROM and varies according to the drive type.

```
AKD Parameter and Command Reference Guide | VBUS Parameters
```

AKD Parameter and Command Reference Guide | VBUS Parameters

#### VBUS.OVFWTHRESH

```
General Information
Type NV Parameter
Description Sets voltage level for over voltage warning.
Units V
Range 0 to 900 V
Default Value 0 (warning disabled)
Data Type U16
See Also N/A
Start Version M_0-0-50-0
```
#### Description

```
If VBUS.VALUE value exeeds VBUS.OVFWTHRESH, then a warning is generated.
```

#### VBUS.RMSLIMIT

```
General Information
Type R/O Parameter
Description Reads the limit for the bus capacitors load.
Units Vrms
Range N/A
Default Value N/A
Data Type Integer
See Also N/A
Start Version M_00-00-55-000
```
#### Description

This parameter reads the limit of the bus capacitor load. When the bus capacitor loads exceeds this limit, the
drive generates fault F503.

Excessive bus capacitor load may indicate a disconnected main supply phase.

```
AKD Parameter and Command Reference Guide | VBUS Parameters
```

AKD Parameter and Command Reference Guide | VBUS Parameters

#### VBUS.UVFTHRESH

```
General Information
Type R/O Parameter
Description Reads the under voltage fault level.
Units V
Range 0 to 900 V
Default Value N/A
Data Type Integer
See Also VBUS.OVFTHRESH
Start Version M_0-0-15
```
#### Description

```
VBUS.UVFTHRESH reads the undervoltage fault level of the DC bus.
The value is read from the drive EEPROM. The value is varied according to drive type.
```

#### VBUS.UVMODE

```
General Information
Type
Description Indicates undervoltage (UV) mode.
Units N/A
Range 0 to 1
Default Value 1
Data Type Boolean
See Also N/A
Start Version M_0-0-37
```
#### Description

This parameter indicates undervoltage (UV) mode.
When VBUS.UVMODE - 0, an undervoltage fault is issued whenever the DC bus goes below the under-
voltage threshold.

When VBUS.UVMODE = 1, an undervoltage fault is issued whenever the DC bus goes below the

under voltage threshold and the controller attempts to enable the drive (software or hardware enable).

```
AKD Parameter and Command Reference Guide | VBUS Parameters
```

AKD Parameter and Command Reference Guide | VBUS Parameters

#### VBUS.UVWTHRESH

```
General Information
Type NV Parameter
Description Sets voltage level for undervoltage warning.
Units V
Range 0 to 900 V
Default Value 0 V (warning disabled)
Data Type U16
See Also N/A
Start Version M_0-0-50-0
```
#### Description

```
If VBUS.VALUE value drops below VBUS.UVWTHRESH, then a warning is generated.
```

#### Measured Bus Voltage: VBUS.VALUE

```
General Information
Type R/O Parameter
Description Reads DC bus voltage.
Units V
Range 0 to 900 V
Default Value N/A
Data Type Integer
See Also N/A
Start Version M_0-0-15
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 361Ah/0
Data Type Integer 32
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

VBUS.VALUE reads the DC bus voltage.

```
AKD Parameter and Command Reference Guide | VBUS Parameters
```

This page intentionally left blank.


### VL Parameters

#### VL.ARPF1 TO VL.ARPF4

```
General Information
Type R/W Parameter
Description Sets the natural frequency of the pole (denominator) of anti-resonance
(AR) filters 1, 2, 3, and 4.
Units Hz
Range 5 to 5,000 Hz
Default Value 500 Hz
Data Type Float
See Also VL.ARPQ1 TO VL.ARPQ4, VL.ARZF1 TO VL.ARZF4, Sets the Q of the
zero (numerator) of anti-resonance filter #1.
Start Version
```
#### Description

VL.ARPF1 sets the natural frequency of the pole (denominator) of AR filter 1. This value is FPin the approx-
imate transfer function of the filter:
ARx( **s** ) = [ **s** ²/(2πFZ)² + **s** /(QZ2πFZ) + 1]/ [ **s** ²/(2πFP)² + **s** /(QP2πFP) + 1]

```
The following block diagram describes the AR filter function; note that AR1 and AR2 are in the forward path,
while AR3 and AR4 are applied to feedback:
```
AR1, AR2, AR3, and AR4 are used in velocity and position mode, but are disabled in torque mode.

**Discrete time transfer function (applies to all AR filters)**

Thevelocity loopcompensation isactually implementedas adigital discretetime systemfunction onthe DSP.
Thecontinuous timetransfer functionis convertedto thediscrete timedomain bya backwardEuler mapping:

```
s ≈ (1-z-1)/t, where t = 62.5 μs
```
The poles are prewarped to FPand the zeros are prewarped to FZ.

```
AKD Parameter and Command Reference Guide | VL Parameters
```

AKD Parameter and Command Reference Guide | VL Parameters

#### VL.ARPQ1 TO VL.ARPQ4

```
General Information
Type R/W Parameter
Description Sets the Q of the pole (denominator) of anti-resonance (AR) filter 1.
Units None
Range 0.2 to 20
Default Value 0.5
Data Type Float
See Also VL.ARPF1 TO VL.ARPF4, VL.ARZF1 TO VL.ARZF4, VL.ARZQ1 TOVL.ARZQ4
Start Version
```
#### Description

```
VL.ARPQ1 sets the Q (quality factor) of the pole (denominator) of AR filter 1. This value is QPin the approx-
imate transfer function of the filter:
```
```
ARx( s ) = [ s ²/(2πFZ)²+ s /(QZ2πFZ) + 1]/ [ s ²/(2πFP)² + s /(QP2πFP) + 1]
```
```
The following block diagram describes the AR filter function; note that AR1 and AR2 are in the forward path,
while AR3 and AR4 are applied to feedback:
```
```
AR1, AR2, AR3, and AR4 are used in velocity and position mode, but are disabled in torque mode.
Discrete time transfer function (applies to all AR filters)
Thevelocity loopcompensation isactually implementedas adigital discretetime systemfunction onthe DSP.
Thecontinuous timetransfer functionis convertedto thediscrete timedomain bya backwardEuler mapping:
s ≈ (1-z-1)/t, where t = 62.5 μs
The poles are prewarped to FPand the zeros are prewarped to FZ.
```

#### VL.ARTYPE1 TO VL.ARTYPE4

```
General Information
Type NVParameter
Description Indicates the method used to calculate BiQuad coefficients.
Units N/A
Range 0
Default Value 0
Data Type U8
See Also N/A
Start Version M_00-00-56-000
```
#### Description

These parameters indicate the method used to calculate the biquad coefficients VL.ARPFx, VL.ARPQx,
VL.ARZFx, and VL.ARZQx. A value of 0 indicates that the coefficients are set directly. This parameter has no
effect on the filter itself, but is only used to determine the original design parameters. Currently, only the value
of 0 is supported.

```
AKD Parameter and Command Reference Guide | VL Parameters
```

AKD Parameter and Command Reference Guide | VL Parameters

#### VL.ARZF1 TO VL.ARZF4

```
General Information
Type R/W Parameter
Description
Sets the natural frequency of the zero (numerator) of anti-resonance
(AR)filter 1.
Units Hz
Range 5 to 5,000 Hz
Default Value 500 Hz
Data Type Float
See Also
```
##### VL.ARPF1 TO VL.ARPF4,VL.ARPQ1 TO VL.ARPQ4, VL.ARZQ1 TO

##### VL.ARZQ4

```
Start Version
```
#### Description

```
VL.ARZF1 sets the natural frequency of the zero (numerator) of AR filter 1. This value is FZin the approximate
transfer function of the filter:
ARx( s ) = [ s ²/(2πFZ)² + s /(QZ2πFZ) + 1]/ [ s ²/(2πFP)² + s /(QP2πFP) + 1]
The following block diagram describes the AR filter function; note that AR1 and AR2 are in the forward path,
while AR3 and AR4 are applied to feedback:
```
```
AR1, AR2, AR3, and AR4 are used in velocity and position mode, but are disabled in torque mode.
Discrete time transfer function (applies to all AR filters)
Thevelocity loopcompensation isactually implementedas adigital discretetime systemfunction onthe DSP.
Thecontinuous timetransfer functionis convertedto thediscrete timedomain bya backwardEuler mapping:
s ≈ (1-z-1)/t, where t = 62.5 μs
The poles are prewarped to FPand the zeros are prewarped to FZ.
```

#### VL.ARZQ1 TO VL.ARZQ4

```
General Information
Type R/W Parameter
Description Sets the Q of the zero (numerator) of anti-resonance filter #1.
Units N/A
Range 0.1 to 5
Default Value 0.5
Data Type Float
See Also VL.ARPF1 TO VL.ARPF4, VL.ARPQ1 TO VL.ARPQ4, VL.ARZF1 TOVL.ARZF4
Start Version
```
#### Description

VL.ARZQ1 sets the Q (quality factor) of the zero (numerator) of AR filter 1. This value is QZin the approximate
transfer function of the filter:

AR1( **s** ) = [ **s** ²/(2πFZ)²+ **s** /(QZ2πFZ) + 1]/ [ **s** ²/(2πFP)² + **s** /(QP2πFP) + 1]

```
The following block diagram describes the AR filter function; note that AR1 and AR2 are in the forward path,
while AR3 and AR4 are applied to feedback:
```
AR1, AR2, AR3 and AR4 are used in velocity and position mode, but are disabled in torque mode.

**Discrete time transfer function (applies to all AR filters)**

Thevelocity loopcompensation isactually implementedas adigital discretetime systemfunction onthe DSP.
Thecontinuous timetransfer functionis convertedto thediscrete timedomain bya backwardEuler mapping:

```
s ≈ (1-z-1)/t, where t = 62.5 μs.
```
The poles are prewarped to FPand the zeros are prewarped to FZ.

```
AKD Parameter and Command Reference Guide | VL Parameters
```

AKD Parameter and Command Reference Guide | VL Parameters

#### VL.BUSFF

```
General Information
Type R/O Parameter
Description Displays the velocity loop feedforward value injected by the field-bus
```
```
Units
```
```
Depends on UNIT.VROTARY or UNIT.VLINEARUNIT.ACCLINEAR
Rotary: rpm, rps, deg/s, (PIN/POUT)/s, rad/s
Linear: counts/s, mm/s, μm/s, (PIN/POUT)/s
Range 0.0 to VL.LIMITP
Default Value 0.0
Data Type Float
See Also VL.FF, VL.KBUSFF
Start Version M_0-0-32
```
#### Description

```
Displays the velocity loop feedforward value injected by the fieldbus.
```

#### VL.CMD

```
General Information
Type R/O Parameter
Description Reads the actual velocity command.
```
```
Units
```
```
Depends on UNIT.VROTARY or UNIT.VLINEARUNIT.ACCLINEAR
Rotary: rpm, rps, deg/s, (PIN/POUT)/s, rad/s
Linear: counts/s, mm/s, μm/s, (PIN/POUT)/s
Range N/A
Default Value N/A
Data Type Float
See Also VL.FB, VL.CMDU, VL.LIMITP, VL.LIMITN
Start Version M_0-0-15
```
#### Description

VL.CMD returns the actual velocity command as it is received in the velocity loop entry after all velocity limits
(such as VL.LIMITN and VL.LIMITP). See velocity loop design diagram for more details.

```
AKD Parameter and Command Reference Guide | VL Parameters
```

AKD Parameter and Command Reference Guide | VL Parameters

#### VL.CMDU

```
General Information
Type R/W Parameter
Description Sets the user velocity command.
```
```
Units
```
```
Depends on UNIT.VROTARY or UNIT.VLINEARUNIT.ACCLINEAR
Rotary: rpm, rps, deg/s, (PIN/POUT)/s, rad/s
Linear: counts/s, mm/s, μm/s, (PIN/POUT)/s
```
```
Range
```
```
Rotary:
-12,000.000 to 12,000.000 rpm
-200.000 to 200.000 rps
-72,000.000 to 72,000.00 deg/s
-1,000.000 to 1,000.000 (PIN/POUT)/s
-1,256.637 to 1,256.637 rad/s
Linear:
-0.200 to 0.200 counts/s
-200.000*MOTOR.PITCH to 200.000*MOTOR.PITCH mm/s
-200,000.000*MOTOR.PITCH to 200,000.000*MOTOR.PITCH μm/s
-1000.000 to 1000.000 (PIN/POUT)/s
Default Value 0
Data Type Float
See Also VL.FB, VL.CMD, DRV.OPMODE, DRV.CMDSOURCE
Start Version M_0-0-15
```
#### Description

```
VL.CMDU sets the user velocity command.
When DRV.OPMODE is set to 1 (velocity loop) and DRV.CMDSOURCE is set to 0 (TCP/IP channel), then
setting this value when the drive is enabled will cause the drive to rotate at the required velocity.
```

#### VL.ERR

```
General Information
Type R/O Parameter
Description Sets the velocity error.
```
```
Units
```
```
Depends on UNIT.VROTARY or UNIT.VLINEAR
Rotary: rpm, rps, deg/s, (PIN/POUT)/s, rad/s
Linear: counts/s, mm/s, μm/s, (PIN/POUT)/s
Range N/A
Default Value N/A
Data Type Float
See Also VL.CMD, VL.FB
Start Version M_0-0-15
```
#### Description

VL.ERR sets the velocity error. It is calculated in the velocity loop as the difference between VL.CMD and
VL.FB. See the velocity loop design for more information.

```
AKD Parameter and Command Reference Guide | VL Parameters
```

AKD Parameter and Command Reference Guide | VL Parameters

#### VL.FB

```
General Information
Type R/O Parameter
Description Reads the velocity feedback.
```
```
Units
```
```
Depends on UNIT.VROTARY or UNIT.VLINEARUNIT.ACCLINEAR
Rotary: rpm, rps, deg/s, (PIN/POUT)/s, rad/s
Linear: Counts/s, mm/s, μm/s, (PIN/POUT)/s
Range N/A
Default Value N/A
Data Type Float
See Also VL.CMDU
Start Version M_0-0-15
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 3618h/0
Data Type Integer 32
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

```
VL.FB returns the velocity feedback as it is received in the velocity loop.
```

## VL.FBFILTER

```
General Information
Type R/O Parameter
Description Filters VL.FB value.
```
```
Units
```
```
Depends on UNIT.VROTARY or UNIT.VLINEAR
Rotary: rpm, rps, deg/s, (PIN/POUT)/s, rad/s
Linear: counts/s, mm/s, μm/s, (PIN/POUT)/s
Range N/A
Default Value N/A
Data Type Float
See Also VL.FB
Start Version M-0-0-50-0
```
#### Description

This parameter returns the same value as VL.FB, filtered through a 10 Hz filter.

```
AKD Parameter and Command Reference Guide | VL Parameters
```

AKD Parameter and Command Reference Guide | VL Parameters

## VL.FBSOURCE

```
General Information
Type NV Parameter
Description Sets feedback source for the velocity loop.
Units N/A
Range 0 to 1
Default Value 0
Data Type Boolean
See Also PL.FBSOURCE
Start Version M_00-00-51-000
```
#### Description

```
This parameter determines the feedback source to be used by the velocity loop. A value of 0 selects the pri-
mary feedback, 1 selects the secondary feedback.
```

## VL.FF

```
General Information
Type R/O Parameter
Description Displays the velocity loop overall feedforward value.
```
```
Units
```
```
Depends on UNIT.ACCROTARY or UNIT.ACCLINEAR
Rotary: rpm, rps, deg/s, (PIN/POUT)/s, rad/s
Linear: counts/s, mm/s, μm/s, (PIN/POUT)/s
Range 0 to VL.LIMITP
Default Value 0
Data Type Float
See Also VL.KBUSFF, VL.KVFF, VL.ACCFFGAIN
Start Version M_0-0-32
```
#### Description

This parameter displays the velocity loop overall feedforward value.

```
AKD Parameter and Command Reference Guide | VL Parameters
```

AKD Parameter and Command Reference Guide | VL Parameters

## VL.GENMODE

```
General Information
Type NV Parameter
Description Selects mode of velocity generation (Observer, d/dt).
Units N/A
Range 0 to 1
Default Value 0
Data Type Integer
See Also N/A
Start Version M_0-0-15
```
#### Description

```
This parameter is used to select the velocity generator mode.
Mode Description
```
```
0
```
```
d/dt mode, the derivative of the mechanical
angle of the drive, is fed to a first order low
pass.
1
Luenberger Observer mode, (TBD the Luen-
berger observer is not implemented yet)
```
#### d/dt Mode


## VL.KBUSFF

```
General Information
Type R/W Parameter
Description Sets the velocity loop acceleration feedforward gain value.
Units NA
Range 0.0 to 2.0
Default Value 0.0
Data Type Float
See Also VL.BUSFF
Start Version M_0-0-32
```
#### Description

This parameter sets the gain for the acceleration feedforward (a scaled second derivative of the position com-
mand is added to the velocity command value).

The nominal feedforward value can be multiplied by this gain value.

This will have affect only when using position mode (DRV.OPMODE = 2).

```
AKD Parameter and Command Reference Guide | VL Parameters
```

AKD Parameter and Command Reference Guide | VL Parameters

## VL.KI

```
General Information
Type NV Parameter
Description Sets the velocity loop integral gain for the PI controller.
Units Hz
Range 0.000 to 2,147,483.008 Hz
Default Value 160.000 Hz
Data Type Float
See Also VL.KP
Start Version M_0-0-15
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 354Dh/0
Data Type Integer 32
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

```
VL.KI sets the integral gain of the velocity loop.
```
```
A factor of 2π is included in the time calculation, therefore a PI velocity loop with a constant error of 1 rps in
which VL.KI is set to 160 and VL.KP is set to 1, will take (1000/160)*2π ms to increase the integral gain to 1.
Therefore, the total gain is 2 at this time (see velocity loop structure below).
```
```
Velocity Loop Structure
```

## VL.KP

```
General Information
Type NV Parameter
Description Sets velocity loop proportional gain for the PI controller.
Units A/(rad/sec)
Range 0.001 to 2,147,483.008
Default Value 1
Data Type Float
See Also VL.KI
Start Version M_0-0-15
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 3548h/0
Data Type Integer 32
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

VL.KP sets the proportional gain of the velocity loop.

The idealized velocity loop bandwidth in Hz is:
VL.KP *Kt/ (2π *Jm)

**Where:**

Kt is the motor torque constant and Jm is the total shaft inertia. The units of Kt/Jm are rad/sec^2 /A.

See Velocity Controller Environment Block Diagram for more information.

## VL.KVFF

```
General Information
Type R/W Parameter
Description Velocity loop velocity feedforward gain value
Units NA
Range 0.0 to 2.0
Default Value 0.0
Data Type Float
See Also VL.FF
Start Version M_0-0-32
```
#### Description

This parameter sets the gain for the velocity feedforward (a scaled derivative of the position command is
added to the velocity command value). The nominal feedforward value can be multiplied by this gain value.

This parameter is only used in the position mode (DRV.OPMODE = 2).

```
AKD Parameter and Command Reference Guide | VL Parameters
```

AKD Parameter and Command Reference Guide | VL Parameters

## VL.LIMITN

```
General Information
Type NV Parameter
Description Sets the velocity lower limit.
```
```
Units
```
```
Depends on UNIT.VROTARY or UNIT.VLINEAR
Rotary: rpm, rps, deg/s, (PIN/POUT)/s, rad/s
Linear: counts/s, mm/s, μm/s, (PIN/POUT)/s
```
```
Range
```
```
Rotary:
-12,000.000 to 0.000 rpm
-200.000 to 0.000 rps
-72,000.000 to 0.000 deg/s
-1,000.000 to 0.000 (PIN/POUT)/s
-12,56.637 to 0.000 rad/s
Linear:
-0.200 to 0.000 counts/s
-200.000*MOTOR.PITCH to 0.000 mm/s
-200,000.000*MOTOR.PITCH to 0.000 μm/sec
-1,000.000 to 0.000 (PIN/POUT)/s
```
```
Default Value
```
```
Rotary:
-3,000.000 rpm
-50.000 rps
-17,998.998 deg/s
-250.000 (PIN/POUT)/s
-314.159 rad/s
Linear:
-0.050 Counts/s
-50*MOTOR.PITCH mm/s
-49,999.996*MOTOR.PITCH μm/sec
-250.000 (PIN/POUT)/s
Data Type Float
See Also VL.LIMITP, VL.CMD
Start Version M_0-0-15
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number
3623h/0
Data Type Integer 32
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

```
VL.LIMITN sets the velocity command negative limit.
```

If the input to the velocity loop is lower than VL.LIMITN, then the actual velocity command VL.CMD is limited
by the value of VL.LIMITN.

```
AKD Parameter and Command Reference Guide | VL Parameters
```

AKD Parameter and Command Reference Guide | VL Parameters

## VL.LIMITP

```
General Information
Type NV Parameter
Description Sets the velocity high limit.
```
```
Units
```
```
Depends on UNIT.VROTARY or UNIT.VLINEAR
Rotary: rpm, rps, deg/s, (PIN/POUT)/s, rad/s
Linear: counts/s, mm/s, μm/s, (PIN/POUT)/s
```
```
Range
```
```
Rotary:
0.000 to 12,000.000 rpm
0.000 to 200.000 rps
0.000 to 72,000.000 deg/s
0.000 to 1,000.000 (PIN/POUT)/s
0.000 to 1256.637 rad/s
Linear:
0.000 to 0.200 Counts/s
0.000 to 200.000*MOTOR.PITCH mm/sec
0.000 to 200,000.000*MOTOR.PITCH μm/s
0.000 to 1,000.000 (PIN/POUT)/s
```
```
Default Value
```
```
Rotary:
3,000.000 rpm
50.000 rps
17,998.998 deg/s
250.000 (PIN/POUT)/s
314.159 rad/s
Linear:
0.050 Counts/s
50.000*MOTOR.PITCH mm/sec
49,999.996*MOTOR.PITCH μm/sec
250.000 (PIN/POUT)/s
Data Type Float
See Also VL.LIMITN, VL.CMD
Start Version M_0-0-15
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 3622h/0
Data Type Integer 32
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

```
VL.LIMITP sets the velocity command positive limit.
```

If the input to the velocity loop is higher than VL.LIMITP, then the actual velocity command VL.CMD is limited
by the value of VL.LIMITP.

## VL.LMJR

```
General Information
Type R/W Parameter
Description Sets the ratio of the estimated load moment of inertia relative to the motormoment of inertia.
Units NA
Range 0 to 100.0
Default Value 0
Data Type Float
See Also IL.KACCFF, IL.FF
Start Version M_0-0-32
```
#### Description

This parameter is used in the internal calculation of the current loop acceleration feed forward gain value.

```
AKD Parameter and Command Reference Guide | VL Parameters
```

AKD Parameter and Command Reference Guide | VL Parameters

## VL.THRESH

```
General Information
Type NV Parameter
Description Sets the over speed fault value.
```
```
Units
```
```
Depends on UNIT.VROTARY or UNIT.VLINEAR
Rotary: rpm, rps, deg/s, (PIN/POUT)/s, rad/s
Linear: counts/s, mm/s, μm/s, (PIN/POUT)/s
```
```
Range
```
```
Rotary:
0 to 1,200.000 rpm
0 to 200.000 rps
0 to 72,000.000 deg/s
0 to 1,000.000 (PIN/POUT)/s
0.000 to 1,256.637 rad/s
Linear:
0.000 to 0.200 counts/s
0.000 to 200.000*MOTOR.PITCH mm/sec
0.000 to 200,000.000*MOTOR.PITCH μm/s
0 to 1,000.000 (PIN/POUT)/s
```
```
Default Value
```
```
Rotary:
1,000.000 rpm
16.667 rps
21,600.000 deg/s
300.000 (PIN/POUT)/s
376.991 rad/s
Linear:
0.060 counts/s
60.000*MOTOR.PITCH mm/sec
60,000.000*MOTOR.PITCH μm/s
300.000 (PIN/POUT)/s
Data Type Float
See Also VL.CMD, VL.CMDU
Start Version M_0-0-15
```
```
Fieldbus Information
EtherCAT COE & CANopen
Index/Subindex or
Parameter Number 3627h/0
Data Type Integer 32
PDO Mappable No
Start Version M_00-00-62-000
```
#### Description

```
VL.THRESH sets the threshold for the velocity over which an over speed fault is generated.
```

The value is considered as an absolute value, hence it applies for both negative and positive velocities.

#### Example

VL.THRESH is set to 600 rpm. A velocity command of 700 rpm will generate an over speed fault.

```
AKD Parameter and Command Reference Guide | VL Parameters
```

This page intentionally left blank.


