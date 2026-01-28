# Operators in Python
#what is operator
# An operator is a special symbol or keyword that performs operations on one or more operands (values or variables) to produce a result.
# Operators are used to perform various operations such as arithmetic calculations, comparisons, logical operations, and more.

# Types of Operators in Python:
# 1. Arithmetic Operators
a = 10
b = 3   
print("Arithmetic Operators:")
print("Addition:", a + b)          # Addition
print("Subtraction:", a - b)       # Subtraction
print("Multiplication:", a * b)    # Multiplication
print("Division:", a / b)          # Division
print("Floor Division:", a // b)   # Floor Division 
print("Modulus:", a % b)           # Modulus
print("Exponentiation:", a ** b)   # Exponentiation

# 2. Comparison Operators
print("\nComparison Operators:")
print("Equal to:", a == b)          # Equal to
print("Not equal to:", a != b)      # Not equal to
print("Greater than:", a > b)       # Greater than
print("Less than:", a < b)          # Less than 
print("Greater than or equal to:", a >= b)  # Greater than or equal to
print("Less than or equal to:", a <= b)     # Less than or equal to

# 3. Logical Operators
print("\nLogical Operators:")
x = True
y = False
print("Logical AND:", x and y)      # Logical AND
print("Logical OR:", x or y)        # Logical OR
print("Logical NOT:", not x)        # Logical NOT

# 4. Assignment Operators
print("\nAssignment Operators:")
c = 5
print("Initial value of c:", c) 
c += 2            # c = c + 2
print("After c += 2:", c)            # c = c + 2
c *= 3            # c = c * 3
print("After c *= 3:", c)            # c = c * 3
c -= 4            # c = c - 4
print("After c -= 4:", c)            # c = c - 4
c /= 2            # c = c / 2
print("After c /= 2:", c)            # c = c / 2
c %= 3            # c = c % 3
print("After c %= 3:", c)            # c = c % 3

# 5. Membership Operators
print("\nMembership Operators:")
my_list = [1, 2, 3, 4, 5]
print("Is 3 in my_list?", 3 in my_list)        # Membership test
print("Is 6 not in my_list?", 6 not in my_list)  # Membership test



# 6. Identity Operators
print("\nIdentity Operators:")
x1 = [1, 2, 3]
y1 = x1
z1 = [1, 2, 3]
print("x1 is y1:", x1 is y1)        # Identity test
print("x1 is z1:", x1 is z1)        # Identity test 
print("x1 is not z1:", x1 is not z1)  # Identity test
print("x1 == z1:", x1 == z1)        # Equality test
print("x1 != z1:", x1 != z1)        # Inequality test

# Note: 'is' checks for identity (same memory location), while '==' checks for equality (same value).

# 7. Bitwise Operators
print("\nBitwise Operators:")
p = 5      # Binary: 0101
q = 3      # Binary: 0011
print("Bitwise AND:", p & q)        # Bitwise AND
print("Bitwise OR:", p | q)         # Bitwise OR
print("Bitwise XOR:", p ^ q)        # Bitwise XOR
print("Bitwise NOT of p:", ~p)      # Bitwise NOT
print("Left Shift p by 1:", p << 1) # Left Shift
print("Right Shift p by 1:", p >> 1) # Right Shift

# Note: Bitwise operators work on the binary representation of integers.
