# # What is a String?
# # A string is a sequence of characters enclosed in quotes.


name = "Haresh"
city = 'Lahore'
# # You can use:
# # Single quotes ' '
# # Double quotes " "
# print("It's a")
# quote = 'He said "Hello"' 
# print(quote)
# Triple quotes ''' ''' or """ """

# # Multiline Strings
# text="""dfsdfds"""
# tet = """This is
# a multiline
# string"""

# print(tet)
# print(text)

# # String is Ordered
# # Each character has an index.

# word = "Python"

# Index	Value
# 0	P
# 1	y
# 2	t
# 3	h
# 4	o
# 5	n
# Indexing
# print(word[0])   # P
# print(word[-1])  # n
# word="Python"
# # # Slicing
# print(word[0:4])   # Pyth
# print(word[::2])   # Pto
# print(word[::-1])  # nohtyP (reverse)

# # String is Immutable
# # ❌ Cannot change characters
# # But you can replace whole string:
# word[0] = "J"   # Error
# replace() creates a new string and returns it.
# text = "hello"
# new_text = text.replace("h", "H")

# print(text)      # hello (original unchanged)
# print(new_text)  # Hello (new string)




# word = "Java"

# # String Length
# print(len(word))

# # String Methods (Very Important)
# # Case Methods
# text = "hello World"

# print(text.upper())     # HELLO WORLD
# print(text.lower())     # hello world
# print(text.title())     # Hello World
# print(text.capitalize())# Hello world

# # Remove Spaces
# msg = "   Python   "
# print(msg.strip()) #Removes space from both sides
# print(msg.lstrip()) # Removes only from left side
# print(msg.rstrip()) #Removes only from right side

# text= "World"
# # Replace
# print(text.replace("World", "Python"))

# # Split
# data = "apple, banana, mango"
# print(data.split(","))
# print(data.split()) #space

# # Join
# words = ["I", "love", "Python"] 
# w="dssdf"
# print(" ".join(words)) #ILovePython

# # Find & Count
# text = "bdnana"
# print(text.find("a"))   # first index
# print(text.count("a"))  # total count

# # Check Methods
# print("hello".isalpha())   # True
# print("hello123".isalpha()) # False
# print("hello world".isalpha()) # False (because of space)

# print("123".isdigit())   # True
# print("12a3".isdigit())  # False
# print("123 ".isdigit())  # False (space not allowed)

# print("abc123".isalnum())  # True
# print("abc 123".isalnum()) # False (space)
# print("abc@123".isalnum()) # False (@ symbol)

# print("   ".isspace())   # True
# print("\t".isspace())    # True
# print(" a ".isspace())   # False


# String Concatenation
# a = "Hello"
# b = "World"
# print(a + " " + b)

# #String Repetition
# print("Hi" * 3)

# # String Formatting (Very Important)
# # f-Strings (Best Way)
# name = "Haresh"
# age = 22
# print("My name is {name} and I am {age} years old.")

# # ✅ format() before (3.6)
# print("My name is {} and I am {} years old.".format(name, age))


#  Escape Characters
print("He said \"Hello\"")
print('He said "Hello"')
print("Line1\nLine2")
print("Tab\tSpace")


# #  Looping Through String
# for char in "Python":
#     print(char)

# # Membership Operator
print("Py" in "Python")
print("PY".lower() in "Python".lower())

# #Comparing Strings
# print("apple" == "apple")
# print("apple" > "banana")

# #  Palindrome Example
word = "madam"

if word == word[::-1]:
    print("Palindrome")


# # String vs List Difference
# # Feature	String	List
# # Mutable	❌ No	✅ Yes

# # Advanced: String Interning (Concept)

# # Python stores identical strings in memory once to save space.

a = "hello"
b = "hello"



# # Real-World Use Cases

# # ✔ Form validation
# # ✔ Email checking
# # ✔ Password rules
# # ✔ Data cleaning
# # ✔ Text processing
# # ✔ File handling\n