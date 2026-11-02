# PRACTICAL 03: HMAC-SHA256 message authentication
import hmac
import hashlib

message = input("Enter message: ")
secret_key = input("Enter secret key: ")
key_bytes = secret_key.encode("utf-8")
mac = hmac.new(key_bytes, message.encode("utf-8"), hashlib.sha256).hexdigest()
print("Generated MAC:", mac)

received = input("Enter message again for verification: ")
new_mac = hmac.new(key_bytes, received.encode("utf-8"), hashlib.sha256).hexdigest()
if hmac.compare_digest(mac, new_mac):
    print("MAC Verified - Message is authentic and unchanged")
else:
    print("MAC Verification Failed - Message may be modified")
