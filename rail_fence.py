#Rail fence generated using gpt

def rail_fence_encrypt(text, depth):
    if depth == 1:
        return text

    rails = [''] * depth
    row = 0
    direction = 1   # 1 = down, -1 = up

    for ch in text:
        rails[row] += ch
        row += direction

        if row == 0 or row == depth - 1:
            direction *= -1

    return ''.join(rails)


def rail_fence_decrypt(cipher, depth):
    if depth == 1:
        return cipher

    # Step 1: mark zigzag pattern
    pattern = [['\n'] * len(cipher) for _ in range(depth)]

    row, direction = 0, 1
    for col in range(len(cipher)):
        pattern[row][col] = '*'
        row += direction
        if row == 0 or row == depth - 1:
            direction *= -1

    # Step 2: fill letters row-wise
    index = 0
    for i in range(depth):
        for j in range(len(cipher)):
            if pattern[i][j] == '*' and index < len(cipher):
                pattern[i][j] = cipher[index]
                index += 1

    # Step 3: read zigzag
    result = ''
    row, direction = 0, 1

    for col in range(len(cipher)):
        result += pattern[row][col]
        row += direction
        if row == 0 or row == depth - 1:
            direction *= -1

    return result


# -------- RUN --------
text = input("Enter text: ")
depth = int(input("Enter depth (rails): "))

cipher = rail_fence_encrypt(text, depth)
print("Cipher:", cipher)

plain = rail_fence_decrypt(cipher, depth)
print("Decrypted:", plain)