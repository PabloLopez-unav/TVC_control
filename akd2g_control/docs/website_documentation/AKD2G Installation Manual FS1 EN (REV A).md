## **AKD[®] 2G-Sxx** with Functional Safety Option 1 STO - SIL2 

## **Installation Manual** , English 

Manual Edition: A, December 2019 

Safety Edition: S101, December 2019 Valid for AKD[®] 2G-S Hardware Revision A Part Number 907-200003-00 

Original Document 

For safe and proper use, follow these instructions. Keep for future use. 

Beta Drives: All approvals are pending. 

**Record of Document Revisions** 

**Edition Remarks** ... Table with lifecycle information of this document (➜ # 151) A, 12/2019 First edition ~~—_————~~ 

**Hardware Revision (HR)** 

**AKD2G Firmware Workbench KAS IDE Remarks** A from 02-00-00-000 from 2.00.0.0000 from 3.01 Beta revision ~~—~~ 

## **Trademarks** 

AKD is a registered trademark of Kollmorgen Corporation. 

- EnDat is a registered trademark of Dr. Johannes Heidenhain GmbH. 

- EtherCAT is a registered trademark and patented technology, licensed by Beckhoff Automation GmbH, Germany. 

HIPERFACE is a registered trademark of Max Stegmann GmbH. 

PROFINET is a registered trademark of PROFIBUS and PROFINET International (PI). Windows is a registered trademark of Microsoft Corporation. 

## **Current patents** 

- US Patent 2017/02111640 (method and apparatus for power saving, fail-safe control of an electromechanical brake), patent pending 

- US Patent 2017/0093230 (system and methof for improved CD power line communication), patent pending US Patent 16,247,478 (method and apparatus for limiting the output voltages of switching mode power supplies), patent pending 

- US Patent 8,154,228 (Dynamic Braking For Electric Motors) 

- US Patent 8,214,063 (Auto-tune of a Control System Based on Frequency Response) US Patent 10.374.468 (System and method for improved DC power line communication) 

Patents referring to fieldbus functions are listed in the matching fieldbus manual. 

## **Technical changes which improve the performance of the device may be made without prior notice!** 

This document is the intellectual property of Kollmorgen. All rights reserved. No part of this work may be reproduced in any form (by photocopying, microfilm or any other method) or stored, processed, copied or distributed by electronic means without the written permission of Kollmorgen. 

AKD2G-S Installation Manual, Safety 1 | Table of Contents 

## **1 Table of Contents** 

|**1 **|**Table of Contents**|**3**|
|---|---|---|
|**2 **|**General**|**9**|
||2.1 About this Installation Manual|10|
||2.2 Using the PDF Format|10|
||2.3 Symbols Used|11|
||2.4 Abbreviations Used|12|
|**3 **|**Product Safety**|**13**|
||3.1 You should pay attention to this|14|
||3.2 Use as Directed|16|
||3.3 Prohibited Use|17|
||3.4 Warning note labels|17|
||3.4.1 Notes placed on the product|17|
||3.4.2 Adhesive label in the package|17|
||3.5 Shock-hazard Protection|18|
||3.5.1 Leakage current|18|
||3.5.2 Residual current protective device (RCD)|18|
||3.5.3 Isolating transformers|18|
||3.6 Stop / Emergency Stop / Emergency Off|19|
||3.6.1 Stop|19|
||3.6.2 Emergency Stop|20|
||3.6.3 Emergency Off|20|
|**4 **|**Product life cycle handling**|**21**|
||4.1 Transport|22|
||4.2 Packaging|22|
||4.3 Storage|22|
||4.4 Installation, setup and normal operation|23|
||4.5 Decommissioning|23|
||4.6 Maintenance and cleaning|23|
||4.7 Disassembly|23|
||4.8 System Repair|24|
||4.9 Disposal|24|
|**5 **|**Package**|**25**|
||5.1 Package Supplied|26|
||5.2 Nameplate|26|
||5.3 Part Number Scheme|27|
|**6 **|**Technical description and data**|**28**|
||6.1 The AKD2G Family of Digital Drives|29|
||6.2 Ambient Conditions, Ventilation, and Mounting Position|31|
||6.3 Mechanical Data|31|
||6.4 Performance Data|32|
||6.5 Electrical data|33|
||6.5.1 Single axis variants (S)|33|
||6.5.1.1 Mains supply data, 1 phase AC, type AKD2G-Sxx- (S)|33|
||6.5.1.2 Mains supply data, 3 phase AC, type AKD2G-Sxx- (S)|33|
||6.5.1.3 Mains supply data, DC, type AKD2G-Sxx- (S)|33|
||6.5.1.4 Auxiliary voltage input data, 24VDC, type AKD2G-Sxx- (S)|33|
||6.5.1.5 Output data, type AKD2G-Sxx- (S)|34|
||6.5.2 Dual axis variants (D: I1=I2)|35|
||6.5.2.1 Mains supply data, 1 phase AC, type AKD2G-Sxx- (D)|35|
||6.5.2.2 Mains supply data, 3 phase AC, type AKD2G-Sxx- (D)|35|



AKD2G-S Installation Manual, Safety 1 | Table of Contents 

||6.5.2.3 Mains supply data, DC, type AKD2G-Sxx- (D)|35|
|---|---|---|
||6.5.2.4 Auxiliary voltage input data, 24VDC, type AKD2G-Sxx- (D)|35|
||6.5.2.5 Output data, type AKD2G-Sxx- (D)|36|
||6.6 Electrical Motor Braking|37|
||6.6.1 Dynamic Braking|37|
||6.6.2 Regeneration braking|37|
||6.6.2.1 Functional description|37|
||6.6.2.2 Technical data for AKD2G-Sxx-6V|38|
||6.6.2.3 Technical data for AKD2G-Sxx-7V|38|
||6.7 LCD Display and Push-buttons (B1, B2)|39|
||6.8 SD Card Slot|41|
|**7 **|**Mechanical Installation**|**42**|
||7.1 Important Notes|43|
||7.2 Guide to Mechanical Installation|43|
||7.3 Dimensions|44|
|**8 **|**Electrical Installation**|**45**|
||8.1 Important Notes|46|
||8.2 Guide to electrical installation|47|
||8.3 Wiring|48|
||8.3.1 General|48|
||8.3.2 Mating connectors|48|
||8.3.3 Cable and Wire Requirements|49|
||8.3.3.1 Cable material|49|
||8.3.3.2 Cable Length|49|
||8.3.3.3 T-Connector wiring|49|
||8.3.3.4 Cable cross sections and requirements|50|
||8.3.4 Protective Earth connection|51|
||8.4 EMI Noise Reduction|52|
||8.4.1 Recommendations for EMI noise reduction|52|
||8.4.2 Shielding with external shielding busbar|53|
||8.4.2.1 Shielding Concept|53|
||8.4.2.2 Shielding Busbar|54|
||8.4.3 Shielding connection to the drive|55|
||8.4.3.1 Shielding Concept|55|
||8.4.3.2 Grounding plates and shield connection clamps|56|
||8.4.3.3 Motor connector X1/X2 with shielding connection|56|
||8.5 Connection Overview|57|
||8.5.1 Connector Position AKD2G-Sxx-6V|57|
||8.5.2 Connector Position AKD2G-Sxx-7V|58|
||8.5.3 Wiring overview, single axis drive|59|
||8.5.4 Wiring overview, dual axis drive|60|
||8.5.5 Connector pin assignments|61|
||8.5.5.1 X1 and X2: Motor, Brake, Feedback 1|61|
||8.5.5.2 X3: Mains, regen resistor, DC-Bus|61|
||8.5.5.3 X10: 24 VDC|62|
||8.5.5.4 X11, X12: Motion Bus|62|
||8.5.5.5 X13, X14: CAN bus (optional)|62|
||8.5.5.6 X20: Service|62|
||8.5.5.7 X21: I/O, Feedback 4|63|
||8.5.5.8 X22: I/O extended, EEO2, Feedback 5|64|
||8.5.5.9 X23: Feedback 3, EEO1, I/O|65|
||8.5.5.10 X41: SFA Feedback converter, EEO3/EEO4 (accessory)|66|
||8.6 Power and Logic Voltage Supply (X3/X10)|67|
||8.6.1 Mains power supply (X3)|67|



AKD2G-S Installation Manual, Safety 1 | Table of Contents 

|8.6.1.1 Wiring examples mains power supply|68|
|---|---|
|8.6.1.2 Fusing|71|
|8.6.2 Auxiliary voltage power supply 24 VDC (X10)|76|
|8.6.2.1 Fusing|76|
|8.6.2.2 Wiring example 24 VDC supply|76|
|8.7 DC Bus link (X3)|77|
|8.7.1 Fusing|77|
|8.7.2 Wiring example with T connectors|78|
|8.7.3 Wiring example with busbar|78|
|8.8 External Regen resistor (X3)|79|
|8.8.1 Fusing and Wiring|79|
|8.9 Motor Power, Brake and Feedback connection|80|
|8.9.1 Motor connectivity, some examples|80|
|8.9.2 Motor single cable connection|81|
|8.9.2.1 Motor Power, Brake and Feedback connectors X1, X2|81|
|8.9.2.2 Feedback connectors X21, X22, X23|82|
|8.9.3 Motor dual cable connection|83|
|8.9.3.1 Motor power and motor brake connectors X1, X2|84|
|8.9.3.2 Feedback connectors X1, X2, X41, X21, X22, X23|84|
|8.9.4 Motor Holding Brake Connection|85|
|8.9.5 Feedback Connection|87|
|8.9.5.1 Feedback Connector X1, X2|88|
|8.9.5.2 Feedback Connector X21|89|
|8.9.5.3 Feedback Connector X22|90|
|8.9.5.4 Feedback Connector X23|91|
|8.9.5.5 Feedback Connector X41 (SFA, accessory)|92|
|8.10 Electronic Gearing, EEO, Master-Slave|93|
|8.10.1 Electronic Gearing|93|
|8.10.2 Emulated Encoder Output (EEO)|94|
|8.10.3 Master-Slave control|96|
|8.10.3.1 Master-Slave using X22|96|
|8.10.3.2 Master-Slave using optional X23 or X41|96|
|8.11 Motion Bus Interface (X11/X12)|97|
|8.11.1 EtherCAT®|97|
|8.12 CAN-Bus Interface (X13/X14)|99|
|8.12.1 CAN-Bus Topology|99|
|8.12.2 CAN-Bus Wiring|100|
|8.12.3 Baud rate for CAN-Bus|101|
|8.12.4 Node Address for CAN-Bus|101|
|8.12.5 CAN-Bus Termination|101|
|8.13 Service Interface (X20)|102|
|8.13.1 Possible Network Configurations|102|
|8.14 I/O Connection (X21/X22/X23)|103|
|8.14.1 Pinout|103|
|8.14.2 Technical data|104|
|8.14.3 Analog Input|105|
|8.14.4 Analog Output|106|
|8.14.5 Digital Inputs|107|
|8.14.5.1 Digital-In 1 and 2|107|
|8.14.5.2 Digital-In 3 to 12|108|
|8.14.5.3 Digital-In/Out 1 and 2|109|
|8.14.5.4 Digital-In/Out 3 to 6|110|
|8.14.6 Digital Outputs|111|
|8.14.6.1 Digital-Out 1 to 6|111|



AKD2G-S Installation Manual, Safety 1 | Table of Contents 

|8.14.6.2 Digital-Out 7 and 8|112|
|---|---|
|8.14.6.3 Digital-In/Out 1 and 2|113|
|8.14.6.4 Digital-In/Out 3 to 6|113|
|8.14.6.5 Digital-Out 9, Relay contacts|114|
|**9 Setup**|**115**|
|9.1 Important Notes|116|
|9.2 Guide to drive setup|117|
|9.2.1 Initial Drive Test Procedure|117|
|9.2.1.1 Unpacking, mounting, and wiring the AKD2G|117|
|9.2.1.2 Minimum wiring for drive test without load, example|117|
|9.2.1.3 Confirm connections (example: directly to PC)|118|
|9.2.1.4 System integration|118|
|9.2.1.5 Install and start WorkBench|119|
|9.2.1.6 Setup the axis in WorkBench|119|
|9.2.1.7 Enable the axis (Hardware)|119|
|9.2.1.8 Move the motor axis|119|
|9.2.1.9 Tune the axis|119|
|9.2.2 Setup software WorkBench|120|
|9.2.2.1 Use as directed|120|
|9.2.2.2 Software description|121|
|9.2.2.3 Hardware requirements|121|
|9.2.2.4 Operating systems|121|
|9.2.2.5 Installation under Windows 7/8/10|122|
|9.3 Switch-On and Switch-Off Behavior|123|
|9.3.1 Switch-on behavior in standard operation|124|
|9.3.2 Switch-off behavior|124|
|9.4 Fault and Warning Messages|125|
|9.4.1 Fault and warning messages AKD2G|125|
|9.5 Troubleshooting|126|
|**10 Functional Safety**|**127**|
|10.1 General notes|128|
|10.1.1 Use as directed|129|
|10.1.2 Prohibited use|129|
|10.1.3 Abbreviations used for functional safety|129|
|10.1.4 Enclosure, wiring|130|
|10.2 Settings|131|
|10.3 Safety Function Option 1 (I/O, SIL2 PLd)|132|
|10.3.1 Technical Data|133|
|10.3.2 Safety Properties Overview|133|
|10.3.3 STO (Safe Torque Off)|134|
|10.3.3.1 Important Notes|134|
|10.3.3.2 Activation|134|
|10.3.3.3 Restart|135|
|10.3.3.4 Timing|136|
|10.3.3.5 Safety Diagnostic view in WorkBench|136|
|10.3.3.6 Fault Reaction / Failure Messages|137|
|10.4 Verification|137|
|10.5 Safety Faults, Safety Warnings|138|
|10.5.1 Drive LCD Display|138|
|10.5.2 Drive Safety Faults|139|
|10.5.3 Drive Safety Warnings|139|
|10.5.4 Troubleshooting safety functionality|139|
|10.6 Functional Safety Keyword Reference Guide|140|
|10.6.1 AXIS#.SAFE.STO Keywords|141|



AKD2G-S Installation Manual, Safety 1 | Table of Contents 

||10.6.1.1 AXIS#.SAFE.STO.ACTIVE|141|
|---|---|---|
|D**e** **s**c**r**ip**t**io n<br>Co**n**t**e**x<br>V<br>r io n s<br>G<br>a lIn fo rma tio n||**1** **4** **1**|
||10.6.1.2 AXIS#.SAFE.STO.A|142|
|D**e** **s**c**r**ip**t**io n<br>Co**n**t**e**x<br>V<br>r io n s<br>G<br>a lIn fo rma tio n||**1** **4** **2**|
||10.6.1.3 AXIS#.SAFE.STO.B|142|
|D**e** **s**c**r**ip**t**io n<br>Co**n**t**e**x<br>V<br>r io n s<br>G<br>a lIn fo rma tio n||**1** **4** **2**|
||10.6.1.4 AXIS#.SAFE.STO.REPORTFAULT|143|
|D**e** **s**c**r**ip**t**io n<br>Co**n**t**e**x<br>V<br>r io n s<br>G<br>a lIn fo rma tio n||**1** **4** **3**|
|**11 Approvals**||**144**|
||11.1 Conformance with UL/cUL|145|
||11.2 Conformance with European Directives|146|
||11.3 Conformance with RoHS|147|
||11.4 Conformance with REACH|147|
||11.5 Functional Safety approval|147|
||11.6 Conformance with EAC|147|
|**12 Index**||**149**|
|**13 Record of document revisions**||**151**|



AKD2G-S Installation Manual, Safety 1 | 

--- / --- 

AKD2G-S Installation Manual, Safety 1 | 2   General 

## **2 General** 

|**2.1**|**About this Installation Manual**|**10**|
|---|---|---|
|**2.2**|**Using the PDF Format**|**10**|
|**2.3**|**Symbols Used**|**11**|
|**2.4**|**Abbreviations Used**|**12**|



AKD2G-S Installation Manual, Safety 1 | 2   General 

## **2.1 About this Installation Manual** 

This document, the _AKD[®] 2G Installation Manual_ ("Instructions Manual" according to EC Machinery Directive 2006/42/EU), describes the AKD[®] 2G series of digital drives and includes information needed to safely install an AKD2G. 

This document is valid for AKD2G single axis drive or dual axis drive with 110 V to 240 V or 240 V to 480 V mains voltage. 

- Ouput stages: 3 A or 6 A or 12 A rated current 

- Programmability options: Base drive or Position Indexer drive Connectivity options: analog, CANopen, EtherCAT, Ethernet/IP I/O options: Extended I/O (X22), Feedback&EEO (X23) Functional Safety Option: FS1 with STO; SIL2 PLd 

A digital version of this manual (pdf format) is available on the DVD included with your drive. AKD2G information for use consist of: 

- _Product Safety Guide_ : multi-language document with safety information, part of product delivery in Europe, printed on paper DIN A5. 

- _Installation Manual_ : This document, describes the AKD2G series of digital drives and includes information needed to safely install an AKD2G. 

- _WorkBench Online Help_ : describes how to use your drive in common applications. It also provides tips for maximizing your system performance with the AKD2G. The _Online Help_ includes the _Parameter and Command Reference Guide_ which provides information for the parameters and commands used to program the AKD2G. 

- _CAN-BUS Communication_ : describes how to use your drive in CANopen applications. _EtherCAT Communication_ : describes how to use your drive in EtherCAT applications. _Accessories Manual_ : provides information for accessories like cables and regen res- 

- istors used with AKD2G. Regional variants of this manual exist. 

All documents can be downloaded from the Kollmorgen website www.kollmorgen.com. 

## **2.2 Using the PDF Format** 

This document includes several features for ease of navigation 

|**Cross References**<br>~~——~~|Table of contents and index include active cross references.<br>~~——~~|
|---|---|
|**Table of contents and**<br>**index**<br>~~——~~|Lines are active cross references. Click on the line and the appro-<br>priate page is accessed.<br>~~——~~|
|**Page/chapter numbers**<br>**in the text**<br>~~——~~|Page/chapter numbers with cross references are active links.<br>~~——~~|



AKD2G-S Installation Manual, Safety 1 | 2   General 

## **2.3 Symbols Used** 

## **Warning Symbols** 

|**Warning Symbols**||
|---|---|
|**Symbol**|**Indication**<br>Indicates a hazardous situation which, if not avoided, will result<br>in death or serious injury.|
|(VAWARNING|Indicates a hazardous situation which, if not avoided, could res-<br>ult in death or serious injury.<br>(VAWARNING|
||Indicates a hazardous situation which, if not avoided, could res-<br>ult in minor or moderate injury.|
|NOTESC<br>a|Indicates situations which, if not avoided, could result in prop-<br>erty damage.<br>SC|
|NOTESC<br>aNe<br>A|This symbol indicates important notes.<br>SC<br>~~ee~~|
|NOTESC<br>aNe<br>A|Warning of a danger (general). The type of danger is specified<br>by the text next to the symbol.<br>SC<br>~~ee~~|
|NOTE SC<br>a Ne<br>A<br>y<br>JAN<br>A|Warning of danger from electricity and its effects.<br>SC<br>~~ee~~<br>ee|
|A <br>An|Warning of danger from hot surface.<br> ee|
|A<br>A=<br>N|Warning of danger from suspended loads.|
|IN<br>LON|Warning of danger from automatic start.<br>|



## **Drawing symbols** 

**==> picture [392 x 207] intentionally omitted <==**

**----- Start of picture text -----**<br>
Symbol Description Symbol Description<br>Signal ground Diode<br>ee ee ee<br>Chassis ground Relay<br>ml FLL | GO<br>Protective earth Relay switch off delayed<br>©)j|wml |<br>Resistor Normally open contact<br>Fuse Normally closed contact<br>State-of-the-art firewall EMC filter<br>**----- End of picture text -----**<br>


AKD2G-S Installation Manual, Safety 1 | 2   General 

## **2.4 Abbreviations Used** 

Abbreviations related to functional safety (➜ # 129). 

|**Abbreviation**<br>(➜# 53)|**Meaning**<br>"see page 53" in this document|
|---|---|
|➜xyz|"see chapter xyz" in this document|
|Ω|Ohms|
|A#, AXIS#|A# or AXIS# are placeholders for the axis number. Used with keywords or<br>signal names|
|AGND|Analog ground|
|AMSL|Above mean sea level|
|Axis|Depends on context, either one AKD2G output stage or one load axis of the<br>full motion system.|
|CAT|Category|
|CE|Communité Européenne|
|COM|Serial interface for a personal computer|
|DGND|Digital ground|
|EEPROM|Electrically erasable programmable memory|
|EEO|Emulated Encoder Output|
|EMC|Electromagnetic compatibility|
|EMF|Electromagnetic force|
|FS1, FS2, FS3|Functional Safety Option 1, 2, 3|
|FSoE|Fail safe over EtherCAT|
|KAS|Kollmorgen Automation Suite|
|KAS IDE|Setup software (Kollmorgen Automation Suite Integrated Development<br>Environment)|
|KDN|Kollmorgen Developer Network|
|LED|Light-emitting diode|
|LSB|Low significant byte (or bit)|
|MSB|Main significant byte (or bit)|
|NI|Zero pulse|
|OSSD|Output Signal Switching Device|
|PC|Personal computer|
|PE|Protective earth|
|PELV|Protective Extra Low Voltage|
|PLC|Programmable logic control|
|PWM|Pulse-width modulation|
|RAM|Random access memory (volatile memory)|
|RBrake/RB|Regen resistor (also called a brake resistor)|
|RBext|External regen resistor|
|RBint|Internal regen resistor|
|RCD|Residual current device|
|RES|Resolver|
|S1|Continuous operation|
|tbd|To be determined (in process)|
|VAC|Volts, alternating current|
|VDC|Volts, direct current|



AKD2G-S Installation Manual, Safety 1 | 3   Product Safety 

## **3 Product Safety** 

|**3.1**|**You should pay attention to this**|**14**|
|---|---|---|
|**3.2**|**Use as Directed**|**16**|
|**3.3**|**Prohibited Use**|**17**|
|**3.4**|**Warning note labels**|**17**|
|**3.5**|**Shock-hazard Protection**|**18**|
|**3.6**|**Stop / Emergency Stop / Emergency Off**|**19**|



AKD2G-S Installation Manual, Safety 1 | 3   Product Safety 

## **3.1 You should pay attention to this** 

This section helps to recognize risks and avoid dangers to people and objects. 

## **Specialist staff required!** 

Only properly qualified personnel are permitted to perform such tasks as transport, installation and setup. Qualified specialist staff are persons with expertise in transport, installation, assembly, commissioning and operation of electrotechnical equipment. 

Transport, storage, unpacking: only by personnel with knowledge of handling electrostatically sensitive components. 

- Mechanical installation: only by personnel with mechanical expertise. Electrical installation: only by personnel with expertise in electrical engineering. Basic tests / setup: only by personnel with expertise in electrical engineering and drive technology. 

The qualified personnel must know and observe ISO 12100 / IEC 60364 / IEC 60664 and national accident prevention regulations. 

## **Read the documentation!** 

Read the available documentation before installation and commissioning. Improper handling of the devices can cause harm to people or damage to property. The operator of systems using the drive system must ensure that all personnel who work with the drive read and understand the manual before using the drive. 

## **Check Hardware Revision!** 

Check the Hardware Revision Number of the product (see product label). This number is the link between your product and the manual. The product Hardware Revision Number must match the Hardware Revision Number on the cover page of the manual. 

## **Pay attention to the technical data!** 

Adhere to the technical data and the specifications on connection conditions. If permissible voltage values or current values are exceeded, the devices can be damaged. Unsuitable motor or wrong wiring will damage the system components. Check the combination of drive and motor. Compare the rated voltage and current of the units. 

## **Perform a risk assessment!** 

The manufacturer of the machine must generate a risk assessment for the machine, and take appropriate measures to ensure that unforeseen movements cannot cause injury or damage to any person or property. Additional requirements on specialist staff may also result from the risk assessment. 

## **Automatic restart** 

The drive might restart automatically after power on, voltage dip or interruption of the supply voltage, depending on the parameter setting. Risk of death or serious injury for humans working in the machine. 

If the parameter AXIS#.ENDEFAULT is set to 1, then place a warning sign to the machine (Warning: Automatic Restart at Power On) and ensure, that power on is not possible, while humans are in a dangerous zone of the machine. In case of using an undervoltage protection device, you must observe EN 60204-1:2006 chapter 7.5 . 

**ATTENTION** : The drive is ready to operate with pre-configured STO function. 

AKD2G-S Installation Manual, Safety 1 | 3   Product Safety 

## **Observe electrostatically sensitive components!** 

The devices contain electrostatically sensitive components which may be damaged by incorrect handling. Electrostatically discharge your body before touching the device. Avoid contact with highly insulating materials (artificial fabrics, plastic film etc.). Place the device on a conductive surface. 

## **Hot surface!** 

Drives may have hot surfaces during operation. The housing can reach temperatures above 80°C. Risk of minor burns! Measure the temperature, and wait until the housing has cooled down below 40 °C before touching it. 

## **Earthing!** 

It is vital that you ensure that the drive is safely earthed to the PE (protective earth) busbar in the switch cabinet. Risk of electric shock. Without low-resistance earthing no personal protection can be guaranteed. 

## **Leakage Current!** 

Since the leakage current to PE is more than 3.5 mA, in compliance with IEC61800-5-1 the PE connection must either be doubled or a connecting cable with a cross-section >10 mm² must be used. Deviating measures according to regional standards might be possible. 

## **High voltages!** 

The equipment produces high electric voltages up to 900 V. Lethal danger exists at live parts of the device. Do not open or touch the equipment during operation. Keep all covers and cabinet doors closed. Built-in protection measures such as insulation or shielding may not be removed. Work on the electrical installation may only be performed by trained and qualified personnel, in compliance with the regulations for safety at work, and only with switched off mains supply, and secured against restart. 

Never undo any electrical connections to the drive while it is live. There is a danger of electrical arcing with damage to contacts and personal injury. Wait at least 5 minutes after disconnecting the drive from the main supply power before touching potentially live sections of the equipment (such as contacts) or removing any connections. 

Always measure the voltage in the DC bus link and wait until the voltage is below 50 V before handling components. 

## **Functional Safety!** 

The assessment of the safety functions according to EN13849 or EN 62061 must finally be done by the user. 

## **Reinforced Insulation** 

Thermal sensors, motor holding brakes and feedback systems built into the connected motor must have reinforced insulation (according to IEC61800-5-1) against system components with power voltage, according to the required application test voltage. All Kollmorgen components meet these requirements. 

## **Never modify the drive!** 

It is not allowed to modify the drive hardware without permission by the manufacturer. Opening the housing causes loss of warranty. 

AKD2G-S Installation Manual, Safety 1 | 3   Product Safety 

## **3.2 Use as Directed** 

The AKD2G drives are exclusively intended for driving suitable synchronous servomotors with closed-loop control of torque, speed, and/or position. 

AKD2G are components that are built into electrical plants or machines and can only be operated as integral components of these plants or machines. The manufacturer of the machine used with a drive must generate a risk assessment for the machine. When the drives are built into machines or plant, the drive must not be used until it has been established that the machine or plant fulfills the requirements of the regional directives. 

## **Cabinet and wiring** 

Drives must only be operated in a closed control cabinet suitable for the ambient conditions (➜ # 31). Ventilation or cooling may be necessary to keep the temperature within the cabinet below 40 °C or 60 °C if using extended range operation with derating. 

Use only copper conductors for wiring. The conductor cross-sections can be derived from the standard IEC 60204 (alternatively for AWG cross-sections: NEC Table 310-16, 75 °C column). 

## **Power supply** 

The drives can be supplied by 1, 2 or 3 phase or DC industrial supply networks. 

Drives in the AKD2G series can be supplied as follows: 

- AKD2G-Sxx-6Vxx: 

- 1, 2 or 3 phase industrial supply networks (not more than 10 kA symmetrical rated current at 120 V and 240 V) or DC supply. 

- AKD2G-Sxx-7Vxx: 

- 3 phase industrial supply networks (not more than 42 kA symmetrical rated current at 240 V, 400 V and 480 V) or DC supply. 

Connection to other voltage types of supply networks is possible with an additional isolating transformer. 

Repeated overvoltages between phases (L1, L2, L3) and the housing of the drive must not exceed 1000 V peak. In accordance with IEC 61800, voltage spikes (< 50 µs) between phases must not exceed 1000 V. Voltage spikes (< 50 µs) between a phase and the housing must not exceed 2000 V. 

EMC filter measures for AKD2G-Sxx-6Vxx must be implemented by the user. Refer to the regional Accessories Manual for recommended filter types. 

## **Motor voltage rating** 

The rated voltage of the motors must be at least as high as the DC bus link voltage divided by √2 produced by the drive (UnMotor>=UDC/√2). 

## **Functional Safety** 

Beta drives: Safety functions are neither approved nor certified yet. Do not use this functionality in applications with functional safety request until further notice. 

- The network, to which the drive is connected, must be secured according to state-of-theart information technology security requirements. 

- The user IT specialists shall analyze whether further security requirements are applicable to ensure functional safety. 

Review the chapter "Use as Directed" in the Functional Safety section (➜ # 127) before using safety functionality. 

AKD2G-S Installation Manual, Safety 1 | 3   Product Safety 

## **3.3 Prohibited Use** 

Other use than that described in chapter “Use as directed” is not intended and can lead to personnel injuries and equipment damage. The drive may not be used with a machine that does not comply with appropriate national directives or standards. The use of the drive in the following environments is also prohibited: 

- potentially explosive areas 

- environments with corrosive and/or electrically conductive acids, alkaline solutions, oils, vapors, dusts 

- ships or offshore applications 

The drive must not be connected directly to the Internet. If the network, to which the drive is connected, is not secured according to state-of-the-art information technology, this could be a functional safety risk. 

## **3.4 Warning note labels** 

## **3.4.1 Notes placed on the product** 

**==> picture [92 x 102] intentionally omitted <==**

**----- Start of picture text -----**<br>
AKD2G<br>Wait 5 minutes<br>after removing power<br>before servicing.<br>**----- End of picture text -----**<br>


## **3.4.2 Adhesive label in the package** 

- Follow the instructions given on the adhesive labels in the package. If a warning note label is damaged, it must be replaced immediately. 

AKD2G-S Installation Manual, Safety 1 | 3   Product Safety 

## **3.5 Shock-hazard Protection** 

## **3.5.1 Leakage current** 

Leakage current via the PE conductor results from the combination of equipment and cable leakage currents. The leakage current frequency pattern includes a number of frequencies, whereby the residual-current circuit breakers definitively evaluate the 50 Hz current. For this reason, the leakage current cannot be measured using a conventional multimeter. Contact our application department for help to calculate the leakage current in your application. 

Since the leakage current to PE is more than 3.5 mA, in compliance with IEC61800-5-1 the PE connection must either be doubled or a connecting cable with a cross-section >10 mm² must be used. Use the PE terminal and the PE connection screws in order to fulfill this requirement. 

The following measures can be used to minimize leakage currents: 

Reduce the length of the engine cable. Use low capacitance motor cables (➜ # 49). 

## **3.5.2 Residual current protective device (RCD)** 

In conformity with IEC 60364-4-41 – Regulations for installation and IEC 60204 – Electrical equipment of machinery, residual current protective devices (RCDs) can be used provided the requisite regulations are complied with. The AKD2G is a 3-phase system with a B6 bridge. Therefore, RCDs which are sensitive to all currents must be used in order to detect any DC fault current. 

Rated residual currents in the RCDs: 

|**10 to 30 mA**|Protection against "indirect contact" (personal fire protection) for stationary<br>and mobile equipment, as well as for "direct contact".|
|---|---|
|**50 to 300 mA**|Protection against "indirect contact" (personal fire protection) for stationary<br>equipment|



Recommendation: In order to protect against direct contact (with motor cables shorter than 5 m) Kollmorgen recommends that each drive be protected individually using a 30 mA RCD which is sensitive to all currents. 

If you use a selective RCD, the more intelligent evaluation process will prevent spurious tripping of the RCD. 

## **3.5.3 Isolating transformers** 

When protection against indirect contact is absolutely essential despite a higher leakage current, or when an alternative form of shock-hazard protection is sought, the AKD2G can also be operated via an isolating transformer. A ground-leakage monitor can be used to monitor for short circuits. 

Keep the length of wiring between the transformer and the drive as short as possible. 

AKD2G-S Installation Manual, Safety 1 | 3   Product Safety 

## **3.6 Stop / Emergency Stop / Emergency Off** 

The control functions Stop, Emergency Stop and Emergency Off are defined by IEC 60204. Notes for functional safety aspects of these functions can be found in ISO 13849 and IEC 62061. 

The parameter AXIS#.DISMODE must be set to implement the different stop categories for software disabling. Consult the _WorkBench Online Help_ for configuring the parameter. 

## **Vertical load could fall!** 

Serious injury could result when the load is not properly blocked. With vertical load the load could fall. 

- Functional safety with hanging load (vertical axes), requires an additional mechanical brake which must be safely operated, for example by a safety control. 

- Set parameter AXIS#.MOTOR.BRAKEIMM to 1 with vertical axes, to apply the motor holding brake (➜ # 85) immediately after faults or Hardware Disable. 

- Risk assessment of the application determines the necessary measures. 

## **3.6.1 Stop** 

The stop function shuts down the machine in normal operation. The stop function is defined by IEC 60204. 

The Stop Category must be determined by a risk evaluation of the machine. 

Stop function must have priority over assigned start functions. The following stop categories are defined: 

## **Stop Category 0** 

Shut-down by immediate switching-off the energy supply to the drive machinery (this is an uncontrolled shut-down). 

For stop without using safety functions like STO, set AXIS#.DISMODE to 0. The safety function STO stops the drive as required by Stop Category 0 (IEC 62061). 

## **Stop Category 1** 

A controlled shut-down, whereby the energy supply to the drive machinery is maintained to perform the shut-down, and the energy supply is only interrupted when the shut-down has been completed. 

For stop without using safety functions like SS1, set AXIS#.DISMODE to 2. The safety function SS1 stops the drive as required by Stop Category 1 (IEC 62061). 

## **Stop Category 2** 

A controlled shut-down, whereby the energy supply to the drive machinery is maintained. This category shall be realized with a safety function like SS2. Safety function SS2 stops the drive as required by Stop Category 2 (IEC 62061). 

Stop Category 0 and Stop Category 1 stops must be operable independently of the operating mode, whereby a Category 0 stop must have priority. 

If necessary, provision must be made for the connection of protective devices and lock-outs. If applicable, the stop function must signal its status to the control logic. A reset of the stop function must not create a hazardous situation. 

AKD2G-S Installation Manual, Safety 1 | 3   Product Safety 

## **3.6.2 Emergency Stop** 

The Emergency Stop function is used for the fastest possible shutdown of the machine in a dangerous situation. The Emergency Stop function is defined by IEC 60204. Principles of emergency stop devices and functional aspects are defined in ISO 13850. 

The Emergency Stop function will be triggered by the manual actions of a single person. It must be fully functional and available at all times. The user must understand instantly how to operate this mechanism (without consulting references or instructions). 

- The Stop Category for the Emergency Stop must be determined by a risk evaluation of the machine. 

In addition to the requirements for stop, the Emergency Stop must fulfill the following requirements: 

- Emergency Stop must have priority over all other functions and controls in all operating modes. 

- The energy supply to any drive machinery that could cause dangerous situations must be switched off as fast as possible, without causing any further hazards ( Stop Category 0) or must be controlled in such a way, that any movement that causes danger, is stopped as fast as possible (Stop Category 1). 

- The reset must not initiate a restart. 

## **3.6.3 Emergency Off** 

The Emergency Off function is used to switch-off the electrical power supply of the machine. This is done to prevent users from any risk from electrical energy (for example electrical impact). Functional aspects for Emergency Off are defined in IEC 60364-5-53. 

The Emergency Off function will be triggered by the manual actions of a single person. 

- The result of a risk evaluation of the machine determines the necessity for an Emergency Off function. 

Emergency Off is done by switching off the supply energy by electro-mechanical switching devices. This results in a category 0 stop. If this stop category is not possible in the application, then the Emergency Off function must be replaced by other measures (for example by protection against direct touching). 

AKD2G-S Installation Manual, Safety 1 | 4   Product life cycle handling 

## **4 Product life cycle handling** 

|**4.1**|**Transport**|**22**|
|---|---|---|
|**4.2**|**Packaging**|**22**|
|**4.3**|**Storage**|**22**|
|**4.4**|**Installation, setup and normal operation**|**23**|
|**4.5**|**Decommissioning**|**23**|
|**4.6**|**Maintenance and cleaning**|**23**|
|**4.7**|**Disassembly**|**23**|
|**4.8**|**System Repair**|**24**|
|**4.9**|**Disposal**|**24**|



AKD2G-S Installation Manual, Safety 1 | 4   Product life cycle handling 

## **4.1 Transport** 

Transport the AKD2G in accordance with IEC 61800-2 as follows: 

- Transport only by qualified personnel in the manufacturer’s original recyclable packaging. **NOTICE:** Avoid shocks while transporting. 

- Vibration/Shock: AKD2G is tested for environmental class 2M1 of IEC 60721-3-2. 

- Store at or below maximum stacking height 8 cartons (see "Storage" (➜ # 22)) 

- Transport only within specified temperature ranges: 

- -25 to +70 °C, max. rate of change 20 K/hour, class 2K3. 

- Transport only within specified humidity: 

- max. 95% relative humidity at +40°C, no condensation, class 2K3. 

The drives contain electrostatically sensitive components that can be damaged by incorrect handling. Electrostatically discharge yourself before touching the drive. Avoid contact with highly insulating materials, such as artificial fabrics and plastic films. Place the drive on a conductive surface. 

If the packaging is damaged, check the unit for visible damage. Inform the shipper and the manufacturer of any damage to the package or product. 

## **4.2 Packaging** 

The AKD2G packaging consists of recyclable cardboard with inserts and a label on the outside of the box. 

|**Model**<br>AKD2G-Sxx-6V03 to 6V12|**Package**<br>**(mm) HxWxL**<br>158 x 394 x 292|**Total Weight**<br>**(kg)**<br>4.2|
|---|---|---|
|AKD2G-Sxx-7V03 to 7V12|158 x 394 x 292|4.3|



Mating connectors are **not** included in the package of a standard drive. Mating connectors are included when the drive is ordered with accessories (append “-A” to the model number). 

## **4.3 Storage** 

Store the AKD2G in accordance with IEC 61800-2 as follows: 

- Store only in the manufacturer’s original recyclable packaging. 

- Store at or below maximum stacking height 8 cartons. 

- Store only within specified temperature ranges: -25 to +55 °C, max.rate of change 20 K/hour, class 1K4. 

- Storage only within specified humidity: 5 to 95% relative humidity, no condensation, class 1K3. 

- Store in accordance with the following duration requirements: Less than 1 year: without restriction. 

   - More than 1 year: capacitors must be re-formed before setting up and operating the drive. Re-forming procedures are described in the KDN (Forming). 

AKD2G-S Installation Manual, Safety 1 | 4   Product life cycle handling 

## **4.4 Installation, setup and normal operation** 

Installation and setup information are given in this manual: 

- Mechanical installation (➜ # 42) 

- Electrical installation (➜ # 45) 

- Setup (➜ # 115) 

Normal operation tested for environmental class 3K3 according to IEC 61800-2 (➜ # 31). The manufacturer of the machine defines the necessary end user expertise based on the risk assessment for the machine and describes the requirements for normal operation based on the application. 

## **4.5 Decommissioning** 

Only professional staff who are qualified in electrical engineering are allowed to decommission parts of the system. 

## **DANGER** : Lethal Voltages! 

There is a danger of serious personal injury or death by electrical shock or electrical arcing. 

- Switch off the main switch of the switchgear cabinet. 

- Secure the system against restarting. 

- Block the main switch. 

- Wait at least 5 minutes after disconnecting. 

## **4.6 Maintenance and cleaning** 

The device does not require maintenance. Opening the device voids the warranty. The inside of the unit can only be cleaned by the manufacturer. 

Do not immerse or spray the device. Avoid that liquid enters the device. 

To clean the device exterior: 

1. Decommission the device (see chapter 4.5 "Decommissioning"). 

2. Casing: Clean with isopropanol or similar cleaning solution. **Caution** : Highly Flammable! Risk of injury by explosion and fire. 

   - Observe the safety notes given on the cleaning liquid package. 

   - Wait at least 30 minutes after cleaning before putting the device back into operation. 

3. Protective grill on fan: Clean with a dry brush. 

## **4.7 Disassembly** 

Only professional staff who are qualified in electrical engineering are allowed to disassemble parts of the system. 

1. Decommission the device (see chapter 4.5 "Decommissioning"). 

2. Check temperature. 

**CAUTION** : High Temperature! Risk of minor burns. During operation, the heat sink of the drive may reach temperatures above 80 °C (176 °F). Before touching the device, check the temperature and wait until it has cooled below 40 °C (104 °F). 

3. Remove the connectors. Disconnect the potential earth connection last. 

4. Demount: loosen the fastening screws. Remove the device. 

AKD2G-S Installation Manual, Safety 1 | 4   Product life cycle handling 

## **4.8 System Repair** 

Only professional staff who are qualified in electrical engineering are allowed to exchange parts of the drive system. 

**CAUTION** : Automatic Start! During replacement work a combination of hazards and multiple episodes may occur. 

- Work on the electrical installation may only be performed by trained and qualified personnel, in compliance with the regulations for safety at work, and only with use of prescribed personal safety equipment. 

## **Exchange of the device** 

Only the manufacturer can repair the device. Opening the device voids the warranty. 

1. Decommission the device (see chapter 4.5 "Decommissioning"). 

2. Demount the device (see chapter 4.7 "Disassembly"). 

3. Send the device to the manufacturer. 

4. Install a new device as described in this manual. 

5. Setup the system as described in this manual. 

## **Exchange of other drive system parts** 

If parts of the drive system ( for example cables) must be replaced, proceed as follows: 

1. Decommission the device (see chapter 4.5 "Decommissioning"). 

2. Exchange the parts. 

3. Check all connections for correct fastening. 

4. Setup the system as described in this manual. 

## **4.9 Disposal** 

To dispose the unit properly, contact a certified electronic scrap disposal merchant. 

In accordance with the WEEE-2012/19/EU guideline and similar, the manufacturer accepts returns of old devices and accessories for professional disposal. Transport costs are the responsibility of the sender. 

Contact Kollmorgen and clarify the logistics. 

Send the devices in the original packaging to the manufacturer address: 

|**North America**<br>**KOLLMORGEN**<br>201 West Rock Road<br>Radford, VA 24141, USA|**South America**<br>**KOLLMORGEN**<br>Avenida João Paulo Ablas, 2970<br>Jardim da Glória, Cotia – SP<br>CEP 06711-250, Brazil|
|---|---|
|**Europe**|**Asia**|
|**KOLLMORGEN Europe GmbH**<br>Pempelfurtstr. 1<br>40880 Ratingen, Germany|**KOLLMORGEN**<br>Room 302, Building 5, Lihpao Plaza,<br>88 Shenbin Road, Minhang District,<br>Shanghai, China.|



AKD2G-S Installation Manual, Safety 1 | 5   Package 

## **5 Package** 

|**5.1**|**Package Supplied**|**26**|
|---|---|---|
|**5.2**|**Nameplate**|**26**|
|**5.3**|**Part Number Scheme**|**27**|



AKD2G-S Installation Manual, Safety 1 | 5   Package 

## **5.1 Package Supplied** 

When a standard drive from the AKD2G series is delivered, the following items are included in the drive package: 

   - AKD2G 

   - Printed copy of _AKD[®] 2G Product Safety Guide_ . 

   - DVD with WorkBench setup software . 

   - Panel safety label 

   - **ATTENTION** : Drive is ready to operate with pre-configured STO function. 

- Mating connectors are **not** included in the package of a standard drive. 

- Mating connectors are included when the drive is ordered with accessories (append “-A” to the model number). 

Mating connectors listed below are never delivered with the drive. These mating connectors are usually part of the cables: 

- Motor mating connector (X1, X2), 

- SubD (X23, X41) for Feedback, 

- RJ25 (X13, X14) for CAN-Bus, and 

- RJ45 (X11, X12, X20) for Service and EtherCAT. 

## **Accessories sold separately** 

Accessories must be ordered separately if required, see regional Accessories Manual. 

- EMC filters for mains supply voltage, categories C2 or C3. 

- External regen resistor. 

- Mating connector kits. 

- Motor mating connector. 

- Hybrid cable. Assembled hybrid motor cables are available for all regions. 

- Motor cable. Assembled motor cables are available for all regions. 

- Feedback cable. Assembled feedback cables are available for all regions. 

- SFA (Smart Feedback Adapter) . 

- SDB Module (Safe Dynamic Brake Module). 

- Ethernet service cable. 

## **5.2 Nameplate** 

A nameplate is attached to the side of the drive. The picture below is similar to the nameplate on the device. 

AKD2G-S Installation Manual, Safety 1 | 5   Package 

## **5.3 Part Number Scheme** 

Use the part number scheme for product identification only, not for the order process, because not all combinations of features are possible. 

- Mating connectors are **not** included in the package of a standard drive. 

Mating connectors are included when the drive is ordered with accessories (append “-A” to the model number). 

## **Example AKD2G-SPE-7V06S-A1IO-0000** 

AKD2G IP20 housing, position indexer, EtherCAT, 240 V to 480 V mains supply, 6 A rated current, single axis, Hardware Revision A, dual channel STO SIL2 PLd, with additional I/O connector X22, uncoated, no mating connectors. 

## **Example AKD2G-SPE-6V03D-A1DX-A000-A** 

AKD2G IP20 housing, position indexer, EtherCAT, 120 V to 240 V mains supply, 2 x 3 A rated current, dual axis, Hardware Revision A, dual channel STO SIL2 PLd, with all possible connectors (basis + X23), PCBs coated, with mating connectors. 

AKD2G-S Installation Manual, Safety 1 | 6   Technical description and data 

## **6 Technical description and data** 

|**6.1**|**The AKD2G Family of Digital Drives**|**29**|
|---|---|---|
|**6.2**|**Ambient Conditions, Ventilation, and Mounting Position**|**31**|
|**6.3**|**Mechanical Data**|**31**|
|**6.4**|**Performance Data**|**32**|
|**6.5**|**Electrical data**|**33**|
|**6.6**|**Electrical Motor Braking**|**37**|
|**6.7**|**LCD Display and Push-buttons (B1, B2)**|**39**|
|**6.8**|**SD Card Slot**|**41**|



AKD2G-S Installation Manual, Safety 1 | 6   Technical description and data 

## **6.1 The AKD2G Family of Digital Drives** 

**Available AKD2G-SP (Position Indexer) versions Funct. Connectivity Rated Voltages Current Axis Rev Safety N-** : Analog **6V** : **03** : 3 A **S-** : Single **A 1** : SIL2 **C-** : CANopen 120/240VAC 1~ **06** : 6 A **D-** : Dual I1=I2 STO **E-** : EtherCAT 240VAC 3~ **12** : 12 A **P-*** : PROFINET RT/IRT 170/340 VDC **24*** : 24 A **I-*** : EtherNet/IP **7V** : 240/400/480VAC 3~ 340/565/680 VDC ~~an~~ 

**Funct. Connectivity Rated Voltages Current Axis Rev Safety N-** : Analog **6V** : **03** : 3 A **S-** : Single **A 1** : SIL2 **C-** : CANopen 120/240VAC 1~ **06** : 6 A **D-** : Dual I1=I2 STO **E-** : EtherCAT 240VAC 3~ **12** : 12 A **P-*** : PROFINET RT/IRT 170/340 VDC **24*** : 24 A **I-*** : EtherNet/IP **7V** : 240/400/480VAC 3~ 340/565/680 VDC ~~an~~ **Connector Options for Drives with Functional Safety 1 Single Axis Dual Axis 00** : Basis (X21) **00** : Basis (X21, X22) **IO** : Basis + X22 **F3** : Basis + X23 **F3** : Basis + X23 **DX** : Basis + X22+X23 * Available 2020 **Standard features** Single axis or dual axis in one housing ~~—~~ Supply voltages: DC AC single phase, split phase, three phase AC neutral or leg grounded Single or group supply, single or group mains fusing 

- Motion bus on board, TCP/IP service channel on board 

- SFD3, HIPERFACE DSL motor feedback support on board 

- Support for many conventional motor feedback types 

- Step / Direction input on board 

- Encoder emulation on board 

- Use with synchronous servomotors, linear motors, and induction machines 

## **Power section** 

- Single or three phase AC supply, 5% to 110% of rated AC voltage over 47 to 63 Hz. Connection to higher AC voltage mains only via isolating transformer. DC supply, voltage range 5% to 110% of rated DC voltage. Fusing to be provided by the user. 

- Three phase bridge rectifier, integral soft-start circuit. 

- DC bus link voltage can be connected in parallel for power sharing. 

- Floating current sensors measure actual motor current 

- Regenerative circuit with dynamic distribution of the generated power between several drives on the same DC bus link circuit. 

- Internal regen resistor for all models, optional external regen resistor if required. 

## **Functional Safety Options** 

FS1: STO; SIL2 PLd, command by I/O (➜ # 132). 

## **Electrical safety** 

- Appropriate insulation / creepage distances and electrical isolation for safe electrical separation, per IEC 61800-5-1, between the power input / motor connections and the signal electronics. 

- Soft-start, over voltage detection, short-circuit protection, phase-loss detection. Temperature monitoring of the drive and motor. 

- Electronic motor overload protection: foldback mechanism or optional fault response. 

AKD2G-S Installation Manual, Safety 1 | 6   Technical description and data 

## **Auxiliary supply voltage 24VDC** 

From an external, safety approved 24 V ±10% power supply (PELV). 

## **Parameter setting** 

Setup software WorkBench for setup via TCP/IP. Download control parameter packages via CoE 

## **Full digital control** 

Digital current loop (update 1.28 µs / command 62.5 µs) Digital velocity loop (update period 62.5 µs) Digital position loop (update period 250 µs) 

## **Inputs/Outputs (X21/X22/X23)** 

- 2 programmable analog input (➜ # 105) 

- 2 programmable analog output (➜ # 106) 

- 12 programmable digital inputs (➜ # 107) 

- 8 programmable digital outputs (➜ # 111) 

- 6 programmable digital input/outputs (➜ # 111) 

- 4 safe STO inputs (dual channel STO per axis) (➜ # 127) 

## **Connector Options** 

**IO** : X22 connector with additional digital inputs and outputs. 

- **F3** : X23 connector for conventional motor feedbacks (Resolver, SFD, Tamagawa Smart Abs, Comcoder, 1Vp-p Sin-Cos encoders, incremental encoders, EnDAT 2.1/2.2 and HIPERFACE). 

**DX** : all possible connectors for extended I/O and feedback connections. 

## **Customization** 

- 0000: uncoated PCBs, standard 

- 0xxx: uncoated PCBs, customized coding 

- A000: coated PCBs, standard 

- Axxx: coated PCBs, customized coding 

## **Connectivity** 

Feedback inputs (➜ # 87) 

- Encoder emulation output (➜ # 94) 

- Digital Inputs/Outputs (➜ # 103) 

- Service Interface (➜ # 102) 

- CANopen (➜ # 99) 

- Motion Bus interface (➜ # 97) 

## **Accessories** 

**SFA** (Smart Feedback Adapter) (➜ # 92). 

- Hybrid motor cables, motor power cables, motor feedback cables. External regen resistors. 

For accessories refer to your regional _Accessories Manual_ . 

AKD2G-S Installation Manual, Safety 1 | 6   Technical description and data 

## **6.2 Ambient Conditions, Ventilation, and Mounting Position** 

|**Storage, Transport**|(➜# 22)|
|---|---|
|**Normal operation**|Environmental class 3K3 according to IEC 61800-2|
|**Surrounding tem-**<br>**perature in operation**|Internal regen resistor used:<br>0 to +40 °C under rated conditions<br>+40 to +60 °C with output current derating 3 % per Kelvin<br>Internal regen resistor not used:<br>0 to +50 °C under rated conditions<br>+50 to +60 °C with output current derating 2 % per Kelvin|
|**Humidity in operation**|Relative humidity 5 to 85%, no condensation, IEC 61800-2 class<br>3K3|
|**Site altitude**|Up to 1000 m above mean sea level (AMSL): no restriction<br>1,000 to 2,000 m AMSL: power derating 1.5%/100 m<br>Maximum altitude: 2000 m AMSL|
|**Pollution level**|Pollution level 2 as per IEC 60664-1|
|**Vibration**|Class 3M1 according to IEC 61800-2|
|**Shock**|Class L according to IEC 61800-2|
|**Drive protection**|IP 20 according to IEC 60529|
|**Drive EMC immunity**|Increased immunity according to EN 61800-5-2|
|**Mounting**|Vertical position, in a cabinet with protection of at least IP 54<br>Minimum cabinet size (WxHxD): 406 x 406 x 254 mm|
|**Ventilation**<br>_|Built-in fan in all drive variants<br>~~ee~~|
|_|The drive shuts down in case of excessively high temperature in<br>the control cabinet. Make sure sufficient forced ventilation is sup-<br>plied within the control cabinet.<br>~~ee~~|



## **6.3 Mechanical Data** 

|Weight|**Units**<br>kg|**AKD2G-Sxx-**<br>**6V03S,**<br>**6V06S,**<br>**6V12S**<br>**6V03D,**<br>**6V06D**<br>**7V03S,**<br>**7V06S**<br>**7V03D,**<br>**7V06D,**<br>**7V12S**<br>2.4<br>2.5<br>2.5<br>2.7|**AKD2G-Sxx-**<br>**6V03S,**<br>**6V06S,**<br>**6V12S**<br>**6V03D,**<br>**6V06D**<br>**7V03S,**<br>**7V06S**<br>**7V03D,**<br>**7V06D,**<br>**7V12S**<br>2.4<br>2.5<br>2.5<br>2.7|**AKD2G-Sxx-**<br>**6V03S,**<br>**6V06S,**<br>**6V12S**<br>**6V03D,**<br>**6V06D**<br>**7V03S,**<br>**7V06S**<br>**7V03D,**<br>**7V06D,**<br>**7V12S**<br>2.4<br>2.5<br>2.5<br>2.7|**AKD2G-Sxx-**<br>**6V03S,**<br>**6V06S,**<br>**6V12S**<br>**6V03D,**<br>**6V06D**<br>**7V03S,**<br>**7V06S**<br>**7V03D,**<br>**7V06D,**<br>**7V12S**<br>2.4<br>2.5<br>2.5<br>2.7|
|---|---|---|---|---|---|
|Width|mm|76|76|75|75|
|Height, without connectors|mm|235|235|272|272|
|Height, with connectors|mm|303|303|340|340|
|Depth, without connectors|mm|221|221|221|221|
|Depth, with connectors|mm|232|232|232|232|



Dimension Drawing see section Mechanical Installation (➜ # 42). 

AKD2G-S Installation Manual, Safety 1 | 6   Technical description and data 

|**Performance Data**<br>Normal PWM Switching Frequency (dynamic)<br>~~oe~~|**Units**<br>kHz<br>~~oe~~|**AKD2G-Sxx-**<br>**6V03S/D**<br>**6V06S/D**<br>**6V12S/D**<br>**7V03S/D**<br>**7V06S**<br>**7V06D**<br>**7V12S**<br>15<br>11<br>10.4<br>~~oe~~|**AKD2G-Sxx-**<br>**6V03S/D**<br>**6V06S/D**<br>**6V12S/D**<br>**7V03S/D**<br>**7V06S**<br>**7V06D**<br>**7V12S**<br>15<br>11<br>10.4<br>~~oe~~|**AKD2G-Sxx-**<br>**6V03S/D**<br>**6V06S/D**<br>**6V12S/D**<br>**7V03S/D**<br>**7V06S**<br>**7V06D**<br>**7V12S**<br>15<br>11<br>10.4<br>~~oe~~|
|---|---|---|---|---|
|High Load PWM Switching Frequency (dynamic)<br>~~oe~~|kHz<br>~~oe~~|10.4<br>~~oe~~|8.2<br>~~oe~~|7.0<br>~~oe~~|
|High Load Stalled PWM Switching Frequency<br>(dynamic)<br>~~oe~~|kHz<br>~~oe~~|5.2<br>~~oe~~|4.1<br>~~oe~~|3.5<br>~~oe~~|
|Voltage rise speed dU/dt<br>~~oe~~|kV/µs<br>~~oe~~|7.0<br>~~oe~~|||
|Current Loop Update Period<br>~~oe~~|µs<br>~~oe~~|1.28*<br>~~oe~~|||
|Velocity Loop Update Period<br>~~oe~~|µs<br>~~oe~~|62.5<br>~~oe~~|||
|Position Loop Update Period<br>~~oe~~|µs<br>~~oe~~|250<br>~~oe~~|||
|Current Loop Bandwidth<br>~~oe~~|Hz<br>~~oe~~|3000<br>~~oe~~|||
|Velocity Loop Bandwidth<br>~~oe~~|Hz<br>~~oe~~|750<br>~~oe~~|||
|Position Loop Bandwidth<br>~~oe~~|Hz<br>~~oe~~|350<br>~~oe~~|||
|Max. motor electrical frequency<br>~~oe~~|Hz<br>~~oe~~|599<br>~~oe~~|||



AKD2G-S Installation Manual, Safety 1 | 6   Technical description and data 

## **6.5 Electrical data** 

## **6.5.1 Single axis variants (S)** 

|**6.5.1.1**<br>**Mains supply data, 1 phase AC, type AKD2G-Sxx- (S)**|
|---|
|**Input data**<br>**Units**<br>**6V03S**<br>**6V06S**<br>**6V12S**<br>Operational supply voltage (line-line)<br>VAC<br>12 to 265<br>Rated supply voltage<br>VAC<br>240<br>Rated supply input frequency (±5%)<br>Hz<br>50 to 60<br>Permitted switch on/off frequency<br>1/h<br>30<br>Rated input power at 240 V<br>kVA<br>0.9<br>1.7<br>4.0<br>Rated input current<br>A<br>4.0<br>7.1<br>13<br>Max. inrush current<br>A<br>10<br>Rated DC bus link voltage<br>VDC<br>300<br>~~ZZ~~|
|**6.5.1.2**<br>**Mains supply data, 3 phase AC, type AKD2G-Sxx- (S)**|
|**Input data**<br>**Units**<br>**6V03S**<br>**6V06S**<br>**6V12S**<br>**7V03S**<br>**7V06S**<br>**7V12S**<br>Operational supply voltage (L1/L2/L3)<br>VAC<br>12 to 265<br>24 to 525<br>Rated supply voltage<br>VAC<br>240<br>480<br>Rated supply input frequency (±5%)<br>Hz<br>50 to 60<br>Permitted switch on/off frequency<br>1/h<br>30<br>Rated input power at 240 V (* at 480 V)<br>kVA<br>1.3<br>2.2<br>4.0<br>1.3*(?)<br>2.2*(?)<br>4.0*(?)<br>Rated input current<br>A<br>3.2<br>5.3<br>9.7<br>3.2(?)<br>5.3(?)<br>9.7(?)<br>Max. inrush current<br>A<br>10<br>Rated DC bus link voltage<br>VDC<br>310<br>620<br>~~Ts~~|
|(?) = to be verified|
|**6.5.1.3**<br>**Mains supply data, DC, type AKD2G-Sxx- (S)**|
|**Input data**<br>**Units**<br>**6V03S**<br>**6V06S**<br>**6V12S**<br>**7V03S**<br>**7V06S**<br>**7V12S**<br>Operational supply voltage (DC+/DC-)<br>VDC<br>17 to 370<br>34 to 740<br>Rated supply voltage<br>VDC<br>340<br>680<br>Permitted switch on/off frequency<br>1/h<br>30<br>Rated input power at 340 V (* at 680 V)<br>kW<br>0.62<br>1.25<br>2.5<br>1.25*<br>2.5*<br>5.0*<br>Rated input current<br>A<br>2.0<br>4.0<br>8.0<br>2.0<br>4.0<br>8.0<br>Max. inrush current through AC input<br>A<br>10<br>Rated DC bus link voltage<br>VDC<br>340<br>680<br>**6.5.1.4**<br>**Auxiliary voltage input data, 24VDC, type AKD2G-Sxx- (S)**<br>**Input data**<br>**Units**<br>**6V03S**<br>**6V06S**<br>**6V12S**<br>**7V03S**<br>**7V06S**<br>**7V12S**<br>Aux. voltage supply (PELV)<br>VDC<br>24 V (±10%, check voltage drop)<br>- control current without motor brake<br>A<br>< 1.0<br>- control current with one motor brake<br>A<br>< 3.1<br>~~——~~|



AKD2G-S Installation Manual, Safety 1 | 6   Technical description and data 

## **6.5.1.5 Output data, type AKD2G-Sxx- (S)** 

|**Continuous output current ( ± 3%)**|**Units**<br>Arms|**6V03S**<br>3|**6V06S**<br>6|**6V12S**<br>12|**7V03S**<br>3|**7V06S**<br>6|**7V12S**<br>12|
|---|---|---|---|---|---|---|---|
|**Peak output current (for 5s, ±3%)**|Arms|9|18|30|9|18|30|
|**Continuous output power at rated input current**||||||||
|at 1 x 120 VAC|kW|0.22|0.44|0.875|-|-|-|
|at 1 x 240 VAC|kW|0.44|0.875|1.8|-|-|-|
|at 3 x 120 VAC|kW|0.31|0.625|1.25|-|-|-|
|at 3 x 240 VAC|kW|0.625|1.25|2.5|0.625|1.25|2.5|
|at 3 x 400 VAC|kW|-|-|-|1.05|2.1|4.2|
|at 3 x 480 VAC|kW|-|-|-|1.25|2.5|5.0|
|at 170 VDC|kW|0.31|0.625|1.25|-|-|-|
|at 340 VDC|kW|0.625|1.25|2.5|0.625|1.25|2.5|
|at 565 VDC|kW|-|-|-|1.05|2.1|4.2|
|at 680 VDC|kW|-|-|-|1.25|2.5|5.0|
|**Peak output power (for 1 s)**||||||||
|at 1 x 120 VAC|kW|1.1|2.1|4.1|-|-|-|
|at 1 x 240 VAC|kW|2.1|4.2|6.3|-|-|-|
|at 3 x 120 VAC|kW|1.5|3|4.5|-|-|-|
|at 3 x 240 VAC|kW|3.0|6.0|9.0|3.0|6.0|9.0|
|at 3 x 400 VAC|kW|-|-|-|5.0|10|15|
|at 3 x 480 VAC|kW|-|-|-|6.0|12|18|
|at 170 VDC|kW|1.5|3|4.5|-|-|-|
|at 340 VDC|kW|3.0|6.0|9.0|3.0|6.0|9.0|
|at 565 VDC|kW|-|-|-|5.0|10|15|
|at 680 VDC|kW|-|-|-|6.0|12|18|
|**Noise emission at 1 m,**<br>**low/high speed fan**|dB(A)|< 50 / 60||||||
|**Regeneration braking**|(➜# 37)|||||||
|**Brake output**||||||||
|Voltage (±10%)|VDC|24||||||
|Voltage power saving|VDC|12 to 24||||||
|Output under current fault|mA|100 (required for fault detection)||||||
|Output over current fault|A|2.25 (required for fault detection)||||||
|Output current, maximum|A|2.1||||||



AKD2G-S Installation Manual, Safety 1 | 6   Technical description and data 

## **6.5.2 Dual axis variants (D: I1=I2)** 

|**6.5.2.1**<br>**Mains supply data, 1 phase AC, type AKD2G-Sxx- (D)**|
|---|
|**Input data**<br>**Units**<br>**6V03D**<br>**6V06D**<br>Operational supply voltage (line-line)<br>VAC<br>12 to 265<br>Rated supply voltage<br>VAC<br>240<br>Rated supply input frequency (±5%)<br>Hz<br>50 to 60<br>Permitted switch on/off frequency<br>1/h<br>30<br>Rated input power at 240 V<br>kVA<br>2.2<br>4.0<br>Rated input current<br>A<br>7.2<br>13<br>Max. inrush current<br>A<br>10<br>Rated DC bus link voltage<br>VDC<br>300<br>~~a~~|
|**6.5.2.2**<br>**Mains supply data, 3 phase AC, type AKD2G-Sxx- (D)**|
|**Input data**<br>**Units**<br>**6V03D**<br>**6V06D**<br>**7V03D**<br>**7V06D**<br>Operational supply voltage (L1/L2/L3)<br>VAC<br>12 to 265<br>24 to 525<br>Rated supply voltage<br>VAC<br>240<br>480<br>Rated supply input frequency (±5%)<br>Hz<br>50 to 60<br>Permitted switch on/off frequency<br>1/h<br>30<br>Rated input power at 240 V (* at 480 V)<br>kVA<br>2.2<br>4.0<br>4.49*(?)<br>7.65*(?)<br>Rated input current<br>A<br>5.3<br>9.7<br>5.3 (?)<br>9.7 (?)<br>Max. inrush current (at 240 V/480 V, 20°C)<br>A<br>10<br>Rated DC bus link voltage<br>VDC<br>310<br>620<br>~~ee~~|
|(?) = to be verified|
|**6.5.2.3**<br>**Mains supply data, DC, type AKD2G-Sxx- (D)**|
|**Input data**<br>**Units**<br>**6V03D**<br>**6V06D**<br>**7V03D**<br>**7V06D**<br>Operational supply voltage (DC+/DC-)<br>VDC<br>17 to 370<br>34 to 740<br>Rated supply voltage<br>VDC<br>340<br>680<br>Permitted switch on/off frequency<br>1/h<br>30<br>Rated input power at 340 V (* at 680 V)<br>kW<br>1.25<br>2.5<br>2.5*<br>5*<br>Rated input current<br>A<br>4<br>8<br>4<br>8<br>Max. inrush current through AC input<br>A<br>10<br>Rated DC bus link voltage<br>VDC<br>340<br>680<br>~~===~~|
|**6.5.2.4**<br>**Auxiliary voltage input data, 24VDC, type AKD2G-Sxx- (D)**|
|**Input data**<br>**Units**<br>**6V03D**<br>**6V06D**<br>**7V03D**<br>**7V06D**<br>Aux. voltage supply (PELV)<br>VDC<br>24 V (±10%, check voltage drop)<br>- current without motor brake<br>A<br><1<br>- control current with one motor brake<br>A<br><3.1<br>- control current with two motor brakes<br>A<br><5.2<br>~~—_———~~|



AKD2G-S Installation Manual, Safety 1 | 6   Technical description and data 

## **6.5.2.5 Output data, type AKD2G-Sxx- (D)** 

Drive current and power output values are listed for Axis1/Axis2. 

|**Continuous output current ( ± 3%)**|**Units**<br>Arms|**6V03D**<br>3/3|**6V06D**<br>6/6|**7V03D**<br>3/3|**7V06D**<br>6/6|
|---|---|---|---|---|---|
|**Peak output current (for 5s, ±3%)**|Arms|9/9|18/18|9/9|18/18|
|**Continuous output power at rated input current**||||||
|at 1 x 120 VAC|kW|0.22/0.22|0.44/0.44|-|-|
|at 1 x 240 VAC|kW|0.44/0.44|0.875/0.875|-|-|
|at 3 x 120 VAC|kW|0.31/0.31|0.625/0.625|-|-|
|at 3 x 240 VAC|kW|0.625/0.625|1.25/1.25|0.625/0.625|1.25/1.25|
|at 3 x 400 VAC|kW|-|-|1.05/1.05|2.1/2.1|
|at 3 x 480 VAC|kW|-|-|1.25/1.25|2.5/2.5|
|at 170 VDC|kW|0.31/0.31|0.625/0.625|-|-|
|at 340 VDC|kW|0.625/0.625|1.25/1.25|0.625/0.625|1.25/1.25|
|at 565 VDC|kW|-|-|1.05/1.05|2.1/2.1|
|at 680 VDC|kW|-|-|1.25/1.25|2.5/2.5|
|**Peak output power (for 1 s)**||||||
|at 1 x 120 VAC|kW|1.1/1.1|2.1/2.1|-|-|
|at 1 x 240 VAC|kW|2.1/2.1|4.2/4.2|-|-|
|at 3 x 120 VAC|kW|1.5/1.5|3.0/3.0|-|-|
|at 3 x 240 VAC|kW|3.0/3.0|6.0/6.0|3.0/3.0|6.0/6.0|
|at 3 x 400 VAC|kW|-|-|5.0/5.0|10/10|
|at 3 x 480 VAC|kW|-|-|6.0/6.0|12/12|
|at 170 VDC|kW|1.5/1.5|3.0/3.0|-|-|
|at 340 VDC|kW|3.0/3.0|6.0/6.0|3.0/3.0|6.0/6.0|
|at 565 VDC|kW|-|-|5.0/5.0|10/10|
|at 680 VDC|kW|-|-|6.0/6.0|12/12|
|**Noise emission at 1 m,**<br>**low/high speed fan**|dB(A)|< 50 / 60||||
|**Regeneration braking**|(➜# 37)|||||
|**Brake output**||||||
|Voltage (±10%)|VDC|24||||
|Voltage power saving|VDC|12 to 24||||
|Output under current fault|mA|100 (required for fault detection)||||
|Output over current fault|A|2.25 (required for fault detection)||||
|Output current, maximum|A|2.1 per brake||||



AKD2G-S Installation Manual, Safety 1 | 6   Technical description and data 

## **6.6 Electrical Motor Braking** 

## **6.6.1 Dynamic Braking** 

Dynamic braking is a method to slow down a servo system by dissipating the mechanical energy driven by the motor back EMF. 

Dynamic braking is not functional safe. . 

The AKD2G has a built in advanced dynamic braking mode which operates fully in hardware. When activated, the drive powers the motor terminals with voltages to maximize the stopping force per amount of motor current. This advanced method forces all of the dynamic braking current to be stopping current and insures the fastest stopping per ampere of motor terminal current. 

When current is not being limited, the mechanical energy is being dissipated in the motor winding resistance. 

- When current is being limited, energy is returned to the drive bus capacitors. 

The drive also limits the maximum dynamic braking motor terminal current via the _AXIS#.DBILIMIT_ parameter to insure that the drive, motor, and customer load do not see excessive currents/forces. 

Whether and how the AKD2G uses dynamic braking depends on ( _AXIS#.DISMODE_ ). 

## **6.6.2 Regeneration braking** 

When the amount of returned energy from the motor builds the bus capacitor voltage up enough the drive activates the regenerative braking circuit to start dumping the returned energy in the regen resistor (also called regenerative resistor or brake resistor). All AKD2G offer internal resistor plus the ability to connect an external resistor depending on the application requirements. 

External regen resistors are described in the regional _Accessories Manual_ . 

## **6.6.2.1 Functional description** 

## **1. Individual drives, not coupled through the DC bus link circuit (+DC, -DC)** 

When the energy fed back from the motor has an average or peak power that exceeds the preset level for the brake power rating, the drive generates the warning "W2010 Regen Energy Critical”. If the power exceeds the set fault level, the regenerative circuit will switch off and the drive will disable. 

## **2. Several drives coupled through the DC bus link (+DC, -DC)** 

Using the built-in regenerative circuit, several drives of the same series can be operated from a common DC-bus link (➜ # 77), without any additional measures. 90% of the combined power of all the coupled drives is always available for peak and continuous power. If the power of the drive with the lowest switch-off threshold (resulting from tolerances) exceeds the set fault level, the regenerative circuit will switch off on that drive. 

**Switch-off on over voltage** : With the regenerative circuit switched off, the returned energy is not dissipated and therefore the DC-bus link level increases. The drive reports an overvoltage fault if the DC-bus voltage threshold is exceeded. When this happens, the drive power stage is immediately disabled and the load coasts to a stop with the fault message “F2006 Bus Over voltage". 

The ready to operate contact (terminals X21/B5-B6) is opened (➜ # 114). 

Observe the regeneration time (some minutes) after full load with peak brake power. 

AKD2G-S Installation Manual, Safety 1 | 6   Technical description and data 

## **6.6.2.2 Technical data for AKD2G-Sxx-6V** 

Technical data for the regenerative circuit depends on the drive type and the mains voltage. Supply voltages, capacitance, and switch-on voltages are all nominal values. 

|**Brake circuit**<br>**AKD2G-Sxx-**<br>**Rated data**<br>**Units**<br>**6Vxxy**<br>**all types**<br>Regen start voltage at rated supply voltage<br>V<br>Overvoltage limit<br>V<br>Maximum regenerative duty cycle<br>%<br>Internal regen resistor<br>Ω<br>Continuous power, internal resistor<br>W<br>Peak brake power, internal resistor (0.5s)<br>kW<br>External regen resistor (recommended 15 Ω)<br>Ω<br>Continuous brake power, external resistor<br>kW<br>Peak brake power, external (1s)<br>kW|**Brake circuit**<br>**AKD2G-Sxx-**<br>**Rated data**<br>**Units**<br>**6Vxxy**<br>**all types**<br>Regen start voltage at rated supply voltage<br>V<br>Overvoltage limit<br>V<br>Maximum regenerative duty cycle<br>%<br>Internal regen resistor<br>Ω<br>Continuous power, internal resistor<br>W<br>Peak brake power, internal resistor (0.5s)<br>kW<br>External regen resistor (recommended 15 Ω)<br>Ω<br>Continuous brake power, external resistor<br>kW<br>Peak brake power, external (1s)<br>kW|**Brake circuit**<br>**AKD2G-Sxx-**<br>**Rated data**<br>**Units**<br>**6Vxxy**<br>**all types**<br>Regen start voltage at rated supply voltage<br>V<br>Overvoltage limit<br>V<br>Maximum regenerative duty cycle<br>%<br>Internal regen resistor<br>Ω<br>Continuous power, internal resistor<br>W<br>Peak brake power, internal resistor (0.5s)<br>kW<br>External regen resistor (recommended 15 Ω)<br>Ω<br>Continuous brake power, external resistor<br>kW<br>Peak brake power, external (1s)<br>kW|**AC Supply**<br>**120V / 240V**<br>380|
|---|---|---|---|
||Overvoltage limit|V|420|
||Maximum regenerative duty cycle|%|35*|
||Internal regen resistor|Ω|15|
||Continuous power, internal resistor|W|100|
||Peak brake power, internal resistor (0.5s)|kW|3 / 9|
||External regen resistor (recommended 15 Ω)|Ω|>10|
||Continuous brake power, external resistor|kW|5|
||Peak brake power, external (1s)|kW|5 / 14|
|**6V03S, 6V06S**|Absorption energy in capacitors (+/- 20%)|Ws|6 / 23|
||DC Bus Capacitance|µF|1640|
|**6V12S, 6V03D,**<br>**6V06D**|Absorption energy in capacitors (+/- 20%)|Ws|9 / 35|
||DC Bus Capacitance|µF|2460|



* depends on connected regen resistor power. 

## **6.6.2.3 Technical data for AKD2G-Sxx-7V** 

Technical data for the regenerative circuit depends on the drive type and the mains voltage. Supply voltages, capacitance, and switch-on voltages are all nominal values. 

|**Brake circuit**<br>**AKD2G-Sxx-**<br>**Rated data**<br>**Units**<br>**7Vxxy**<br>**all types**<br>Regen start voltage at rated supply voltage<br>V<br>Overvoltage limit<br>V<br>Maximum regenerative duty cycle<br>%<br>Internal regen resistor<br>Ω<br>Continuous power, internal resistor<br>W<br>Peak brake power, internal resistor (0.5s)<br>kW<br>External regen resistor (recommended 33 Ω)<br>Ω<br>Continuous brake power, external resistor<br>kW<br>Peak brake power, external (1s)<br>kW|**Brake circuit**<br>**AKD2G-Sxx-**<br>**Rated data**<br>**Units**<br>**7Vxxy**<br>**all types**<br>Regen start voltage at rated supply voltage<br>V<br>Overvoltage limit<br>V<br>Maximum regenerative duty cycle<br>%<br>Internal regen resistor<br>Ω<br>Continuous power, internal resistor<br>W<br>Peak brake power, internal resistor (0.5s)<br>kW<br>External regen resistor (recommended 33 Ω)<br>Ω<br>Continuous brake power, external resistor<br>kW<br>Peak brake power, external (1s)<br>kW|**Brake circuit**<br>**AKD2G-Sxx-**<br>**Rated data**<br>**Units**<br>**7Vxxy**<br>**all types**<br>Regen start voltage at rated supply voltage<br>V<br>Overvoltage limit<br>V<br>Maximum regenerative duty cycle<br>%<br>Internal regen resistor<br>Ω<br>Continuous power, internal resistor<br>W<br>Peak brake power, internal resistor (0.5s)<br>kW<br>External regen resistor (recommended 33 Ω)<br>Ω<br>Continuous brake power, external resistor<br>kW<br>Peak brake power, external (1s)<br>kW|**AC Supply**<br>**240V**<br>**400V/480V**<br>380<br>633 / 760|**AC Supply**<br>**240V**<br>**400V/480V**<br>380<br>633 / 760|
|---|---|---|---|---|
||Overvoltage limit|V|420|840|
||Maximum regenerative duty cycle|%|35*||
||Internal regen resistor|Ω|33||
||Continuous power, internal resistor|W|100||
||Peak brake power, internal resistor (0.5s)|kW|4|17|
||External regen resistor (recommended 33 Ω)|Ω|>25||
||Continuous brake power, external resistor|kW|2|6|
||Peak brake power, external (1s)|kW|6|24|
|**7V03S, 7V06S**|Absorption energy in capacitors (+/- 20%)|Ws|3|30 / 18|
||DC Bus Capacitance|µF|235||
|**7V12S, 7V03D,**<br>**7V06D**|Absorption energy in capacitors (+/- 20%)|Ws|6|50 / 35|
||DC Bus Capacitance|µF|470||



* depends on connected regen resistor power. 

AKD2G-S Installation Manual, Safety 1 | 6   Technical description and data 

## **6.7 LCD Display and Push-buttons (B1, B2)** 

The drive offers an LCD display and two push-buttons B1 / B2 for navigation. 

## **Push-button actions** 

A short button press invokes the action corresponding to the symbol directly above the button. On the dashboard for example, 

- a short press on B1 causes the menu system to appear, and 

- a short press on B2 causes a help screen to appear. 

A long press (greater than 2 seconds) on B2 returns the display to the previous screen. 

|A long press (greater than 2 seconds) on B2 returns the display to the previous screen.<br>*|A long press (greater than 2 seconds) on B2 returns the display to the previous screen.|
|---|---|
|**More B1 / B2 Functions**<br>Boot from SD card|**Description**<br>Push both buttons during power up to boot with data from SD<br>card. Press the buttons first, then hold it down while turning on<br>the 24 V power supply.|
|Boot from flash fallback<br>image|Remove the SD card, then press both buttons and hold them<br>down while turning on the 24 V power supply to boot from an on-<br>board recovery image. The fallback image includes a set of boot-<br>loader, operational, and control FPGA that implements suf-<br>ficient programming support to update missing or corrupt files.|



## **LCD display** 

- Left Colored section 

Color: axis status (enabled, disabled, or faulted). 

First icon: axis command source (analog, service, electronic gearing, or fieldbus). Second icon: axis operation mode (torque, velocity, or position). Axis ID: A1 or A2. 

- Right Non-colored section: 

No Fault/Warning: three virtual LEDs corresponding to axis disable sources (Safe Torque Off, Hardware Enable, and Controlled Stop). Faults or warnings: fault or warning code. 

Center blue bar: 

   - Drive and axis names IP address 

   - Drive model number 

   - Firmware version 

- Bottom blue bar: 

   - indicates whether the service port is connected to WorkBench, and shows the actions that will be invoked by pushing the B1 / B2 buttons. 

AKD2G-S Installation Manual, Safety 1 | 6   Technical description and data 

## **Dual axes LCD display** 

For dual-axis drives, the top section shows axis 1 information, the bottom section those for axis 2. 

## **Single axis LCD display** 

For single axis drives, the top section shows axis 1 information while the section between the center and bottom bars is a data area where some important actual values of the axis are visible: position, velocity, current. 

AKD2G-S Installation Manual, Safety 1 | 6   Technical description and data 

## **Faults and Warnings** 

The display shows the code of the fault or warning that occurred. If a fault occurs, the color of the left section switches to red. Navigate with B1 / B2 to the Fault screen to see a short description of the fault or warning. 

See WorkBench Onlinehelp for more details. 

## **6.8 SD Card Slot** 

AKD2G offer a SD card slot . to boot the drive with data from the SD Memory card 

These features can be started from the drive display using push-buttons B1/B2. 

## **Supported SD card types** 

SD cards are formatted by the manufacturer. The following table outlines the SD card types and AKD2G support. 

|**SD Type**<br>SD (SDSC)|**File System**<br>FAT16|**Capacity**<br>1MB to 2GB|**Supported**<br>**YES**|
|---|---|---|---|
|SDHC|FAT32|4GB to 32GB|**YES**|
|SDXC|exFAT (Microsoft)|>32GB to 2TB|**NO**|



## **Features** 

## **Boot AKD2G with data from SD card:** 

- Remove 24V. Apply 24V with buttons B1 and B2 pressed. Release buttons after the display is updated. 

AKD2G-S Installation Manual, Safety 1 | 7   Mechanical Installation 

## **7 Mechanical Installation** 

|**7.1**|**Important Notes**|**43**|
|---|---|---|
|**7.2**|**Guide to Mechanical Installation**|**43**|
|**7.3**|**Dimensions**|**44**|



AKD2G-S Installation Manual, Safety 1 | 7   Mechanical Installation 

## **7.1 Important Notes** 

## ZA\CAUTION 

## **High EMC Voltage Level!** 

- Risk of electrical shock, if the servo amplifier (or the motor) is not properly EMC-grounded. * Do not use painted (i.e. non-conductive) mounting plates. 

   - In unfavourable circumstances, use copper mesh tape between the earthing bolts and earth potential to deflect currents. 

Protect the drive from impermissible stresses. In particular, do not let any components become bent or any insulation distances altered during transport and handling. Avoid contact with electronic components and contacts. 

The drive will switch itself off in case of overheating. Ensure that there is an adequate flow of cool, filtered air into the bottom of the control cabinet, or use a heat exchanger (➜ # 31). Do not mount devices that produce magnetic fields directly beside the drive. Strong magnetic fields can directly affect internal components. Install devices which produce magnetic field with distance to the drives and/or shield the magnetic fields. 

## **7.2 Guide to Mechanical Installation** 

The following tools are required (at a minimum) to install the AKD2G; your specific installation may require additional tools: 

- M5 hexagon socket-cap screws (ISO 4762) 

- 4 mm T-handle Allen key 

- No. 2 Phillips head screwdriver 

- Small slotted screwdriver 

Install the drive unit as follows: 

1. Prepare the site. 

   - Mount the drive in a closed control cabinet (ambient conditions (➜ # 31)). The site must be free from conductive or corrosive materials. For the mounting position in the cabinet (➜ # 44). 

2. Check ventilation. 

Check that the ventilation of the drive is unimpeded, and keep within the permitted ambient temperature (➜ # 31). Keep the required space clearance above and below the drive (➜ # 44). 

3. Check the cooling system. 

   - If cooling systems are used for the control cabinet, position the cooling system so that condensation water cannot drip onto the drive or peripheral devices. 

4. Mount the drive. 

   - Assemble the drive and power supply near each other on the conductive, grounded mounting plate in the cabinet. 

5. Ground the drive. 

   - For EMC-compliant shielding and grounding, (➜ # 52). Ground the mounting plate, motor housing and CNC-GND of the control system. 

AKD2G-S Installation Manual, Safety 1 | 7   Mechanical Installation 

## **7.3 Dimensions** 

Mounting material: three M5 hexagon socket screws to ISO 4762, 4 mm T-handle Allen key 

Outline width and height dimensions are measured on footprint level (mounting plate). Dimensions on the front plate are slightly smaller. All dimensions in mm. 

|**Dimensions in mm**<br>AKD2G-Sxx-6V (3 to 12 A)|**A**<br>221|**A1**<br>232|**B**<br>235|**B1**<br>303|**C**<br>76|**D**<br>221,5|**E**<br>36|**F**<br>5,8|**G**<br>11,5|**H**<br>7|**M**<br>78|**P**<br>40|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|AKD2G-Sxx-7V (3 to 12 A)|221|232|272|340|75|259|36|5,8|11,5|6|77|39|



AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8 Electrical Installation** 

|**8.1**|**Important Notes**|**46**|
|---|---|---|
|**8.2**|**Guide to electrical installation**|**47**|
|**8.3**|**Wiring**|**48**|
|**8.4**|**EMI Noise Reduction**|**52**|
|**8.5**|**Connection Overview**|**57**|
|**8.6**|**Power and Logic Voltage Supply (X3/X10)**|**67**|
|**8.7**|**DC Bus link (X3)**|**77**|
|**8.8**|**External Regen resistor (X3)**|**79**|
|**8.9**|**Motor Power, Brake and Feedback connection**|**80**|
|**8.10**|**Electronic Gearing, EEO, Master-Slave**|**93**|
|**8.11**|**Motion Bus Interface (X11/X12)**|**97**|
|**8.12**|**CAN-Bus Interface (X13/X14)**|**99**|
|**8.13**|**Service Interface (X20)**|**102**|
|**8.14**|**I/O Connection (X21/X22/X23)**|**103**|



AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.1 Important Notes** 

Only professional staff who are qualified in electrical engineering are allowed to install the drive. Wires with color green with one or more yellow stripes must not be used other than for protective earth (PE) wiring. 

## 4 DANGER 

## **High Voltage up to 900 V!** 

There is a danger of serious personal injury or death by electrical shock or electrical arcing. Capacitors can still have dangerous voltages present up to 5 minutes after switching off the supply power. Control and power connections can still be live, even if the motor is not rotating. 

   - Only install and wire the equipment when it is not live. 

   - Make sure that the cabinet is safely disconnected (for instance, with a lock-out and warning signs). 

   - Never remove electrical connections to the drive while it is live. 

   - Wait at least 5 minutes after disconnecting the drive from the main supply power before touching potentially live sections of the equipment (e.g. contacts) or undoing any connections. 

   - To be sure, measure the voltage in the DC bus link and wait until it has fallen below 50 V. 

- Wrong mains voltage, unsuitable motor or wrong wiring will damage the drive. Check the combination of drive and motor. Compare the rated voltage and current of the units. Implement the wiring according to the matching connection diagram, see (➜ # 59) and following. Make sure that the maximum permissible rated voltage at the terminals L1, L2, L3 or +DC, – DC is not exceeded by more than 10% even in the most unfavorable circumstances (see IEC 60204-1). 

- Excessively high external fusing will endanger cables and devices. The fusing of the mains power and logic power must be installed by the user. Hints for use of Residual-current circuit breakers (RCD) (➜ # 18). 

- Since the leakage current to PE is more than 3.5 mA, in compliance with IEC61800-5-1 the PE connection must either be doubled or a connecting cable with a cross-section >10 mm² must be used. Deviating measures according to regional standards might be possible. The drive status shall be monitored by the PLC to acknowledge critical situations. We recommend wiring the ready to operate relay contact in series into the emergency off circuit of the installation. The emergency off circuit must operate the supply contactor. 

- It is permissible to use the setup software to alter the settings of the drive. Any other alterations will invalidate the warranty. 

AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.2 Guide to electrical installation** 

Kollmorgen recommends to install the drive electrical system as follows: 

1. Select cables in accordance with IEC 60204 (➜ # 49). 

2. Install shielding and ground the drive. 

   - For EMC-compliant shielding and grounding, see (➜ # 52). Ground the mounting plate, motor housing and CNC-GND of the control system. 

3. For functional safety information, see (➜ # 127). 

4. Wire the drive and connectors. 

   - Observe the "Recommendations for EMI noise reduction": (➜ # 52). 

      - Wire the "Ready to Operate" contact into the emergency off circuit of the system. Connect the digital control inputs and outputs. 

      - Connect up analog ground (also if a fieldbus is used). Connect the analog input source, if required. Connect the motor (hybrid cable or power, brake and feedback cables). Connect shielding at both ends. 

      - If required, connect the external regen resistor (with fusing). 

      - AKD2G-Sxx-6V: connect EMC filters (shielded lines between filter and drive) for second environment requirements to product category C2. Connect the auxiliary voltage supply Connect the main electrical supply. Check maximum permitted voltage value (➜ # 33). Check proper use of residual-current circuit breakers (RCD): (➜ # 18). Connect the PC (➜ # 102) for setting up the drive. 

5. Check the wiring against the wiring diagrams: 

|Overview AKD2G single axis|(➜# 59)|
|---|---|
|Overview AKD2G dual-axis|(➜# 60)|
|Connector pinout|(➜# 61) ff|
|Mains power supply:|(➜# 68) ff|
|Logic power supply:|(➜# 76)|
|DC Bus Link:|(➜# 77)|
|External Regen Resistor:|(➜# 79)|
|Motor single cable connection:|(➜# 81)|
|Motor dual cable connection:|(➜# 83)|
|Electronic gearing:|(➜# 93)|
|- Encoder emulation:|(➜# 94)|
|- Master Slave:|(➜# 96)|
|EtherCAT interface:|(➜# 97)|
|CAN-Bus interface:|(➜# 99)|
|Service interface:|(➜# 102)|
|Digital and analog I/O:|(➜# 103)|
|Functional Safety option 1:|(➜# 132)|



AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.3 Wiring** 

Only professional staff who are qualified in electrical engineering are allowed to install the drive. Wires with color green with one or more yellow stripes must not be used other than for protective earth (PE) wiring. When installing or replacing cables, use only standardized components, which complies to the cable and wire requirements (➜ # 49). 

## **8.3.1 General** 

## **High Voltage up to 900 V!** 

There is a danger of serious personal injury or death by electrical shock or electrical arcing. * Only install and wire the equipment when it is not live, that is, when neither the electrical 

- Only install and wire the equipment when it is not live, that is, when neither the electrical supply nor the 24 V auxiliary voltage nor the supply voltages of any other connected equipment is switched on. 

- Make sure that the cabinet is safely disconnected (for instance, with a lock-out and warning signs). The individual voltages are switched on for the first time during setup. 

The chassis ground symbol, which is used in all the wiring diagrams, indicates that you must take care to provide an electrically conductive connection with the largest feasible surface area between the unit indicated and the mounting plate in the control cabinet. This connection is for the effective grounding of HF interference, and must not be confused with the PE-symbol (PE = protective earth, safety measure as per IEC 60204). 

## **8.3.2 Mating connectors** 

- Connectors X1, X2, , X10, X21, X22 are spring clamp connectors. X3 connector with screw terminals. 

X3 and X10 T-type connectors on request. Connectors X22 and X23 are optional. 

|**#**<br>X1/2<br>a|**Description**<br>Motor, two wire feed-<br>back, holding brake<br> a|**Type**<br>Connector, 4 pol. power<br>~~es~~<br>~~ee~~|**Max. Cross**<br>**Section**<br>10 mm², 8 awg<br>~~es~~<br>ee<br>~~ee~~|**Tightening**<br>**Torque/Nm**<br>0.55<br>~~ee~~<br>ee|
|---|---|---|---|---|
|||Connector, 4 pol. signal<br> ~~ee~~<br>ee|0.5 mm², 21 awg<br>ee<br>~~ee~~<br>ee||
|X3<br>~~ee~~<br>a|Mains power, regen<br>resistor, DC-Bus<br>~~ee~~<br>|Connector, 8 pol.<br>~~ee~~<br>ee<br>ee<br>|6 mm², 10 awg<br>~~ee~~<br>ee<br>eee<br>|0.55<br>~~ee~~<br>ee<br>ee<br>|
|X10/X10T<br>~~a~~<br>a|24V power supply<br>~~a~~<br>|Connector or T-type, 2<br>pol.<br>ee<br>~~a~~<br>ee<br>|2.5 mm², 14 awg<br>ee <br>~~a~~<br>eee<br>|0.2 to 0.25<br> ee<br>~~a~~<br>ee<br>|
|X11/12<br>a|Motion Bus<br>|RJ45<br>ee <br>|0,5 mm², 21 awg<br> eee <br>|n/a<br> ee<br>|
|X13/14<br>~~a~~|CAN In/Out<br>~~a~~|RJ11<br>~~a~~|0,5 mm², 21 awg<br>~~a~~|n/a<br>~~a~~|
|X20|Service Port|RJ45|0,5 mm², 21 awg|n/a|
|X21<br>~~a~~|I/O control signals<br>~~a~~|Connector, 2x11 pol.<br>~~a~~|1.5 mm², 16 awg<br>~~a~~|n/a<br>~~a~~|
|X22<br>~~a~~|I/O control signals<br>~~a~~|Connector, 2x10 pol.<br>~~a~~<br>eee|1.5 mm², 16 awg<br>~~a~~<br>eee|n/a<br>~~a~~<br>eee|
|X23<br>~~a~~|Conventional feed-<br>back models<br>~~a~~|SubD 15pol. HD (female)<br>~~a~~<br>eee|0,5 mm², 21 awg<br>~~a~~<br>eee|0.4<br>~~a~~<br>eee|



AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.3.3 Cable and Wire Requirements** 

## **8.3.3.1 Cable material** 

For information on the chemical, mechanical, and electrical characteristics of the cables please refer to the accessories manual or contact customer support. 

- To reach the maximum permitted cable length, you must use cable material with the following capacitance requirements: 

   - Motor power cable: less than 150 pF/m (phase core to shield capacitance) 

   - Motor Feedback cable: less than 120 pF/m (signal core to shield capacitance) Hybrid motor cable: 

   - less than 120 pF/m (phase core/core capacitance) 

   - less than 210 pF/m (phase core/shield capacitance) 

   - less than 120 pF/m (signal core/core capacitance) 

   - less than 210 pF/m (signal core/shield capacitance) 

   - BUS Element: 45 pF/m @ 800kHz & charact. wave resistance 110±10Ω @ 10MHz 

## **8.3.3.2 Cable Length** 

- Cables should not exceed the maximum lengths stated below. The recommended maximum cable length of motor cables depends on the used cable material and the feedback type. Cable functionality is only guaranteed up to the maximum length when using unmodified Kollmorgen engineered cables. 

Length of motor power cables, feedback cables and motor brake cables is equal. 

|**AKM2G**<br>**Performance Line Cables**<br>**Feedback**<br>**Max. Length [m]**<br>SFD3<br>50|**AKM2G**<br>**Performance Line Cables**<br>**Feedback**<br>**Max. Length [m]**<br>SFD3<br>50|**AKM**<br>**Performance Line Cables**<br>**Value Line Cables**<br>**Feedback**<br>**Max. Length [m]**<br>**Feedback**<br>**Max. Length [m]**<br>All<br>25<br>All<br>12|
|---|---|---|
|DSL|25||
|Endat 2.2|25||
|Resolver|50||



The maximum cable length for digital I/O supply (24V/DGND) is 3 m. If longer cables are required, the user need to take care of additional EMC measures. 

## **8.3.3.3 T-Connector wiring** 

If you use mating T-connectors for 24 VDC supply, mains voltage supply and DC-Bus link, you must prepare the connecting cables with wire end ferrules. 

You can prepare cables with cross-section 2.5 mm² (up to to 6 mm²) with a uniform length of 170 mm, if the modules are lined up close together. 

Use wire end ferrules with plastic collars, for example 2.5 mm² x 17 mm. 

AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.3.3.4 Cable cross sections and requirements** 

|The tables below describe the recommended interface cross sections and cable require-|
|---|
|ments related to AKD2G in accordance with IEC 60204. For multi-axes systems, observe|
|the specific operating conditions for your system.|
|**Power Cables**<br>**Cross Section**<br>**Remarks**<br>**EU**<br>**US**<br>Mains supply<br>1x3 A:<br>2x3 A:<br>1x6 A:<br>2x6 A:<br>1x12 A:<br>2x12 A:<br>1.5 mm²<br>1.5 mm²<br>1.5 mm²<br>2.5 mm²<br>2.5 mm²<br>6 mm²<br>14 awg<br>14 awg<br>14 awg<br>14 awg<br>14 awg<br>10 awg<br>600 V rated ,minimum 75°C<br>24 V supply<br>max.<br>2.5 mm²<br>14 awg<br>single core<br>DC bus link,<br>Regen resistor<br>3/6 A:<br>12 A:<br>1.5 mm²<br>2.5 mm²<br>14 awg<br>14 awg<br>1000 V rated, min. 75°C,<br>shielded for lengths >0.20 m<br>**I/O cables**<br>Analog I/Os<br>min.<br>0.25 mm²<br>24 awg<br>shielded twisted pairs<br>Digital I/Os<br>0.5 mm²<br>20 awg<br>single core<br>~~—~~|
|**Motor Power Cable (power) & Motor Combination Cable (power & brake)**|
|**Cross Section [mm]**<br>**Current Carrying**<br>**Capacity**<br>**Remarks**<br>**Cable**<br>**Combi Cable**<br>(4x1)<br>(4x1.0+(2x0.75))<br>0A < I0rms ≤10.1A<br>1000 V Rated, 80°C<br>Current carrying capacity<br>acc. to IEC 60204-1:2006<br>Table 6, Column B2<br>The brackets (...) show<br>the shielding.<br>(4x1.5)<br>(4x1.5+(2x0.75))<br>10.1A < I0rms ≤13.1A<br>(4x2.5)<br>(4x2.5+(2x1.0))<br>13.1A < I0rms ≤17.4A<br>(4x4)<br>(4x4.0+(2x1.0))<br>17.4A < I0rms ≤23A<br>(4x6)<br>(4x6.0+(2x1.0))<br>23A < I0rms ≤30A<br>~~—_~~|
|**Motor Feedback Cable**|
|**Type**<br>**Cross Section [mm]**<br>**Remarks**<br>Resolver<br>(4x2x0.25)<br>300 V rated, 80°C<br>Shielded twisted pairs<br>The brackets (...) show<br>the shielding.<br>EnDat 2.1, BiSS B<br>(6x2x0.25)<br>HIPERFACE<br>(5x2x0.25)<br>EnDat 2.2, BiSS C<br>(5x2x0.25)<br>SFD<br>(3x2x0.25)<br>Comcoder<br>(8x2x0.25)<br>~~==~~|
|**Motor Hybrid Cable**<br>**Type**<br>**Cross Section [mm]**<br>**Current Carrying**<br>**Capacity**<br>**Remarks**<br>SFD3/DSL<br>(4x1.0+(2x0.34)+(2x0.75))<br>0A < I0rms ≤10.1A<br>1000 V rated, 80°C<br>Current carrying capacity<br>acc. to IEC 60204-1:2006<br>Table 6, Column B2<br>4 power lines &<br>2 brake lines &<br>2 SFD3/DSL signal lines<br>or<br>6 EnDat 2.2 signal lines<br>SFD3/DSL<br>(4x1.5+(2x0.34)+(2x0.75))<br>10.1A < I0rms ≤13.1A<br>SFD3/DSL<br>(4x2.5+(2x0.34)+(2x1.0))<br>13.1A < I0rms ≤17.4A<br>SFD3/DSL<br>(4x4.0+(2x0.34)+(2x1.0))<br>17.4A < I0rms ≤23A<br>SFD3/DSL<br>(4x6.0+(2x0.34)+(2x1.0))<br>23A < I0rms ≤30A<br>Endat 2.2<br>(4x1.5+(2x0.75)+<br>(2x2x0.14+2x0.25))<br>10.1A < I0rms ≤13.1A<br>Endat 2.2<br>(4x4.0+(2x1.0)+<br>(2x2x0.14+2x0.25))<br>17.4A < I0rms ≤23A<br>~~==~~|



AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.3.4 Protective Earth connection** 

Protective Earth connection of the system components is a safety measure per IEC 60204. Ensure the proper grounding of all components with the PE rail in the control cabinet as reference potential. Connect each ground individually with the intended grounding cable (neutral point connection). 

The leakage current from AKD2G against PE is more than 3.5 mA. In accordance with EN 61800-5-1, the PE connection must therefore either be double implemented or a connection cable with >10mm² cross-section used. 

In order to keep the impedance as low as possible, we recommend a copper earthing strap for the PE connection on the PE block. 

Wire the PE connections immediately after installing the devices as the first electrical connection. Now you insert all the other lines and connectors. For disassembly, release the PE connections as the last connection. 

For the use of residual current protective devices (RCD), refer to (➜ # 18). 

AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.4 EMI Noise Reduction** 

## **Electromagnetic Fields!** 

Electromagnetic radiation may, by acting on electrically conductive materials, lead to potential hazardous danger (warming, failure of implants). 

- Work on the electrical installation may only be performed by trained and qualified personnel, in compliance with the regulations for safety at work, and only with switched off mains supply, and secured against restart. 

- Grounding, equipotential bonding and radiation-reducing shields may not be removed. 

## **8.4.1 Recommendations for EMI noise reduction** 

The following guidelines will help you to reduce problems with electrical noise in your application. 

- **Ensure good connections between the cabinet components.** Connect the back panel and cabinet door to the cabinet body using several conductive braids. Never rely on hinges or mounting bolts for ground connections. 

- **Ensure good ground connection.** Connect from cabinet to proper earth ground. Ground leads should be the same gauge as the leads to main power, but must cover the regional legal requirements, example (➜ # 51). 

- **Use Kollmorgen cables.** Route power and control cables separately, Kollmorgen recommends a distance of at least 200 mm to improve interference immunity. **Ground the shielding at both ends.** Ground all shielding with large areas (low impedance), with metalized connector housings or shield connection clamps wherever possible. For cables entering a cabinet, connect shields on all 360° of the cable. Never connect a simple “pigtail.” For more information on shielding concepts, (➜ # 53). **With separate mains filter, maintain separation of leads entering and exiting the mains filter (line power filter).** Locate the filter as close as possible to the point where the incoming power enters the cabinet. If it is necessary for input power and motor leads to cross, cross them at 90°. **Observe cable length limits.** Maximum cable length for digital I/O supply (24V/DGND) is 3 m. If longer cables are required, you need to take care of additional EMC measures. **Feedback lines and Hybrid Cables may not be extended, since the shielding would be interrupted and the signal processing may be disturbed.** Install all feedback cables with an adequate cross-section, per IEC 60204 (➜ # 49) and use the requested cable material to reach maximum cable length. 

- **Splice cables properly.** If you need to divide cables, use connectors with metal backshells. Ensure that both shells connect along the full 360° of the shields. **Use differential inputs for analog signals.** Noise susceptibility in analog signals is greatly reduced by using differential inputs. Use twisted-pair, shielded signal lines, connecting shields on both ends. 

- **Cables between drives and filters or external regen resistors must be shielded.** Install all power cables with an adequate cross-section per IEC 60204 (➜ # 49) and use the requested cable material to reach maximum cable length. 

AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.4.2 Shielding with external shielding busbar** 

For best practice use of shielded cables Kollmorgen recommends a star point shield connection, for example, with a shielding busbar. 

## **8.4.2.1 Shielding Concept** 

Example with AKD2G-Sxx--6Vxx, EMC filter and external regen resistor. 

AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.4.2.2 Shielding Busbar** 

The power cable shields (line in, motor cable, external regen resistor) can be routed to an additional busbar via shield clamps. 

Kollmorgen recommends using Weidmüller KLBÜ shield clamps. 

A possible scenario for setting up a busbar for the above shield clamps is described below. 

1. Cut a busbar of the required length from a brass rail (cross-section 10 x 3 mm) and drill holes in it as indicated. All shield clamps required must fit between the drill holes. 

__ |ACAUTION| | Risk of injury due to the spring force of the coil spring. Use pincers. 

2. Squeeze together the coil spring and the supporting plate and push the busbar through the opening in the holder. 

3. Mount the busbar with the shield clamps fitted on the assembly plate. Use either metal spacer bushes or screws with nuts and accessories to maintain a spacing of 50 mm. Earth the busbar using a single conductor with a cross-section of at least 2.5 mm². 

4. Strip the external cable sheath to a length of approx. 30 mm, taking care not to damage the braided shield. Push the shield clamp up and route the cable to it via the busbar. | | NOTICE | Make sure there is good contact between the shield clamp and the braided shield. ~~oe~~ 

AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.4.3 Shielding connection to the drive** 

You can connect cable shielding directly to the drive by using grounding plates, shield connection clamps, and a motor connector with strain relief and grounding plate. 

## **8.4.3.1 Shielding Concept** 

Example with AKD2G-Sxx--7Vxx, dual-axis. 

AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.4.3.2 Grounding plates and shield connection clamps** 

A grounding plate is mounted to the drive. 

Use shield connection clamps (see accessories manual). These hook into the grounding plate and ensure optimum contact between the shield and the grounding plate. 

Kollmorgen recommends using Phoenix Contact SK14 shield clamps with cable clamp range of 6-13mm. 

## **8.4.3.3 Motor connector X1/X2 with shielding connection** 

Alternative connection for the motor power connection by mating connector with shield plate and strain relief. Kollmorgen motor power and hybrid motor cables are configured with shield plate. 

Strip the external cable sheath to a length of approx. 80 mm, taking care not to damage the braided shield. Push the braided shield (1) back over the cable and secure with a rubber sleeve (2) or shrink sleeve. 

Shorten all the wires apart from the protective earth (PE) wire (green/yellow) by about 20 mm so that the PE wire is now the longest wire. Strip all wires and fit wire end ferrules. 

Secure the braided shield of the cable with metal cable ties (3) and fasten the cable. 

Wire the connector as shown in the connection diagram. Plug in the connector to the socket on the front of the AKD2G and secure it with the red clip. 

AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.5 Connection Overview** 

## **8.5.1 Connector Position AKD2G-Sxx-6V** 

The graphics shows an AKD2G with supply voltage 110 V to 240 V. X2 is available with dual-axis drives only. Optional: I/O, F3 or DX (➜ # 27). 

AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.5.2 Connector Position AKD2G-Sxx-7V** 

The graphics shows an AKD2G with supply voltage 240 V to 480 V. X2 is available with dual-axis drives only. Optional: I/O, F3 or DX (➜ # 27). 

AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.5.3 Wiring overview, single axis drive** 

AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.5.4 Wiring overview, dual axis drive** 

AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.5.5 Connector pin assignments** 

Information to connectors and wiring (➜ # 48). 

## **8.5.5.1 X1 and X2: Motor, Brake, Feedback 1** 

oll 1(u) & 4 pin, pitch 7.62 mm plus 2x2 pin pitch 3.81 mmSpring clamps Motor power, Motor brake (X1: axis 1, X2: axis 2) edeOu oN). X1: Input for commutation feedback 1X2: Input for commutation feedback 2 ((➜➜ # 87)# 87) Wiring example: Om: DC Bus link (➜ # 77) Motor single cable connection (➜ # 81) Motor dual cable connection (➜ # 83) - , 

|**Pin**<br>1|**Label**<br>U|**Signal**<br>U|**Description**<br>Motor phase U|
|---|---|---|---|
|2|V|V|Motor phase V|
|3|W|W|Motor phase W|
||retention latch,shield screw|||
|5|PE|PE|Protective earth|
|B+|B+|BR+|Motor holding brake +|
|B-|B-|BR-|Motor holding brake -|
|F+|F+|COM+|SFD3 + or HIPERFACE DSL +|
|F-|F-|COM-|SFD3 - or HIPERFACE DSL -|



## **8.5.5.2 X3: Mains, regen resistor, DC-Bus** 

8 pin, pitch 7.62 mm Screw terminals Optional T version (in process) Mains supply, External regen resistor, DC Bus Wiring example: 

- Power supply (➜ # 67) DC Bus link (➜ # 77) External regen resistor (➜ # 79) 

|**Pin**<br>1|**Label**<br>PE|**Signal**<br>PE|**Description**<br>Protective earth|
|---|---|---|---|
|2|R|L1|3~ mains supply L1, 1~ supply L, DC supply +|
|3|S|L2|3~ mains supply L2|
|4|T|L3|3~ mains supply L3, 1~ supply N, DC supply -|
|5|Ri|RBint|internal regen resistor|
|6|RE|-RB|external regen resistor -|
|7|+DC|+DC (+RBext)|DC Bus link+ and/or external regen resistor +|
|8|-DC|-DC|DC Bus link -|



AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.5.5.3 X10: 24 VDC** 

2 pin, pitch 5.08 mm Spring clamps Optional T version 24 VDC supply voltage Wiring example: (➜ # 76) 

|**Pin**<br>1|**Signal**<br>+ 24 V|**Description**<br>+24 VDC supply voltage, PELV|
|---|---|---|
|2|GND|Ground for 24 VDC supply voltage, PELV|



## **8.5.5.4 X11, X12: Motion Bus** 

RJ45 with built-in green/red dual-color LED X12 IN port, X11 OUT port EtherCAT Interface Details: (➜ # 97) 

|**Pin**<br>1|**Signal**<br>Tx+|**Description**<br>Transmit +|**Pin**<br>5|**Signal**<br>Term.|**Description**<br>Termination|
|---|---|---|---|---|---|
|2|Tx-|Transmit -|6|Rx-|Receive -|
|3|Rx+|Receive +|7|Term.|Termination|
|4|Term.|Termination|8|Term.|Ttermination|



## **8.5.5.5 X13, X14: CAN bus (optional)** 

RJ-11 X14 IN port, X13 OUT port Up to 1 Mbit operation Node ID to be set by WorkBench Interface Details: (➜ # 99) 

|**Pin**<br>1|**Signal**<br>n.c.|**Description**<br>not used|**Pin**<br>4|**Signal**<br>CAN_low|**Description**<br>CAN bus low signal|
|---|---|---|---|---|---|
|2|Shield|Chassis|5|CAN_GND|CAN bus ground|
|3|CAN_high|CAN bus high signal|6|n.c.|not used|



## **8.5.5.6 X20: Service** 

=* RJ45 with built-in green and yellow LEDs 100/10 Mbit Ethernet TCP/IP =Py Supports auto-IP, DHCP and fixed IP addressing * Supports point-to-point (i.e. Auto-IP) and connection via network switches * Supports automatic discovery in WorkBench if in the same sub-net. 7 Interface Details: (➜ # 102) 

|**Pin**<br>1|**Signal**<br>Tx+|**Description**<br>Transmit +|**Pin**<br>5|**Signal**<br>Term.|**Description**<br>Termination|
|---|---|---|---|---|---|
|2|Tx-|Transmit -|6|Rx-|Receive -|
|3|Rx+|Receive +|7|Term.|Termination|
|4|Term.|Termination|8|Term.|Termination|



AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.5.5.7 X21: I/O, Feedback 4** 

- 2 x 11 pins (left column A, right column B), pitch 3.5 mm Spring clamps Analog and digital I/O 

- Input for feedback 4 (➜ # 87) Wiring examples: 

- Analog input (➜ # 105) 

   - Analog output (➜ # 106) 

   - Digital input (➜ # 107) 

   - Digital Output (➜ # 111) 

   - Feedback (➜ # 89) 

## **Digital I/O connectivity** 

|**Pin**<br>A1<br>a|**Signal**<br>Analog-In (AIN) 1 +<br>a|**Description**<br>Analog Input +/- 10 V|**Description**<br>Analog Input +/- 10 V|**Description**<br>Analog Input +/- 10 V|**Description**<br>Analog Input +/- 10 V|**Description**<br>Analog Input +/- 10 V|
|---|---|---|---|---|---|---|
|A2<br>~~|~~<br>||Analog-In (AIN) 1 -<br>~~|~~||||||
|A3*<br>~~|~~<br>a|Digital-In (DIN) 1<br>~~|~~<br>~~ee~~|Fast, isolated, sink, type EN 61131-2 type 1<br>~~ee~~|||||
|A4*<br>a|Digital-In (DIN) 2<br>ee|Fast, isolated, sink, type EN 61131-2 type 1<br>~~ee~~|||||
|A5<br>a <br>a|Digital-In (DIN) 3<br> ee<br>~~ee~~|Slow, isolated, sink, type EN 61131-2 type 1<br>~~ee~~<br>~~ee~~|||||
|A6<br>a|Digital-In (DIN) 4<br>ee|Slow, isolated, sink, type EN 61131-2 type 1<br>~~ee~~|||||
|A7<br>a <br>a<br>a|Digital-In (DIN) 5<br> ee<br>~~ee~~<br>ee|Slow, isolated, sink, type EN 61131-2 type 1<br>~~ee~~<br>~~ee~~<br>~~ee~~|||||
|A8<br>a|Digital-In (DIN) 6<br>ee|Slow, isolated, sink, type EN 61131-2 type 1<br>~~ee~~|||||
|A9<br>a <br>a<br>a|Digital-In (DIN) 7<br> ee<br>~~ee~~<br>ee|Slow, isolated, sink, type EN 61131-2 type 1<br>~~ee~~<br>~~ee~~<br>~~ee~~|||||
|A10<br>a<br>OO<br>Pe|Digital-In (DIN) 8<br>ee<br>~~Ell~~|Slow, isolated, sink, type EN 61131-2 type 1<br>~~ee~~<br>~~Ell~~<br>e~~e~~|||||
|A11<br>a <br>OO<br>Pe|STO-<br>A-<br>A1<br> ee<br>~~Ell~~|Slow, isolated, sink, fail-safe,<br>STO<br>~~ee~~<br>~~Ell~~|axis<br>~~ee~~<br>~~Ell~~|1<br>~~ee~~<br>~~Ell~~|channel<br>~~ee~~<br>~~Ell~~<br>e|A<br>~~ee~~<br>~~Ell~~<br>e~~e~~|
|OO~~Ell~~<br>e~~e~~<br>Pea<br>ee~~ee~~|||||||
|B1<br>Pea|Analog-Out (AOUT) 1<br>ee|Analog Output, 0 to +10 V<br>e~~e~~<br>~~ee~~|||||
|B2<br>a<br>a<br>a|AGND<br>ee<br>re<br>ee|Ground for analog I/O<br>~~ee~~<br>~~ee~~<br>~~ee~~|||||
|B3<br>a <br>a|+24 V<br> re<br>ee|+24 VDC for digital I/O and STO<br>~~ee~~<br>~~ee~~|||||
|B4<br>a<br>a<br>a|DGND<br>ee<br>re<br>ee|Ground for digital I/O and STO<br>~~ee~~<br>~~ee~~<br>~~ee~~|||||
|B5<br>a <br>a|Digital-Out (DOUT) 9 +<br> re<br>ee|Relay contact, normally open, 24 VDC, 1A<br>~~ee~~<br>~~ee~~|||||
|B6<br>a<br>a<br>a|Digital-Out (DOUT) 9 -<br>ee<br>re<br>ee|Relay contact, normally open, 24 VDC, 1A<br>~~ee~~<br>~~ee~~<br>~~ee~~|||||
|B7<br>a <br>a|Digital-Out (DOUT) 1<br> re<br>ee|Isolated, high-side, 100 mA<br>~~ee~~<br>~~ee~~|||||
|B8<br>a<br>a<br>a|Digital-Out (DOUT) 2<br>ee<br>re<br>ee|Isolated, high-side, 100 mA<br>~~ee~~<br>~~ee~~<br>~~ee~~|||||
|B9<br>a <br>a<br>re|Digital-Out (DOUT) 3<br> re<br>ee<br>re|Isolated, high-side, 100 mA<br>~~ee~~<br>~~ee~~<br>e~~e~~|||||
|B10<br>a<br>re<br>OO|Digital-Out (DOUT) 4<br>ee<br>re<br>~~Ell~~|Isolated, high-side, 100 mA<br>~~ee~~<br>e~~e~~<br>~~Ell~~<br>e~~r~~|||||
|B11<br>re<br>OO|STO-<br>B-<br>A1<br>re<br>~~Ell~~|Slow, isolated, sink, fail-safe,<br>STO<br>e<br>~~Ell~~|axis<br>e<br>~~Ell~~|1<br>e<br>~~Ell~~|channel<br>e~~e~~<br>~~Ell~~<br>e|B<br>~~e~~<br>~~Ell~~<br>e~~r~~|



***Feedback 4 connectivity, Step/Direction CW/CCW (input)** 

|**Pin**<br>A3|**Signal**<br>Step, CW|**Description**<br>Fast, isolated, sink, type EN 61131-2 type 1|
|---|---|---|
|A4|Direction, CCW|Fast, isolated, sink, type EN 61131-2 type 1|



AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.5.5.8 X22: I/O extended, EEO2, Feedback 5** 

- 2 x 10 pins (left column A, right column B), pitch 3.5 mm Spring clamps 

- Analog and digital I/O Input for feedback 5 (➜ # 87) Output for incremental encoder emulation (EEO2) Wiring examples: - Analog input (➜ # 105) 

   - Analog output (➜ # 106) Digital input (➜ # 107) Digital output (➜ # 111) 

   - Feedback (➜ # 90) Encoder emulation (EEO2) (➜ # 94) Master-Slave (➜ # 96) 

## **Digital I/O connectivity** 

|**Pin**<br>A12<br>C=|**Signal**<br>STO-<br>A-<br>A2<br>C=|**Description**<br>Slow, isolated, sink, fail-safe,<br>STO<br>axis<br>2<br>channel<br>A<br>eET—E———|**Description**<br>Slow, isolated, sink, fail-safe,<br>STO<br>axis<br>2<br>channel<br>A<br>eET—E———|**Description**<br>Slow, isolated, sink, fail-safe,<br>STO<br>axis<br>2<br>channel<br>A<br>eET—E———|**Description**<br>Slow, isolated, sink, fail-safe,<br>STO<br>axis<br>2<br>channel<br>A<br>eET—E———|**Description**<br>Slow, isolated, sink, fail-safe,<br>STO<br>axis<br>2<br>channel<br>A<br>eET—E———|
|---|---|---|---|---|---|---|
|A13<br>C=<br>a~~se~~<br>a|Digital-In (DIN) 9<br>C=<br>~~se~~<br>es|Slow, isolated, sink, type EN 61131-2 type 1<br>eET—E———<br>~~se~~|||||
|A14<br>a|Digital-In (DIN) 10<br>es|Slow, isolated, sink, type EN 61131-2 type 1|||||
|A15<br>a<br>a~~se~~<br>a|Digital-In (DIN) 11<br>es<br>~~se~~<br>es|Slow, isolated, sink, type EN 61131-2 type 1<br>~~se~~|||||
|A16<br>a|Digital-In (DIN) 12<br>es|Slow, isolated, sink, type EN 61131-2 type 1|||||
|A17<br>a<br>a~~s~~|AGND<br>es<br>~~s~~|Ground for analog I/O<br>~~se~~|||||
|A18<br>~~es~~|Analog-In (AIN) 2+<br>~~es~~|Analog Input, +/- 10 V<br>~~es~~|||||
|A19<br>~~es~~<br>a|Analog-In (AIN) 2-<br>~~es~~||||||
|A20*<br>a|Digital-In/Out (DIO) 1 +<br>es|RS485 input or output|||||
|A21*<br>~~ss~~|Digital-In/Out (DIO) 1 -<br>~~ss~~|RS485 input or output<br>~~ss~~|||||
|~~|~~<br>LZllL,eeeeTET—T—E——ER—Ea|||||||
|B12<br>LZ|STO-<br>B-<br>A2<br>LZllL,eeeeTET—T—E——ER—Ea|Slow, isolated, sink, fail-safe,<br>STO<br>llL,eeeeTET—T—E——ER—Ea|axis<br>llL,eeeeTET—T—E——ER—Ea|2<br>llL,eeeeTET—T—E——ER—Ea|channel<br>llL,eeeeTET—T—E——ER—Ea|B<br>llL,eeeeTET—T—E——ER—Ea|
|B13<br>LZ<br>a|Digital-Out (DOUT) 5<br>LZllL,eeeeTET—T—E——ER—Ea<br>es|Isolated, high-side, 100 mA<br>llL,eeeeTET—T—E——ER—Ea|||||
|B14<br>a<br>a|Digital-Out (DOUT) 6<br>es<br>~~s~~|Isolated, high-side, 100 mA<br>~~se~~|||||
|B15<br>~~e~~|Digital-Out (DOUT) 7 +<br>~~e~~|Fast, isolated, sink or source, 100 mA<br>~~es~~<br>|||||
|B16<br>~~e~~<br>a|Digital-Out (DOUT) 7 -<br>~~e~~<br>||||||
|B17<br>~~es~~|Digital-Out (DOUT) 8 +<br>~~es~~|Fast, isolated, sink or source, 100 mA<br>~~es~~<br>|||||
|B18<br>~~es~~<br>a<br>a|Digital-Out (DOUT) 8 -<br>~~es~~<br>es<br>||||||
|B19<br>a<br>a|Analog-Out (AOUT) 2<br>es<br>|Analog Output, 0 to +10 V<br>|||||
|B20*<br>a<br>a|Digital-In/Out (DIO) 2 +<br>es<br>~~se~~<br>es|RS485 input or output<br>~~se~~|||||
|B21*<br>a|Digital-In/Out (DIO) 2 -<br>es|RS485 input or output|||||



***Feedback 5 connectivity (input) *EEO2 connectivity (output)** 

|**Pin**||**Incremental**||**Step/Dir**||**CW/CCW**||**Pin**||**Incremental Encoder**|
|---|---|---|---|---|---|---|---|---|---|---|
|||**Encoder**||||||A20||A+|
|A20||Track A +||Step +||CW +||A21||A -|
|A21||Track A -||Step -||CW -||B20||B+|
|B20||Track B +||Dir +||CCW +||B21||B -|
||||||||||||
|B21||Track B -||Dir -||CCW -|||||



AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.5.5.9 X23: Feedback 3, EEO1, I/O** 

- Sub-D high density 15 pin, female 

- Input for feedback 3 (➜ # 87) 

- Output for incremental encoder emulation (EEO1) 

- Additional Digital-In/Out 

- Wiring examples: 

   - Feedback (➜ # 91) Encoder emulation (EEO1) (➜ # 95) Master-Slave (➜ # 96) Digital input (➜ # 107) Digital output (➜ # 111) 

## **Feedback 3 connectivity (input)** 

|**X23**<br>**Pin**<br>1<br>a|**SFD**<br>-|**Resol-**<br>**ver**<br>-<br>se|**BiSS**<br>**B**<br>-<br>se|**BiSS**<br>**C**<br>-<br>ee|**EnDAT**<br>**2.1**<br>-<br>ee|**EnDAT**<br>**2.2**<br>-|**HIPER**<br>**FACE**<br>-<br>GG|**Sine/**<br>**Cos**<br>-<br>GG|**Sine/**<br>**Cos**<br>**+Hall**<br>Hall U<br>GG|**Incr.**<br>**Enc.**<br>-<br>GG|**Incr.**<br>**Enc.**<br>**+Hall**<br>Hall U|**Hall**<br>Hall U<br>GO|**Smart**<br>**Abs**<br>-<br>GO|**Step/**<br>**Dir**<br>-|**CW/**<br>**CCW**<br>-|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|2<br>a<br>a<br>a|-<br>|-<br>se<br>se<br>|CLK+<br>se <br>se <br>|CLK+<br> ee<br> ee<br>|CLK+<br>ee<br>ee<br>~~QO~~<br>|CLK+<br>~~QO~~<br>|-<br>GG<br>~~QO~~<br>|-<br>GG<br>~~QO~~|Hall V<br>GG|-<br>GG|Hall V|Hall V<br>GO<br>OO|-<br>GO<br>OO|Step+<br>OO|CW+|
|3<br>~~ee~~<br>a<br>a|-<br>~~ee~~<br>ee|-<br>~~ee~~<br>ee|CLK-<br>~~ee~~<br>ee|CLK-<br>~~ee~~<br>ee|CLK-<br>~~ee~~<br>~~QO~~<br>QO|CLK-<br>~~ee~~<br>~~QO~~<br>QO|-<br>~~ee~~<br>~~QO~~<br>QO|-<br>~~ee~~<br>~~QO~~|Hall W<br>~~ee~~|-<br>~~ee~~<br>I|Hall W<br>~~ee~~<br>I|Hall W<br>~~ee~~<br>OO<br>GO|-<br>~~ee~~<br>OO<br>GO|Step-<br>~~ee~~<br>OO<br>GO|CW-<br>~~ee~~|
|4<br>a <br>a<br>a|SEN+<br> ee|-<br>ee<br>es|SEN+<br>ee<br>ee|SEN+<br>ee<br>ee|SEN+<br>~~QO~~<br>QO<br>ee|SEN+<br>~~QO~~<br>QO|SEN+<br>~~QO~~<br>QO<br>OQ|SEN+<br>~~QO~~<br>OQ|SEN+<br>OQ|SEN+<br>I<br>(QO|SEN+<br>I<br>(QO|-<br>OO<br>GO<br>(QO|SEN+<br>OO<br>GO<br>(QO|-<br>OO<br>GO|-|
|5<br> <br>a<br>a|SEN-<br> ee|-<br>ee <br>es|SEN-<br> ee<br>ee|SEN-<br>ee<br>ee|SEN-<br>QO <br>ee|SEN-<br> QO|SEN-<br>QO<br>OQ|SEN-<br>OQ|SEN+<br>OQ|SEN+<br>I<br>(QO|SEN+<br>I <br>(QO|-<br> GO<br>(QO|SEN+<br>GO<br>(QO|-<br>GO|-|
|6<br>a<br>a|COM+<br>|R1 Ref+<br>es <br>se<br>|DAT+<br> ee<br>se <br>|DAT+<br>ee<br> ee<br>|DAT+<br>ee<br>ee<br>~~QO~~<br>|DAT+<br>~~QO~~<br>|DAT+<br>OQ<br>~~QO~~<br>|Zero+<br>OQ<br>~~QO~~|Zero+<br>OQ|Zero+<br> (QO|Zero+<br>(QO|-<br>(QO<br>OO|SD+<br>(QO<br>OO|Dir+<br>OO|CCW+|
|7<br>~~ee~~<br>a<br>a|COM-<br>~~ee~~<br>ee|R2 Ref-<br>~~ee~~<br>ee|DAT-<br>~~ee~~<br>ee|DAT-<br>~~ee~~<br>ee|DAT-<br>~~ee~~<br>~~QO~~<br>QO|DAT-<br>~~ee~~<br>~~QO~~<br>QO|DAT-<br>~~ee~~<br>~~QO~~<br>QO|Zero-<br>~~ee~~<br>~~QO~~|Zero-<br>~~ee~~|Zero-<br>~~ee~~<br>I|Zero-<br>~~ee~~<br>I|-<br>~~ee~~<br>OO<br>GO|SD-<br>~~ee~~<br>OO<br>GO|Dir-<br>~~ee~~<br>OO<br>GO|CCW-<br>~~ee~~|
|8<br>a <br>a<br>a|-<br> ee|Th+<br>ee<br>es|Th+<br>ee<br>ee|-<br>ee<br>ee|Th+<br>~~QO~~<br>QO<br>ee|-<br>~~QO~~<br>QO|Th+<br>~~QO~~<br>QO<br>OQ|Th+<br>~~QO~~<br>OQ|Th+<br>OQ|Th+<br>I<br>(QO|Th+<br>I<br>(QO|Th+<br>OO<br>GO<br>(QO|Th+<br>OO<br>GO<br>(QO|Th+<br>OO<br>GO|Th+|
|9<br> <br>a<br>a|-<br> ee|Th-<br>ee <br>es|Th-<br> ee<br>ee|-<br>ee<br>ee|Th-<br>QO <br>ee|-<br> QO|Th-<br>QO<br>OQ|Th-<br>OQ|Th-<br>OQ|Th-<br>I<br>(QO|Th-<br>I <br>(QO|Th-<br> GO<br>(QO|Th-<br>GO<br>(QO|Th-<br>GO|Th-|
|10<br>a|+5 V|-<br>es <br>se|+5 V<br> ee<br>se|+5 V<br>ee<br> ee|+5 V<br>ee<br>ee|+5 V|+5 V<br>OQ|+5 V<br>OQ|+5 V<br>OQ|+5 V<br> (QO|+5 V<br>(QO|+5 V<br>(QO|+5 V<br>(QO|+5 V|+5 V|
|11<br>ee|0 V<br>ee|-<br>ee|0 V<br>ee|0 V<br>ee|0 V<br>QQ|0 V<br>QQ|0 V<br>QQ|0 V<br>QQ|0 V|0 V|0 V|0 V<br>OO|0 V<br>OO|0 V|0 V|
|12<br>a<br>a|-<br>se|S1 SIN+<br>se <br>es|A+<br> ee<br>ee|-<br>ee<br>ee|A+<br>QQ<br>ee|-<br>QQ|SIN+<br>QQ<br>OQ|A+<br>OQ|A+<br>OQ|A+<br>(QO|A+<br>OO<br>(QO|-<br>OO<br>(QO|-<br>OO<br>(QO|-<br>OO|-|
|13<br>a|-|S3 SIN-<br>es|A-<br>ee|-<br>ee|A-<br>ee|-|SIN-<br>OQ|A-<br>OQ|A-<br>OQ|A-<br>(QO|A-<br>(QO|-<br>(QO|-<br>(QO|-|-|
|14<br>a<br>a<br>ee|-<br>ee|S2 COS+<br>es <br>se<br>ee|B+<br> ee<br>se <br>es|-<br>ee<br> ee<br>es|B+<br>ee<br>ee<br>sn|-<br>sn|COS+<br>OQ|B+<br>OQ|B+<br>OQ|B+<br> (QO|B+<br>(QO|-<br>(QO|-<br>(QO|-|-|
|15<br>ee|-<br>ee|S4 COS-<br>ee|B-<br>es|-<br>es|B-<br>sn|-<br>sn|COS-|B-|B-|B-|B-|-|-|-|-|



CLK = CLOCK, DAT = DATA, SEN = SENSE, Th = Thermal control 

## **EEO1 connectivity (output) Digital I/O connectivity** 

|**Pin**|**Incremental**<br>**Encoder**||**Pin**<br>2|**Digital I/0**<br>Digital-In/Out 6 +|
|---|---|---|---|---|
|6|Zero+||3|Digital-In/Out 6 -|
|7|Zero-||6|Digital-In/Out 5 +|
|11|0 V||7|Digital-In/Out 5 -|
|12|A +||10|+5 V|
|13|A-||11|0 V|
|14|B+||12|Digital-In/Out 3 +|
|15|B-||13|Digital-In/Out 3 -|
||||14|Digital-In/Out 4 +|
||||15|Digital-In/Out 4 -|



AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.5.5.10 X41: SFA Feedback converter, EEO3/EEO4 (accessory)** 

- Sub-D high density 15 pin, female 1 m cable, 3 flying leads with ferrules for connection to X1, X2 

- Input for electronic gearing 

- When connected to X1: Input for feedback 1 (➜ # 87) When connected to X2: Input for feedback 2 (➜ # 87) 

- Output for incremental encoder emulation (EEO3 / EEO4) (➜ # 95) 

- SFA Adapter converts conventional feedback signals to 2 wire feedback format Wiring examples: Feedback and Encoder emulation (➜ # 92) Master-Slave (➜ # 96) 

## **Feedback 1/2 connectivity (input)** 

|**X41**<br>**Pin**<br>1<br>a<br>a|**SFD**<br>-<br>a<br>a|**Resol-**<br>**ver**<br>-<br>a<br>ee|**BiSS**<br>**B**<br>-<br>a<br>ee|**EnDAT**<br>**2.1**<br>-<br>ss<br>ee|**EnDAT**<br>**2.2**<br>-<br>ss<br>ee|**HIPER-**<br>**FACE**<br>-<br>sses<br>ee|**Sine/**<br>**Cos**<br>-<br>es<br>es|**Sine/**<br>**Cos**<br>**+Hall**<br>Hall U<br>ee<br>es|**Incr.**<br>**Enc.**<br>-<br>ee<br>es|**Incr.**<br>**Enc.**<br>**+Hall**<br>Hall U<br>Gs<br>es|**Hall**<br>Hall U<br>es|**Smart**<br>**Abs**<br>-|**Step/**<br>**Dir**<br>-|**CW/**<br>**CCW**<br>-|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|2<br>a <br>a<br>a|-<br> a<br>a<br>a|-<br>a <br>ee<br>ee|CLK+<br> a <br>ee<br>es|CLK+<br> ss<br>ee<br>es|CLK+<br>ss<br>ee<br>es|-<br>sses<br>ee<br>ee|-<br>es <br>es<br>es|Hall V<br> ee<br>es<br>es|-<br>ee<br>es<br>es|Hall V<br>Gs<br>es<br>ss|Hall V<br>es<br>ss|-|Step+|CW+|
|3<br>a <br>a<br>a|-<br> a<br>a<br>a|-<br>ee <br>ee<br>rei|CLK-<br> ee <br>es<br>i|CLK-<br> ee<br>es<br>es|CLK-<br>ee <br>es<br>es|-<br> ee<br>ee<br>ee|-<br>es<br>es<br>Gs|Hall W<br>es <br>es<br>ss|-<br> es <br>es<br>ss|Hall W<br> es <br>ss<br>QO|Hall W<br> es<br>ss|-|Step-|CW-|
|4<br>a <br>a<br>ee|SEN+<br> a<br>a<br>ee|-<br>ee <br>rei<br>eeie|SEN+<br> es<br>i<br>ie|SEN+<br>es<br>es<br>eees|SEN+<br>es <br>es<br>es|SEN+<br> ee <br>ee<br>ss|SEN+<br> es <br>Gs<br>ss|SEN+<br> es <br>ss<br>ss|SEN+<br> es <br>ss<br>QQ|SEN+<br> ss<br>QO<br>QQ|-<br>ss<br>GO|SEN+<br>GO|-|-|
|5<br>a <br>ee<br>a|SEN-<br> a<br>ee<br>a|-<br>rei<br>eeie<br>ee|SEN-<br>i<br>ie<br>ee|SEN-<br>es<br>eees<br>ee|SEN-<br>es <br>es<br>ee|SEN-<br> ee<br>ss<br>ee|SEN-<br>Gs <br>ss<br>es|SEN+<br> ss<br>ss<br>es|SEN+<br>ss<br>QQ<br>es|SEN+<br>QO<br>QQ<br>es|-<br>GO<br>es|SEN+<br>GO|-|-|
|6<br>ee<br>a<br>a|COM+<br>ee<br>a<br>a|R1 Ref+<br>eeie<br>ee<br>ee|DAT+<br>ie <br>ee<br>es|DAT+<br> eees<br>ee<br>es|DAT+<br>es <br>ee<br>es|DAT+<br> ss<br>ee<br>ee|Zero+<br>ss<br>es<br>es|Zero+<br>ss<br>es<br>es|Zero+<br>QQ<br>es<br>es|Zero+<br>QQ<br>es<br>ss|-<br>GO<br>es<br>ss|SD+<br>GO|Dir+|CCW+|
|7<br>a <br>a<br>a|COM-<br> a<br>a<br>a|R2 Ref-<br>ee <br>ee<br>rei|DAT-<br> ee <br>es<br>i|DAT-<br> ee<br>es<br>es|DAT-<br>ee <br>es<br>es|DAT-<br> ee<br>ee<br>ee|Zero-<br>es<br>es<br>Gs|Zero-<br>es <br>es<br>ss|Zero-<br> es <br>es<br>ss|Zero-<br> es <br>ss<br>QO|-<br> es<br>ss|SD-|Dir-|CCW-|
|8<br>a <br>a<br>ee|-<br> a<br>a<br>ee|Th+<br>ee <br>rei<br>eeie|Th+<br> es<br>i<br>ie|Th+<br>es<br>es<br>eees|-<br>es <br>es<br>es|Th+<br> ee <br>ee<br>ss|Th+<br> es <br>Gs<br>ss|Th+<br> es <br>ss<br>ss|Th+<br> es <br>ss<br>QQ|Th+<br> ss<br>QO<br>QQ|Th+<br>ss<br>GO|Th+<br>GO|Th+|Th+|
|9<br>a <br>ee<br>a|-<br> a<br>ee<br>a|Th-<br>rei<br>eeie<br>ee|Th-<br>i<br>ie<br>eeie|Th-<br>es<br>eees<br>ie|-<br>es <br>es|Th-<br> ee<br>ss<br>es|Th-<br>Gs <br>ss<br>es|Th-<br> ss<br>ss<br>eses|Th-<br>ss<br>QQ<br>es|Th-<br>QO<br>QQ<br>es|Th-<br>GO<br>es|Th-<br>GO|Th-|Th-|
|10<br>ee<br>a<br>a|+5 V<br>ee<br>a<br>a|-<br>eeie<br>ee<br>eeee|+5 V<br>ie <br>eeie<br>ee|+5 V<br> eees<br>ie<br>es|+5 V<br>es <br>es|+5 V<br> ss<br>es<br>eees|+5 V<br>ss<br>es<br>es|+5 V<br>ss<br>eses<br>es|+5 V<br>QQ<br>es<br>es|+5 V<br>QQ<br>es<br>es|+5 V<br>GO<br>es|+5 V<br>GO|+5 V|+5 V|
|11<br>a <br>a<br>a|0 V<br> a<br>a<br>a|-<br>ee <br>eeee<br>rei|0 V<br> eeie<br>ee<br>i|0 V<br>ie<br>es<br>es|0 V<br>es<br>es|0 V<br>es<br>eees<br>ee|0 V<br>es <br>es<br>Gs|0 V<br> eses<br>es<br>ss|0 V<br>es <br>es<br>ss|0 V<br> es<br>es<br>QO|0 V<br>es|0 V|0 V|0 V|
|12<br>a <br>a<br>ee|-<br> a<br>a<br>ee|S1 SIN+<br>eeee<br>rei<br>eeie|A+<br>ee <br>i<br>ie|A+<br> es<br>es<br>eees|-<br>es <br>es<br>es|SIN+<br> eees<br>ee<br>ss|A+<br>es<br>Gs<br>ss|A+<br>es <br>ss<br>ss|A+<br> es<br>ss<br>QQ|A+<br>es<br>QO<br>QQ|-<br>GO|-<br>GO|-|-|
|13<br>a <br>ee<br>a|-<br> a<br>ee<br>a|S3 SIN-<br>rei<br>eeie<br>ee|A-<br>i<br>ie<br>eei|A-<br>es<br>eees<br>i|-<br>es <br>es<br>es|SIN-<br> ee<br>ss<br>ee|A-<br>Gs <br>ss<br>es|A-<br> ss<br>ss<br>es|A-<br>ss<br>QQ<br>es|A-<br>QO<br>QQ<br>es|-<br>GO<br>es|-<br>GO|-|-|
|14<br>ee<br>a<br>a|-<br>ee<br>a<br>ee|S2 COS+<br>eeie<br>ee<br>ee|B+<br>ie <br>eei<br>ee|B+<br> eees<br>i<br>eees|-<br>es <br>es<br>es|COS+<br> ss<br>ee<br>es|B+<br>ss<br>es<br>es|B+<br>ss<br>es<br>es|B+<br>QQ<br>es<br>es|B+<br>QQ<br>es<br>dO|-<br>GO<br>es<br>dO|-<br>GO<br>dO|-|-|
|15<br>a <br>a|-<br> a<br>ee|S4 COS-<br>ee<br>ee|B-<br>eei<br>ee|B-<br>i <br>eees|-<br> es<br>es|COS-<br>ee <br>es|B-<br> es<br>es|B-<br>es <br>es|B-<br> es<br>es|B-<br>es<br>dO|-<br>es<br>dO|-<br>dO|-|-|



CLK = CLOCK, DAT = DATA, SEN = SENSE, Th = Thermal control 

## **EEO3 / EEO4 connectivity (output)** 

|**X41 Pin**<br>6|**Incremental**<br>**Encoder**<br>Zero+|
|---|---|
|7|Zero-|
|11|0 V|
|12|A +|
|13|A-|
|14|B+|
|15|B-|



AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.6 Power and Logic Voltage Supply (X3/X10)** 

## **8.6.1 Mains power supply (X3)** 

Drives in the AKD2G series can be supplied as follows: 

## **AKD2G-Sxx-6V** 

1, 2 or 3 phase industrial AC supply networks: 120 V or 240 VAC nominal. DC supply networks: 17 VDC to 370 VDC. 

## **AKD2G-Sxx-7V** 

3 phase industrial AC supply networks: 240 V, 400 V or 480 VAC nominal. DC supply networks: 34 VDC to 740 VDC. 

Connection to other voltage types of AC supply networks is possible with an additional isolating transformer. 

Periodic overvoltages between phases (L1, L2, L3) and the PE/housing of the drive must not exceed 1000 V peak. In accordance with IEC 61800, voltage spikes (< 50 µs) between phases must not exceed 1000 V. Voltage spikes (< 50 µs) between a phase and the PE/housing must not exceed 2000 V. 

8 pin, pitch 7.62 mm optional T version Wiring example: 1 phase AC supply (➜ # 68) 

| - 2 phase AC supply (➜ # 68) ae 3 phase AC supply (➜ # 69) DC supply (➜ # 70) ,[7] * AKD2G-Sxx-6V requires external EMC filter for use in | industrial environment, product category C. t Mating connector data (➜ # 48) t Fusing with different system structures (➜ # 71) ff 

|**Pin**<br>1|**Label**<br>PE|**Signal**<br>PE|**1~ Supply**<br>Protective earth|**2~Supply**<br>Protective earth|**3~ Supply**<br>Protective earth|**DC Supply**<br>Protective earth|
|---|---|---|---|---|---|---|
|2|R|L1|Phase L1|Phase L1|Phase L1|+ DC|
|3|S|L2|n.c.|n.c.|Phase L2|n.c.|
|4|T|L3|Neutral N|Phase L2|Phase L3|- DC|



For DC supply: observe notes (➜ # 70). 

AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.6.1.1 Wiring examples mains power supply** 

## **One phase AC mains (AKD2G-Sxx-6V)** 

- Directly to one phase supply network with neutral line. 

- Activate single phase supply (VBUS.THREEPHASE = 0). 

- Set VBUS.ACNOMINAL to desired nominal AC line voltage for lines other than nominal rated VAC. 

- AC line filtering to be provided by the user. Use shielded cable between filter and drive. 

## **Two phases AC mains (AKD2G-Sxx-6V)** 

- Directly to two-phase supply network without neutral line. 

- Activate single phase supply (VBUS.THREEPHASE = 0). 

- Set VBUS.ACNOMINAL to desired nominal AC line voltage for lines other than nominal rated VAC. 

- AC line filtering to be provided by the user. Use shielded cable between filter and drive. 

AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **Three phases AC mains (all AKD2G-Sxx-)** 

- Directly to 3-phase supply network. 

- Activate 3-phase supply (VBUS.THREEPHASE = 1). 

- Set VBUS.ACNOMINAL to desired nominal AC line voltage for lines other than nominal rated VAC. 

- AC line filtering for AKD2G-Sxx-6V to be provided by the user. Use shielded cable. 

AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **DC Supply (all AKD2G-Sxx-)** 

- Activate DC supply (VBUS.DCOPERATION = 1). 

- Set VBUS.ACNOMINAL to desired DC voltage divide by √2 for VDC other than nominal rated. 

- Any DC supply filtering for AKD2G-Sxx-6V to be provided by the user. 

## DC Supply to mains lines R/T (L1/L3) 

DC power source is connected to the drive AC line inputs. This wiring provides soft start of the energy storage capacitors inside the drive and the AC rectifier diodes prevents motor regeneration energy from returning to the dc power source. That is, by powering the drive from the AC line input connections, the drive’s energy absorption and energy dissipation mechanisms can work normally. 

## DC Supply to DC Bus lines X3/7-8 

When wiring DC power supply to the drive DC Bus terminals X3 pins 7 and 8, the user is responsible for current and power management using additional external devices. 

## **User resposibility:** 

- The power supply system design must ensure inrush current protection by limiting input current during power up. 

- Provide a means to safely absorb energy from the motor when slowing down/regenerating. If the DC power source is a battery energy absorption should just work. 

- DC supply polarity must be properly wired. Improper polarity of DC power will damage the drive and void warranty. 

AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.6.1.2 Fusing** 

## **Fuse types** 

- UL fuses: Class J, 600 VAC 200 kA (SCCR rating), time-delay. The fuse must be UL and CSA listed, UL recognized is not sufficient. Alternate fuses and breakers to Class J must have similar or better Ip and I²T performance per UL 508A SB4.2 at the necessary SCCR rating. 

- CE fuses: types gS or gG, 400 V/500 V, time-delay 

- Fuse holders: Combined with the standard fuse blocks, finger safe fuse holders must be used according to IEC 60529. 

- Automatic circuit breakers: max. rating is 30 A, observe SCCR rating 

- Group installation fusing: max. rating of fuses or breakers for group installation is 30 A 

## **AC supply, single drives, line fusing** 

- F1, F2, F3: depends on sum of current and cabinet requirements. 

- Filters for special EMC requirements only (➜ # 146). 

- FN1, FN2, FN3 maximum rating: 30 A. 

- FN1, FN2, FN3 recommended rating see table below: 

|**Drive**<br>**Model**<br>AKD2G-Sxx-6V03S|**FN1, FN2, FN3:**<br>**Ampere rating**<br>10 A (Time-Delay)|**Example class J**<br>**Eaton**<br>LPJ10SP/DFJ10|**Example class J**<br>**Ferraz Shawmut**<br>AJT10/HSJ10|
|---|---|---|---|
|AKD2G-Sxx-6V06S<br>AKD2G-Sxx-6V03D|10 A (Time-Delay)|LPJ10SP/DFJ10|AJT10/HSJ10|
|AKD2G-Sxx-6V12S<br>AKD2G-Sxx-6V06D|15 A (Time-Delay)|LPJ15SP/DFJ15|AJT15/HSJ15|
|AKD2G-Sxx-7V03S|10 A (Time-Delay)|LPJ10SP/DFJ10|AJT10/HSJ10|
|AKD2G-Sxx-7V06S<br>AKD2G-Sxx-7V03D|10 A (Time-Delay)|LPJ10SP/DFJ10|AJT10/HSJ10|
|AKD2G-Sxx-7V12S<br>AKD2G-Sxx-7V06D|15 A (Time-Delay)|LPJ15SP/DFJ15|AJT15/HSJ15|



AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

**AC supply, group of drives, line fusing** 

- F1, F2, F3: depends on sum of current and cabinet requirements. Filters for special EMC requirements only (➜ # 146). 

- FN1, FN2, FN3 maximum rating: fuse size for group installation is limited to 30 A max. FN1, FN2, FN3 rating should be 1.25 * sum current. 

|**Group sum current**<br>6 A to 30 A|**FN1, FN2, FN3:**<br>**Ampere rating**<br>30 A (Time-Delay)|**Example class J**<br>**Eaton**<br>LPJ30SP/DFJ30|**Example class J**<br>**Ferraz Shawmut**<br>AJT30/HJ30|
|---|---|---|---|



AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **AC supply, single drives, automatic circuit breakers** 

F1, F2, F3: depends on sum of current and cabinet requirements. 

Filters for special EMC requirements only (➜ # 146). FN maximum rating: 30 A 

FN recommended rating and regional approvals see table below: 

|**Drive Model**<br>AKD2G-Sxx-6V|**Ampere**<br>**rating**<br>15 A|**SCCR**<br>**rating**<br>35 kA|**Example UL**<br>**Eaton or ABB**<br>SU203M-K30|**Example CE**<br>**Siemens**<br>3VA51954EC310|
|---|---|---|---|---|
|AKD2G-Sxx-7V|15 A|65 kA|FDC3015L|3VA51956EC310|



AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **AC supply, group of drives, automatic circuit breakers** 

- F1, F2, F3: depends on sum of current and cabinet requirements. 

- Filters for special EMC requirements only (➜ # 146). 

- FN maximum rating: circuit breaker size for group installation is limited to 30 A max. FN rating should be 1.25 * sum current. 

FN recommended rating and regional approvals see table below: 

|**Group sum current**<br>**Ampere**<br>**rating**<br>**SCCR**<br>**rating**<br>**Example UL**<br>**Eaton or ABB**<br>**Example CE**<br>**Siemens**<br>**AKD2G-Sxx-6V**|**Group sum current**<br>**Ampere**<br>**rating**<br>**SCCR**<br>**rating**<br>**Example UL**<br>**Eaton or ABB**<br>**Example CE**<br>**Siemens**<br>**AKD2G-Sxx-6V**|**Group sum current**<br>**Ampere**<br>**rating**<br>**SCCR**<br>**rating**<br>**Example UL**<br>**Eaton or ABB**<br>**Example CE**<br>**Siemens**<br>**AKD2G-Sxx-6V**|**Group sum current**<br>**Ampere**<br>**rating**<br>**SCCR**<br>**rating**<br>**Example UL**<br>**Eaton or ABB**<br>**Example CE**<br>**Siemens**<br>**AKD2G-Sxx-6V**|**Group sum current**<br>**Ampere**<br>**rating**<br>**SCCR**<br>**rating**<br>**Example UL**<br>**Eaton or ABB**<br>**Example CE**<br>**Siemens**<br>**AKD2G-Sxx-6V**|
|---|---|---|---|---|
|6 A to 9A|15 A|10 kA|SU203M-K15|3VA51954EC310A|
|12 A to 15 A|20 A|10 kA|SU203M-K20|3VA51204EC310A|
|18 A to 24 A|30 A|10 kA|SU203M-K30|3VA51304EC310A|
|27 A to 36 A|30 A|10 kA|SU203M-K30|3VA51304EC310A|
|**AKD2G-Sxx-7V**|||||
|6 A to 9A|15 A|100 kA|FDC3015L|3VA51956EC310A|
|12 A to 15 A|20 A|100 kA|FDC3020L|3VA51206EC310A|
|18 A to 24 A|30 A|100 kA|FDC3030L|3VA51306EC310A|
|27 A to 36 A|30 A|100 kA|FDC3030L|3VA51306EC310A|



AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **DC supply, single drives, line fusing** 

- F1, F2, F3: depends on sum of current and cabinet requirements. 

- Filters for special EMC requirements only (➜ # 146). FN1, FN2 maximum rating 30 A 

FN1, FN2 recommended rating see table below: 

|**Drive Model**<br>AKD2G-Sxx-6V03S|**Ampere rating**<br>10 A (Time-Delay)|**Example UL**<br>**Eaton**<br>DFJ-10|**Example CE**<br>**Mersen**<br>HP6M10|
|---|---|---|---|
|AKD2G-Sxx-6V06S<br>AKD2G-Sxx-6V03D|15 A (Time-Delay)|DFJ-15|HP6M15|
|AKD2G-Sxx-6V12S<br>AKD2G-Sxx-6V06D|15 A (Time-Delay)|DFJ-15|HP6M15|
|AKD2G-Sxx-7V03S|10 A (Time-Delay)|FWP-10B|HP10M10|
|AKD2G-Sxx-7V06S<br>AKD2G-Sxx-7V03D|10 A (Time-Delay)|FWP-10B|HP10M10|
|AKD2G-Sxx-7V12S<br>AKD2G-Sxx-7V06D|15 A (Time-Delay)|FWP-15B|HP10M15|



AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.6.2 Auxiliary voltage power supply 24 VDC (X10)** 

The following diagram describes external 24 VDC power supply (PELV). The required supply current rating depends on the use of motor brake (➜ # 33) or (➜ # 35). 

—— ; . 2 pin, pitch 5.08 mm =_,= me2 X10 ° optional T version 3 van ® 7 Mating connector data (➜ # 48) Undervoltage fault limit 19 V —_ : ° Overvoltage fault limit 30 V | Top View ao 6 **Pin Signal Description** 1 + 24 V +24 VDC supply voltage, PELV 2 GND Ground for 24 VDC supply voltage, PELV 

|**24 V supply (PELV)**<br>Aux. voltage supply (PELV)|**Units**<br>VDC|**Input data**<br>**single axis**<br>**Input data**<br>**dual axis**<br>24 V (±10%, check voltage drop)|**Input data**<br>**single axis**<br>**Input data**<br>**dual axis**<br>24 V (±10%, check voltage drop)|
|---|---|---|---|
|- control current without motor brake|A|1|1.25|
|- control current with one motor brake|A|3.5|3.75|



## **8.6.2.1 Fusing** 

Use 24 VDC supply manufacturers recommendation for fusing. 

## **8.6.2.2 Wiring example 24 VDC supply** 

Example for three phase power supply unit. 

AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.7 DC Bus link (X3)** 

The DC bus link can be connected in parallel so that the power returned from slowing down motors is divided between all the drives that are connected to the same DC bus link circuit. Every drive must have its own power connection to mains voltage sharing the same branch, over current protection devices, even if the DC bus link is used. Drives working generatively very often should be placed beside drives, which need energy. That reduces current flow on longer distances. 

The sum of the rated currents for all drives connected in parallel to an AKD2G must not exceed 48 A. 

Examples:12S-12S-12D-12D-12D or 06D-12S-12D-06D-06D-03S-03S-03S 

Wiring: Use 6 mm² unshielded single cores with a max. length of 200 mm; use 6 mm² shielded cables for longer lengths. In this case no fuse for line protection is required. 

The drives can be destroyed if DC bus link voltages are different. Only drives with mains supply that share the same AC branch, over current protection devices (identical mains supply voltage) may have the DC bus links interconnected. 

Interconnection of DC bus links works best in systems powered by 3-phase AC or DC power. Consult Kollmorgen for DC bus linking with single phase AC power input. 

8 pin, pitch 7.62 mm 

optional T version 

Mating connector data (➜ # 48) 

|**Pin**||**Label**|**Signal**|**Description**|
|---|---|---|---|---|
|7||+DC|+DC|DC Bus link positive|
|8||-DC|-DC|DC Bus link negative|



## **8.7.1 Fusing** 

External regen fusing FB1/FB2 (➜ # 79). DC bus link fusing depends on topology (see next page (➜ # 78)). 

|**Wiring**<br>**topology**<br>**Ampere**<br>**rating@240V**<br>**Ampere**<br>**rating@480V**<br>**UL region**<br>**example Eaton:**<br>**CE Region**<br>**example Mersen:**<br>**AKD2G-Sxx-6V**|**Wiring**<br>**topology**<br>**Ampere**<br>**rating@240V**<br>**Ampere**<br>**rating@480V**<br>**UL region**<br>**example Eaton:**<br>**CE Region**<br>**example Mersen:**<br>**AKD2G-Sxx-6V**|**Wiring**<br>**topology**<br>**Ampere**<br>**rating@240V**<br>**Ampere**<br>**rating@480V**<br>**UL region**<br>**example Eaton:**<br>**CE Region**<br>**example Mersen:**<br>**AKD2G-Sxx-6V**|**Wiring**<br>**topology**<br>**Ampere**<br>**rating@240V**<br>**Ampere**<br>**rating@480V**<br>**UL region**<br>**example Eaton:**<br>**CE Region**<br>**example Mersen:**<br>**AKD2G-Sxx-6V**|**Wiring**<br>**topology**<br>**Ampere**<br>**rating@240V**<br>**Ampere**<br>**rating@480V**<br>**UL region**<br>**example Eaton:**<br>**CE Region**<br>**example Mersen:**<br>**AKD2G-Sxx-6V**|
|---|---|---|---|---|
|Group: Fgroup|max. 30 A|na|DFJ-30|HP6M30|
|Busbar: Fbus|max. 15 A|na|DFJ-15|HP6M15|
|**AKD2G-Sxx-7V**|||||
|Group: Fgroup|max. 30 A||FWP-30B|HP10M30|
|Busbar: Fbus|max. 15 A||FWP-15B|HP10M15|



AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.7.2 Wiring example with T connectors** 

Without DC Bus fuses, other devices can become damaged or destroyed if, for example, a device fails due to an internal short circuit. If multiple drives are connected in parallel, then it is usual to insert DC Bus fuses (Fgroup) between groups of drives (with a group consisting of two or three devices, depending on the current) in order to limit any possible resulting damage. Fgroup fuses cannot avoid damage by current peaks completely. 

## **8.7.3 Wiring example with busbar** 

If a device fails in this system due to a short-circuit, only its fuses (Fbus) are tripped and the rest of the network continues uninterrupted. The solid busbars can conduct significantly larger currents than T connectors, because the compensating current does not flow through the connector as above. 

AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.8 External Regen resistor (X3)** 

For technical data on the regenerative brake circuit (➜ # 37). 

Fusing (such as fusible cut-outs or power switches) to be provided by the user. 

8 pin, pitch 7.62 mm optional T version Mating connector data (➜ # 48). 

|**Pin**<br>5|**Label**<br>Ri|**Signal**<br>RBint|**Description**<br>internal Regen resistor|
|---|---|---|---|
|6|Re|-RB|external Regen resistor -|
|7|+DC|+RBext|external Regen resistor +|



## **8.8.1 Fusing and Wiring** 

## **FB1 / FB2 fusing** 

|**Drive Model**<br>all AKD2G-Sxx|**Ampere**<br>**rating@240V**<br>10A|**Ampere**<br>**rating@480V**<br>40A|**UL region**<br>**example:**<br>Eaton<br>FWP-xxA14F|**CE Region**<br>**example: Siba**<br>110V to 400V: gRL(gS)<br>400V to 480V: aR|
|---|---|---|---|---|



## **FPS: Frizlen DC Power Switch** 

|**RBext**<br>BAR(U)1500-33|**FPS**<br>FPS-16|**Range [In]**<br>10 to 16 A|**cable cross section**<br>min. 2.5 mm²|
|---|---|---|---|



AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.9 Motor Power, Brake and Feedback connection** 

The AKD2G drive is able to protect the connected motor from overloading, if the parameters are set correctly and the thermal protection sensor is connected and supervised. With Kollmorgen motors the valid data are automatically set by the WorkBench motor database. Refer to parameter AXIS#.MOTOR.RTYPE for supported thermal sensors. 

- The dynamic voltage rise can lead to a reduction in the motor operating life and, on unsuitable motors, to flashovers in the motor winding. 

   - Only install motors with insulation class F (acc. to IEC60085) or above. Only install cables that meet the requirements (➜ # 49). 

## **8.9.1 Motor connectivity, some examples** 

- Axis 1: single cable connection (➜ # 81) commutation feedback: SFD3 or DSL 

- ™ Axis 2: dual cable connection (➜ # 81) commutation feedback: EnDAT, HIPERFACE, Resolver etc. via SFA 

- Axis 1: dual cable connection (➜ # 83) 7 commutation feedback: Resolver, SFD, EnDAT, HIPERFACE, BiSS, SinCos, ComCoder, Hall, SmartAbs etc. via X23 

- = position feedback: - X21: Step/Direction - X22: Step/Direction or incremental encoder 

- Axis 2: single cable connection (➜ # 81) = commutation feedback: SFD3 or DSL Axis 1: dual cable connection (➜ # 83) - commutation feedback: EnDAT, HIPERFACE, Resolver etc. via SFA position feedback:Resolver, SFD, EnDAT, 

- - HIPERFACE, BiSS, SinCos, ComCoder, Hall, SmartAbs etc. via X23 

- Axis 1: dual cable connection (➜ # 83) - commutation feedback: Resolver, SFD, EnDAT, HIPERFACE, BiSS, SinCos, ComCoder, Hall, SmartAbs etc. via X23 

- - position feedback: - X21: Step/Direction - X22: Step/Direction or incremental encoder 

AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.9.2 Motor single cable connection** 

Motors with two wire feedback systems like SFD3 or Hiperface DSL can be connected to AKD2G via a single Kollmorgen hybrid cable. Depending on the AKD2G version (single or dual axis), one or two single cable motor connections are possible. 

|**Drive type**<br>Single axis standard|**Commutation**<br>**Axis 1**<br>X1|**Commutation**<br>**Axis 2**<br>-|**Velocity/Position loop**<br>**closure**<br>-<br>X21<br>-<br>-|**Velocity/Position loop**<br>**closure**<br>-<br>X21<br>-<br>-|**Velocity/Position loop**<br>**closure**<br>-<br>X21<br>-<br>-|**Velocity/Position loop**<br>**closure**<br>-<br>X21<br>-<br>-|
|---|---|---|---|---|---|---|
|Single axis with Option I/O|X1|-|-|X21|X22|-|
|Single axis with Option F3|X1|-|-|X21|-|X23|
|Single axis with Option DX|X1|-|-|X21|X22|X23|
|Dual axis standard|X1|X2|-|X21|X22|-|
|Dual axis with Option DX|X1|X2|-|X21|X22|X23|



## **8.9.2.1 Motor Power, Brake and Feedback connectors X1, X2** 

- X1 (Feedback 1) / X2 (Feedback 2) Motor Power: 4 pin, pitch 7.62 mm 

- ; Motor Brake: 2 pin, pitch 3.81 mm 

- Motor Feedback: 2 pin, pitch 3.81 mm 

- Cable length: (➜ # 49) 

- Use Kollmorgen cables Mating connector data (➜ # 48). 

Feedback types: SFD3, HIPERFACE DSL 

Pinout is identical for connectors X1 and X2. 

|**Pin**<br>1|**Signal**<br>U|**Description**<br>Motor phase U|
|---|---|---|
|2|V|Motor phase V|
|3|W|Motor phase W|
|5|PE|Protective earth|
|B+|BR+|Brake positive line (safety notes and details (➜# 85))|
|B-|BR-|Brake negative line (safety notes and details (➜# 85))|
|F+|COM+|SFD3, HIPERFACE DSL|
|F-|COM-||



AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.9.2.2 Feedback connectors X21, X22, X23** 

Velocity/Position loop closing Use Kollmorgen cables Mating connector data (➜ # 48). Cable length: (➜ # 49) 

|**Connector**<br>X21|**Functionality**<br>Step/Direction, CW/CCW|**Pinout, Wiring**<br>(➜# 89)|
|---|---|---|
|X22|Step/Direction, CW/CCW, Incremental Encoder|(➜# 90)|
|X23|Several conventional feedback types|(➜# 91)|



AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.9.3 Motor dual cable connection** 

Motors with conventional commutation feedback systems like resolver or sine encoder can be connected to AKD2G with separated power/brake and feedback cables. Feedback functions are assigned with parameters in WorkBench. Scaling and other settings are performed in WorkBench, too. Velocity / Position loop closing and electronic gearing / master-slave connection are possible via X21, X22, X23 depending on the drive version and physical restrictions. 

- X1 (Feedback 1) / X2 (Feedback 2) . Motor Power: 4 pin, pitch 7.62 mm 

   - Motor Brake: 2 pin, pitch 3.81 mm 

   - SFA connection: 2 pin, pitch 3.81 mm 

- Feedback types: see SFA connectivity (➜ # 92) 

- X23 (Feedback 3) 

- SubD HD 15 poles Feedback types: see X23 connectivity (➜ # 91) 

- = X21 (Feedback 4) 

   - 2 x 11 pins (left connector A, right connector B) 

- _ Feedback types: see X21 connectivity (➜ # 89) X22 (Feedback 5) 

- 2 x 10 pins (left connector A, right connector B) Feedback types: see X22 connectivity (➜ # 90) 

- Mating connector data (➜ # 48). 

AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.9.3.1 Motor power and motor brake connectors X1, X2** 

Usually these lines are part of the Kollmorgen motor cable connected to X1 or X2. For motor brake safety notes and functional details (➜ # 85). 

Use Kollmorgen cables Mating connector data (➜ # 48). 

Cable length: (➜ # 49) 

**Pin Signal Description** 1 U Motor phase U 2 V Motor phase V 3 W Motor phase W 5 PE Protective earth B+ BR+ Brake positive, with Kollmorgen cables only B- BRBrake negative, with Kollmorgen cables only **8.9.3.2 Feedback connectors X1, X2, X41, X21, X22, X23** Use Kollmorgen cables Mating connector data (➜ # 48). ~~a~~ Cable length: (➜ # 49) For feedback connection overview (➜ # 87) 

|**Connector**<br>X1/X2|**Functionality**<br>SFD3, DSL, SFA|**Pinout,**<br>**Wiring**<br>(➜# 88)|
|---|---|---|
|X41|SFA at X1 or X2 , several conventional feedback types|(➜# 92)|
|X21|Step/Direction, CW/CCW|(➜# 89)|
|X22|Step/Direction, CW/CCW, Incremental Encoder|(➜# 90)|
|X23|Several conventional feedback types|(➜# 91)|



## **Feedback connector X1, X2, X41** 

Conventional feedback systems can be connected to X1 or X2 via the optional feedback adapter SFA. SFA offers the additional connector X41. 

Connector X1 is a standard connector. Input for SFD3, DSL, or SFA. Connector X2 is standard for dual-axis drives. Input for SFD3, DSL, or SFA. SFA: adapter for several conventional feedback types 

## **Feedback connector X21** 

Connector X21 is a standard connector. 

Input for Step/Direction and CW/CCW. 

## **Feedback connector X22** 

Connector X22 is standard connector for dual-axis drives. Connector X22 is part of option DX or IO for single axis drives. Input for Step/Direction, CW/CCW, Incremental encoder 

## **Feedback connector X23** 

Connector X23 is part of option DX or F3. 

Input for several conventional feedback types. 

AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.9.4 Motor Holding Brake Connection** 

A 24 V holding brake in the motor can be controlled directly by the drive. For proper function, check voltage drop, measure voltage at brake input and check brake function (on and off). 

Brake voltage supply via 24 V ±10% auxiliary voltage supply of the drive on X10. Minimum and maximum brake current see Electrical Data (➜ # 34) respectively (➜ # 36). 

AKD2G offers one motor brake output for every axis on connector X1 and X2. 

|**Connector**||**Usable for**||
|---|---|---|---|
|X1||Primary motor brake axis 1|Primary motor brake axis 1|
|X2||Primary motor brake axis 2|Primary motor brake axis 2|



## **No functional Safety!** 

Serious injury could result when the load is not properly blocked. This function does not ensure functional safety. 

- Functional safety, e.g. with hanging load (vertical axes), requires an additional brake. 

- The Hardware Enable does not initiate a controlled stop but switches off the power stage immediately. 

- Set parameter AXIS#.MOTOR.BRAKEIMM to 1 with vertical axes, to apply the brake immediately after faults or Hardware Disable. 

**Pinout X1 / X2** 

|**Pin**||**Signal**|**Description**|
|---|---|---|---|
|B+||BR+|Brake positive line|
|B-||BR-|Brake negative line|



## **Wiring** 

Usually the brake lines are part of the Kollmorgen hybrid single cable connection to X1 respectively X2 (➜ # 81). 

AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **Functionality** 

The brake function must be enabled through a parameter. The diagram below shows the timing and functional relationships between the controlled stop signal, speed, and braking force. All values can be adjusted with parameters; values in the diagram are default values. 

The drive speed setpoint is internally driven down an adjustable ramp (AXIS#.CS.DEC) to 0 V. 

With default values the output for the brake is switched on when the speed has reached 5 rpm (AXIS#.CS.VTHRESH) for at least 6 ms (AXIS#.CS.TO). The rise (tbrH) and fall (tbrL) times of the holding brake that is built into the motor are different for the various types of motor. 

AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.9.5 Feedback Connection** 

AKD2G offers up to five feedback channels. These channels can serve 

to commutate the motor (single cable (➜ # 81) or dual cable (➜ # 85)), to close the velocity and/or position loops, and to act as a command source (electronic gearing, flying sheer, master-slave (➜ # 93)). 

The usage of the five channels may be freely configured in software, subject only to a few restrictions that are not physically sensible. 

Exactly one feedback channel per axis can commutate the motor. 

- At most one feedback channel per axis can serve as the command source and the same feedback channel cannot also commutate the motor. 

A feedback channel can serve as the command source for more than one axis. 

FB1 cannot commutate axis 2. FB2 cannot commutate axis 1. 

|**Feedback**<br>**channel**<br>Feedback 1|**Connector**<br>X1|**Usable for**<br>Axis 1: commutation feedback|**Pinout**<br>(➜# 88)|
|---|---|---|---|
||X41|Axis 1 via SFA on X1: commutation feedback|(➜# 92)|
|Feedback 2|X2|Axis 2: commutation feedback|(➜# 88)|
|Feedback 2|X41|Axis 2 via SFA on X2: commutation feedback|(➜# 92)|
|Feedback 3|X23|commutation feedback, velocity/position, command|(➜# 91)|
|Feedback 4|X21|commutation feedback, velocity/position, command|(➜# 89)|
|Feedback 5|X22|commutation feedback, velocity/position, command|(➜# 90)|



|**Feedback Types**<br>SFD3|**Connectors**<br>X1, X2|
|---|---|
|Encoder HIPERFACE DSL|X1, X2|
|Resolver|X23, X41|
|SFD|X23, X41|
|SinCos Encoder BiSS B (analog)|X23, X41|
|Encoder BiSS C (digital)|X23|
|SinCos Encoder EnDat 2.1|X23, X41|
|Encoder EnDat Digital 2.2|X23, X41|
|Encoder HIPERFACE|X23, X41|
|Sine Encoder|X23, X41|
|Sine Encoder + Hall|X23, X41|
|Incremental Encoder|X22, X23, X41|
|Incremental Encoder + Hall (Comcoder)|X23, X41|
|Hall Sensors|X23, X41|
|Tamagawa Smart Abs|X23, X41|
|Step/Direction|X21, X22, X23, X41|
|CW/CCW|X21, X22, X23, X41|



AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.9.5.1 Feedback Connector X1, X2** 

- 4 pin, pitch 7.62 mm plus 2x2 pin pitch 3.81 mm 

- Input for commutation feedback: SFD3, DSL, SFA 

## **Wiring example SFD3 or HIPERFACE DSL** 

## **Wiring example conventional Feedback types with SFA** 

## **Electrical data** 

Rated voltage 5 V. 

Rated current is 350 mA simultaneously for X1 and X2. 

|**Pin**<br>F+|**Signal**<br>COM+|**Description**<br>SFD3 +, HIPERFACE DSL +, SFA +|
|---|---|---|
|F-|COM-|SFD3 -, HIPERFACE DSL -, SFA -|



AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.9.5.2 Feedback Connector X21** 

- 2 x 11 pins (left connector A, right connector B), pitch 3.5 mm Fast input, isolated, sink, type EN 61131-2 type 1 Input for commutation or position feedback. 

- Input for Electronic Gearing, (➜ # 93) Mating connector data (➜ # 48). 

## **Wiring example** 

|**X21 Pin**<br>A3|**Step/Direction**<br>Step|**CW/CCW**<br>CW|
|---|---|---|
|A4|Direction|CCW|
|B4|Common (DGND)|Common (DGND)|



AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.9.5.3 Feedback Connector X22** 

- Standard for dual axis drives, (➜ # 27), optional for single axis drives 

- 2 x 10 pins (left connector A, right connector B), pitch 3.5 mm RS485 inputs 

- Input for commutation or position feedback. Input for Electronic Gearing, (➜ # 93) Output for encoder emulation (EEO2), (➜ # 94) Mating connector data (➜ # 48). 

## **Wiring example (Input)** 

EEO output connection is similar. 

|**X22 Pin**<br>A20|**Step/Direction**<br>Step +|**CW/CCW**<br>CW +|**Incremental Encoder**<br>Track A +|
|---|---|---|---|
|A21|Step -|CW -|Track A -|
|B20|Direction +|CCW +|Track B +|
|B21|Direction -|CCW -|Track B -|
|A17|AGND|AGND|AGND|



AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.9.5.4 Feedback Connector X23** 

- k[2] Connectivity Option F3 or DX (➜ # 27) Sub-D high density 15 pin, female 

   - Use Kollmorgen feedback cables 

   - Input for several feedback types 

   - Input for Electronic Gearing, (➜ # 93) 

   - Output for encoder emulation (EEO1), (➜ # 94) 

   - Digital input (➜ # 107), Digital output (➜ # 111) Mating connector data (➜ # 48). 

## **Encoder power supply (X23 pins 10/11):** 

- 2 Maximum voltage 9 V with shorted sense contacts (4/5), rated voltage 5 V +/-5%. 2 Rated supply current is 200 mA. 

- 2 Voltage rise time ~4 ms with full load and 220 µF of capacitance. 2 Encoder power lines capacitance 10 µF to 220 µF 

|**X23**<br>**Pin**<br>1<br>a<br>a|**SFD**<br>-<br>|**Resol-**<br>**ver**<br>-<br>ee|**BiSS**<br>**B**<br>-<br>ee|**BiSS**<br>**C**<br>-<br>eeDe|**EnDat**<br>**2.1**<br>-<br>De|**EnDat**<br>**2.2**<br>-<br>es|**HIPER-**<br>**FACE**<br>-<br>es|**Sine/**<br>**Cos**<br>-<br>es|**Sine/**<br>**Cos**<br>**+Hall**<br>Hall U|**Incr.**<br>**Enc.**<br>-|**Incr.**<br>**Enc.**<br>**+Hall**<br>Hall U|**Hall**<br>Hall U|**Smart**<br>**Abs**<br>-|**Step/**<br>**Dir**<br>-|**CW/**<br>**CCW**<br>-|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|2<br>a <br>a|-<br> a<br>a|-<br>ee<br>a|CLK+<br>ee|CLK+<br>eeDe<br>ee|CLK+<br>De <br>ee<br>es|CLK+<br> es<br>ee<br>es|-<br>es<br>eeee<br>es|-<br>es<br>ee<br>es|Hall V<br>ee <br>es|-<br> ee<br>ee|Hall V<br>ee<br>ee|Hall V<br>ee|-<br> ee|Step+<br>ee|CW+<br>ee|
|3<br>a<br>Fa|-<br>a|-<br>a|CLK-|CLK-|CLK-<br>es|CLK-<br>es|-<br>es|-<br>es<br>ee|Hall W<br>es<br>ee|-<br>ee<br>ee|Hall W<br>ee<br>ee|Hall W|-|Step-|CW-|
|4<br>a <br>a <br>Fa<br>a|SEN+<br> a <br> a <br>|-<br> a<br> a~~ee~~<br>se|SEN+<br>~~ee~~<br>se|SEN+<br>~~ee~~<br>rePe|SEN+<br>es<br>~~ee~~<br>Pe|SEN+<br>es<br>~~ee~~|SEN+<br>es<br>~~ee~~<br>~~Gs~~|SEN+<br>es<br>~~ee~~<br>ee<br>~~Gs~~|SEN+<br>es <br>~~ee~~<br>ee<br>~~Gs~~|SEN+<br> ee<br>~~ee~~<br>ee<br>~~Gs~~|SEN+<br>ee<br>~~ee~~<br>ee|-<br>~~ee~~|SEN+<br>~~ee~~|-<br>~~ee~~|-<br>~~ee~~|
|5<br>Fa<br>a|SEN-<br>|-<br>se|SEN-<br>se|SEN-<br>rePe|SEN-<br>Pe|SEN-|SEN-<br>~~Gs~~|SEN-<br>ee<br>~~Gs~~|SEN+<br>ee<br>~~Gs~~|SEN+<br>ee<br>~~Gs~~|SEN+<br>ee|-|SEN+|-|-|
|6<br>Fa<br>a <br>a|COM+<br> a<br>a|R1 Ref+<br>se<br>a|DAT+<br>se|DAT+<br> rePe<br>ee|DAT+<br>Pe<br>ee<br>es|DAT+<br>ee<br>es|DAT+<br>~~Gs~~<br>eeee<br>es|Zero+<br>ee <br>~~Gs~~<br>ee<br>es|Zero+<br> ee<br>~~Gs~~<br>ee <br>es|Zero+<br>ee<br>~~Gs~~<br> ee<br>ee|Zero+<br>ee<br>ee<br>ee|-<br>ee|SD+<br> ee|Dir+<br>ee|CCW+<br>ee|
|7<br>a<br>Fa|COM-<br>a|R2 Ref-<br>a|DAT-|DAT-|DAT-<br>es|DAT-<br>es|DAT-<br>es|Zero-<br>es<br>ee|Zero-<br>es<br>ee|Zero-<br>ee<br>ee|Zero-<br>ee<br>ee|-|SD-|Dir-|CCW-|
|8<br>a <br>a <br>Fa<br>a|-<br> a <br> a <br>|Th+<br> a<br> a~~ee~~<br>se|Th+<br>~~ee~~<br>se|-<br>~~ee~~<br>rePe|Th+<br>es<br>~~ee~~<br>Pe|-<br>es<br>~~ee~~|Th+<br>es<br>~~ee~~<br>~~Gs~~|Th+<br>es<br>~~ee~~<br>ee<br>~~Gs~~|Th+<br>es <br>~~ee~~<br>ee<br>~~Gs~~|Th+<br> ee<br>~~ee~~<br>ee<br>~~Gs~~|Th+<br>ee<br>~~ee~~<br>ee|Th+<br>~~ee~~|Th+<br>~~ee~~|Th+<br>~~ee~~|Th+<br>~~ee~~|
|9<br>Fa<br>a|-<br>|Th-<br>se|Th-<br>se|-<br>rePe|Th-<br>Pe|-|Th-<br>~~Gs~~|Th-<br>ee<br>~~Gs~~|Th-<br>ee<br>~~Gs~~|Th-<br>ee<br>~~Gs~~|Th-<br>ee|Th-|Th-|Th-|Th-|
|10<br>Fa<br>a <br>a|+5 V<br> a<br>a|-<br>se<br>a|+5 V<br>se|+5 V<br> rePe<br>ee|+5 V<br>Pe<br>ee<br>es|+5 V<br>ee<br>es|+5 V<br>~~Gs~~<br>eeee<br>es|+5 V<br>ee <br>~~Gs~~<br>ee<br>es|+5 V<br> ee<br>~~Gs~~<br>ee <br>es|+5 V<br>ee<br>~~Gs~~<br> ee<br>ee|+5 V<br>ee<br>ee<br>ee|+5 V<br>ee|+5 V<br> ee|+5 V<br>ee|+5 V<br>ee|
|11<br>a<br>Fa|0 V<br>a|-<br>a|0 V|0 V|0 V<br>es|0 V<br>es|0 V<br>es|0 V<br>es<br>ee|0 V<br>es<br>ee|0 V<br>ee<br>ee|0 V<br>ee<br>ee|0 V|0 V|0 V|0 V|
|12<br>a <br>a <br>Fa<br>a|-<br> a <br> a <br>|S1 SIN+<br> a<br> a~~ee~~<br>se|A+<br>~~ee~~<br>se|-<br>~~ee~~<br>rePe|A+<br>es<br>~~ee~~<br>Pe|-<br>es<br>~~ee~~|SIN+<br>es<br>~~ee~~<br>~~Gs~~|A+<br>es<br>~~ee~~<br>ee<br>~~Gs~~|A+<br>es <br>~~ee~~<br>ee<br>~~Gs~~|A+<br> ee<br>~~ee~~<br>ee<br>~~Gs~~|A+<br>ee<br>~~ee~~<br>ee|-<br>~~ee~~|-<br>~~ee~~|-<br>~~ee~~|-<br>~~ee~~|
|13<br>Fa<br>a|-<br>|S3 SIN-<br>se|A-<br>se|-<br>rePe|A-<br>Pe|-|SIN-<br>~~Gs~~|A-<br>ee<br>~~Gs~~|A-<br>ee<br>~~Gs~~|A-<br>ee<br>~~Gs~~|A-<br>ee|-|-|-|-|
|14<br>Fa<br>a|-<br> a|S2 COS+<br>se|B+<br>se|-<br> rePe<br>ee|B+<br>Pe<br>ee|-<br>ee|COS+<br>~~Gs~~<br>eeee|B+<br>ee <br>~~Gs~~<br>ee<br>eee|B+<br> ee<br>~~Gs~~<br>ee <br>eee|B+<br>ee<br>~~Gs~~<br> ee<br>ee|B+<br>ee<br>ee<br>eee|-<br>ee <br>eee|-<br> ee<br>ee|-<br>ee<br>ee|-<br>ee<br>ee~~e~~|
|15<br>a|-<br>~~ee~~|S4 COS-<br>~~ee~~|B-<br>~~ee~~|-<br>~~ee~~|B-<br>~~ee~~|-<br>~~ee~~|COS-<br>~~ee~~|B-<br>~~ee~~<br>eee|B-<br>~~ee~~<br>eee|B-<br>~~ee~~<br>ee|B-<br>~~ee~~<br>eee|-<br>~~ee~~<br>eee|-<br>~~ee~~<br>ee|-<br>~~ee~~<br>ee|-<br>~~ee~~<br>ee~~e~~|



CLK = CLOCK, DAT = DATA, SEN = SENSE, Th = Thermal control 

AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.9.5.5 Feedback Connector X41 (SFA, accessory)** 

SFA ( **S** mart **F** eedback **A** dapter) converts conventional feedback signals to a 2-wire serial signal. SFA can be laid into the cable duct or may be mounted to a DIN rail using a standard DIN rail clip. 

SFA adds a 15 pole HD SubD female connector X41 to the system for connection of a Kollmorgen motor feedback cable (see regional _Accessories Manual_ ). Dimensions (LxWxD): 88.6 x 55.6 x 21.2 (28.6 with rail clip). Order codes see regional Accessories Manual. 

- Sub-D high density 15 pin, female 

- 1 m shielded cable with 3 flying leads for connection to X1 or X2 The cable shield is connected with cable ties to the X1/X2 shield plates (cut-off the unused shield wire). Connected feedback must be set in WorkBench Use Kollmorgen feedback cables Input for Electronic Gearing, (➜ # 93) Output for encoder emulation (EEO3/EEO4), (➜ # 94) Master-Slave (➜ # 96) 

Connect the flying leads of the SFA cable to X1 (FB1, EEO3) or X2 (FB2, EEO4) : 

## **Supported feedback types, pinout** 

|**X41**<br>**Pin**<br>1<br>a<br>a|**SFD**<br>-<br>a<br>a|**Resol-**<br>**ver**<br>-<br>a|**BiSS**<br>**B**<br>-<br>ee<br>es|**EnDat**<br>**2.1**<br>-<br>ee<br>es|**EnDat**<br>**2.2**<br>-<br>ee<br>es|**HIPER-**<br>**FACE**<br>-<br>ee<br>eees|**Sine/**<br>**Cos**<br>-<br>es|**Sine/**<br>**Cos**<br>**+Hall**<br>Hall U<br>ss|**Incr.**<br>**Enc.**<br>-<br>ss|**Incr.**<br>**Enc.**<br>**+Hall**<br>Hall U<br>ee<br>ss|**Hall**<br>Hall U<br>ee<br>ss|**Smart**<br>**Abs**<br>-<br>ee|**Step/**<br>**Dir**<br>-<br>ee|**CW/**<br>**CCW**<br>-|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|2<br>a <br>a|-<br> a <br>a|-<br> a|CLK+<br>ee<br>es|CLK+<br>ee<br>es|CLK+<br>ee<br>es|-<br>ee<br>eees|-<br>es|Hall V<br>ss|-<br>ss|Hall V<br>ee<br>ss|Hall V<br>ee<br>ss|-<br>ee|Step+<br>ee|CW+|
|3<br>a <br>a<br><br>a|-<br> a<br>a<br>|-<br>a<br>|CLK-<br>es<br><br>|CLK-<br>es<br>De<br>|CLK-<br>es <br>De<br>|-<br> eees<br>DeBe<br>|-<br>es <br>Be<br>|Hall W<br> ss<br>|-<br>ss<br>|Hall W<br>ss<br>|Hall W<br>ss<br>|-<br>|Step-<br>|CW-<br>|
|4<br>a <br>a<br>a|SEN+<br> a<br><br>|-<br>a<br>|SEN+<br><br>|SEN+<br>De<br>|SEN+<br>De<br>|SEN+<br>DeBe<br>|SEN+<br>Be<br><br>es|SEN+<br><br>eses|SEN+<br><br>es|SEN+<br>|-<br>|SEN+<br>|-<br>|-<br>|
|5<br> <br>a<br>a<br>a|SEN-<br> a <br>~~ee~~<br>a|-<br> a <br>~~ee~~|SEN-<br> <br>~~ee~~<br>es|SEN-<br> De<br>~~ee~~<br>es|SEN-<br>De<br>~~ee~~<br>es|SEN-<br>DeBe<br>~~ee~~<br>eees|SEN-<br>Be<br>~~ee~~<br>es<br>es~~ss~~|SEN+<br>~~ee~~<br>eses<br>~~ss~~|SEN+<br>~~ee~~<br>es<br>~~ss~~|SEN+<br>~~ee~~<br>~~ss~~|-<br>~~ee~~<br>~~ss~~|SEN+<br>~~ee~~|-<br>~~ee~~|-<br>~~ee~~|
|6<br>a <br>a|COM+<br> a|R1 Ref+|DAT+<br>es|DAT+<br>es|DAT+<br>es|DAT+<br>eees|Zero+<br>es<br>es~~ss~~|Zero+<br>eses<br>~~ss~~|Zero+<br>es<br>~~ss~~|Zero+<br>~~ss~~|-<br>~~ss~~|SD+|Dir+|CCW+|
|7<br> <br>a<br>a|COM-<br> a<br>a|R2 Ref-<br>a|DAT-<br>es|DAT-<br>es<br>De|DAT-<br>es <br>De|DAT-<br> eees<br>DeBe|Zero-<br>es~~ss~~<br>Be|Zero-<br>~~ss~~|Zero-<br>~~ss~~|Zero-<br>~~ss~~|-<br>~~ss~~|SD-|Dir-|CCW-|
|8<br>a<br>a|-<br>a<br>|Th+<br>a|Th+|Th+<br>De|-<br>De|Th+<br>DeBe|Th+<br>Be<br>es|Th+<br>eses|Th+<br>es|Th+|Th+|Th+|Th+|Th+|
|9<br>a <br>a<br>a<br>a|-<br> a <br>~~ee~~<br>a|Th-<br> a<br>~~ee~~|Th-<br>~~ee~~<br>es|Th-<br>De<br>~~ee~~<br>es|-<br>De<br>~~ee~~<br>es|Th-<br>DeBe<br>~~ee~~<br>eees|Th-<br>Be<br>~~ee~~<br>es<br>es~~ss~~|Th-<br>~~ee~~<br>eses<br>~~ss~~|Th-<br>~~ee~~<br>es<br>~~ss~~|Th-<br>~~ee~~<br>~~ss~~|Th-<br>~~ee~~<br>~~ss~~|Th-<br>~~ee~~|Th-<br>~~ee~~|Th-<br>~~ee~~|
|10<br>a <br>a|+5 V<br> a|-|+5 V<br>es|+5 V<br>es|+5 V<br>es|+5 V<br>eees|+5 V<br>es<br>es~~ss~~|+5 V<br>eses<br>~~ss~~|+5 V<br>es<br>~~ss~~|+5 V<br>~~ss~~|+5 V<br>~~ss~~|+5 V|+5 V|+5 V|
|11<br> <br>a<br>a|0 V<br> a<br>a|-<br>a|0 V<br>es|0 V<br>es<br>De|0 V<br>es <br>De|0 V<br> eees<br>DeBe|0 V<br>es~~ss~~<br>Be|0 V<br>~~ss~~|0 V<br>~~ss~~|0 V<br>~~ss~~|0 V<br>~~ss~~|0 V|0 V|0 V|
|12<br>a<br>a|-<br>a<br>|S1 SIN+<br>a|A+|A+<br>De|-<br>De|SIN+<br>DeBe|A+<br>Be<br>es|A+<br>es|A+<br>es|A+|-|-|-|-|
|13<br>a <br>a<br>a<br>a|-<br> a <br>~~ee~~<br>a<br>|S3 SIN-<br> a<br>~~ee~~<br>|A-<br>~~ee~~<br>es<br>|A-<br>De<br>~~ee~~<br>es<br>|-<br>De<br>~~ee~~<br>es<br>|SIN-<br>DeBe<br>~~ee~~<br>eees<br>|A-<br>Be<br>~~ee~~<br>es<br>es~~ss~~<br>|A-<br>~~ee~~<br>es<br>~~ss~~<br>|A-<br>~~ee~~<br>es<br>~~ss~~<br>|A-<br>~~ee~~<br>~~ss~~<br>|-<br>~~ee~~<br>~~ss~~<br>|-<br>~~ee~~<br>|-<br>~~ee~~<br>|-<br>~~ee~~<br>|
|14<br>a <br>a|-<br> a<br>|S2 COS+<br>|B+<br>es<br>|B+<br>es<br>|-<br>es<br>|COS+<br>eees<br>|B+<br>es<br>es~~ss~~<br>|B+<br>es<br>~~ss~~<br>|B+<br>es<br>~~ss~~<br><br>ee|B+<br>~~ss~~<br><br>ee|-<br>~~ss~~<br><br>ee|-<br><br>ee|-<br><br>ee|-<br>|
|15<br> <br>a|-<br> a<br>~~ee~~|S4 COS-<br>~~ee~~|B-<br>es<br>~~ee~~|B-<br>es<br>~~ee~~|-<br>es <br>~~ee~~|COS-<br> eees<br>~~ee~~|B-<br>es~~ss~~<br>~~ee~~|B-<br>~~ss~~<br>~~ee~~|B-<br>~~ss~~<br>~~ee~~<br>ee|B-<br>~~ss~~<br>~~ee~~<br>ee|-<br>~~ss~~<br>~~ee~~<br>ee|-<br>~~ee~~<br>ee|-<br>~~ee~~<br>ee|-<br>~~ee~~|



CLK = CLOCK, DAT = DATA, SEN = SENSE, Th = Thermal control 

AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.10 Electronic Gearing, EEO, Master-Slave** 

|**Electronic Gearing, EEO, Master-Slave**||
|---|---|
|AKD2G offers several feedback channels. These channels may also be used as the com-||
|mand source (input) for electronic gearing or master-slave or for EEO (Emulated Encoder Out-||
|put).||
|**Feedback**<br>**channel**<br>**EEO**<br>**channel**<br>**Connector**<br>**Pinout and**<br>**wiring example**<br>**Keyword to configure**<br>**the sensor type**<br>Feedback 1<br>EEO3<br>X1<br>(➜# 88)<br>FB1.SELECT<br>X41<br>(➜# 92)<br>Feedback 2<br>EEO4<br>X2<br>(➜# 88)<br>FB2.SELECT<br>X41<br>(➜# 92)<br>Feedback 3<br>EEO1<br>X23<br>(➜# 91)<br>FB3.SELECT<br>Feedback 4<br>n/a<br>X21<br>(➜# 89)<br>FB4.SELECT<br>Feedback 5<br>EEO2<br>X22<br>(➜# 90)<br>FB5.SELECT<br>~~———~~||
|**8.10.1 Electronic Gearing**||
|AKD2G offers up to five feedback channels. Any of these channels may be used as the gear-||
|ing command source. The gearing source is selected for each axis using||
|AXIS#.GEAR.FBSOURCE. Refer to the WorkBench Online Help for more information.||



## **8.10.1 Electronic Gearing** 

AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.10.2 Emulated Encoder Output (EEO)** 

The drive calculates the motor shaft position from the cyclic- absolute signals of the commutation feedback, generating incremental-encoder compatible pulses or CW/CCW signals or Pulse/Direction signals from this information. 

The resolution and the index (zero) position can be set in WorkBench. The outputs are driven from an internal supply voltage. Refer to the WorkBench Online Help for more information. 

When using a multispeed resolver (more than 2 poles) as commutation feedback, the EEO will create only one zero pulse per each mechanical revolution of the motor. The zero pulse is dependent on the motors starting position! 

- Examples for Master-Slave connection see (➜ # 96). 

## **Technical characteristics X22, EEO2** 

Pulse outputs on the connector X22 are 2 signals, tracks A and B, with 90° phase difference (i.e. in quadrature, hence the alternative term “A quad B” output). 

- Electrical Interface: RS-485, max. current 100 mA, the maximum number of connected slaves is determined by the loading characteristics of the slaves, 32 slaves can be driven if the input impedance of the bias network is 10kΩand only one slave has a DC termination resistor. 

- Max signal (channel) output frequency: 3 MHz 

- The pulses per revolution value is settable 

- Pulse phase shift: 90°±20° 

|**X22**<br>A17|**Signals EEO2**<br>AGND|**Description**<br>Analog ground|
|---|---|---|
|A20|Track A+|EEO2 output, channel A positive|
|A21|Track A-|EEO2 output, channel A negative|
|B20|Track B+|EEO2 output, channel B positive|
|B21|Track B-|EEO2 output, channel B negative|



AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **Technical characteristics X23, EEO1** 

Pulse outputs on the SubD connector X23 are 3 signals, A, B and Index, with 90° phase difference (i.e. in quadrature, hence the alternative term “A quad B” output), with a zero pulse. 

- Electrical Interface: 5V TTL, current 60 mA, max. number of connected slaves is determined by the loading characteristics of the slaves, 32 slaves can be driven if the input impedance of the bias network is 10kΩand only one slave has a DC termination resistor. Max signal (channel) output frequency: 3 MHz The pulses per revolution value is settable Pulse phase shift: 90°±20° 

|**X23**<br>6|**Signals EEO1**<br>Zero+|**Description**<br>EEO1 output, index positive|
|---|---|---|
|7|Zero-|EEO1 output, index negative|
|11|0 V|EEO1 output, ground|
|12|Track A+|EEO1 output, channel A positive|
|13|Track A-|EEO1 output, channel A negative|
|14|Track B+|EEO1 output, channel B positive|
|15|Track B-|EEO1 output, channel B negative|



## **Technical characteristics X41 (SFA), EEO3/EEO4 (in process)** 

Pulse outputs on the SubD connector X41 are 3 signals, A, B and Index, with 90° phase difference (i.e. in quadrature, hence the alternative term “A quad B” output), with a zero pulse. 

- Electrical Interface: 5V TTL, current 60 mA, max. number of connected slaves is determined by the loading characteristics of the slaves, 32 slaves can be driven if the input impedance of the bias network is 10kΩand only one slave has a DC termination resistor. Max signal (channel) output frequency: 3 MHz The pulses per revolution value is settable Pulse phase shift: 90°±20° 

|**X41**<br>6|**Signals EEO3**<br>Zero+|**Description**<br>EEO3 output, index positive|
|---|---|---|
|7|Zero-|EEO3 output, index negative|
|11|0 V|EEO3 output, ground|
|12|Track A+|EEO3 output, channel A positive|
|13|Track A-|EEO3 output, channel A negative|
|14|Track B+|EEO3 output, channel B positive|
|15|Track B-|EEO3 output, channel B negative|



AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.10.3 Master-Slave control** 

Several AKD2G can be connected as slave drives to another AKD2G which acts as a master. The slave drives use the master's encoder output signal (EEO, (➜ # 94)) as command input and follow these commands (velocity and direction). 

## **8.10.3.1 Master-Slave using X22** 

The master is configured for EEO2 (➜ # 94) on X22, the Slave uses X22 for command input. 

## **8.10.3.2 Master-Slave using optional X23 or X41** 

The master is configured for EEO1 (➜ # 95) on X23 or EEO3/EEO4 ((➜ # 95) with SFA) on X41, the Slave uses X23 (or X41 with SFA) for command input. 

AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.11 Motion Bus Interface (X11/X12)** 

The motion bus interface has two RJ-45 connectors. 

RJ-45 with built-in green/red dual-color LED. X12 IN port, X11 OUT port EtherCAT® Ethernet I/P, PROFINET RT/IRT (available 2020) 

**==> picture [394 x 74] intentionally omitted <==**

**----- Start of picture text -----**<br>
Pin Signal Description Pin Signal Description<br>1 Tx+ Transmit + 5 Termination Bob Smith termination<br>Rs es | |<br>2 Tx- Transmit - 6 Rx- Receive -<br>Rs es<br>3 | Rx+ Receive + 7 Termination Bob Smith termination<br>Rs || e Gs<br>ss 4 Termination Bob Smith termination | 8 s Termination Bob Smith termination<br>**----- End of picture text -----**<br>


Do not connect the Ethernet line for the PC or PAC with the set up software to the motion bus interface X11/X12. The service Ethernet cable must be connected to X20. 

## **8.11.1 EtherCAT®** 

AKD2G drives (connectivity option **E** ) can be connected as slaves to the EtherCAT® network (CoE) via RJ-45 connectors X12 (in port) and X11 (out port). The communication status is indicated by the built-in connector LEDs. 

|EtherCAT® is a registered<br>trademark and patented tech-<br>nology, licensed by Beckhoff<br>Automation GmbH, Ger-<br>many.<br>EtherCAT.<br>| en<br>x12<br>=|**Conn.**<br>X11<br>„Out“|**Name**<br>„ERR“<br>indicator|**Function**<br>Returns potentials failures during Ether-<br>CAT communication.|**Function**<br>Returns potentials failures during Ether-<br>CAT communication.|
|---|---|---|---|---|
||||Indicator code|EtherCAT state|
||||Off|No Error.|
||||Blinking|Invalid configuration.|
||||Single Flash|Local error e.g. due to syn-<br>chronization error.|
||||Double Flash|Process data watchdog<br>e.g. sync manager<br>timeout.|
||X11<br>„Out”<br>en|Link/Activity|On/Blinking: Physical link/Data Traffic on.<br>Static off: No link.||
||X12<br>„In“<br>en|„RUN“<br>indicator|Returns the device state:||
||||Indicator code|EtherCAT state|
||||Off|INIT|
||||Blinking|PRE-OPERATIONAL|
||||Single Flash|SAFE-OPERATIONAL|
||||On|OPERATIONAL|
||||Flickering|Initialization or<br>BOOTSTRAP|
||X12<br>„In”|Link/Activity|On/Blinking: Physical link/Data Traffic on.<br>Static off: No link.||



AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **Bus topology example (EtherCAT®)** 

We suggest to use Kollmorgen ENCP cables. For more possible system solutions refer to the WorkBench Online Help. 

## **Communication profile** 

For EtherCAT® communication profile description refer to the manual " _AKD2G EtherCAT® Communication_ ". 

AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.12 CAN-Bus Interface (X13/X14)** 

AKD2G drives with connectivity option **C** can be connected to a CAN-Bus via two 6-pin RJ25 connectors X13/X14. 

RJ25 Up to 1000 kbit/s operation Node ID to be set by WorkBench Baudrate to be set by WorkBench 

|**Pin**||**Signal**|**Description**|
|---|---|---|---|
|1||Termination|Internal Termination Resistor|
|2||Shield|Chassis|
|3||CAN_high|CAN bus high signal|
|4||CAN_low|CAN bus low signal|
|5||CAN_GND|CAN bus ground|
|6||Termination|Internal Termination Resistor|



## **8.12.1 CAN-Bus Topology** 

We recommend the use of Kollmorgen CBP000 cables. 

## **Cable requirements** 

To meet ISO 11898, a bus cable with a characteristic impedance of 120 Ωshould be used. The maximum usable cable length for reliable communication decreases with increasing transmission speed. 

As a guide, you can use the following values measured by Kollmorgen; however, these values are not assured limits: 

- Characteristic impedance: 100–120 Ω 

- Cable capacitance max.: 60 nF / 1000 m 

- Lead loop resistance: 159.8 Ω/ 1000 m 

|Characteristic impedance: 100–120 Ω<br>Cable capacitance max.: 60 nF / 1000 m<br>Lead loop resistance: 159.8 Ω/ 1000 m<br>°<br>°<br>°|||||
|---|---|---|---|---|
|**Transmission Rate (kBaud)**|1000|500|250|125|
|**Maximum Cable Length (m)**|25|100|250|500|



Lower cable capacitance (max. 30 nF / 1000 m) and lower lead resistance (loop resistance, 115 Ω/ 1000 m) allow larger distances. The characteristic impedance 150 ± 5 Ωrequires terminating resistor 150 ± 5 Ω. 

## **Communication profile** 

For CANopen communication profile description refer to the manual " _AKD2G CAN-Bus Communication_ ". 

AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.12.2 CAN-Bus Wiring** 

AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.12.3 Baud rate for CAN-Bus** 

The transmission rate can be set via the parameter **CANBUS.BAUD** in WorkBench. 

|**Baud rate [kBit/s]**<br>125|**CANBUS.BAUD**<br>125 (default)|
|---|---|
|250|250|
|500|500|
|1000|1000|



With a fix baud rate, the drive sends the boot up message with the baud rate saved in the drive's non volatile memory after a power cycle. 

## **8.12.4 Node Address for CAN-Bus** 

The node address can be set via parameter **CANBUS.NODEID** in WorkBench. 

After changing the node address, you must turn off the 24 V auxiliary supply for the drive and then turn it on again. 

## **8.12.5 CAN-Bus Termination** 

The last bus device on both ends of the CAN-Bus system must have termination resistors. The AKD2G has built-in 132 ohms resistors that can be activated by connecting pins 1 and 6. An optional termination plug is available for AKD2G ( _P-AKD-CAN-TERM_ ). The optional termination plug is an RJ25 connector with an enclosed wire jumper between pins 1&6. The termination plug should be inserted into the X13 connector of the last drive in the CAN network. 

Remove the termination connector if the AKD2G is not the last CAN-Bus device and use X13 for connecting the next CAN node. 

AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.13 Service Interface (X20)** 

- RJ45 with built-in green/red dual-color LED 100/10 Mbit Ethernet TCP/IP 

- Supports Auto-IP, DHCP and fixed IP addressing 

- Supports point-to-point (i.e. Auto-IP) and connection via network switches 

- Supports automatic discovery in WorkBench if in the same subnet. 

|**Pin**||**Signal**|**Description**|
|---|---|---|---|
|1||Tx+|Transmit +|
|2||Tx-|Transmit -|
|3||Rx+|Receive +|
|4||Termination|Bob Smith termination|
|5||Termination|Bob Smith termination|
|6||Rx-|Receive -|
|7||Termination|Bob Smith termination|
|8||Termination|Bob Smith termination|



Operating, position control, and motion-block parameters can be set up by using the setup software on an ordinary commercial PC (➜ # 121). 

Connect the service interface X20 of the drive to an Ethernet interface on the PC directly or via a network switch, **while the supply to the equipment is switched off.** Use standard Cat. 5 Ethernet cables for connection (in some cases crossover cables will also work). 

Confirm that the link LED on the AKD2G (RJ45 connector) and on your PC (or network switch) are both illuminated. If both lights are green, then you have a good electrical connection. 

## **8.13.1 Possible Network Configurations** 

AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.14 I/O Connection (X21/X22/X23)** 

## **8.14.1 Pinout** 

## **X21 X22 X23** 

standard standard for dual-axis drives o optional 2 x 11 pins, pitch 3.5 mm to optional for single axis drives t SubD 15 pins HD A: left connector to 2 x 10 pins, pitch 3.5 mm t Mating connector: B: right connector to A: left connector male to B: right connector 

|**X21**<br>cE<br>a]<br>=|**Pin**<br>**Signal**<br>**Pin**<br>**Signal**<br>A1<br>Analog-In (AIN) 1 +<br>B1<br>Analog-Out (AOUT) 1<br>A2<br>Analog-In (AIN) 1 -<br>B2<br>AGND<br>A3*<br>Digital-In (DIN) 1<br>B3<br>+24 V<br>ES | el<br>~~|~~<br>~~**—**ee~~<br>x21|
|---|---|
||<br>ee|A4*<br>Digital-In (DIN) 2<br>B4<br>DGND<br>A5<br>Digital-In (DIN) 3<br>(HW-Enable Axis 1)<br>B5<br>Digital-Out (DOUT) 9 +<br>(Relay)<br>A6<br>Digital-In (DIN) 4<br>(HW-Enable Axis 2)<br>B6<br>Digital-Out (DOUT) 9 -<br>(Relay)<br>A7<br>Digital-In (DIN) 5<br>B7<br>Digital-Out (DOUT) 1<br>A8<br>Digital-In (DIN) 6<br>B8<br>Digital-Out (DOUT) 2<br>A9<br>Digital-In (DIN) 7<br>B9<br>Digital-Out (DOUT) 3<br>A10<br>Digital-In (DIN) 8<br>B10<br>Digital-Out (DOUT) 4<br>A11<br>STO-<br>A-<br>A1<br>B11<br>STO-<br>B-<br>A1<br>|<br>=<br>=<br>=<br>+——~~Pf~~<br>ee<br>=<br>ee=<br>ee<br>~~—~~<br>~~oo~~<br>EEE<br>~~=~~<br>—E—|
|**X22 (optional **|**for single axis drives, standard for dual-axis drives)**|
|:<br>E<br>|<br>=|**Pin**<br>**Signal**<br>**Pin**<br>**Signal**<br>A12<br>STO-<br>A-<br>A2,<br>dual-<br>axis<br>B12<br>STO-<br>B-<br>A2,<br>dual-<br>axis<br>A13<br>Digital-In (DIN) 9<br>B13<br>Digital-Out (DOUT) 5<br>A14<br>Digital-In (DIN) 10<br>B14<br>Digital-Out (DOUT) 6<br>A15<br>Digital-In (DIN) 11<br>B15<br>Digital-Out (DOUT) 7 +<br>A16<br>Digital-In (DIN) 12<br>B16<br>Digital-Out (DOUT) 7 -<br>A17<br>AGND<br>B17<br>Digital-Out (DOUT) 8 +<br>~~a~~|)~~Ls~~<br>es<br>es<br>es<br>es<br>oF [JE|
||A18<br>Analog-In (AIN) 2+<br>B18<br>Digital-Out (DOUT) 8 -<br>A19<br>Analog-In (AIN) 2-<br>B19<br>Analog-Out (AOUT) 2<br>A20*<br>Digital-In/Out (DIO) 1 +<br>B20*<br>Digital-In/Out (DIO) 2 +<br>A21*<br>Digital-In/Out (DIO) 1 -<br>B21*<br>Digital-In/Out (DIO) 2 -<br>es~~|~~<br>es|
|**X23 (optional)**<br>**Pin**<br>**Signal**||
|||2<br>Digital-In/Out (DIO) 6 +<br>3<br>Digital-In/Out (DIO) 6 -<br>2ee|
||6<br>Digital-In/Out (DIO) 5 +<br>se|
|1|7<br>Digital-In/Out (DIO) 5 -|
|10<br>+5 V<br>11<br>0 V<br>12<br>Digital-In/Out (DIO) 3 +<br>se<br>a ~~+~~||
||13<br>Digital-In/Out (DIO) 3 -|
||14<br>Digital-In/Out (DIO) 4 +|
||15<br>Digital-In/Out (DIO) 4 -<br>to|



AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.14.2 Technical data** 

|**8.14.2 Technical data**||
|---|---|
|**Interface**<br>Analog inputs<br>Analog-In (AIN) 1 to 2|**Electrical Data**<br>±10 VDC<br>common mode rejection ratio: > 30 dB at 60 Hz<br>resolution 16 bit and full monotonic<br>update rate: 16 kHz<br>non-linearity < 0.1% of full scale<br>offset drift max. 250 µV/°C<br>input impedance > 13 kΩ|
|Analog outputs<br>Analog-Out (AOUT) 1 to 2|0 to +10 VDC, max 20 mA<br>resolution 16 bit and full monotonic<br>update rate: 4 kHz<br>non-linearity < 0.1% of full scale<br>offset drift max. 250 µV/°C<br>short circuit protected to AGND<br>output impedance 110 Ω|
|Digital inputs<br>Digital-In (DIN) 1 to 2<br>IEC 61131-2 Type 1|ON: 11 VDC to 30 VDC, 2 mA to 15 mA<br>OFF: -5 VDC to 5 VDC, max.15 mA<br>galvanic isolation for 60 VDC<br>activation / de-activation delay: < 1 µs / < 1 µs|
|Digital inputs<br>Digital-In (DIN) 3 to 12<br>IEC 61131-2 Type 1|ON: 11 VDC to 30 VDC, 2 mA to 15 mA<br>OFF: -5 VDC to 5 VDC, max.15 mA<br>galvanic isolation for 60 VDC<br>delay activation/de-activation: about 5 µs / 500 µs|
|Digital outputs<br>Digital-Out (DOUT) 1 to 6|max. 30 VDC, 100 mA<br>short circuit proof<br>galvanic isolation for 60 VDC<br>delay activation/de-activation: about 5 µs / 300 µs|
|Digital outputs<br>Digital-Out (DOUT) 7 to 8|volt-free contacts, max 30 VDC, 100 mA<br>sink or source<br>galvanic isolation for 24 VDC from PE<br>delay activation/de-activation: about 5 µs / 50 µs|
|Digital inputs/outputs<br>Digital-In/Out (DIO) 1 to 6<br>RS485|reference potential X22: AGND, X23: 0V<br>input OFF: -0.3 V to +0.3 V<br>selectable termination, difference/single ended<br>delay activation/de-activation: about 50 ns|
|Digital output<br>Digital-Out (DOUT) 9|max. 30 VDC, 1A<br>max. 42 VAC, 1 A<br>galvanic isolation for 24 VDC from PE<br>delay open/close: 10 ms / 10 ms|
|Safe digital inputs<br>Axis 1: STO-A-A1, STO-B-A1<br>Axis 2: STO-A-A2, STO-B-A2|ON: 17 VDC to 30 VDC, 5 mA to 6 mA<br>OFF: 0 VDC to 5 VDC, max.1 mA<br>galvanic isolation for 60 VDC<br>delay activation/de-activation about: 1.5 ms / 3.5 ms|



AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.14.3 Analog Input** 

The drive is fitted with differential inputs for analog torque, velocity, or position control. The standard drive offers one analog input on X21, dual axis drives and drives with built-in option IO or DX offer a second analog input on X22. 

## **Technical characteristics** 

- Differential input voltage range: ± 10 V 

- Maximum input voltage referring to I/O Return: -12.5, +16.0 V 

- Resolution: 16 Bit and fully monotonic 

- Firmware update rate: 16 kHz 

- Unadjusted offset: < 50 mV 

- Offset drift typ: 250 µV / ° C 

- Gain or slope tolerance: +/- 3% 

- Nonlinearity: < 0.1% of full scale or 12.5 mV 

- Common Mode Rejection Ratio: > 30 dB at 60 Hz 

- Input impedance: > 13k Ωs 

- Signal to noise ratio referred to full scale: AIN.CUTOFF = 3000 Hz: 14 bit 

   - AIN.CUTOFF = 800 Hz: 16 bit 

## **Analog Input Wiring Diagram** 

## **Application examples for set point input Analog-In:** 

- reduced-sensitivity input for setting-up/jog operation 

- pre-control/override 

## **Defining the direction of rotation** 

Standard setting: clockwise rotation of the motor shaft (looking at the shaft end) affected by positive voltage between terminal (+ ) and terminal ( - ) 

To reverse the direction of rotation, swap the connections to terminals +/- or change keyword AXIS#.DIR in WorkBench. 

AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.14.4 Analog Output** 

Analog Outputs can be used to output converted analog values of digital measurements recorded in the drive. The standard drive offers one analog output on X21, dual axis drives and drives with built-in option IO or DX offer a second analog output on X22. 

## **Technical characteristics** 

- Output voltage range referring to AGND: 0 to 10 V 

- Resolution: 16 Bit and fully monotonic 

- Update rate: 4 kHz 

- Unadjusted offset: < 50 mV 

- Offset drift typ: 250 µV/°C 

- Gain or slope tolerance: +/- 3% 

- Nonlinearity: < 0.1% of full scale or 20 mV 

- Output impedance: 110 Ω 

- Specification complies with IEC 61131-2 Table 11 

- -3 dB Bandwidth: >8 kHz 

- Maximum output current: 20 mA 

- Capacitive load: any value but response speed limited by max Iout and by Rout 

- Protected for short circuit to AGND 

## **Analog Output Wiring Diagram** 

AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.14.5 Digital Inputs** 

The drive provides 8 digital inputs on X21. Dual axis drives and drives with built-in option IO or DX offer additional 4 inputs on X22 and 2 programmable Input/Outputs on X22. If X23 is built-in and not used for feedback or EEO function, then it offers 4 additional programmable Input/Outputs. 

All inputs can be used to initiate pre-programmed actions. A list of actions is included in the WorkBench. If an input is programmed, it must be saved to the drive. 

The drive provides 4 safe digital inputs on X21 and X22. These inputs can be used as safe inputs, based on the installed functional option (➜ # 127). 

The maximum cable length for digital I/O supply (24V/DGND) is 3 m. If longer cables are required, the user need to take care of EMC measures. 

Depending on the selected function, the inputs are high or low active. Digital input filter can be set in WorkBench to change sensitivity of the inputs (see Online Help). 

## **8.14.5.1 Digital-In 1 and 2** 

These inputs (IEC 61131-2 Type 1) are particularly fast and are therefore suitable for position latch functions. They can also be used as 24 V inputs for electronic gearing (➜ # 93). 

## **Technical characteristics** 

- Floating, reference common line is DGND 

- High: 11 to 30 V/2 to 15 mA , Low: -5 to +5 V/<15 mA 

- Update rate: firmware reads hardware input state every 250 µs 

- High accuracy latch: motor feedback position or interpolated time is latched or captured within 2 µs of input signal transition (with digital input filter set to 40 ns) 

- The AKD2G capture engine is polled every 62.5 µs (16 kHz) by the firmware 

## **Wiring example** 

AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.14.5.2 Digital-In 3 to 12** 

These inputs (IEC 61131-2 Type 1) are programmable with the setup software. 

## **Manufacturer setting:** 

- Digital-In 3: HW-Enable Axis 1 

- Digital-In 4: HW-Enable Axis 2 

- Digital-In 5 ...12: off 

Choose the function you require in WorkBench. For more information refer to WorkBench. 

## **Technical characteristics** 

- Floating, reference common line is DGND 

- High: 11 to 30 V/2 to 15 mA , Low: -5 to +5 V/<15 mA 

Update rate: firmware reads hardware input state every 250 µs 

## **Wiring example** 

AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.14.5.3 Digital-In/Out 1 and 2** 

Pins X22/A20-A21 (Digital-In/Out 1) and X22/B20-B21 (Digital-In/Out 2) can be defined as either inputs or outputs. For programming refer to WorkBench. 

- NOT compatible with 24V signal level! Will be damaged if connected to +24V! 

## **Technical characteristics if configured as input** 

- RS485, reference common line is AGND 

- No wire break detection 

- Digital IN/OUT 1/2: Selectable DC termination for differential or single ended input Update rate: firmware reads hardware input state every 250 µs 

## **Wiring example** 

AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.14.5.4 Digital-In/Out 3 to 6** 

X23 can be used for digital I/O. The channels can be defined as inputs or outputs. For programming refer to WorkBench. 

- NOT compatible with 24V signal level! Will be damaged if connected to +24V! 

## **Technical characteristics if configured as input** 

- RS485, reference common line is 0V 

- No wire break detection 

- Digital IN/OUT 3/4: Selectable DC termination for differential or single ended input 

- Digital IN/OUT 5/6: AC termination for single ended input 

- Update rate: firmware reads hardware input state every 250 µs 

## **Wiring example** 

AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.14.6 Digital Outputs** 

The drive provides 4 digital outputs on X21. For more information refer to the setup software. 

Dual axis drives and drives with built-in option IO or DX offer additional 4 digital outputs and 2 programmable Input/Outputs. If X23 is built-in and not used for feedback or EEO function, then it offers 4 additional programmable Input/Outputs. 

The relay output can be used as fault or ready to operate signal. 

- The maximum cable length for digital I/O supply (24V/DGND) is 3 m. If longer cables are required, the user need to take care of EMC measures. 

Choose the required action in the setup software. Messages from pre-programmed actions. A list of actions is included in the WorkBench. If an output is programmed, it must be saved to the drive. 

## **8.14.6.1 Digital-Out 1 to 6** 

These outputs are programmable with the setup software. By default, all outputs are off. 

## **Technical characteristics** 

- The outputs can switch +5 V to +30 V 

- All digital outputs are floating 

- High side, output current max.100 mA 

- Update rate: 250 µs 

AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.14.6.2 Digital-Out 7 and 8** 

These outputs are programmable with WorkBench. By default, all outputs are not programmed (off). 

## **Technical characteristics** 

- The outputs can switch +5 V to +30 V 

- Galvanic isolation for 24 VDC from PE 

- The two channels are isolated from one another and not referred to a common potential Output current max.100 mA 

- Can be wired as sinking or sourcing (see examples below) 

- Update rate: 250 µs 

## **Wiring examples** 

AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.14.6.3 Digital-In/Out 1 and 2** 

Pins X22/A20-A21 (Digital-In/Out 1) and X22/B20-B21 (Digital-In/Out 2) can be used as either inputs or outputs. For programming refer to WorkBench. 

## **Technical characteristics if configured as output** 

- RS485, reference common line is AGND 

- Selectable DC terminationfor differential or single ended output, no wire break detection Update rate: 250 µs 

## **8.14.6.4 Digital-In/Out 3 to 6** 

X23 can be used for digital I/O. The channels can be defined as inputs or outputs. For programming refer to WorkBench. 

## **Technical characteristics if configured as output** 

- RS485, reference common line is 0V 

- No wire break detection 

- Digital IN/OUT 3/4: Selectable DC termination for differential or single ended output 

- Digital IN/OUT 5/6: AC termination for single ended output Update rate: 250 µs 

AKD2G-S Installation Manual, Safety 1 | 8   Electrical Installation 

## **8.14.6.5 Digital-Out 9, Relay contacts** 

Digital-Out 9 is programmable with the setup software (for more information refer to WorkBench). 

By default, the output function is defined as ready to operate output by action keyword. 

- If an inductive load (relay or similar) is used, a freewheeling diode must be added to the load. 

## **Technical characteristics** 

- Relay output, max. 30 VDC or 42 VAC, 1 A 

- Galvanic isolation for 24 VDC from PE 

- Time to close: max. 10 ms 

- Time to open: max. 10 ms 

AKD2G-S Installation Manual, Safety 1 | 9   Setup 

## **9 Setup** 

|**9.1**|**Important Notes**|**116**|
|---|---|---|
|**9.2**|**Guide to drive setup**|**117**|
|**9.3**|**Switch-On and Switch-Off Behavior**|**123**|
|**9.4**|**Fault and Warning Messages**|**125**|
|**9.5**|**Troubleshooting**|**126**|



AKD2G-S Installation Manual, Safety 1 | 9   Setup 

## **9.1 Important Notes** 

Only professional personnel with extensive knowledge in the fields of electrical engineering and drive technology are allowed to test and set up the drive 

## 4. DANGER 

## **Lethal Voltage!** 

There is a danger of serious personal injury or death by electrical shock. Lethal danger exists at live parts of the device. 

- Built-in protection measures such as insulation or shielding may not be removed. Work on the electrical installation may only be performed by trained and qualified personnel, in compliance with the regulations for safety at work, and only with switched off mains supply, and secured against restart. 

## **Automatic Restart!** 

Risk of death or serious injury for humans working in the machine. The drive might restart automatically after power on, voltage dip or interruption of the supply voltage, depending on the parameter setting. If parameter AXIS#.ENDEFAULT is set to 1, 

then place a warning sign ("WARNING: Possible Automatic Restart" or similar) to the machine. 

- Ensure, that power on is not possible, while humans are in a dangerous zone of the machine. 

## ZA\CAUTION 

## **High Temperature!** 

Risk of minor burns. The heat sink of the drive can reach temperatures up to 80°C in operation. 

Check the heat sink temperature before handling the drive. 

Wait until the heat sink has cooled down to 40°C before touching it. 

If the drive has been stored for more than 1 year, you must re-form the capacitors in the DC bus link circuit. Re-forming procedures are described in the KDN (Forming). Additional information on setting up the equipment: 

- Programming parameters and control loop behavior are described in the AKD2G User Manual (Online Help) . 

The setup of any fieldbus is described in the corresponding manual on the DVD. 

AKD2G-S Installation Manual, Safety 1 | 9   Setup 

## **9.2 Guide to drive setup** 

Setup must be done in two major steps: 

1. Drive setup (this section). This section presents an example to test the drive initially. If the drive (motor, feedback, control circuits, I/Os) is well parameterized, then proceed with the 

2. Functional Safety setup (➜ # 131) . 

## **9.2.1 Initial Drive Test Procedure** 

## **9.2.1.1 Unpacking, mounting, and wiring the AKD2G** 

1. Unpack the drive and accessories. 

2. Mount the drive. 

3. Wire the drive or apply the minimum wiring for drive testing as described below. 

4. Make sure you have on hand the following information about the drive components: rated mains supply voltage 

   - motor type (motor data, if the motor type is not listed in the motor database) feedback unit built into the motor (type, poles/lines/protocol) moment of inertia of the load 

## **9.2.1.2 Minimum wiring for drive test without load, example** 

This wiring diagram based on default settings is for general illustration only and does not fulfill any requirements for EMC, functional safety, or functionality of your application. 

AKD2G-S Installation Manual, Safety 1 | 9   Setup 

## **9.2.1.3 Confirm connections (example: directly to PC)** 

You can turn on logic power to the drive through the X10 connector (mains power voltage is not needed for communications). 

Confirm that the link LEDs on the drive (green LED on the RJ45 connector) and on your PC are both illuminated. If both LEDs are illuminated, then you have a working electrical connection. The LCD display shows a sign, if the connection between AKD2G and WorkBench is active. 

Use WorkBench to configure the drive via the service interface. 

## **9.2.1.4 System integration** 

## **MAC Address** 

The unique MAC address is pre-defined by the manufacturer (see nameplate). 

## **Service IP Address** 

The AKD2G service port X20 supports auto-IP, DHCP and static IP addressing. 

The drive is delivered with IP address 0.0.0.0. Depending on the connection (switch or PC) either DHCP or auto-IP mechanism assignes a unique IP address. 

WorkBench uses the IP address to detect AKD2G devices in the LAN and start communication. With WorkBench you can set a static IP address for the drive (keyword _IP.ADDRESS_ ). 

## **EtherCAT Node Address** 

The EtherCAT node address is assigned automatically by the EtherCAT master. 

## **CAN Node ID** 

Set a CAN node ID for the drive in WorkBench (keyword _CANBUS.NODEID_ ). 

AKD2G-S Installation Manual, Safety 1 | 9   Setup 

## **9.2.1.5 Install and start WorkBench** 

WorkBench is available from the DVD included with the drive. WorkBench is also available on the Kollmorgen Website: www.kollmorgen.com. Select the install file and follow the instructions given by the installer. 

Once installation is complete, click the WorkBench icon to start the program. 

## **9.2.1.6 Setup the axis in WorkBench** 

Use the setup wizard and 

1. Connect the axis, 

2. Setup the axis and 

3. Save parameter set to the drive. 

Refer to the WorkBench Online Help for details. 

## **9.2.1.7 Enable the axis (Hardware)** 

1. Switch 24 V to the STO inputs (X21/A11-B11 for axis 1 or X21/A12-B12 for axis 2) 

2. Switch 24 V to the digital inputs for Hardware Enable Axis 1 (X21/A5) or 2 (X21/A6). 

## **9.2.1.8 Move the motor axis** 

1. Select the axis in WorkBench 

2. Enter Service Motion view 

3. select "Reversing", check the default velocity and time settings for plausibility 

4. Click on Start. 

## **9.2.1.9 Tune the axis** 

Details see _WorkBench Online Help_ 

AKD2G-S Installation Manual, Safety 1 | 9   Setup 

## **9.2.2 Setup software WorkBench** 

This chapter describes the installation of the setup software WorkBench for AKD2G drives. Kollmorgen offers training and familiarization courses on request. 

## **9.2.2.1 Use as directed** 

The setup software is intended to be used for altering and saving the operating parameters for the AKD2G series of drives. The attached drive can be set up with the help of this software, and during this procedure the drive can be controlled directly by the service functions. 

Only professional personnel who have the relevant expertise (➜ # 14) are permitted to carry out online parameter setting for a drive that is running. 

Sets of data that have been stored on data media are not safe against unintended alteration by other persons. Unexpected move could be the result if you use unchecked data. After loading a set of data you must therefore validate parameters which are relevant for the application before enabling the drive. 

AKD2G-S Installation Manual, Safety 1 | 9   Setup 

## **9.2.2.2 Software description** 

Each drive must be configured to the requirements of your machine. For most applications, you can use a PC and WorkBench (the drive setup software) to set up the operating conditions and parameters for your drive. 

The PC is connected to the drive by an Ethernet cable (➜ # 102). The setup software provides the communication between the PC and AKD2G. You can find the setup software on the accompanying DVD and in the download area of the Kollmorgen website. 

You can alter parameters easily and instantly observe the effect on the drive, since there is a continuous (online) connection to the drive. You can also read important actual values from the drive, which are displayed on the monitor of the PC (oscilloscope functions). 

You can save sets of data on data media (archiving) and load them into other drives or use them for backup. You can also print out the data sets. 

Most standard feedback systems are plug and play compatible. Motor nameplate data is stored in the feedback device and read by the drive automatically at startup. Non-plug and play Kollmorgen motors are stored in WorkBench and can be loaded with one-click using the Motor screen in the WorkBench software. 

An extensive online help with integrated description of all variables and functions supports you in each situation. 

## **9.2.2.3 Hardware requirements** 

The Service interface (X20, RJ45) of the drive is connected to the Ethernet interface of the PC by an Ethernet cable (➜ # 102). 

## **Minimum requirements for the PC:** 

Processor: at least 1 GHz RAM: 512 MB 

Graphics adapter : Windows compatible, color, minimum 1024 x 768 dpi 

Drives : hard disk with at least 500 MB free space, DVD drive or download from internet Interface : one free Ethernet Interface, or Switch port 

## **9.2.2.4 Operating systems** 

## **Windows 7/8/10** 

WorkBench works with Windows 7, 8 and 10. DotNet framework 4.6.1 or higher is required. Internet Explorer 10 or higher. 

## **Unix, Linux** 

The software does not run on Unix/Linux. 

AKD2G-S Installation Manual, Safety 1 | 9   Setup 

## **9.2.2.5 Installation under Windows 7/8/10** 

The DVD includes an installation program for the setup software. The latest setup software can be downloaded from www.kollmorgen.com. 

## **Installation** 

- Autostart function activated: 

- Insert the DVD into a free drive. A window with the start screen opens. There you find a link to the setup software WorkBench. Click it and follow the instructions. Autostart function deactivated: 

- Insert the DVD into a free drive. Click **Start** (task bar), then **Run** . Enter the program call: x:\index.htm (x = correct DVD drive letter). 

Click **OK** and proceed as described above. 

## **Connection to the Ethernet interface of the PC** 

- Connect the interface cable to an Ethernet interface on your PC or to a Switch and to the AKD2G service interface X20 (➜ # 102). 

The LCD display shows a sign, if the connection between AKD2G and WorkBench is active. 

AKD2G-S Installation Manual, Safety 1 | 9   Setup 

## **9.3 Switch-On and Switch-Off Behavior** 

This chapter describes the switch-on and switch-off behavior of the AKD2G with STO. 

## **Behavior of “holding brake” function** 

Drives with an enabled holding brake function have a special timing for switching on and off the output stage (➜ # 85). Events that remove the AXIS#.ACTIVE signal trigger the holding brake to apply. As with all electronic circuits, the general rule applies that there is a possibility of the internal holding brake module failing. 

Functional safety, e.g. with hanging load (vertical axes), requires an additional mechanical brake which must be safely operated, for example by a safety control. 

If velocity drops below threshold _AXIS#.CS.VTHRESH_ or timeout occurs during a stop procedure, the brake is applied. Set parameter AXIS#.MOTOR.BRAKEIMM to 1 with vertical axes, to apply the motor holding brake (➜ # 85) immediately after faults or Hardware Disable. 

## **Behavior when undervoltage condition is present** 

The behavior in an undervoltage condition depends on the VBUS.UVMODE setting. 

**VBUS.UVMODE** DC Bus Undervoltage Mode. Consult the _WorkBench Online Help_ for configuring the parameter. **0** The drive will report a F2007 undervoltage fault any time an undervoltage condition occurs. **1 (default)** The drive will report a warning W2007 if not enabled. The drive will report a fault if the drive is enabled when the condition occurs, or an attempt is made to enable while an under voltage condition occurs. ~~—~~ 

**Functional Safety** The drive can be secured to standstill with STO. Even when power is being supplied, the drive shaft is protected against unintentional restart. The chapter “Functional Safety” describes how to use the safety functions (➜ # 128). 

AKD2G-S Installation Manual, Safety 1 | 9   Setup 

## **9.3.1 Switch-on behavior in standard operation** 

The diagram below illustrates the correct functional sequence for switching the drive on. 

## **9.3.2 Switch-off behavior** 

Chapter in process 

AKD2G-S Installation Manual, Safety 1 | 9   Setup 

## **9.4 Fault and Warning Messages** 

## **9.4.1 Fault and warning messages AKD2G** 

A Fault is generally a notification of a critical system failure which will stop machine operation. Depending on the severity of the fault will depend on which system-stop mechanism is used. 

A Warning is generally a notification to the user which is not critical and does not require the machine to immediately shut off. 

Faults and Warnings follow the same pattern and are identified by a four digit code: 

G G X X, where GG is a two digit group code, and XX is a two digit ID. 

|**GG**<br>10|**Group**<br>System|**GG**<br>4#|**Group**<br>Feedback (# indicates feedback number)|
|---|---|---|---|
|11|File|50|Motor|
|15|Hardware|55|Wake and Shake|
|20|Power|60|Motion|
|25|Temperature|70|Fieldbus|
|30|Software|90|Safety|



The display on the front panel of the drive shows the code of the fault or warning that occurred. Navigate with B1 / B2 to the Fault screen to see a short description of the fault or warning. 

You can retrieve faults on a per-axis basis with the keyword: AXIS#.FAULTS, where # is the Axis number. For retrieving warnings use AXIS#.WARNINGS, or DRV.WARNINGS. 

Multiple faults may be present when a fault condition is occurring. Check the WorkBench Fault Screen or read the status of DRV.FAULTS and AXIS#.FAULTS for the entire list of faults. 

DRV.FAULTS will return all faults across all axes, with the format #-GGXX where # is the axis number and GGXX is the four digit fault/warning code. 

Eliminate errors and faults in compliance with work safety rules. Troubleshooting only by qualified and trained staff. 

More information about fault messages, remedy and clearing faults can be found in the WorkBench User Manual . 

AKD2G-S Installation Manual, Safety 1 | 9   Setup 

## **9.5 Troubleshooting** 

Drive problems occur for a variety of reasons, depending on the conditions in your installation. The causes of faults in multi-axis systems can be especially complex. If you cannot resolve a fault or other issue using the troubleshooting guidance presented below, customer support can give you further assistance. 

Eliminate errors and faults in compliance with work safety rules. Troubleshooting only by qualified and trained staff. 

More details on the removal of faults can be found in the WorkBench User Manual. 

|**Problem**<br>HMI message:<br>Communication fault|**Possible Causes**<br>1. wrong cable used, cable plugged<br>into wrong position on drive or PC<br>2. wrong PC interface selected|**Remedy**<br>1. plug cable into the correct sockets on the<br>drive and PC<br>2. select correct interface|
|---|---|---|
|Drive does not enable|1. HW Enable configured but not wired<br>2. HW or SW Enable not set|1. connect HW Enable to the selected input<br>2. Apply 24V to HW Enable and select SW<br>Enable in WorkBench / Fieldbus|
|Motor does not rotate|1. drive not enabled<br>2. software enable not set<br>3. break in setpoint cable<br>4. motor phases swapped<br>5. brake not released<br>6. drive is mechanically blocked<br>7. motor pole no. set incorrectly<br>8. feedback set up incorrectly|1. apply ENABLE signal<br>2. set software enable<br>3. check setpoint cable<br>4. correct motor phase sequence<br>5. check brake control<br>6. check mechanics<br>7. set motor pole no.<br>8. set up feedback correctly|
|Motor oscillates|1. gain is too high (speed controller)<br>2. feedback cable shielding broken<br>3. AGND not wired up|1. reduce AXIS#.VL.KP (speed controller)<br>2. replace feedback cable<br>3. join AGND to CNC-GND|
|Drive reports<br>following error|1. Irms or Ipeak set too low<br>2. current or velocity limits apply<br>3. accel/decel ramp is too long|1. verify motor/drive sizing<br>2. verify that AXIS#.IL.LIMITN/P,<br>AXIS#.VL.LIMITN/P are not limiting the<br>drive<br>3. reduce AXIS#.ACC/AXIS#.DEC|
|Motor overheating|1. motor operating above its rating<br>2. motor current settings incorrect|1. verify motor/drive sizing<br>2. verify motor continuous and peak current<br>values are set correctly|
|Drive too soft|1. AXIS#.VL.Kp (velocity) too low<br>2. AXIS#.VL.Ki (velocity) too low<br>3. filters set too high|1. increase AXIS#.VL.KP (velocity)<br>2. increase AXIS#.VL.KI (velocity)<br>3. refer to documentation regarding reducing<br>filtering (AXIS#.VL.AR*)|
|Drive runs roughly|1. AXIS#.VL.Kp (velocity) too high<br>2. AXIS#.VL.Ki (velocity) too high<br>3. filters set too low|1. reduce AXIS#.VL.KP (velocity)<br>2. reduce AXIS#.VL.KI (velocity)<br>3. refer to documentation regarding increas-<br>ing filtering (AXIS#.VL.AR*)|



AKD2G-S Installation Manual, Safety 1 | 10   Functional Safety 

## **10 Functional Safety** 

Valid for AKD2G Hardware Revision A 

Beta drives: Safety functions are neither approved nor certified yet. Do not use this functionality in applications with functional safety request until further notice. 

## **Revision History for section Functional Safety** 

|**Revision**|**Revision**|||**Remarks**||
|---|---|---|---|---|---|
|S101, 12/2019||||Functional Safety Option 1||
|||||||
|||||||
|||||||
|**10.1**|**General notes**||||**128**|
|**10.2**|**Settings**||||**131**|
|**10.3**|**Safety Function Option 1 (I/O,**|||**Safety Function Option 1 (I/O, SIL2 PLd)**|**132**|
|**10.4**|**Verification**||||**137**|
|**10.5**|**Safety Faults, Safety Warnings**|||**Safety Faults, Safety Warnings**|**138**|
|**10.6**|**Functional Safety Keyword Reference Guide**||||**140**|



AKD2G-S Installation Manual, Safety 1 | 10   Functional Safety 

## **10.1 General notes** 

Resulting Functional Safety classification (SIL and/or PL level) is calculated across the drive system. The drive system usually consists of 

- motion controller (e.g. AKC/KAS), 

- safety controller (e.g. KSM), 

- servo drives (AKD2G) and servo motors (e.g. AKM2G), motor brakes, feedback systems, cables to connect drive and motor, 

- sensors/actors. 

The user must ensure the compliance of the application with all relevant directives and local electrical code. The user is responsible for implementation and validation of the drive system and safety system. 

The safety properties listed in this chapter can be reached with Kollmorgen components. 

Only properly qualified personnel are permitted to perform such tasks as installation, setup and parameterization. 

- Mechanical installation: only by qualified personnel with mechanical expertise according to IEC 60417-6183. 

- Electrical installation: only by qualified personnel with electrotechnical expertise according to IEC 60417-6182. 

- Parameterizing Functional Safety: only by trained personnel with expertise appropriate to the complexity and safety integrity level of the drive system. 

- Verification/Validation: only by trained personnel after any changes to the installation. The expertise of the personnel must be appropriate to the complexity and safety integrity level of the drive system. 

## A\CAUTION 

## **High electrical voltage!** 

Risk of electrical shock! The safety functions do not provide an electrical separation from the power output. If manual access to the motor or drive power terminals is necessary, 

- disconnect the drive from mains supply, 

- consider the discharging time of the DC-Bus link, 

- ensure the cabinet is safely disconnected and protected against unintended switch-on (for instance, with a lock-out and warning signs). 

AKD2G-S Installation Manual, Safety 1 | 10   Functional Safety 

## **10.1.1 Use as directed** 

Safety functions are intended to reduce the risk of the machine operation to the required tolerable risk. To achieve functional safety, the wiring of the safety circuits must meet the safety requirements of IEC 60204, ISO 12100 and ISO 13849. 

- The network, where the drive is connected to, must be secured according to state-of-theart information technology security requirements. 

- The user IT specialists shall analyze whether further security requirements are applicable to ensure functional safety. 

- The drive firmware can be updated. The parameter sets must be reloaded, verified and proof tested before normal operation is started. 

- In certain types of machinery, two motors drive a single mechanical axis; a typical example is a gantry where the two sides of the gantry have their own drives and motors. It is the responsibility of the user to ensure that a fault reaction on the first motor-drive set is also carried out on the second motor-drive set and vice-versa. Safe I/O and/or a safe field bus such as FSoE can be used to achieve this. 

- Beta drives: Safety functions are neither approved nor certified yet. Do not use this functionality in applications with functional safety request until further notice. 

## **10.1.2 Prohibited use** 

The safety functions must not be used if the drive is to be made inactive for Emergency-Off situations. In an Emergency-Off situation, the main relay is switched off (by the EmergencyOff button). 

The STO function requires two-channel control if the performance level SIL2 / PLd Cat.3 in the system is to be achieved. The connection of a constant 24 VDC voltage to one of the STO inputs is not permitted if the safety function is to be used. 

The device does not require maintenance. Opening the device voids the warranty. In case of damage or malfunction the drive must be sent for repair or must be replaced. 

## **10.1.3 Abbreviations used for functional safety** 

More abbreviations see (➜ # 12). 

|**Abbreviation**<br>A#, AXIS#|**Meaning**<br>A# or AXIS# are placeholders for the axis number. Used with keywords<br>(AXIS#.SAFE.STO.ACTIVE) or signal names (STO-A-A#)|
|---|---|
|(➜# 53)|"see page 53" in this document|
|➜xyz|"see chapter xyz" in this document|
|CCF|Common cause failure|
|FS1|Functional Safety Option 1 (STO)|
|HFT|Hardware fault tolerance|
|MTTFd|Mean time to dangerous failure|
|OSSD|Output Switching Signal Device|
|PELV|Protective Extra Low Voltage|
|PFHd|Probability of dangerous failure per hour|
|PL|Performance Level|
|SC|Systematic Capability|
|SFF|Safe failure fraction|
|SIL|Safety Integrity Level|
|STO|Safe Torque Off|
|TM|Mission time|



AKD2G-S Installation Manual, Safety 1 | 10   Functional Safety 

## **10.1.4 Enclosure, wiring** 

## **Enclosure** 

Since the drive meets IP20, you must select an enclosure that permits safe operation of the drive. The enclosure must at least meet IP54 . 

|**Relative Humidity**<br>5 to 95% , no condensation, class 1K3.|**Relative Humidity**<br>5 to 95% , no condensation, class 1K3.|
|---|---|
|**Operation in accordance with IEC 61800-2**<br>**Environmental class**<br>Environmental class 3K3||
|**Temperature**|Internal regen resistor used:<br>0 to +40 °C under rated conditions<br>+40 to +60 °C with current derating 3 % per Kelvin<br>Internal regen resistor not used:<br>0 to +50 °C under rated conditions<br>+50 to +60 °C with current derating 2 % per Kelvin|
|**Relative Humidity**|5 to 85%, no condensation, IEC 61800-2 class 3K3|
|**Site altitude**|Up to 1000 m above mean sea level (AMSL): no restriction<br>1,000 to 2,000 m AMSL: power derating 1.5%/100 m<br>Maximum altitude: 2000 m AMSL|
|**Drive EMC immunity**|Increased immunity according to EN 61800-5-2|
|**Drive Pollution level**|Pollution level 2 as per IEC 60664-1|
|**Drive Vibration class**|Class 3M1 according to IEC 61800-2|
|**Drive Shock class**|Class L according to IEC 61800-2|
|**Drive protection class**|IP20 according to IEC 60529|
|**Enclosure**|Minimum cabinet size (WxHxD): 406 x 406 x 254 mm|
|**Enclosure protection**|At least IP 54 according to IEC 60529|



## **Wiring** 

Wiring inside the specified enclosure (IP54) must meet the requirements of the standard IEC 60204-1 and ISO 13849-2 (Table D.4). 

Wiring outside the specified enclosure (IP54) must be laid durably protected from outside damage (for example, by laying the cable in a duct), placed in different sheathed cables, or protected individually by grounding connection. 

Use copper wires, 0.5 mm² (20 awg), wire ferrules. Maximum distance for unshielded cables 30 m. Maximum cable length for digital I/O supply (24V/DGND) is 3 m. 

When wiring the digital inputs and outputs, take care, that short circuits between the inputs, the outputs or to a supply line are avoided. 

AKD2G-S Installation Manual, Safety 1 | 10   Functional Safety 

## **10.2 Settings** 

## **Display (example for a dual-axis module)** 

**Push-buttons (B1, B2)** 

A short button press invokes the action corresponding to the symbol directly above the button. On the dashboard for example, 

a short press on B1 causes the menu system to appear, and a short press on B2 causes a help screen to appear. 

A long press (greater than 2 seconds) on B2 returns the display to the previous screen. 

|A long press (greater than 2 seconds) on B2 returns the display to the previous screen.<br>Ll|A long press (greater than 2 seconds) on B2 returns the display to the previous screen.|
|---|---|
|**B1 / B2 Functions**<br>Boot from SD card|**Description**<br>Push both buttons during power up to boot with data from SD card.<br>Press the buttons first, then hold it down while turning on the 24 V<br>power supply.|
|Boot from flash<br>fallback image|Remove the SD card, then press both buttons and hold them down<br>while turning on the 24 V power supply to boot from an on-board<br>recovery image.|



AKD2G-S Installation Manual, Safety 1 | 10   Functional Safety 

## **10.3 Safety Function Option 1 (I/O, SIL2 PLd)** 

Beta drives: Safety functions are neither approved nor certified yet. Do not use this functionality in applications with functional safety request until further notice. 

Valid for AKD2G devices with Functional Safety Option 1: 

The safety function STO on the AKD2G with functional safety option 1 is certified. 

The drive is ready to operate with pre-configured STO function. 

## **Standards** 

|**Standard**|**Edition**||**Content**||
|---|---|---|---|---|
|ISO 13849<br>2015|||Safety of machinery: Safety-related parts of control systems||
|IEC 62061<br>2015|||Functional safety of electrical/electronic/programmable electronic||
||||safety-related systems||
|**Available Safety Functions**|**Available Safety Functions**||||
|**Abbr.**|**Function**||**Activation**|**Refer to**|
|**STO**|Safe Torque Off||Safe Torque Off<br>Safe digital inputs for one or for both axis|(➜# 134)|



## **Available Safety Functions** 

AKD2G-S Installation Manual, Safety 1 | 10   Functional Safety 

## **10.3.1 Technical Data** 

Safe inputs are fixed to the STO function. 

When STO function (Safe Torque Off) is not needed, then all STO inputs must be connected directly with +24 V. The STO function is then bypassed and cannot be used. 

## **I/O hardware data** 

Reference ground is DGND Use 24 VDC ±15% PELV power supply Galvanic isolation for 60 VDC High level 17 VDC to 30 VDC, 5 mA to 6 mA Activation delay about 5 µs Low level 0 VDC to 5 VDC, max.1 mA De-activation delay about 500 µs 

## **Pinout** 

**X21 Signal Description** A11 STO-A-A1 STO channel A (for axis 1) B11 STO-B-A1 STO channel B (for axis 1) ~~——__——~~ Drives with two axes, or option IO or DX: **X22 Signal Description** A12 STO-A-A2 STO channel A (for axis 2) B12 STO-B-A2 STO channel B (for axis 2) ~~————~~ **Keywords Keyword Description** AXIS#.SAFE.STO.A Reads the status of STO input channel A for axis #. AXIS#.SAFE.STO.B Reads the status of STO input channel B for axis #. AXIS#.SAFE.STO.ACTIVE Reads the STO status of axis #. AXIS#.SAFE.STO.REPORTFAULT F9000 and W9000 are triggered for axis # only, if set to 1 (default). ~~nn~~ For full keyword description refer to the _Keywords Reference Guide_ (➜ # 140). 

## **Factory Default Settings** 

**ATTENTION** : The drive is ready to operate with pre-configured STO function. AXIS#.SAFE.STO.REPORTFAULT is set to 1. 

## **10.3.2 Safety Properties Overview** 

OSSD test pulses are not required. The inputs however are compatible with safety equipment that emits test pulses. Incoming test pulses of up to 1 ms duration are ignored. The dwell time of the test pulses should not exceed 10%. 

The hardware fault tolerance is HFT = 1 according to IEC 61508. Two faults might lead to loss of the safety functions. 

The systematic capability according to IEC 61508 for the safety-related subsystems of the drive are SC = 2. TM = 20 Years, SFF = 100%. **Function ISO MTTFd DCAVG IEC PFH CCF Response 13849-1 Years [%] 62061 [1/h] [%] time** STO dual channel PL d, Cat. 3 100 60 SIL 2 3.4E-08 >65 < 3.5 ms ~~a~~ 

AKD2G-S Installation Manual, Safety 1 | 10   Functional Safety 

## **10.3.3 STO (Safe Torque Off)** 

**S** afe **T** orque **O** ff description for drive option Functional Safety 1. 

STO is suited for SIL 2 according to IEC 62061 and PLd / Cat.3 according to ISO 13849-1. STO is a type A subsystem according to IEC 61508. 

STO turns off the drive output stage that powers the motor. STO function corresponds to an uncontrolled braking according to IEC 60204-1, category 0. 

## **10.3.3.1 Important Notes** 

The safety properties given in this documentation refers to the device AKD2G with functional safety option 1. The user has to determine the safety properties of the safety chain. 

## **Vertical load could fall!** 

Serious injury could result when a suspended load is not properly blocked. The drive cannot hold a vertical load when STO is active. 

Add a safe mechanical blocking (for instance, a motor-holding brake). 

## **10.3.3.2 Activation** 

The digital STO inputs (channel A and B) must be connected to the output of a safety device, which at least meets the requirements of PLd, Cat. 3 according to ISO 13849. Technical data of the safe inputs (➜ # 133). 

If one of the STO inputs goes open-circuit or 0 V, then power supply to the motor stops within 3.5 ms. The motor will lose all torque and coast to a stop. 

If the drive detects that the two STO inputs are in a different state for longer than 100 ms, then a simultaneity fault F9005 occurs (➜ # 137). 

Review the enclosure and wiring instructions (➜ # 130). 

## **Wiring example STO single axis, SIL2/PLd, Emergency Stop** 

Note: AXIS#.SAFE.STO.REPORTFAULT should be set to 1 if STO is activated by a switch. 

AKD2G-S Installation Manual, Safety 1 | 10   Functional Safety 

## **Wiring example STO dual axis, SIL2/PLd, Safety Control** 

## **10.3.3.3 Restart** 

## Example for Axis 1. 

|Example 1:<br>Axis 1 was disabled,<br>STO is activated|**AXIS1.SAFE.STO.**<br>**REPORTFAULT = 1**<br>Message W9000<br>Restart:<br>1. deactivate STO<br>2. enable axis 1|**AXIS1.SAFE.STO.**<br>**REPORTFAULT = 0**<br>Restart:<br>1. deactivate STO<br>2. enable axis 1|
|---|---|---|
|Example 2:<br>Axis 1 was enabled,<br>STO is activated|Messages W9000 and F9000<br>Restart:<br>1. disable axis 1<br>2. deactivate STO<br>3. clear fault<br>4. enable axis 1|Restart:<br>1. deactivate STO|
|Example 3:<br>Axis 1 was disabled,<br>STO is activated faulty|Message F9005<br>Restart:<br>1. check wiring<br>2. remedy the cause<br>3. deactivate STO<br>4. clear fault<br>5. enable axis 1|Message F9005<br>Restart:<br>1. check wiring<br>2. remedy the cause<br>3. deactivate STO<br>4. clear fault<br>5. enable axis 1|



AKD2G-S Installation Manual, Safety 1 | 10   Functional Safety 

## **10.3.3.4 Timing** 

## Example for axis 1. 

|**Timing**<br>t1<br>ee|**max**<br>es|**Remarks**<br>STO channel A enabled (0 V)|
|---|---|---|
|t1 to t2<br>ee<br>a<br>ee|2 ms<br>es<br>es<br>es|STO enable delay (response time)|
|t2<br>a<br>ee|es<br>es|STO active|
|t3<br>ee<br>a<br>ee|es<br>es<br>es|STO channel B enabled (0 V)|
|t1 to t3<br>a<br>ee|100 ms<br>es<br>es|accepted delay between dual channel edges|
|t4<br>ee<br>a<br>ee|es<br>es<br>es|STO channel B disabled (+24 V)|
|t5<br>a<br>ee|es<br>es|STO channel A disabled (+24 V)|
|t4 to t5<br>ee<br>a<br>ee|100 ms<br>es<br>es<br>es|accepted delay between dual channel edges|
|t5 to t6<br>a<br>ee|2 ms<br>es<br>es|STO release delay|
|t6<br>ee<br>a|es<br>es|STO release|
|t6 to t7<br>a|es|Zero if AXIS#.SAFE.STO.REPORTFAULT<br>=0<br>Until 'no fault' if AXIS#.SAFE.STO.REPORTFAULT<br>=1|
|t7<br>es|es|Power section released.|



## **10.3.3.5 Safety Diagnostic view in WorkBench** 

The WorkBench view "Safety Diagnostic" shows the current status on the safe inputs (AXIS#.SAFE.STO.A / AXIS#.SAFE.STO.B) and the logical status of the STO function for every axis. 

AKD2G-S Installation Manual, Safety 1 | 10   Functional Safety 

## **10.3.3.6 Fault Reaction / Failure Messages** 

With the dual-channel control of the STO (SIL2/PLd Cat.3) safety function, the switch-off paths STO-A-A# and STO-B-A# are switched separately by two outputs of a safety controller. 

W9000 and F9000 are conditioned by the value of AXIS#.SAFE.STO.REPORTFAULT. If this keyword is set to 1 (default value) then the W9000 and F9000 will be triggered as described. 

|**STO-A-A#**<br>0 V<br>I|**STO-B-A#**<br>0 V<br>ss|**ENABLE**<br>0 V<br>ss|**Drive**<br>**Message**<br>W9000|**Motor**<br>**Torque**<br>no|**Safe State**<br>yes|
|---|---|---|---|---|---|
|0 V<br>a|0 V<br>ee|+24 V<br>ee|F9000<br>ee|no|yes|
|+24 V<br>a<br>I|+24 V<br>ee<br>ss|0 V<br>ee<br>ss|-<br>ee|no|no|
|+24 V<br>a|+24 V<br>ee|+24 V<br>ee|-<br>ee|yes|no|
|+24 V<br>a<br>I|0 V<br>ee<br>ss|0 V<br>ee<br>ss|F9005*<br>ee|no|yes|
|+24 V<br>a|0 V<br>ee|+24 V<br>ee|F9005*<br>ee|no|yes|
|0 V<br>a<br>I|+24 V<br>ee<br>ss|0 V<br>ee<br>ss|F9005*<br>ee|no|yes|
|0 V<br>a|+24 V<br>ee|+24 V<br>ee|F9005*|no|yes|



- different status of STO-A/B for more than 100 ms 

A#: A1 for axis 1 or A2 for axis 2. 

## **10.4 Verification** 

Check and verify the STO wiring (examples (➜ # 134)). The installation must be verified by trained personnel after any changes to the installation. The expertise of the personnel must be appropriate to the complexity and safety integrity level of the drive system. 

## **Proof test** 

You must test the STO function after initial start of the axis, after each intervention into the wiring of the system, or after exchange of one or several components of the drive system. 

Precondition: AXIS#.SAFE.STO.REPORTFAULT = 1 

**Warning:** Do not enter hazardous area during proof test! 

- **Method 1, axis remain enabled Method 2, axis disabled** 1. Stop the axis to standstill. 1. Stop the axis to standstill. **2. Caution: Block vertical load. 2. Caution: Block vertical load.** 3. Keep the axis enabled. 3. Disable the axis. 4. Activate the STO function for example by 4. Activate the STO function, for example, opening the protective screen. by opening the protective screen 

- 5. The axis displays fault F9000. 5. The axis displays fault W9000. 

AKD2G-S Installation Manual, Safety 1 | 10   Functional Safety 

## **10.5 Safety Faults, Safety Warnings** 

AKD2G with safety option 1 do not have safety failure modes. 

## **10.5.1 Drive LCD Display** 

The drive offers an LCD display and two push-buttons B1 / B2 for navigation. 

The display on the front panel of the drive shows the code of the fault or warning that occurred. Safety Faults and Warnings follow the same pattern and are identified by a four digit code 90 XX, where 90 is the two digit group code, and XX is a two digit ID. 

Navigate with B1 / B2 to the Fault screen to see a short description of the fault or warning. See WorkBench Onlinehelp for details. 

AKD2G-S Installation Manual, Safety 1 | 10   Functional Safety 

## **10.5.2 Drive Safety Faults** 

More information about drive fault messages, remedy and clearing faults can be found in the WorkBench User Manual. 

|**#**<br>F9000|**Description**<br>Safe torque off.|**Cause**<br>STO function has been triggered.|**Remedy**<br>Reapply supply voltage to STO if safe to do<br>so.|
|---|---|---|---|
|F9005|STO Simultaneity|The two STO inputs did not<br>change state within 100 ms of<br>each other.|Check wiring and safety apparatus|



## **10.5.3 Drive Safety Warnings** 

More information about drive warnings can be found in the WorkBench User Manual. 

|**#**<br>W9000|**Description**<br>Safe torque off.|**Cause**<br>STO function has been triggered.|**Remedy**<br>Reapply supply voltage to STO if safe to do so.|
|---|---|---|---|



## **10.5.4 Troubleshooting safety functionality** 

Eliminate errors and faults in compliance with work safety rules. Troubleshooting only by qualified and trained staff. 

|**Problem**<br>A group "90" safety<br>fault or safety warn-<br>ing message is vis-<br>ible in the drive LCD<br>display|**Possible Causes**<br>**Remedy causes**<br>Refer to the Drive Safety Fault and Warning tables (➜# 139).|**Possible Causes**<br>**Remedy causes**<br>Refer to the Drive Safety Fault and Warning tables (➜# 139).|
|---|---|---|
|A fault or warning<br>message of another<br>group than "90" is vis-<br>ible in the drive LCD<br>display|Refer to the drive fault and drive warnings tables (➜# 125) and more detailled descrip-<br>tions in the WorkBench User Manual.||
|Safety faults and<br>warnings are not vis-<br>ible/reported|AXIS#.SAFE.STO.REPORTFAULT|Set AXIS#.SAFE.STO.REPORTFAULT<br>to 1|
||is set to 0||
|STO cannot be deac-<br>tivated (no torque)|1. External safety device defective.<br>2. STO wiring defective.<br>3. Auxiliary voltage low.<br>4. STO inputs defective.<br>5. F9005 visible.<br>6. OSSD pulses too long (>10% of<br>signal period).<br>7. STO channels are unequal for<br>more than 100ms.|1. Check external safety device.<br>2. Check STO wiring for short-circuit or similar.<br>3. Check voltage level (➜# 133) .<br>4. Send drive to manufacturer for repair.<br>5. Check safety hardware system.<br>6. Check safety controller. Switch off OSSD.<br>7. Check external safety device.|
|Drive does not enable|1. STO is still active.|1. Deactivate STO prior to HW Enable.|



AKD2G-S Installation Manual, Safety 1 | 10   Functional Safety 

## **10.6 Functional Safety Keyword Reference Guide** 

This section describes the keywords used for functional safety. 

## **10.6.1 AXIS#.SAFE.STO Keywords** 

**141** 

AKD2G-S Installation Manual, Safety 1 | 10   Functional Safety 

## **10.6.1 AXIS#.SAFE.STO Keywords** 

This section describes **S** afe **T** orque **O** ff keywords. 

## **10.6.1.1 AXIS#.SAFE.STO.ACTIVE** 

## **Description** 

Indicates the Safe Torque Off (STO) state of the axis. The STO status is an AND link of A (➜ # 142) and B (➜ # 142) signals. 

|**Value**<br>1|**Description**<br>STO active (inputs +0V)|
|---|---|
|0|STO inactive (inputs 24V)|



## **Context** 

For full STO information refer to ➜ STO (Safe Torque Off). 

## **Versions** 

|Type<br>~~==~~|Read Only<br>~~==~~|
|---|---|
|Units<br>~~==~~|N/A<br>~~==~~|
|Range<br>~~==~~|0 or 1<br>~~==~~|
|Default Value<br>~~==~~|N/A<br>~~==~~|
|Data Type<br>~~==~~|Integer<br>~~==~~|
|Stored in Non Volatile Memory<br>~~==~~|No<br>~~==~~|



AKD2G-S Installation Manual, Safety 1 | 10   Functional Safety 

## **10.6.1.2 AXIS#.SAFE.STO.A** 

## **Description** 

Indicates the state for STO-A input. 

|**Value**<br>1|**Description**<br>24V present (STO inactive, allowed to enable)|
|---|---|
|0|24V not present (STO active, axis disabled)|



## **Context** 

For full STO information refer to ➜ STO (Safe Torque Off). 

## **Versions** 

**Action Version Notes** Implemented 02-00-00-000 **General Information** Type Read Only Units N/A Range 0 or 1 Default Value N/A Data Type Integer Stored in Non Volatile Memory No ~~=~~ 

## **10.6.1.3 AXIS#.SAFE.STO.B** 

## **Description** 

Indicates the state for STO-B input. 

|**Value**<br>1|**Description**<br>24V present (STO inactive, allowed to enable)|
|---|---|
|0|24V not present (STO active, axis disabled)|



## **Context** 

For full STO information refer to ➜ STO (Safe Torque Off). 

**Versions** 

**Action Version Notes** Implemented 02-00-00-000 **General Information** Type Read Only Units N/A Range 0 or 1 Default Value N/A Data Type Integer Stored in Non Volatile Memory No 

AKD2G-S Installation Manual, Safety 1 | 10   Functional Safety 

## **10.6.1.4 AXIS#.SAFE.STO.REPORTFAULT** 

## **Description** 

This keyword indicates whether an STO Fault will be created when the STO input is lost while the axis is enabled. 

**Value Description** 1 STO fault is indicated when axis is enabled and an STO occurs (default) 0 STO fault is not indicated (warning is still present) ~~———~~ 

## **Context** 

For full STO information refer to ➜ STO (Safe Torque Off). 

## **Versions** 

**Action Version Notes** Implemented 02-00-00-000 **General Information** Type Read/Write Units N/A Range 0 or 1 Default Value 1 Data Type Integer Stored in Non Volatile Memory Yes ~~=—=~~ 

AKD2G-S Installation Manual, Safety 1 | 11   Approvals 

## **11 Approvals** 

Beta Drives: All approvals are pending. 

|**11.1**|**Conformance with UL/cUL**|**145**|
|---|---|---|
|**11.2**|**Conformance with European Directives**|**146**|
|**11.3**|**Conformance with RoHS**|**147**|
|**11.4**|**Conformance with REACH**|**147**|
|**11.5**|**Functional Safety approval**|**147**|
|**11.6**|**Conformance with EAC**|**147**|



AKD2G-S Installation Manual, Safety 1 | 11   Approvals 

## **11.1 Conformance with UL/cUL** 

Beta Drives: UL pending. 

This drive is listed under UL (Underwriters Laboratories Inc.) file number **E141084** . USL, CNL – Power conversion equipment (NMMS, NMMS7) 

USL (United States Standards - Listed): Indicates Investigated to United States Standard for Power Conversion Equipment, UL 61800-5-1. 

CNL (Canadian National Standards - Listed): Indicates investigation to Canadian Standard for Industrial Control Equipment, CAN/CSA - C22.2, No. 274-17. 

## **UL Markings / Marquages UL** 

|**English**<br>Integral solid state short circuit protection does not<br>provide branch circuit protection. Branch circuit pro-<br>tection must be provided in accordance with the<br>National Electrical Code and any additional local<br>codes.|**Français**<br>provide branch circuit protection. Branch circuit pro-<br>Une protection de court-circuit à semi-conducteur<br>intégrale ne fournit pas de protection de la dériv-<br>ation. Il convient de garantir une protection de la<br>dérivation conforme au NEC et aux réglementations<br>locales en vigueur.|
|---|---|
|This product is suitable for use on a circuit capable<br>of delivering not more than (when protected by<br>fuses):<br>- AKD2G-Sxx-6V: 240 V,<br>10.000 rms symmetrical amperes.<br>- AKD2G-Sxx-7: 480 V,<br>42.000 rms symmetrical amperes.|Ce produit est conçu pour une utilisation sur un cir-<br>cuit capable de fournir maximum (s'il dispose de fus-<br>ibles):<br>- AKD2G-Sxx-6V: 240 V,<br>10 000 ampères symétriques (rms).<br>- AKD2G-Sxx-7V: 480 V,<br>42 000 ampères symétriques (rms).|
|Recommended fuses or breakers, max. 30 A:<br>refer to (➜# 71, Fusing)|Fusibles ou disjoncteurs recommandés, max. 30 A:<br>voir (➜# 71, Fusing)|
|These drives provide solid state motor overload pro-<br>tection at 125% of the rated FLA current. The over-<br>load trip point should not be set to less than 10%<br>above the motor rated current:<br>AXIS#.IL.FOLDFTHRESHU = 1.1 * AXIS#.MOTOR.ICONT.|These drives provide solid state motor overload pro-<br>Ces variateurs offrent une protection contre les sur-<br>charges de moteur à semi-conducteur à 125 % du<br>courant FLA nominal. Le point de déclenchement en<br>surcharge ne doit pas être réglé à moins de 10% au<br>dessus du courant nominal du moteur:<br>AXIS#.IL.FOLDFTHRESHU = 1.1 * AXIS#.MOTOR.ICONT.|
|These devices are intended to be used in a pol-<br>lution degree 2 environment and must be placed in<br>an enclosure with min. size of<br>16 x 16 x 10 inches (406 x 406 x 254 mm)|Ces appareils sont prévus pour une utilisation dans<br>un environnement de pollution de niveau 2 et doivent<br>être placés dans une enceinte avec min. taille de<br>16 x 16 x 10 pouces (406 x 406 x 254 mm)|
|Surrounding air temperature 40°C.<br>Refer to (➜# 31), Ambient Conditions, for other<br>temperature ratings.|La température de l'air ambiant 40 °C.<br>Voir (➜# 31), Ambient Conditions, pour connaître<br>les autres températures.|
|Use minimum 75°C copper wire.|Utilisez un fil en cuivre 75 °C minimum.|
|Use recommended fuses or circuit breakers.|Utilisez les fusibles ou disjoncteurs recommandés.|
|**CAUTION Risk of Electrical Shock!**Capacitors<br>can have dangerous voltages present up to seven<br>minutes after switching off the supply power. For<br>increased safety, measure the voltage in the DC<br>bus link and wait until the voltage is below 50 V.|**ATTENTION: Risque de choc électrique!**Des<br>tensions dangereuses peuvent persister dans les<br>condensateurs jusqu'à sept minutes après la mise<br>hors tension. Pour plus de sécurité, mesurez la ten-<br>sion dans la liaison de bus CC et attendez qu'elle<br>soit inférieure à 50 V.|



AKD2G-S Installation Manual, Safety 1 | 11   Approvals 

## **11.2 Conformance with European Directives** 

Beta Drives: CE in process. 

CE Declarations of Conformity can be found on the Kollmorgen website. 

The drives have been tested by an authorized testing laboratory in a defined configuration, using the system components that are described in this documentation. Any divergence from the configuration and installation described in this documentation means that the user will be responsible for carrying out new measurements to ensure conformance with regulatory requirements. 

Kollmorgen declares the conformity of the product series AKD2G with the following directives: 

- EC Directive 2006/42/EU, Machinery Directive Used harmonized standard EN 61800-5-2 

- EC Directive 2014/35/EU, Low Voltage Directive Used harmonized standard EN 61800-5-1 

- EC Directive 2014/30/EU, EMC Directive 

- Used harmonized standard EN 61800-3 

These devices can cause high-frequency interferences in non industrial environments and may require measures for interference suppression (such as additional external EMC filters). 

Maximum cable length for digital I/O supply (24V/DGND) is 3 m. If longer cables are required, the user need to take care of additional EMC measures. 

## **AKD2G-Sxx-6Vxx** 

AKD2G-Sxx-6Vxx drives do not have integrated ac line EMC filters. Refer to the regional _Accessories Manual_ for recommended external mains filter types. 

With external EMC mains filters for noise emission the AKD2G-Sxx-6Vxx meet the noise immunity requirements of the second environmental category (industrial environment) to a product of the category C2 (motor cable < 10 m). 

With a motor cable length of 10 m or longer and external mains EMC filters, the AKD2G-Sxx6Vxx meet the requirement of category C3. 

## **AKD2G-Sxx-7Vxx** 

AKD2G-Sxx-7Vxx drives have integrated EMC filters. 

The AKD2G-Sxx-7Vxx meet the noise immunity requirements to the 2nd environmental category (industrial environment). 

For noise emission the AKD2G-Sxx-7Vxx meet the requirement to a product of the Category C2 (motor cable < 10 m). 

With a motor cable length of 10 m or longer, the AKD2G-Sxx-7Vxx meet the requirement to the Category C3. 

AKD2G-S Installation Manual, Safety 1 | 11   Approvals 

## **11.3 Conformance with RoHS** 

The device is manufactured in conformance with RoHS Directive 2011/65/EU with delegated directive 2015/863/EU for installation into a machine. 

## **11.4 Conformance with REACH** 

EU Regulation no. 1907/2006 deals with the registration, evaluation, authorization and restriction of chemical substances 1 (abbreviated to "REACH"). 

The device does not contain any substances (CMR substances, PBT substances, vPvB substances and similar hazardous substances stipulated in individual cases based on scientific criteria) above 0.1 mass percent per product that are included on the candidate list. 

## **11.5 Functional Safety approval** 

Beta drives: Safety functions are neither approved nor certified yet. Do not use this functionality in applications with functional safety request until further notice. 

Kollmorgen offers 3 levels of functional safety implementation for AKD2G: 

- Functional Safety Option 1: STO; SIL2 PLd (➜ # 132), safe digital I/O command. 

- Functional Safety Option 2: STO, SS1-t, SBC, SBT, SDB; SIL3 PLe , safe digital I/O command or FSoE. 

- Functional Safety Option 3: STO, SS1-t, SS1-r, SS2, SOS, SLS, SSM, SSR, SDI, SLA, SAR, SLI, SLP, SCA, SBC, SDB, SBT; SIL3 PLe , safe digital I/O command or FSoE. 

This manual is valid for AKD2G drives with Functional Safety Option 1. 

## **11.6 Conformance with EAC** 

EAC is the abbreviation for Eurasian Conformity. The mark is used in the states of the Eurasian Customs Union (Russia, Belarus, Kazakhstan) similar to the European CE mark. Kollmorgen declares, that the device has passed all required conformity procedures in a member state of the Eurasian Customs Union, and that the device meets all technical requirements requested in the member states of the Eurasian Customs Union: 

- Low voltage (TP TC 020/2011) 

- Electromagnetic Compatibility (TP TC 004/2011) 

Contact: SERVOSTAR LLC. , Bld.1, Semyonovskaya nab. 2/1, RU-105094 Moskau 

AKD2G-S Installation Manual, Safety 1 | 11   Approvals 

--- / --- 

AKD2G-S Installation Manual, Safety 1 | 12   Index 

## **12 Index** 

## **A** 

|**Abbreviations**|**12, 129**|
|---|---|
|**Address**||
|CAN|118|
|EtherCAT|118|
|IP|118|
|MAC|118|
|**AKD 2G Family**|**29**|
|**Ambient Conditions**|**31**|
|**Analog setpoints**|**105**|
|**Aux. supply 24V, interface**|**76**|



## **B** 

|**Brake resistor, interface**|**79**|
|---|---|
|**C**||
|**Cable and Wire Requirements**|**49**|
|**Cable Length**|**49**|
|**CANbus**||
|Baud rate|101|
|Cable|99|
|CANopen interface|99|
|Node address|101|
|Termination|101|
|**Commissioning**|**137**|
|**Conformance**||
|CE|146|
|EAC|147|
|Functional Safety|147|
|REACH|147|
|RoHS|147|
|UL, cUL|145|
|**Connector Position**|**57**|
|**Connectors**|**48**|



## **D** 

|**DC Bus Capacitance**|**38**|
|---|---|
|**DC bus link, interface**|**77**|
|**Decommission**|**23**|
|**Dimensions**|**44**|
|**Disassemble**|**23**|
|**Display**|**39**|
|**Disposal**|**24**|
|**Document Revisions**|**151**|
|**DSL**|**81**|
|**Dynamic Braking**|**37**|



## **E** 

|**Electronic Gearing**|**93**|
|---|---|
|**Emergency Off**|**19**|
|**Emergency Stop Function**|**19**|
|**Emulated Encoder Output**|**94**|
|**Enclosure (FS)**|**130**|
|**Encoder emulation, interface**|**94**|
|**EtherCAT**|**97**|



## **F** 

|**Factury Default Setting**|**133**|
|---|---|
|**Fault messages**|**125**|
|**Feedback Connection**|**87**|
|**Functional Safety (FS)**|**127**|
|**Functional Safety 1 (FS1)**|**132**|
|**Fusing**||
|24V supply|76|
|Brake resistor|79|
|DC Bus Link|77|
|Mains supply|71|



## **G** 

|**Grounding**||**47**|
|---|---|---|
|**Grounding Plates**|**Grounding Plates**|**56**|



## **H** 

|**Hardware requirements**||
|---|---|
|WorkBench|121|
|**Hiperface DSL**|**81**|
|**I**||
|**I/O Connection**|**103**|
|**Initial Drive Test**|**117**|
|**Inputs**||
|Analog|105|
|Basic Data|104|
|Digital|107|
|**Installation**||
|Electrical|45|
|Mechanical|42|
|Software WorkBench|122|
|**Installation, Setup, Normal Operation**|**23**|



## **L** 

|**Labels**|**17**|
|---|---|
|**Leakage current**|**18**|
|**M**||
|**Mains supply, interface**|**67**|
|**Maintenance**|**23**|
|**Marquages UL**|**145**|
|**Master-Slave**|**96**|
|**Mating Connectors**|**48**|



**EAC 147** 

AKD2G-S Installation Manual, Safety 1 | 12   Index 

|**Mechanical Data**|**31**|
|---|---|
|**Motion Bus**|**97**|
|**Motor dual cable connection**|**83**|
|**Motor Holding Brake Connection**|**85**|
|**Motor interface**|**80**|
|**Motor single cable connection**|**81**|



## **N** 

|**Nameplate**|**Nameplate**|**26**|
|---|---|---|
|**O**|||
|**Operating systems**|||
||WorkBench|121|
|**Outputs**|||
||Analog|106|
||Basic Data|104|
||Digital|111|
||Relay|114|



## **P** 

|**Package supplied**|**26**|
|---|---|
|**Part number scheme**|**27**|
|**PC connection**|**102**|
|**Product Safety**|**13**|
|**Prohibited Use**||
|Functional Safety|129|
|General|17|
|**Pushbuttons**|**39**|



## **R** 

|**Re-forming**||**116**|
|---|---|---|
|**REACH**||**147**|
|**Regeneration Braking**|**Regeneration Braking**|**37**|
|**Regenerative circuit**|**Regenerative circuit**|**37**|
|**Relay**||**114**|
|**Repair**||**24**|
|**RoHS**||**147**|



|**Setup**|**116**|
|---|---|
|**Setup Software**|**120**|
|**SFA**|**92**|
|**SFD3**|**81**|
|**Shield connection**|**53**|
|**Shielding**|**47**|
|**Shock-hazard protection**|**18**|
|**Site**|**43**|
|**STO**|**134**|
|**Stop Function**|**19**|
|**Switch-on/switch-off behavior**|**123**|
|**Symbols used**|**11**|



## **T** 

|**Trouble Shooting**|**126**|
|---|---|
|**U**||
|**UL Markings**|**145**|
|**Use as directed**||
|Drive|16|
|Functional Safety|129|
|WorkBench Setup Software|120|
|**V**||
|**Ventilation**|**31**|
|Mechanical Installation|43|
|**Verification**|**137**|
|**W**||
|**Warnings**|**125**|
|**Wiring**|**48**|



## **S** 

|**Safety**||
|---|---|
|Functional Safety|127|
|Product Safety|13|
|**Safety Faults**|**138**|
|**Safety Instructions**||
|Drive Setup|116|
|Electrical Installation|46|
|General|14|
|Mechanical Installation|43|
|**Safety Properties**|**133**|
|**Safety Warnings**|**138**|
|**SD Card Slot**|**41**|
|**Service Interface**|**102**|



AKD2G-S Installation Manual, Safety 1 | 13   Record of document revisions 

**13 Record of document revisions** 

**Edition Remarks** A, 12/2019 First edition ~~—_————~~ 

## **About KOLLMORGEN** 

Kollmorgen is a leading provider of motion systems and components for machine builders. Through worldclass knowledge in motion, industry-leading quality and deep expertise in linking and integrating standard and custom products, Kollmorgen delivers breakthrough solutions that are unmatched in performance, reliability and ease-of-use, giving machine builders an irrefutable marketplace advantage. 

Join the Kollmorgen Developer Network for product support. Ask the community ques—__, ~~[!~~ tions, search the knowledge base for answers, get downloads, and suggest improvements. 

|**North America**|**Europe**|
|---|---|
|**KOLLMORGEN**|**KOLLMORGEN Europe GmbH**|
|201 West Rock Road|Pempelfurtstr. 1|
|Radford, VA 24141, USA|40880 Ratingen, Germany|
|**Web:**<br>www.kollmorgen.com|**Web:**<br>www.kollmorgen.com|
|**Mail:**<br>support@kollmorgen.com|**Mail:**<br>technik@kollmorgen.com|
|**Tel.:**<br>+1 - 540 - 633 - 3545|**Tel.:**<br>+49 - 2102 - 9394 - 0|
|**Fax:**<br>+1 - 540 - 639 - 4162|**Fax:**<br>+49 - 2102 - 9394 - 3155|



|**South America**<br>**KOLLMORGEN**<br>Avenida João Paulo Ablas, 2970<br>Jardim da Glória, Cotia – SP<br>CEP 06711-250, Brazil|
|---|
|**Web:**<br>www.kollmorgen.com<br>**Mail:**<br>contato@kollmorgen.com<br>**Tel.:**<br>+55 11 4615-6300|



|**China and SEA**|**China and SEA**|
|---|---|
|**KOLLMORGEN**||
|Room 302, Building 5, Lihpao Plaza,|Room 302, Building 5, Lihpao Plaza,|
|88 Shenbin Road, Minhang District,||
|Shanghai, China.||
|**Web:**|www.kollmorgen.cn|
|**Mail:**|sales.china@kollmorgen.com|
|**Tel.:**|+86 - 400 668 2802|
|**Fax:**|+86 - 21 6248 5367|



