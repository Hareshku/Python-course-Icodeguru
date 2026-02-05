# Functions in python
#A function is a block of code that performs a specific task and runs only when it is called
# Function = Task

# Why Do We Need Functions?
# Without Functions
# Code repetition
# Long, messy programs
# Hard to debug
# Hard to modify
# With Functions
# ✔ Reusability
# ✔ Clean code
# ✔ Easy maintenance
# ✔ Easy debugging
# ✔ Logical separation
# Write once, use many times
#shopping website example
#  



# def function_name():
#     print("Hello from function")


# # def → defines a function
# # function_name → name of the function
# # () → used for parameters
# # : → start of function block
# # Indentation → mandatory


def greet():                     # Function Definition
    print("Hello there!")        # Function Body
greet()                          # Calling the function to execute its code block

# def add_numbers(a, b):          # Function with parameters
#     sum = a + b
#     print(sum)                # Returning the result to the caller

# add_numbers(5, 10)       # Function Call with arguments



def add_numbers_return(a, b):  
    sum = a + b
    return a,b
# to break the function and return the value to the caller                
result = add_numbers_return(5, 10)  
print("Sum is:", result)          


# # Funtion has two things
# # 1. Function Definition 
# # 2. function Calling

# # calculator example
# def calculator(num1, num2, operation):
#     if operation == "add"
#         return num1 + num2
#     elif operation == "subtract":
#         return num1 - num2
#     elif operation == "multiply":
#         return num1 * num2
#     elif operation == "divide":
#         if num2 != 0:
#             return num1 / num2
#         else:
#             return "Error: Division by zero"
#     else:
#         return "Error: Invalid operation"
      
      
# result = calculator(10, 5, "add")
# print("Addition:", result)
# result = calculator(10, 5, "subtract")
# print("Subtraction:", result)
# result = calculator(10, 5, "multiply")
# print("Multiplication:", result)
# result = calculator(10, 5, "divide")


# #default parameters
# def Addition(a=0, b=0, c=0):  
#     return a + b + c
# result = Addition(10,12, 15)
# res=Addition(10, 12) 
# noPaarams=Addition()
# # c will take default value 0
# print("Addition with all parameters:", res)
# print("Addition with default parameter:", result)
# print("Addition with no parameters:", noPaarams)


# #return none 
# def resturn_none(a, b):
#     result = a + b
    
# output = resturn_none(5, 10)
# print("Output is:", output)  # Output will be None since there is no return statement


# one function can return only one value
# def multiple_return(a, b):
#     sum = a + b
#     diff = a - b
#     mutiply = a * b
    #   return sum
#     return sum, diff, mutiply # (sum, diff, multiply) as tuple

# result=multiple_return(10, 20)
# s,d, m = multiple_return(10, 5)
# print("Multiple Returns:", result)  # Output will be a tuple (30, -10, 200)
# print("Sum, Difference, and Product:", s) 
# print("Sum, Difference, and Product:", d)  
# print("Sum, Difference, and Product:", m)  



# positional arguments
# def sum_numbers(a, b):
#     total = a + b
#     return total

# result = sum_numbers(10, 20, 30, 40, 50)
# print("Sum with positional arguments:", result) 


# def sum_numbers(a, b, *args):
#     total = a + b+ sum(args)
#     return total

# result = sum_numbers(10, 20, 30, 40, 50)
# print("Sum with positional arguments:", result) 
    
# def sum_numbers(*args):
#     total =sum(args)
#     return total

# result = sum_numbers(10, 20, 30, 40, 50)
# print("Sum with positional arguments:", result) 
    
# Variable scope
# L → Local
# E → Enclosing
# G → Global
# B → Built-in

# Local Scope
# A variable created inside a function.

# def show_marks():
#     marks = 85  # local variable
#     print(marks)

# # print(marks)
# show_marks()


# Global Scope
# A variable created outside all functions.

# school = "ABC School"  # global variable
# def show_school():
#     print(school)

# show_school()



# Global Variable Modification
# count = 10
# def update():
#     count = count + 1  # ❌ Error

# count = 10
# def update():
#     global count
#     count = count + 1

# update()
# print(count)


# Enclosing Scope (Nested Functions)
# Variables in an outer function, used by an inner function.

def outer():
    msg = "Hello"

    def inner():
        print(msg)

    inner()
outer()

# Modifying Enclosing Variable
# def outer():
#     count = 5
#     def inner():
#         nonlocal count
#         count += 1
#         print(count)
#     inner()
# outer()
