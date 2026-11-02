# PRACTICAL 08: Basic IDS demonstration (requires: python -m pip install psutil)
import psutil

suspicious_ports = [21, 23, 445, 3389]
print("===== Intrusion Detection System =====")
print("Scanning active network connections...\n")
try:
    connections = psutil.net_connections(kind="inet")
except psutil.AccessDenied:
    print("Access denied. Run Command Prompt as Administrator.")
    raise SystemExit(1)

found = False
for connection in connections:
    if connection.raddr:
        remote_ip = connection.raddr.ip
        remote_port = connection.raddr.port
        print("Connection:", remote_ip, "Port:", remote_port)
        if remote_port in suspicious_ports:
            print("ALERT! Monitored port detected:", remote_port)
            found = True
if not found:
    print("\nNo connections to the listed ports were detected.")
print("\nIDS scan completed.")
