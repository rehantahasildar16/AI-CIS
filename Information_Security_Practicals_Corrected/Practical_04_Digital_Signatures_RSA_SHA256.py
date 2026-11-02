# PRACTICAL 04: Simplified educational RSA digital signature with SHA-256
import hashlib

p, q = 61, 53
n = p * q
phi = (p - 1) * (q - 1)
e = 17
d = pow(e, -1, phi)
print("Public Key :", (e, n))
print("Private Key:", (d, n))

message = input("Enter message: ")
digest = int(hashlib.sha256(message.encode("utf-8")).hexdigest(), 16)
signature = pow(digest % n, d, n)
print("Digital Signature:", signature)

received = input("Enter message for verification: ")
received_digest = int(hashlib.sha256(received.encode("utf-8")).hexdigest(), 16)
verified_digest = pow(signature, e, n)
if verified_digest == received_digest % n:
    print("Digital Signature Verified")
    print("Message is authentic and unchanged")
else:
    print("Digital Signature Verification Failed")
    print("Message may have been modified")
print("Note: Simplified classroom demonstration only; not secure for real-world signing.")
