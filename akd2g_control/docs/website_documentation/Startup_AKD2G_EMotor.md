## **How to startup the AKD2G Motor controller** 

## **1. Connect power** 

   - a. Connect 230V to X3: 

      - i. Yellow on PE 

      - ii. Brown on L1 

      - iii. Blue on L2 

   - b. Connect 24VDC to X10 

**2. Connect e-motors** 

   - a. Connect motor 1 on X1 

   - b. Connect motor 2 on X2 

## **3. Connect Service cable** 

   - a. Connect a RJ45-cable to X20 and on the other side to the computer 

**4. Connect IO-output with 24VDC/0VDC for motor 1** 

**JUST CONNECT THE TWO BLACK SWITCHES TO THE ESC AND FOLLOW THE CABLES; THERE SHOULD BE JUST TWO FREE, POSITIVE AND NEGATIVE, CONNECT BOTH TO THE POWER SUPPLY. PLUG AND PLAY** 

- a. X21-B3 24VDC 

- b. X21-B4 0VDC 

- c. X21-A11 24VDC 

- d. X21-B11 24VDC 

- e. X21-A5 24VDC 

Installation and Set-up 

1. Go to website : https://www.kollmorgen.com/en-us/developer-network/akd2gdownloads 

2. Download Safe motion monitor v2 (SMM2) *Safety Certified * 

3. After Downloading, open folder Workbench and run Kollmorgen WorkBench setup and install. 

4. Open Workbench and connect the HMI cable to your pc. The device will show up as following 

5. Click on connect. New Window should pop-up 

6. On the left pane, go to device settings>power> AC line Phases. Set to 0- Single Phase. 

7. Then on the left pane, Click on Axis 1 in axis overview set axis status as enable, (For Axis to be enabled STO must be off which is done with wiring 24v supply to A11 and B11 as shown in the connection description on page 1) 

8. If there are no errors a green bar with a tick should show up on the bottom of the screen. 

9. To test the motor, expand Axis 1> Motion> Service motion. Set current at 1 Amps and click on start. 

10. Default Operation mode is torque which can be changed under Axis 1>Settings. 

11. Once the motors are connected, following the previous steps, go to the Service Motions option. There are three options to move the motors manually, as shown in the images. The movement speed is determined by the amount of current (Amperes): with positive current the arm extends, and with negative current the arm retracts. 

The three options are: a single pulse with the duration set in milliseconds, another option with two pulses sent periodically, and a third option with continuous current. There is a movement limit, after which it brakes and no longer moves. 

WARNING: WE DO NOT KNOW IF THERE IS CURRENT LIMITATION (SPEED OF MOVEMENT) BASED ON THE FREEDOM OF MOTION OF THE GIMBAL. EXCESSIVE CURRENT COULD MECHANICALLY DAMAGE THE ARMS. 

**==> picture [434 x 356] intentionally omitted <==**

**----- Start of picture text -----**<br>
wieia 4 NY ServiceService motion allows Motionyou to start and stop some test motions.<br>«BP —<br>4 no_name (0.0.0.0) Service Motion Mode: © Pulse O Reversing O Continuous<br>Group: Group 1 v<br>Current 1: —<br>0.266 Ams<br>Add New Device... Add New Group...<br>4 ® no-name (Simulated)<br>BB Scope<br>tel Parameter Load/Save 0 ——___—_—__><br>Terminal —<br>, B =— Time 1:<br>> (Gj Device Diagnostics __500) ms<br>4 @& Ans 1(1)<br>‘@) Feedback<br>I Motor<br>( Thermal Protection<br>(©) Brake p> Start A Axis is inactive.<br>Units<br>Limits Position Feedback: 0.000 Counts 16Bit<br>@ Home ————_—<br>#,_ Slider© Enable/DisableTuning Current Feedback: 0.000 Ams<br>w@ PerformanceServo Tuner<br>(Jog Motion<br>Ny Service Motion<br>[J Motion Tasks<br>b @® Asis2 (2)<br>**----- End of picture text -----**<br>


**==> picture [426 x 298] intentionally omitted <==**

**----- Start of picture text -----**<br>
wl a # Service Motion<br>4 & Project Service motion allows you to start and stop some test motions.<br>Salaun(0.0.0.0) Service Motion Mode: ©) Pulse © Reversing O Continuous<br>Current 1: = —————»<br>0.266 Ams<br>Add New Device... Add New Group.<br>4 ® no-name (Simulated)”<br>B® Scope<br>(el Parameter Load/Save Current2: | ————_»<br>b arei ings |_ ae eeTime 1: Time 2:<br>> (G Device Diagnostics L500} ms ___ 500) ms<br>4 @ Axis 1(1)<br>‘@) Feedback<br>t Motor<br>@ Thermal Protection<br>(©) Brake > Start A Avisis inactive.<br>Units<br>Limits Position Feedback: 0.000 Counts 16Bit<br>@ Home ity Feedback:<br>@ Enable/Disable Current Feedback: 0.000 Ams<br>#. Slider Tuning<br>® PerformanceServo Tuner<br>4 &% Motion<br>‘i Jog Motion<br>[Ff] Motion Tasks<br>b @m Adds2 (2)<br>**----- End of picture text -----**<br>


**==> picture [436 x 355] intentionally omitted <==**

**----- Start of picture text -----**<br>
pala oe a # Service Motion<br>, BP ‘ect Service motion allows you to start and stop some test motions.<br>b- no_name (0.0.0.0) Service Motion Mode: © Pulse O Reversing © Continuous<br>Current 1: ame<br>0.266, Ams<br>Add New Device... Add New Group.<br>4 ® no-name (Simulated)*<br>B Scope<br>fel Parameter Load/Save 0 ———————+<br>@, Terminal<br>> @@ Device Settings<br>4 @ Axis 1(1)<br>‘@) Feedback<br>I Motor<br>( Thermal Protection<br>(OQ) Brake > Start A\ Ais is inactive.<br>Units<br>Limits Position Feedback: 0.000 Counts 16Bit<br>@ Home locity Feedback:<br>> Ci) Current Loop “ md<br>© Enable/Disable Current Feedback: 0.000 Ams<br>#, Slider Tuning<br>® PerformanceServo Tuner<br>[J Motion Tasks<br>> @® Anas2 (2)<br>**----- End of picture text -----**<br>


