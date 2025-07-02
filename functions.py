'''
def greet(name):
    print(f"Hello, {name}")
    
greet("Alice") # This function takes a name as input and prints a greeting message.

def add(a, b):
    return a + b # This function takes two numbers and returns their sum.

result = add(2,5)
print(result) # This prints the result of the addition.
'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1) # This function calculates the factorial of a number recursively.

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}") # This function greets a person with a customizable greeting.

greet("Bob", "Good Morning") # This calls the greet function with the name "Bob".

