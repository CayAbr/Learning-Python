#Numeric Data

num = 3

print(3)
print(type(num)) # Prints the type of the variable num

num2 = 3.14

print(num2)

print(type(num2)) # Prints the type of the variable num2

# Variables
my_variable = 10
total_count = 0
user = 'John'

#Invalid variable names
second_variable = 10 # Invalid, cannot start with a number # Valid, starts with a letter

user_name = 'Andre' # Invalid, cannot contain special characters like '/' # Valid, uses underscore instead of special character

#Operators
# Arithmetic Operators
# Arithmetic operators are used to perform mathematical operations on numeric values.
# Addition (+)
# Subtraction (-)
# Multiplication (*)
# Division (/)
# Modulus (%) # Returns the remainder of a division operation
# Exponentiation (**)

x = 10
y = 2

print(x + y) # Addition
print(x - y) # Subtraction
print(x * y) # Multiplication
print(x / y) # Division
print(x % y) # Modulus
print(5 % 2) # Modulus operation, returns the remainder of 5 divided by 2
print(x ** y) # Exponentiation, raises x to the power of y

#Assignment Operators
x = 10

x = x + 2 # Equivalent to x += 2
x -= 2 # Equivalent to x = x - 2

print(x) # Prints the value of x after the operations

#Operators with Strings
# Concatenation (+)

str1 = 'Hello'
str2 = 'World'

print(str1 + ' ' + str2 + ' ' + str2) # Concatenates str1 and str2 with a space in between

print(str1 * 3) # Repeats str1 three times

#Control Statements

num = -5

if num > 0:
    print("This number is positive")
    
elif num == 0:
    print("This number is zero") 

else:
    print("This number is negative")
    
# Input values 

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : ")) 

if num1 > num2:
    print(num1, "is greater than", num2)
elif num2 > num1:
    print(num2, "is greater than", num1)
else:
    print("Both numbers are equal")
    
#Loops
# For Loop

fruits = ['apple', 'banana', 'cherry']

for fruit in fruits:
    print(fruit) # Prints each fruit in the list
    
numbers = [1, 2, 5, 7]
    

for number in numbers:
    print(number) # Prints each number in the list 
    
# Using While Loop to count from 1 to 5

count = 1

while count <= 5:
    print(count) # Prints the value of count
    count +=1 # Increments count by 1 in each iteration
    
#Loop Control Statements

# Break Statement

fruits = ["apple", "banana", "cherry", "date"]

for fruit in fruits:
    if fruit == "cherry":
        break # Exits the loop when fruit is "cherry"
    print(fruit) # Prints each fruit until "cherry" is encountered

#Continue Statement
fruits = ["apple", "banana", "cherry", "date"]

print()

for fruit in fruits:
    if fruit == "cherry":
        continue # Skips the rest of the loop when fruit is "cherry"
    print(fruit) # Prints each fruit except "cherry"
    
# Pass Statement
fruits = ["apple", "banana", "cherry", "date"]

print()

for fruit in fruits:
    if fruit == "cherry":
        pass # Does nothing when fruit is "cherry"
    print(fruit) # Prints each fruit, including "cherry" since pass does nothing

# While Loop with Break and Continue

count = 0

while count < 5:
    print(count) # Prints the value of count
    count += 1 # Increments count by 1
    if count == 3:
        break # Exits the loop when count is reached - 3
