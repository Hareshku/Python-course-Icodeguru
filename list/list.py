# List i python
# What is a List in Python?
# A list is a collection used to store multiple values in a single variable.

# example
# numbers = [1, 2, 3, 4]
# names = ["Ali", "Haresh", "Sara"]
# mixed = [1, "Python", True, 3.5]

# # Key points
# # Ordered (items have fixed positions)
# # Mutable (can be changed)
# # Allows duplicate values
# # Can store any data type

# # empty = []
# # numbers = list((1, 2, 3))   # using list()

# fruits = ["apple", "banana", "mango"]

# print(fruits[0])   # apple
# print(fruits[2])   # mango

# # Negative indexing
# print(fruits[-1])  # mango
# print(fruits[-2])  # banana

# # Slicing Lists
# numbers = [0, 1, 2, 3, 4, 5]
# print(numbers[1:4])   # [1, 2, 3]
# print(numbers[:3])    # [0, 1, 2]
# print(numbers[3:])    # [3, 4, 5]
# print(numbers[::2])   # [0, 2, 4]
# print(numbers[::-1])  # reverse list

# # modifying a list 
# fruits = ["apple", "banana", "mango"]
# fruits[1] = "orange"

# print(fruits)


# # 🔹 Adding Elements
# # append() – add at end
# fruits.append("grapes")

# # insert() – add at specific index

# fruits.insert(1, "mango")

# # extend() – add multiple elements
# fruits.extend(["pear", "peach"])

# # 🔹 Removing Elements
# fruits.remove("banana")   # by value
# fruits.pop()              # last item
# fruits.pop(1)             # by index
# del fruits[0]             # delete by index
# fruits.clear()            # empty list

# # 🔹 List Length
# print(len(fruits))

# # 🔹 Looping Through Lists
# # Using for
# for fruit in fruits:
#     print(fruit)

# # Using index
# for i in range(len(fruits)):
#     print(i, fruits[i])

# # 🔹 Checking Membership
# if "apple" in fruits:
#     print("Apple exists")

# # 🔹 Sorting Lists
# numbers = [4, 1, 3, 2]

# numbers.sort()              # ascending
# numbers.sort(reverse=True)  # descending

# sorted_list = sorted(numbers)  # returns new list

# # 🔹 Reversing Lists
# numbers.reverse()