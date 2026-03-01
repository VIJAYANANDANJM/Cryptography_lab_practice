#columnar generated using gpt

text = input("Enter plaintext: ").replace(" ", "").lower()
key = input("Enter key: ").lower()

cols = len(key)

# padding
while len(text) % cols != 0:
    text += 'x'

rows = len(text) // cols

# create grid
grid = [text[i:i+cols] for i in range(0, len(text), cols)]

# determine column order
order = sorted(range(cols), key=lambda i: key[i])

# encryption
cipher = ''
for col in order:
    for row in grid:
        cipher += row[col]

print("Cipher:", cipher)

# decryption
plain = [''] * len(text)
index = 0

for col in order:
    for r in range(rows):
        plain[r*cols + col] = cipher[index]
        index += 1

print("Decrypted:", ''.join(plain))