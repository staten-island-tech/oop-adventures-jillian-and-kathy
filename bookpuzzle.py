import time
""" import pygame """
import sys

class WordleGame:
    def __init__(self, word, hint):
        self.word = word
        self.hint = hint
        self.guess_history = []
        self.infinite = True
        self.double = []

    def make_guess(self, enter):
        self.guess_history.append(enter)
        print("Your guesses: ", self.guess_history)

        if enter == self.word:
            self.infinite = False
            print("The word is", self.word.upper() + "! Congrats!!!")
        elif len(enter) != len(self.word):
            print("Must be a 5-letter word")
        else:
            for letter in range(len(enter)):
                if enter[letter] == self.word[letter]:
                    print(enter[letter], "is correct and in the right spot.")
                    self.double.append(enter[letter])
                elif enter[letter] in self.word and enter[letter] not in self.double:
                    print(enter[letter], "is either not in the word or is in the wrong spot. Figure it out!")
                    self.double.append(enter[letter])
                elif enter[letter] not in self.word or enter[letter] in self.double:
                    print(enter[letter], "is either not in the word or is in the wrong spot. Figure it out!")

    def display_hint(self):
        print("Here is a hint:", self.hint)

    def play_game(self):
        print("Your final puzzle is a Wordle")
        self.display_hint()

        while self.infinite:
            enter = input("Enter your 5 letter guess: ")
            self.make_guess(enter)

game = WordleGame(word="debug", hint="Related to fixing code")
game.play_game()


""" word = "debug"
guesshistory = []
infinite = True
print("Your final puzzle is a Wordle")
print("Here is a hint:", "Related to fixing code")
while infinite == True:
    enter = input("Enter your 5 letter guess: ")
    guesshistory.append(enter)
    double = []
    print("Your guesses: ", guesshistory)
    if enter == word:
        infinite = False
        print("The word is DEBUG! Congrats!!!")
    elif len(enter) != len(word):
        print("Must be 5 letter word")
    elif len(enter) == len(word):
        for letter in range(len(enter)):
            if enter[letter] == word[letter]:
                print(enter[letter], "is correct and in the right spot.")
                double.append(enter[letter])
            elif enter[letter] in word and enter[letter] not in double:
                print(enter[letter], "is either not in the word or is in the wrong spot. Figure it out!")
                double.append(enter[letter])
            elif enter[letter] not in word or enter[letter] in double:
                print(enter[letter], "is either not in the word or is in the wrong spot. Figure it out!") """