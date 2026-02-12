# 1. What is a Dictionary in Python?
# A dictionary is a data structure used to store data in key–value pairs.
# Think of it like:
# A phone contact list → name : number
# A student record → roll_no : marks
# A shopping cart → product : price

student = {
    "name": "Ali",
    "age": 20,
    "marks": 85
}

# 2. Why Do We Use Dictionaries?
# Fast data access
# Data is meaningful (not index-based)
# Used everywhere: APIs, databases, JSON, configs
# Unlike lists, dictionaries don’t use index numbers.

# 🔹 3. Dictionary Syntax
# dict_name = {key: value, key: value}


# Example:

car = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2022
}

# 4. Dictionary Characteristics

# ✔ Mutable (can change)
# ✔ Unordered (before Python 3.7)
# ✔ Keys must be unique
# ✔ Keys must be immutable (str, int, tuple)
# ❌ Keys cannot be list or dict

# 5. Accessing Values

# Using keys, not indexes:

print(car["brand"])   # Toyota


# If key doesn’t exist → KeyError

# Safe way:

print(car.get("price"))   # None

# 6. Adding New Items
car["price"] = 2500000
print(car)

# 7. Updating Values
car["year"] = 2023

# 8. Removing Items
del car["model"]


# Other ways:

car.pop("year")
car.clear()

# 9. Dictionary Methods (Important)
# keys()
print(car.keys())

# values()
print(car.values())

# items()
print(car.items())

# 10. Looping Through Dictionary
# Loop keys
for key in car:
    print(key)

# Loop values
for value in car.values():
    print(value)

# Loop key + value
for key, value in car.items():
    print(key, ":", value)

# 11. Checking Key Existence
if "brand" in car:
    print("Brand exists")

# 12. Dictionary Length
print(len(car))

# 13. Nested Dictionaries (Very Important)

# Real-world example: student database

students = {
    101: {"name": "Ali", "marks": 85},
    102: {"name": "Sara", "marks": 90}
}


# Access:

print(students[101]["name"])

# 14. Dictionary with List Values
shopping_cart = {
    "fruits": ["apple", "banana"],
    "total": 500
}

#15. Copying Dictionary
new_car = car.copy()


#creates reference, not copy

#16. Dictionary Comprehension (Advanced)

squares = {x: x*x for x in range(1, 6)}
print(squares)


#17. Real-World Use Case: Shopping Website
def calculate_total(cart):
    total = 0
    for price in cart.values():
        total += price
    return total

cart = {
    "Laptop": 80000,
    "Mouse": 1500,
    "Keyboard": 3000
}

print(calculate_total(cart))


# Same function reused in:
# Cart page
# Checkout
# Invoice
# Email receipt