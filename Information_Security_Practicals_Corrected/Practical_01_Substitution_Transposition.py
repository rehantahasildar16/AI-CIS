# PRACTICAL 01: Caesar substitution and Rail Fence transposition ciphers

def caesar_encrypt(text, shift):
    result = ""
    shift %= 26
    for ch in text:
        if ch.isascii() and ch.isalpha():
            start = ord("A") if ch.isupper() else ord("a")
            result += chr((ord(ch) - start + shift) % 26 + start)
        else:
            result += ch
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

message = input("Enter message for Caesar Cipher: ")
shift = int(input("Enter shift value: "))
encrypted = caesar_encrypt(message, shift)
decrypted = caesar_decrypt(encrypted, shift)
print("\n--- Caesar Cipher ---")
print("Encrypted message:", encrypted)
print("Decrypted message:", decrypted)
print("Original message verified:", decrypted == message)

def rail_fence_encrypt(text, rails):
    if rails < 1:
        raise ValueError("Number of rails must be at least 1.")
    if rails == 1 or rails >= len(text):
        return text
    rows = [""] * rails
    row, direction = 0, 1
    for ch in text:
        rows[row] += ch
        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1
        row += direction
    return "".join(rows)

def rail_fence_decrypt(cipher, rails):
    if rails < 1:
        raise ValueError("Number of rails must be at least 1.")
    if rails == 1 or rails >= len(cipher):
        return cipher
    pattern, row, direction = [], 0, 1
    for _ in range(len(cipher)):
        pattern.append(row)
        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1
        row += direction
    counts = [pattern.count(i) for i in range(rails)]
    rows, pos = [], 0
    for count in counts:
        rows.append(list(cipher[pos:pos + count]))
        pos += count
    result = []
    for rail in pattern:
        result.append(rows[rail].pop(0))
    return "".join(result)

message = input("\nEnter message for Rail Fence Cipher: ")
rails = int(input("Enter number of rails: "))
encrypted = rail_fence_encrypt(message, rails)
decrypted = rail_fence_decrypt(encrypted, rails)
print("\n--- Rail Fence Cipher ---")
print("Encrypted message:", encrypted)
print("Decrypted message:", decrypted)
print("Original message verified:", decrypted == message)
