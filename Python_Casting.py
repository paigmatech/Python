# Casting in Python is done using constructor functions:
# int() - Converts to an integer.
# float() - Converts to a floating-point number.
# str() - Converts to a string.

# Integer casting
x = int(1)       # x will be 1
y = int(2.8)     # y will be 2
z = int("3")     # z will be 3

print(x)         # Outputs: 1
print(y)         # Outputs: 2
print(z)         # Outputs: 3

# Float casting
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

print(x)         # Outputs: 1.0
print(y)         # Outputs: 2.8
print(z)         # Outputs: 3.0
print(w)         # Outputs: 4.2

# String casting
x = str("s1")    # x will be 's1'
y = str(2)       # y will be '2'
z = str(3.0)     # z will be '3.0'

print(x)         # Outputs: s1
print(y)         # Outputs: 2
print(z)         # Outputs: 3.0

# Type checking
print(type(x))   # Outputs: <class 'str'>
print(type(y))   # Outputs: <class 'str'>
print(type(z))   # Outputs: <class 'str'>