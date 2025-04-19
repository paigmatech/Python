# Python Logical Operators
# Logical operators are used to combine conditional statements.
#
# In Python, there are three logical operators:
# and, or, and not.
#
# The `and` operator returns True if both statements are true.
# The `or` operator returns True if one of the statements is true.
# The `not` operator returns True if the statement is false.


x = 5  # Assigning value 5 to x
y = 10  # Assigning value 10 to y
z = 15  # Assigning value 15 to z

# `and` operator
print(x < y and y < z)  # True, because both conditions (x < y and y < z) are true
print(x < y and y > z)  # False, because the second condition (y > z) is false
print(x < y or y > z)  # True, because one of the conditions (x < y) is true
print(x > y or y > z)  # False, because both conditions (x > y and y > z) are false

# `not` operator
print(not(x < y))  # False, because the condition (x < y) is true, and `not` negates it
print(not(x > y))  # True, because the condition (x > y) is false, and `not` negates it

# Example with strings
str1 = "Hello"
str2 = "World"

# `and` operator with strings
print(str1 == "Hello" and str2 == "World")  # True, because both conditions are true
print(str1 == "Hello" and str2 == "Python")  # False, because the second condition is false

# `or` operator with strings
print(str1 == "Hello" or str2 == "Python")  # True, because the first condition is true
print(str1 == "Python" or str2 == "Python")  # False, because both conditions are false

# `not` operator with strings
print(not(str1 == "Python"))  # True, because the condition (str1 == "Python") is false
print(not(str2 == "World"))  # False, because the condition (str2 == "World") is true