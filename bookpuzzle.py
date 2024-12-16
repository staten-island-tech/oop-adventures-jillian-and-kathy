import time
""" import pygame """
import sys


word = "debug"
infinite = True
print("Your final puzzle is a Wordle")
while infinite == True:
    enter = input("Enter your 5 letter guess: ")
    double = []
    if enter == word:
        infinite = False
        print("The word is DEBUG! Congrats!!!")
    elif len(enter) != len(word):
        print("Must be 5 letter word")
    elif len(enter) == len(word):
        for letter in range(len(enter)):
            if enter[letter] == word[letter]:
                print(enter[letter], "is correct and in the right spot")
            elif enter[letter] in word and enter[letter] not in double:
                print(enter[letter], "is correct but in the wrong spot")
                double.append(enter[letter])
            elif enter[letter] not in word:
                print(enter[letter], "is not in the word")






""" class book():
    def __init__(self, word, )
        self. = 
        self. = 
    def guess(word,) """