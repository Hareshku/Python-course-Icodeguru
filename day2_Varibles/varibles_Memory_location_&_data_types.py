# Variable, Memory location and data types in Python
a=10          # Integer variable  
# "a" is the name of the variable
# "=" is the assignment operator
# "10" is the value assigned to the variable

# Rules for naming variables in Python:
# 1. Variable names must start with a letter (a-z, A-Z) or an underscore (_)
# 2. The rest of the variable name can contain letters, digits (0-9), or underscores
# 3. Variable names are case-sensitive (e.g., myVar and myvar are different)
# 4. Variable names cannot be a reserved keyword in Python (e.g., if, else, while, for, etc.) 
# 5. Variable names should not contain spaces
# 6. Variable names should be descriptive and meaningful

# Examples of valid variable names:
my_variable = 5
_variable2 = "Hello"
var3 = 3.14

# Examples of invalid variable names:
# 1variable = 10      # Starts with a digit
# my-variable = 20    # Contains a hyphen
# my variable = 30    # Contains a space

# Naming conventions:
# 1. snake_case: Words are separated by underscores (e.g., my_variable_name)
# 2. camelCase: The first word is lowercase, and subsequent words are capitalized (e.g., myVariableName)
# 3. PascalCase: Each word is capitalized (e.g., MyVariableName


# Memory location
# When program runs then only variable is created in RAM and value is stored in it
#RAM allocates memory to store the value of the variable
# Each variable has a unique memory address

# Data types in Python:
a = 10          # Integer variable  
b = 3.14        # Float variable  
c = "Hello"     # String variable
d = True        # Boolean variable    
e = None        # NoneType variable

# Printing variable values and their data types
print("Value of a:", a, "Type of a:", type(a))
print("Value of b:", b, "Type of b:", type(b))    
print("Value of c:", c, "Type of c:", type(c))
print("Value of d:", d, "Type of d:", type(d))
print("Value of e:", e, "Type of e:", type(e))

# Demonstrating memory locations of variables
print("Memory location of a:", id(a))
print("Memory location of b:", id(b))
print("Memory location of c:", id(c))
print("Memory location of d:", id(d))
print("Memory location of e:", id(e)) 


# String definition in Python:
str1 = "Hello, World!"   # Using double quotes
str2 = 'Python is fun.'   # Using single quotes 
str3 = """This is a 
multi-line string."""    # Using triple double quotes

str4 = '''This is also a 
multi-line string.'''    # Using triple single quotes

print(str4)
Str5 = "It's a beautiful day!"  # Using single quote inside double quotes
print(Str5)
Str6 = 'He said, "Hello!"'     # Using double quote inside single quotes
print(Str6)
Str7 = "He said, \"Hello!\""   # Using escape character for double quote
print(Str7)
Str8 = 'It\'s a beautiful day!' # Using escape character for single quote
print(Str8)