## Python Collections (Arrays)
## There are four collection data types in the Python programming language:

## List is a collection which is ordered and changeable. Allows duplicate members.
## Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
## Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
## Dictionary is a collection which is ordered** and changeable. No duplicate members.

thislist = ["apple", "banana", "cherry"]  # Creating a list with three elements

thislist.append("orange")  # Adding "orange" to the end of the list

print(thislist)  # Printing the updated list

thislist.append("Guava")  # Adding "orange" to the end of the list

print(thislist)  # Printing the updated list

thislist = ["apple", "banana", "cherry"]
print(thislist[1])
# Printing the second element of the list (index 1)
print(thislist[-1])
# Printing the last element of the list (negative index -1)
print(thislist[1:])
# Printing all elements from index 1 to the end of the list
print(thislist[2:3])
