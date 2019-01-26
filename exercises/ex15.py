# reads sys package and imports argv module
from sys import argv

# sets argv input into respective variables
script, filename = argv

# opens text file and assigns to variable
txt = open(filename)

# prints the name of file
print(f"Here's your file {filename}:")
# prints the contents of the file
print(txt.read())
txt.close()

# asks user to type filename
print("Type the filename again:")
# sets name of file to variable

file_again = input("> ")

# opens file and sets contents to variable
txt_again = open(file_again)

# prints contents of variable
print(txt_again.read())
txt_again.close()
