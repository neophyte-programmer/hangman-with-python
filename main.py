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

    lives = 7

    while len(wordLetters) > 0 and lives > 0:
        # showing the user the letters they have used
        print(f"You have {lives} lives left. You have used these letters: ", " ".join(usedLetters))

        # showing the user the word but with blanks where they haven't guessed
        wordList = [letter if letter in usedLetters else "_" for letter in word]
        print("Current Word: ", " ".join(wordList))

        userLetter = input("Guess a letter: ").upper()
        if userLetter in alphabet - usedLetters:
            usedLetters.add(userLetter)
            if userLetter in wordLetters:
                wordLetters.remove(userLetter)

            else:
                lives = lives - 1
                print("Sorry, the letter you entered is not in the word.")

        elif userLetter in usedLetters:
            print("You have already guessed this letter! Please try again ")

        else:
            print("Invalid character! Please try again")

    if lives == 0:
        print(f"Oops! You died. The word was {word}")
    else:
        print("Hooray! You guessed the word correctly!")


hangman()
