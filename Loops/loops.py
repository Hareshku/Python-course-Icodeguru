#What is loops in Python?
#Loops are used to execute a block of code repeatedly for a certain number of times or until a specific condition is met.
#They help automate repetitive tasks and reduce code redundancy.

#Why loops are important?
#Loops enable efficient handling of repetitive tasks, allowing for dynamic processing of data and automation of workflows.

#When to use loops?
#Use loops when you need to perform the same operation multiple times, such as iterating over a list, processing items in a collection, or executing a block of code until a condition changes.

print("Hello world!")
print("Hello world!")
print("Hello world!")
print("Hello world!")
print("Hello world!")
print("Hello world!")
print("Hello world!")
print("Hello world!")
print("Hello world!")

# I want to print "Hello world!" 100 times
#Instead of writing the print statement 100 times, we can use a loop to achieve this  
for i in range(100):
    print("Hello world!")

#Types of Loops in Python:
#1. For Loop
#2. While Loop
#3. Nested Loop


# 1. For Loop
# A for loop is used to iterate over a sequence (like a list, tuple, dictionary, set, or string) or other iterable objects.
# It allows you to execute a block of code for each item in the sequence.
#When to use for loop?
#Use a for loop when you know the number of iterations in advance or when iterating over a collection of items.
#What is finite loop?
#A finite loop is a loop that has a predetermined number of iterations or a specific condition that will eventually be met, causing the loop to terminate.
#What is infinite loop?
#An infinite loop is a loop that continues to execute indefinitely because its terminating condition is never met.

#What is index?
#An index is a numerical representation of the position of an element within a sequence, such as a list or string. In Python, indexing starts at 0, meaning the first element is at index 0, the second at index 1, and so on.  

#Finite loop example using for loop



for i in range(5):  # Loop will run 5 times (0 to 4)
    print("Iteration:", i)
    

for i in range(1, 6):  # Loop will run from 1 to 5
    print("Number:", i)
    
    
for i in range(2, 11, 2):  # Loop will run from 2 to 10 with a step of 2
    print("Even Number:", i)
    
name= "Python"
for char in name:
    print(char)
    

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit) 
    
#While Loop
#A while loop repeatedly executes a block of code as long as a specified condition is true. 
#When to use while loop?
#Use a while loop when the number of iterations is not known in advance and depends on a condition being met.
#Finite loop example using while loop

count = 0
while count < 5:
    print("Count is:", count)
    count += 1
    
    
    
#Infinite loop example using while loop
# Uncomment the following lines to see an infinite loop in action 

# while True:
#     print("This loop will run forever unless interrupted.") 


#Nested Loop
#A nested loop is a loop that exists inside another loop. The inner loop runs completely for each iteration of the outer loop.
#When to use nested loop? 
#Use nested loops when you need to perform complex iterations, such as iterating over multi-dimensional data structures (like matrices) or when dealing with combinations of items.
#Finite loop example using nested loop
for i in range(3):  # Outer loop
    for j in range(2):  # Inner loop
        print(f"Outer loop iteration {i}, Inner loop iteration {j}")
    
#Infinite loop example using nested loop
# Uncomment the following lines to see an infinite nested loop in action
# while True:  # Outer infinite loop
#     while True:  # Inner infinite loop
#         print("This inner loop will run forever unless interrupted.") 
# Note: Be cautious when using infinite loops, as they can cause your program to become unresponsive. Always ensure you have a way to break out of them, such as a keyboard interrupt (Ctrl+C) or a specific condition to exit the loop.

#Break and Continue Statements in Loops
#Break Statement: The break statement is used to exit a loop prematurely when a certain condition is met. It immediately terminates the loop and transfers control to the statement following the loop.

#Continue Statement: The continue statement is used to skip the current iteration of a loop and move to the next iteration. It allows you to bypass certain conditions without exiting the loop entirely.

#Example of Break Statement
print("Break Statement Example:")
for i in range(10):
    if i == 5:
        print("Breaking the loop at i =", i)
        break
    print("i =", i) 
    
    
#Example of Continue Statement
print("Continue Statement Example:")    
for i in range(10):
    if i % 2 == 0:
        print("Skipping even number i =", i)
        continue
    print("i =", i)
#In this example, when i is 5, the loop breaks and exits. In the continue example, even numbers are skipped, and only odd numbers are printed.

