# Python has a set of built-in methods that you can use on strings.

a = "Hello, World!"
print(a.upper())  # converts all characters to uppercase
print(a.lower())  # converts all characters to lowercase
print(a.strip())  # removes any whitespace from the beginning or the end
a = "Hello, World!"
print(a.replace("H", "J"))  # replaces a string with another string
print(a.split(","))  # splits the string into substrings if it finds a comma
print(a.split(" "))  # splits the string into substrings if it finds a space
print(a.split("o"))  # splits the string into substrings if it finds an "o"

#String Concatenation
#To concatenate, or combine, two strings you can use the + operator.
#ExampleGet

a = "Hello"
b = "World"
c = a + b
print(c)

print(a + " " + b)  # concatenates two strings
print(a * 3)  # prints the string three times
print(a * 0)  # prints the string zero times
print(a * 1)  # prints the string one time

# we can combine strings and numbers by using f-strings or the format() method!
# F-Strings
# F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
# To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)