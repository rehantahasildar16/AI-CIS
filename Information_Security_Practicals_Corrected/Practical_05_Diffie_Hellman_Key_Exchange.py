# PRACTICAL 05: Diffie-Hellman key exchange
p, g = 23, 5
alice_private = 6
bob_private = 15

alice_public = pow(g, alice_private, p)
bob_public = pow(g, bob_private, p)
print("Alice's Public Key:", alice_public)
print("Bob's Public Key:", bob_public)

alice_secret = pow(bob_public, alice_private, p)
bob_secret = pow(alice_public, bob_private, p)
print("Alice's Shared Secret:", alice_secret)
print("Bob's Shared Secret:", bob_secret)

if alice_secret == bob_secret:
    print("Key Exchange Successful")
else:
    print("Key Exchange Failed")
