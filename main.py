import random
from words import words
import string


def getValidWord(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = getValidWord(words)
    wordLetters = set(word) # the letters in the word
    alphabet = set(string.ascii_uppercase)
    usedLetters = set() # letters that the user has guessed

    while len(wordLetters) > 0:
        # showing the user the letters they have used
        print("You have used these letters: ", " ".join(usedLetters))

        # showing the user the word but with blanks where they haven't guessed
        wordList = [letter if letter in usedLetters else "_" for letter in word]
        print("Current Word: ", " ".join(wordList))

        userLetter = input("Guess a letter: ").upper()
        if userLetter in alphabet - usedLetters:
            usedLetters.add(userLetter)
            if userLetter in wordLetters:
                wordLetters.remove(userLetter)

        elif userLetter in usedLetters:
            print("You have already guessed this letter! Please try again ")

        else:
            print("Invalid character! Please try again")


hangman()