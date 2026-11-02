# PRACTICAL 07: Local HTTPS server using SSL/TLS
# Generate server.key and server.crt using commands in README.txt first.
import http.server
import ssl
from pathlib import Path

HOST, PORT = "localhost", 4443
folder = Path(__file__).resolve().parent
cert_file, key_file = folder / "server.crt", folder / "server.key"
if not cert_file.exists() or not key_file.exists():
    raise FileNotFoundError("Generate server.crt and server.key first; see README.txt.")

httpd = http.server.HTTPServer((HOST, PORT), http.server.SimpleHTTPRequestHandler)
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile=str(cert_file), keyfile=str(key_file))
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
print("HTTPS Server running at https://{}:{}".format(HOST, PORT))
print("Press Ctrl+C to stop.")
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nHTTPS server stopped.")
finally:
    httpd.server_close()
