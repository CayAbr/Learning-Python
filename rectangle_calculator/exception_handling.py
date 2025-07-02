## File: rectangle_calculator/exception_handling.py
'''
try:        # This is the start of the try block
    print(x)    # This will raise an exception because x is not defined
except:     # This is the start of the except block
    print("Something went wrong") # This will execute if an exception occurs in the try block
finally:    # This block will always execute, regardless of whether an exception occurred or not
    print("The 'try except' is finished.")          # This will always execute
'''
'''
try:
    print(x)
except NameError:
    print("Variable x is not defined.")
else:
    print("Everything went wrong")
    
x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")  # This will raise an exception if x is less than 0
'''


    
    