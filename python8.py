# Demonstration of operators in Python

# Arithmetic Operators
a = 10
b = 3
print("Addition:", a + b)        # Addition
print("Subtraction:", a - b)     # Subtraction
print("Multiplication:", a * b)  # Multiplication
print("Division:", a / b)        # Division
print("Floor Division:", a // b) # Floor Division
print("Modulus:", a % b)         # Modulus
print("Exponentiation:", a ** b) # Exponentiation

# Comparison Operators
print("Equal:", a == b)          # Equal
print("Not Equal:", a != b)      # Not Equal
print("Greater Than:", a > b)    # Greater Than
print("Less Than:", a < b)       # Less Than
print("Greater or Equal:", a >= b) # Greater or Equal
print("Less or Equal:", a <= b)  # Less or Equal

# Logical Operators
x = True
y = False
print("Logical AND:", x and y)   # Logical AND
print("Logical OR:", x or y)     # Logical OR
print("Logical NOT:", not x)     # Logical NOT

# Bitwise Operators
c = 5  # Binary: 0101
d = 3  # Binary: 0011
print("Bitwise AND:", c & d)     # Bitwise AND
print("Bitwise OR:", c | d)      # Bitwise OR
print("Bitwise XOR:", c ^ d)     # Bitwise XOR
print("Bitwise NOT:", ~c)        # Bitwise NOT
print("Left Shift:", c << 1)     # Left Shift
print("Right Shift:", c >> 1)    # Right Shift

# Assignment Operators
e = 5
e += 3  # e = e + 3
print("Add and Assign:", e)
e *= 2  # e = e * 2
print("Multiply and Assign:", e)

# Membership Operators
lst = [1, 2, 3, 4, 5]
print("Is 3 in list?", 3 in lst)       # in
print("Is 6 not in list?", 6 not in lst) # not in

# Identity Operators
f = [1, 2, 3]
g = [1, 2, 3]
h = f
print("f is g:", f is g)   # is
print("f is h:", f is h)   # is
print("f is not g:", f is not g) # is not