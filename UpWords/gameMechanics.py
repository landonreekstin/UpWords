from functools import reduce
import math
import random


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
letters = {"A": 7, "B": 3, "C": 4, "D": 5, "E": 8, "F": 3, "G": 3, "H": 3, "I": 7, "J": 1, "K": 2, "L": 5, "M": 5, 
"N": 5, "O": 7, "P": 3, "Qu": 1, "R": 5, "S": 6, "T": 5, "U": 5, "V": 1, "W": 2, "X": 1, "Y": 2, "Z": 1}

# returns true if the word played is valid and false otherwise
def isValid(listOfLetters):
    word = reduce(lambda x, y: x + y, listOfLetters)
    word = word.lower()
    return word in dictionary

# add regex or similar for proper noun checking

# calculates the score of a word once its played and returns it as an integer
def score(listOfLetters):
    total = 0
    if len(listOfLetters) == 7:
        total += 20
    for letter in listOfLetters:
       total +=  letter.square.height + 2
    return total
    # need to add intersections of words

# gets new
def getNewLetter(dic):
    index = weightedPick(dic)
    

def weightedPick(dic):
    r = random.uniform(0, sum(dic.itervalues()))
    s = 0.0
    for k, w in dic.iteritems():
        s += w
        if r < s: return k
    return k

