letter = input("Guess a letter")
word = ["craftsmanship"]
blanks = ["____________"]
guesses = 0
# Converts the word to lowercase
letter = letter.lower()
if(letter.isalpha() == False):
	print("That's not a letter!")

if(letter.isalpha() == True):
	print("Correct")

if(letter in word):
	print("It's right")
# Checks if only letters are present


# Some useful variables
guesses = []
maxfails = 7

guess = input("Guess a letter: ")
