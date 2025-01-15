# Simple bool algebra
print(True and not False) # True
print(False or True) # True

# Bitwise AND : a bit is 1 if both are 1s
print(3 & 2) # 2

# Bitwise OR : a bit is 1 if either or both are 1s
print(12 | 5) # 13

# Binary right shift (shift all bits 4 places to the right)
# bin(9) = 1001 = 0000
print(9 >> 4) # 0

# Binary left shift (shift all bits 3 places to the left)
print(7 << 3) # 56

# Modulo and bit shift
print(15 >> (7 - (3 % 8)) & 1) # 0