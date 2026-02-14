# What is the sets in Python
# A set is an unordered collection of unique elements. It is defined using curly braces {} or the set() constructor.

# set properties:
# 1. Unordered: The elements in a set do not have a specific order.
# 2. Unique: A set cannot contain duplicate elements. If you try to add a duplicate element, it will be ignored.
# 3. Mutable: You can add or remove elements from a set after it has been created.  

# Syntax 
# my_set = {1, 2, 3}  # Using curly braces
# my_set = set([1, 2, 3])  # Using the set
# # Example
# my_set = {1, 2, 3, 4, 5}
# print(my_set)  # Output: {1, 2, 3, 4, 5}

# set operations:
# 1. Union: Combines all unique elements from both sets.
# 2. Intersection: Returns only the elements that are present in both sets.

# 3. Difference: Returns the elements that are present in one set but not in the other.
# 4. Symmetric Difference: Returns the elements that are present in either set but not in both.

# Example 
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union
union_set = set1.union(set2)  
print("Union:", union_set)  # Output: {1, 2, 3, 4, 5, 6}

# Intersection
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)  # Output: {3, 4}

# Difference
difference_set = set1.difference(set2)
print("Difference (set1 - set2):", difference_set)  # Output: {1, 2}  
difference_set2 = set2.difference(set1)
print("Difference (set2 - set1):", difference_set2)  # Output: {5, 6} 

# Symmetric Difference
sym_diff_set = set1.symmetric_difference(set2)
print("Symmetric Difference:", sym_diff_set)  # Output: {1, 2, 5, 6}  

# Real-world applications of sets:
# 1. Removing duplicates from a list
# 2. Membership testing (checking if an element is in a set)
# 3. Set operations (union, intersection, difference)
# 4. Data analysis (finding unique values, common values, etc.)

