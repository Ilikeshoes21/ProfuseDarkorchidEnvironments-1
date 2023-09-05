# String Practice:

# Create a Python program that asks the user to input a sentence.
sentence = input("Write a sentence")
print(f'{sentence}')
# Print the first and last letter of the sentence.
print(sentence[0:1])
print(sentence[-1])
# Convert the entire sentence to uppercase and print the result.
print(sentence.upper())
# Find and print a substring from the inputted sentence.
print(sentence[3:7])
# Replace a word in the sentence and print the updated sentence.
print(sentence.replace("a","i"))


# Input Practice:

# Create a Python program that asks the user for their name, age, and favorite movie.
Name = input("What is your name?")
Age = input("What is your age?")
Movie = input("What is your favorite movie?")
# Print a message back to the user with this information.
print(f'Your name is {Name}. You are {Age} years old and your favorite movie is {Movie}.')
# Note: Make sure to convert the age to an integer.


# F-String Practice:

# Create a Python program that asks the user for three objects in the room.
object1 = input("Name one object in the room")
object2 = input("Now name another")
object3 = input("One more")
# Create variables from these objects and insert those variables into an f-string sentence.
print(f'{Name} sees a {object1}, a {object2}, and a {object3}')
# Print the f-string sentence.

# Advanced String Practice:

# Create a Python program that reverses the words in a sentence inputted by the user.
# For example, if the user inputs "Python is fun", the program should print "fun is Python"
# To reverse words in a given string 
# input string
string = f'{sentence}'
# reversing words in a given string
s = string.split()[::-1]
l = []
for i in s:
    # appending reversed words to l
    l.append(i)
# printing reverse words
print(" ".join(l))
# Advanced Input Practice:

# Create a Python program that asks the user for the name of their favorite book, movie, and song.

# Print a message that says, "Your favorite book is [Book], your favorite movie is [Movie], and your favorite song is [Song]."


# Advanced F-String Practice:

# Create a Python program that asks the user for their name, age, and the current year.
# Use f-strings to print a message like: "Hello [Your Name], you were born in [Current Year - Your Age]."

# Type Conversion Practice:

# Create a Python program that asks the user for two numbers.
# Print the sum, difference, product, and quotient of the two numbers.
# Note: Make sure to convert the input to integers before performing any calculations.

# Summary Challenge:

# Find a summary of a movie online and create a variable called movie_summary and store the summary in this variable.
# Print the length of the summary.
# Uppercase the entire summary and print it.
# Replace a word in the summary and print the updated summary.
# Print the last word of the summary.


# Real Challenge:

# Create a Python program that asks the user for their first and last name, their age, and their favorite color.
# Using f-strings, print a message that says, "Hello [First Name] [Last Name], you are [Age] years old and your favorite color is [Favorite Color]."