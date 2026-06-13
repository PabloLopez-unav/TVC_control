"""
Scans Modbus holding registers across multiple address ranges to find
which ones the AKD2G responds to without exception code 2.
"""

from pymodbus.client import ModbusTcpClient

DRIVE_IP = "169.254.78.209"
PORT     = 502
SLAVE_ID = 1  # Scan Axis 1 only

RANGES = [
    (0x0000, 0x00FF, "Low addresses"),
    (0x1000, 0x10FF, "0x1000 range"),
    (0x2000, 0x20FF, "0x2000 range"),
    (0x6000, 0x60FF, "CiA 402 range"),
]

def scan(client, start, end, label):
    hits = []
    for addr in range(start, end + 1):
        r = client.read_holding_registers(address=addr, count=1, device_id=SLAVE_ID)
        if not r.isError():
            hits.append((addr, r.registers[0]))
    if hits:
        print(f"\n[{label}] Found {len(hits)} readable registers:")
        for addr, val in hits:
            print(f"  0x{addr:04X} ({addr:5d}) = 0x{val:04X} ({val})")
    else:
        print(f"[{label}] No readable registers found")
    return hits

def main():
    print(f"Connecting to {DRIVE_IP}:{PORT} ...")
    client = ModbusTcpClient(DRIVE_IP, port=PORT)
    if not client.connect():
        print("Connection failed")
        return

    print("Connected. Scanning...\n")
    all_hits = []
    for start, end, label in RANGES:
        all_hits += scan(client, start, end, label)

    client.close()
    print(f"\nTotal readable registers found: {len(all_hits)}")

if __name__ == "__main__":
    main()
