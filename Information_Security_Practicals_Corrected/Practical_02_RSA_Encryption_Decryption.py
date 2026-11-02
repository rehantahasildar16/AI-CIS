# PRACTICAL 02: RSA encryption and decryption (educational example)
p, q = 61, 53
n = p * q
phi = (p - 1) * (q - 1)
e = 17
d = pow(e, -1, phi)
print("Public Key:", (e, n))
print("Private Key:", (d, n))
message = int(input("Enter a number to encrypt (0 to {}): ".format(n - 1)))
if not 0 <= message < n:
    print("Error: Message must be between 0 and {}.".format(n - 1))
else:
    encrypted = pow(message, e, n)
    decrypted = pow(encrypted, d, n)
    print("Original message:", message)
    print("Encrypted message:", encrypted)
    print("Decrypted message:", decrypted)
    print("Decryption successful:", decrypted == message)
