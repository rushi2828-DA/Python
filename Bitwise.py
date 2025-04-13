a = 10  # Binary: 1010
b = 4   # Binary: 0100

print("a =", a, "in binary:", bin(a))
print("b =", b, "in binary:", bin(b))

# Bitwise AND
print("a & b:", a & b)  # 1010 & 0100 = 0000 (0)

# Bitwise OR
print("a | b:", a | b)  # 1010 | 0100 = 1110 (14)

# Bitwise XOR
print("a ^ b:", a ^ b)  # 1010 ^ 0100 = 1110 (14)

# Bitwise NOT
print("~a:", ~a)        # -(a+1) = -11 (inverts bits)

# Left Shift
print("a << 1:", a << 1)  # 10100 (20)

# Right Shift
print("a >> 1:", a >> 1)  # 0101 (5)
