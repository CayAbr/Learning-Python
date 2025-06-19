#strings

message = """Bob's World
is cool"""

print(message)

#Advanced string formatting
#Indexing

message = ' Hello, World! '

print(message[0]) # First character
print(message[1]) # Second character

print(message[-1]) # Last character

print(len(message)) # Lenght of the string 

print(message.strip())  # Removes leading and trailing whitespaces
print(message.lower()) # Converts all characters to lowercase
print(message.split()) # Splits the string into a list of words
print(message.upper()) # Converts all characters to uppercase
print(message.replace('World', 'Coders')) # Replace a substring with another substring 