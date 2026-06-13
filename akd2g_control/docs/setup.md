# AKD2G Drive — Setup & Connection

## Hardware

- **Drive model:** Kollmorgen AKD2G (dual-axis servo drive, CANopen variant)
- **Connection:** Ethernet cable — laptop → **Service/HM port** on drive
- **Drive IP:** `169.254.78.209`
- **Modbus TCP port:** `502`
- **Configuration software:** Kollmorgen Workbench (installed on laptop)
- **Package manager:** `uv` (use `uv run python script.py` and `uv sync`)

## Physical Ports on the Drive

The AKD2G has **three ports** — it matters which one you use:

| Port        | Protocol        | Use                                                        |
|-------------|-----------------|-------------------------------------------------------------|
| **Service/HM** | Ethernet TCP/IP | ✅ **This one** — for laptop, Workbench, Python/Modbus TCP |
| **IN**      | CANopen         | Receives signal from a CANopen master or previous device   |
| **OUT**     | CANopen         | Passes CANopen signal to the next device in the chain      |

### What is CANopen?
CANopen is an industrial fieldbus protocol built on CAN bus (Controller Area Network). It is used when a **PLC or motion controller** needs to command multiple drives on the same network. Even though the IN/OUT connectors may look like Ethernet, they carry CAN signals and are **not compatible** with a standard Ethernet cable.

For direct laptop control (Workbench + Python), always use **Service/HM**:

```
Laptop ──ethernet── [Service/HM]  AKD2G  [IN/OUT] ──canopen── (future PLC if needed)
```

## What is the AKD2G?

The AKD2G is a **single physical drive unit** that controls **two independent motors**:

| Axis   | Modbus Slave ID | Controls  |
|--------|-----------------|-----------|
| Axis 1 | `1`             | Motor 1   |
| Axis 2 | `2`             | Motor 2   |

Both axes share the same Ethernet connection and IP address but are fully independent — each has its own enable state, encoder feedback, fault status, and motion commands.

## Network / Subnet Note

The IP `169.254.x.x` is a **link-local address** (auto-assigned when no DHCP server is present). Make sure your laptop's Ethernet adapter is also on the `169.254.x.x` subnet, or set it to:

- IP: `169.254.78.1` (or any `169.254.x.x` that isn't the drive's IP)
- Subnet mask: `255.255.0.0`

## Checking Connection in Workbench

1. Open Kollmorgen Workbench
2. Click **Scan for Drives** or check the top connection bar
3. Drive should appear at `169.254.78.209`
4. If connected, Axis 1 and Axis 2 will both appear as sub-nodes

## Enabling Modbus TCP (if not already on)

In Workbench: **Drive > Settings > Fieldbus / Communication**
- Enable: **Modbus TCP**
- Port: `502`
- Save and reboot drive if prompted

---

## Troubleshooting — Connection Timeout

If Python times out (`Connection to (169.254.78.209, 502) failed: timed out`) even though Workbench connects fine, run these diagnostics in PowerShell:

```powershell
# Run all three tests at once
Write-Host "`n--- TEST 1: Ping ---" -ForegroundColor Cyan
ping 169.254.78.209 -n 2

Write-Host "`n--- TEST 2: Your Ethernet adapter IP ---" -ForegroundColor Cyan
ipconfig | Select-String -Pattern "Ethernet|IPv4|Subnet"

Write-Host "`n--- TEST 3: Port 502 (Modbus) ---" -ForegroundColor Cyan
Test-NetConnection -ComputerName 169.254.78.209 -Port 502
```

### What the results mean

| Symptom | Cause | Fix |
|---------|-------|-----|
| Ping fails | Laptop not on same subnet | Set Ethernet adapter IP to `169.254.78.1`, mask `255.255.0.0` |
| Ping works, port 502 fails | Modbus TCP not enabled on drive | Enable in Workbench → Drive → Settings → Communication |
| Port 502 open, Python still fails | Windows Firewall blocking port 502 | Temporarily disable firewall to test, then add an inbound rule for port 502 |

### Fix laptop subnet (if needed)
1. Control Panel → Network and Sharing Center → Change adapter settings
2. Right-click Ethernet adapter → Properties
3. Select **IPv4** → Properties → Use the following address:
   - IP: `169.254.78.1`
   - Subnet mask: `255.255.0.0`
   - Gateway: *(leave blank)*
