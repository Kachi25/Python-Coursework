# Logic and Bitwise Operations

# Ask the user for two Boolean inputs
value1 = input("Enter True or False: ").strip().lower() == "true"
value2 = input("Enter True or False: ").strip().lower() == "true"

# Demonstrate logical operators
print("\nLogical Operators:")

print("AND:", value1 and value2)
print("OR:", value1 or value2)
print("NOT value1:", not value1)
print("NOT value2:", not value2)

# Define two integers
x = 9
y = 5

# Display integers in binary
print("\nBitwise Operators:")
print("x =", x, "Binary:", bin(x))
print("y =", y, "Binary:", bin(y))

# Demonstrate bitwise operators
print("AND (&):", bin(x & y))
print("OR (|):", bin(x | y))
print("XOR (^):", bin(x ^ y))
print("NOT (~):", bin(~x))
print("Left Shift (<<):", bin(x << 1))
print("Right Shift (>>):", bin(x >> 1))
