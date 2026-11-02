INFORMATION SECURITY PRACTICALS - CORRECTED FILES
Based on your uploaded Information--security--Practicals.pdf (10 practicals).

CONTENTS
01 Caesar substitution + Rail Fence transposition (Python)
02 RSA encryption/decryption (Python)
03 HMAC-SHA256 Message Authentication Code (Python)
04 Simplified RSA digital signature with SHA-256 (Python)
05 Diffie-Hellman key exchange (Python)
06 IPsec router configuration examples (TXT files for Cisco Packet Tracer)
07 Local SSL/TLS HTTPS server (Python + OpenSSL)
08 Basic IDS network-connection scan (Python + psutil)
09 File SHA-256 hash calculation (Python)
10 Windows Firewall TCP 8080 rule (PowerShell)

RUN PYTHON FILES
Extract this ZIP, open the folder in VS Code or Command Prompt, then run:
python Practical_01_Substitution_Transposition.py
Replace the filename with the practical you want.

INSTALL
Practical 01-05 and 09 use Python standard library.
Practical 08:
python -m pip install psutil

PRACTICAL 06 - CISCO PACKET TRACER
Create: PC0 - Switch0 - Router0 - Router1 - Switch1 - PC1.
PC0: IP 192.168.1.10, mask 255.255.255.0, gateway 192.168.1.1.
PC1: IP 192.168.2.10, mask 255.255.255.0, gateway 192.168.2.1.
Use Router0 and Router1 config TXT files as a starting example. Test ordinary routing/ping before applying IPsec.
Packet Tracer IOS versions and router models differ; some may not support every crypto command shown. Interface names may also vary.

PRACTICAL 07 - SSL/TLS
Install OpenSSL for Windows and add it to PATH. Open Command Prompt in this folder.
Generate private key:
openssl genrsa -out server.key 2048
Generate a self-signed localhost certificate:
openssl req -new -x509 -key server.key -out server.crt -days 365 -subj "/CN=localhost" -addext "subjectAltName=DNS:localhost,IP:127.0.0.1"
Then run:
python Practical_07_SSL_TLS_HTTPS_Server.py
Open https://localhost:4443 in a browser. A self-signed certificate warning is expected for this lab.

PRACTICAL 10 - FIREWALL
Run PowerShell as Administrator and execute:
.\Practical_10_Firewall_Rule_Configuration.ps1
The script creates an inbound block rule for TCP port 8080. To remove:
Remove-NetFirewallRule -DisplayName "Block TCP 8080"
Do not change firewall settings on a managed/college PC without permission.

IMPORTANT ERROR CHECKS / LIMITATIONS
- Practical 01: The original PDF reuses the function names encrypt/decrypt for both cipher types, causing the Caesar functions to be overwritten. This version uses separate function names and validates rail count.
- Practical 02: Checks that the entered integer is in the valid RSA range 0 to n-1.
- Practical 04: The PDF's small-key RSA/hash-modulo example is only a classroom demonstration. It is not secure for real digital signatures.
- Practical 06 and 10 are configuration practicals, not Python programs; their files are TXT and PS1.
- Practical 08: A port in the demonstration list does not prove an intrusion. Run as Administrator if Windows restricts connection visibility.
- Practical 09: SHA-256 hashing calculates a file fingerprint; it does not by itself detect malware. Never execute unknown samples on your normal computer.
