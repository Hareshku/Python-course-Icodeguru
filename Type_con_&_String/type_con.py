
# Type conversion is the process of converting a value from one data type to another. In Python, we often need this because different operations or functions require specific data types.

# Why We Do Type Conversion

# Compatibility in operations:
# Some operations only work with specific types. For example:

# x = "10"
# y = 5
# # print(x + y)  # ❌ Error
# print(int(x) + y)  # ✅ Works → 15


# # Here, we convert string "10" to integer using int() so we can add it to 5.

# # Data input from users:
# # Inputs are always read as strings. To perform calculations, we convert them:
# #  Calculator
# # age = input("Enter your age: ")  # User enters 20 → '20' (string)
# # age = int(age)  # Convert to integer for calculations


# # Working with collections:
# # Sometimes you want a set from a list to remove duplicates, or a tuple from a list to make it immutable:

# # numbers = [1, 2, 2, 3]
# # unique_numbers = set(numbers)  # {1, 2, 3}

# # print(unique_numbers)
# # Interfacing with functions:
# # Some functions require specific data types:

# # def square(n: int):
# #     return n * n

# # print(square(int("5")))  # Convert string to int before passing

# # Two Types of Type Conversion

# # Implicit Type Conversion (Type Casting automatically)
# # Python converts types automatically when needed:

# # x = 5        # int
# # y = 2.5      # float
# # z = x + y    # x converted to float automatically
# # print(z, type(z))  # 7.5 <class 'float'>


# # Explicit Type Conversion (Type Casting manually)
# # We use conversion functions like int(), float(), str() to convert types manually:

# x = "10"
# y = int(x)  # Explicit conversion


# # 💡 In short:
# # We do type conversion to avoid errors, perform calculations correctly, and use data in the format required by functions or operations.

# # Methods
# # int() → Integer
# # Converts a compatible value to an integer.

# x = "25"
# y = int(x)  # string to integer
# print(y, type(y))  # 25 <class 'int'>

# z = 10.7
# print(int(z))  # 10 (decimal part removed)

# 2. float() → Float

# Converts a compatible value to a floating-point number.

# x = "12.5"
# y = float(x)  # string to float
# print(y, type(y))  # 12.5 <class 'float'>

# z = 10
# print(float(z))  # 10.0

# 3. str() → String

# Converts a value to a string.

# x = 100
# y = str(x)
# print(y, type(y))  # '100' <class 'str'>

# z = 12.5
# print(str(z))  # '12.5'

# 4. bool() → Boolean

# Converts a value to True or False.

# x = 0
# y = bool(x)
# print(y, type(y))  # False <class 'bool'>

# z = 25
# print(bool(z))  # True


# Note: 0, 0.0, '', [], {}, () → False. Everything else → True.
# " " true 
# 5. list() → List

# Converts an iterable (like string, tuple, set) to a list.

# x = "hello"
# y = list(x)
# print(y, type(y))  # ['h', 'e', 'l', 'l', 'o'] <class 'list'>

# z = (1, 2, 3)
# print(list(z))  # [1, 2, 3]

# 6. tuple() → Tuple

# Converts an iterable to a tuple.

# x = [1, 2, 3]
# y = tuple(x)
# print(y, type(y))  # (1, 2, 3) <class 'tuple'>

# z = "abc"
# print(tuple(z))  # ('a', 'b', 'c')

# 7. set() → Set

# Converts an iterable to a set (removes duplicates).

# x = [1, 2, 2, 3, 3, 3]
# y = set(x)
# print(y, type(y))  # {1, 2, 3} <class 'set'>

# z = "hello"
# print(set(z))  # {'h', 'e', 'l', 'o'} (order may vary)

# 8. dict() → Dictionary

# Converts an iterable of key-value pairs to a dictionary.

x = [("a", 1), ("b", 2)]
y = dict(x)
print(y, type(y))  # {'a': 1, 'b': 2} <class 'dict'>

# z = [ [1, "one"], [2, "two"] ]
# print(dict(z))  # {1: 'one', 2: 'two'}


# ⚠️ Note: The input must be an iterable of pairs (2 elements each) to convert into a dictionary.