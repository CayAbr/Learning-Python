fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Accesses the first element in the list

fruits[1] = "blueberry"  # Modifies the second element in the list
print(fruits) # Prints the modified list

# Append a new element to the list
fruits = ["apple", "banana", "cherry"]

fruits.append("kiwi") # Adds "kiwi" to the end of the list
print(fruits)  # Prints the updated list

# Insert a new element at a specific position
fruits.insert(1, "orange")  # Inserts "orange" at index 1
print(fruits)  # Prints the updated list

#Remove an element from the list
fruits.remove("kiwi")  # Removes "kiwi" from the list
print(fruits)  # Prints the updated list

# Sort the list in ascending order
fruits.sort()  # Sorts the list alphabetically
print(fruits)  # Prints the sorted list

# Reverse the order of the list
fruits.sort(reverse=True)  # Sorts the list in reverse order
print(fruits)  # Prints the reversed list