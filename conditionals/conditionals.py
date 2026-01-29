# What is conditional statements in Python?
# Conditional statements are used to perform different actions based on whether a certain condition is true or false
# They allow you to control the flow of your program by executing specific blocks of code depending on the evaluation of conditions.

# Why conditional statements are important?
# They enable decision-making in your code, allowing for dynamic behavior based on varying inputs or states

# when to use conditional statements?
# Use conditional statements when you need to execute different code paths based on specific conditions or criteria.

# Types of Conditional Statements in Python:

# If True/False:
# then block of code will execute

if True:
    print("This block executes because the condition is True.")
    
if False:
    print("This block does not execute because the condition is False.")    
    

    
# # 2. if-else statement

# Real word application where we use if-else statement?
# Example: User authentication system
# Shoping cart checkout process
# Google drive file upload

print("File Upload Status:")
if 10 ==5:
 print("Upload successful")
else:
 print("Upload failed")


# If else using operators
a = 10
b = 20
if a < b:
    print(f"{a} is less than {b}")
else:
    print(f"{a} is not less than {b}")


# multiple conditions with if-elif-else

# Why other condition don't excute in if-elif-else?
# Because in an if-elif-else structure, once a condition is met and its block of code is executed, the rest of the conditions are skipped. This is designed to ensure that only one block of code runs, based on the first true condition.

# best case: 1st condition is true | stop checking further
# worst case: last condition is true | check all conditions
# CPU processing Units consumed will be less in if-elif-else when compared to multiple if statements.


marks =  87
print("Grade Evaluation:")
if marks >= 91:
    print("Grade: A+")
elif marks  >= 83:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B+")
elif marks >= 68:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C+")
elif marks >= 50:
    print("Grade: C") 
else:
    print("Grade: F")    


# # Multiple if statements
# # Problem with multiple if statements is that all conditions are evaluated independently, which can lead to multiple blocks of code being executed if more than one condition is true. This can result in unintended behavior, especially when the conditions are meant to be mutually exclusive.

# # This will consume more processing Units of CPU.
marks =  82 
print("Grade Evaluation with Multiple if Statements:")
if marks >= 91:
    print("Grade: A+")
if marks  >= 83:
    print("Grade: A")
if marks >= 75:
    print("Grade: B+")
if marks >= 68:
    print("Grade: B")
if marks >= 60:
    print("Grade: C+")    
if marks >= 50:
    print("Grade: C")
if marks < 50:
    print("Grade: F")

    # what is difference between multiple if statements used with logical operators and if-elif-else statement?  
# Multiple conditions using logical operators

# Best case: 1st condition is true | will check all conditions
# Worst case: last condition is true | will check all conditions

Marks =  85
print("Grade Evaluation with Logical Operators:")
if Marks >= 91 and Marks <= 100:
    print("Grade: A+")
if Marks >= 83 and Marks < 91:
    print("Grade: A")
if Marks >= 75 and Marks < 83:
    print("Grade: B+")      
if Marks >= 68 and Marks < 75:
    print("Grade: B")
if Marks >= 60 and Marks < 91:
    print("Grade: C+")
if Marks >= 60 and Marks < 68:
    print("Grade: C+")
if Marks >= 50 and Marks < 60:
    print("Grade: C")
if Marks < 50:
    print("Grade: F")
    

# Nested if statements
# Nested if statements are used when you need to make a decision based on multiple conditions that depend on each other.
# They allow for more complex decision-making processes by placing one if statement inside another. 

# ATM example 
pin_correct = False
balance = 1000
withdraw_amount = 500
print("ATM Transaction:")
if pin_correct:
    print("PIN verified.")
    if balance >= withdraw_amount:
        balance -= withdraw_amount
        print("Withdrawal successful.")
    else:
        print("Insufficient balance.")
else:
    print("Invalid PIN.")