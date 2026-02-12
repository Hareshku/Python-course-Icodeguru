# #1. What is a Tuple?
# # A tuple is a collection of items that is:
# # Ordered
# # Indexed
# #Immutable (cannot be changed after creation)
# #Think of a tuple like a sealed package 📦 — once packed, you can’t change what’s inside.

# colors = ("red", "green", "blue")

# # 2. Why Do We Use Tuples?
# # To store fixed data
# # Safer than lists (cannot be modified accidentally)
# # Faster than lists
# # Used in returning multiple values
# # Real-world examples:
# # Days of the week
# # RGB color codes
# # Coordinates (x, y)
# # Database records

# # Creating a Tuple
# # Basic tuple
# numbers = (1, 2, 3)

# # Without parentheses (tuple packing)
# numbers = 1, 2, 3

# # Single-element tuple 
# single = (5,)   # comma is required
# # (5) is NOT a tuple.

# # Tuple Characteristics
# # Feature	Tuple
# # Ordered
# # Indexed
# # Mutable	
# # Duplicate allowed	
# # Faster than list	

# # Accessing Tuple Elements
# # Using index:
# fruits = ("apple", "banana", "cherry")
# print(fruits[0])    # apple


# # Negative index:
# print(fruits[-1])   # cherry

# #6. Slicing Tuples
# print(fruits[0:2])


# # 7. Tuple is Immutable (Very Important)

# # This will cause an error:
# fruits[0] = "mango"


# # That’s the main difference from lists.
# # 8. Looping Through Tuples
# for item in fruits:
#     print(item)

# # 9. Checking Membership
# if "apple" in fruits:
#     print("Found")

# # 10. Tuple Length
# print(len(fruits))

# # 11. Tuple Methods (Only 2!)
# numbers = (1, 2, 3, 2, 2)

# # count()
# print(numbers.count(2))  # 3

# # index()
# print(numbers.index(3))  # 2


# # Why only 2 methods?
# # Because tuples cannot change.

# # 12. Tuple Packing & Unpacking (Very Important)
# # Packing
# data = "Ali", 22, "CS"

# # Unpacking
# name, age, dept = data


# # Real-world example:

# def get_user():
#     return "Ali", 22

# name, age = get_user()

# # 13. Returning Multiple Values from a Function
# def calculate(a, b):
#     return a+b, a-b, a*b

# result = calculate(10, 5)
# print(result)

# # Python returns a tuple

# # 14. Nested Tuples
# points = ((1, 2), (3, 4), (5, 6))
# print(points[0][1])  # 2

# # 15. Tuple vs List (Important Comparison)
# # Feature	List	Tuple
# # Mutable	
# # Speed	Slower	Faster
# # Safety	Less	More
# # Use case	Dynamic data	Fixed data

# # 16. Tuple in Dictionary Keys (Advanced Use)

# # Tuples can be dictionary keys because they are immutable.

# locations = {
#     (10, 20): "Park",
#     (30, 40): "Mall"
# }

# # 17. When Should You Use Tuple?

# # ✔ Data should not change
# # ✔ Function returns multiple values
# # ✔ Fixed configuration values
# # ✔ Dictionary keys

# # 🧠 Rule:

# # If data should never change → use tuple

# # 18. Common Beginner Mistakes

# # ❌ Forgetting comma in single-element tuple
# # ❌ Trying to modify tuple
# # ❌ Confusing list and tuple
# # ❌ Overusing tuple when list is better

# # 19. Performance Insight (Advanced)

# # Tuples:

# # Use less memory
# # Faster iteration
# # Preferred in large datasets (read-only)

# # 20. Real-World Example: Student Record 
# student = ("Ali", 101, 85)
# name, roll, marks = student


# ✔ Safe
# ✔ Structured
# ✔ Clean




# 🔹 1️⃣ Basic Definition
# Data Type	What It Stores
# List	Ordered collection of values
# Tuple	Ordered, immutable collection
# Dictionary	Key–value pairs
# Set	Unordered collection of unique values
# 🔹 2️⃣ Syntax Difference
# # List
# list = [1, 2, 3]

# # Tuple
# t = (1, 2, 3)
# t = (10, 20, 30)

# temp = list(t)
# temp[0] = 99
# t = tuple(temp)

# print(t)
# # Dictionary
# d = {"a": (1,2,3), "b": 2}
# print()
# dict={}
# # Set
# s = {1, 2, 3}
# empty=set()

# 🔹 3️⃣ Ordered vs Unordered
# Type	Ordered?
# List	✅ Yes
# Tuple	✅ Yes
# Dictionary	✅ (Python 3.7+ insertion order)
# Set	❌ No
# 🔹 4️⃣ Mutable vs Immutable
# Type	Mutable?
# List	✅ Yes
# Tuple	❌ No
# Dictionary	✅ Yes
# Set	✅ Yes
# 🔹 5️⃣ Duplicate Values
# Type	Allow Duplicates?
# List	✅ Yes
# Tuple	✅ Yes
# Dictionary	❌ Keys No (Values Yes)
# Set	❌ No

# Example:

# s = {1, 1, 2}
# print(s)   # {1, 2}

# 🔹 6️⃣ How We Access Data
# Type	Access Method
# List	Index
# Tuple	Index
# Dictionary	Key
# Set	Cannot use index
# 🔹 7️⃣ Real-World Usage
# 🔹 List → Dynamic Data

# Shopping cart items:

# cart = ["laptop", "mouse", "keyboard"]

# 🔹 Tuple → Fixed Data

# Coordinates:

# location = (24.86, 67.01)

# 🔹 Dictionary → Mapped Data

# Student record:

# student = {"name": "Ali", "marks": 85}

# 🔹 Set → Unique Data

# Unique visitors:

# visitors = {"Ali", "Sara", "Ali"}

# 🔹 8️⃣ Performance Overview
# Type	Speed	Memory
# Tuple	Fastest	Less
# List	Medium	Medium 
# Set	Fast lookup	Medium
# Dictionary	Fastest lookup by key	More
# 🔹 9️⃣ When To Use What?

# Use List when:

# Order matters

# Data changes frequently

# Use Tuple when:

# Data should not change

# Safety is important

# Use Dictionary when:

# Data has labels (key → value)

# Use Set when:

# You need unique values

# You need fast membership checking

# 🔹 1️⃣0️⃣ Simple Memory Analogy
# Type	Analogy
# List	Notebook 📒
# Tuple	Sealed document 📜
# Dictionary	Phonebook 📖
# Set	Unique ID scanner 🎫
# 🔹 Final One-Line Summary

# List → Ordered & changeable

# Tuple → Ordered & fixed


# Dictionary → Key–value mapping

# Set → Unique unordered values