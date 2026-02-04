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



def function_name():
    print("Hello from function")


# def → defines a function
# function_name → name of the function
# () → used for parameters
# : → start of function block
# Indentation → mandatory


def greet():                     # Function Definition
    print("Hello there!")        # Function Body
greet()                          # Calling the function to execute its code block

def add_numbers(a, b):          # Function with parameters
    sum = a + b
    print(sum)                # Returning the result to the caller

add_numbers(5, 10)       # Function Call with arguments


# calculator example
def calculator(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"
      
      
result = calculator(10, 5, "add")
print("Addition:", result)
result = calculator(10, 5, "subtract")
print("Subtraction:", result)
result = calculator(10, 5, "multiply")
print("Multiplication:", result)
result = calculator(10, 5, "divide")