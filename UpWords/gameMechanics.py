from functools import reduce


##################
### Dictionary ###
##################
wordsFile = open("words.txt", "r")
dictionary = []
for line in wordsFile:
    stripped_line = line.strip()
    lowercaseWord = stripped_line.lower()
    dictionary.append(lowercaseWord)
wordsFile.close()

###############
### Letters ###
###############
letters = ["J", "Qu", "V", "X", "Z", "K", "W", "Y", "K", "W", "Y", "B", "F", "G", "H", "P", "B", "F", "G", "H", "P", 
"B", "F", "G", "H", "P", "C", "C", "C", "C", "D", "L", "M", "N", "R", "T", "U", "D", "L", "M", "N", "R", "T", "U", 
"D", "L", "M", "N", "R", "T", "U", "D", "L", "M", "N", "R", "T", "U", "D", "L", "M", "N", "R", "T", "U", "S", "S", 
"S", "S", "S", "S", "A", "I", "O", "A", "I", "O", "A", "I", "O", "A", "I", "O", "A", "I", "O", "A", "I", "O", "A", 
"I", "O", "E", "E", "E", "E", "E", "E", "E", "E"]


# returns true if the word played is valid and false otherwise
def isValid(listOfLetters):
    word = reduce(lambda x, y: x + y, listOfLetters)
    word = word.lower()
    return word in dictionary

# calculates the score of a word once its played and returns it as an integer
def score(word):
    return 0




