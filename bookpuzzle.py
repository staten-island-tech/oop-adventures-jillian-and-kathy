import time
""" import pygame """
import sys

lettercorrect = []
lettertry = []
word = "debug"
infinite = True
print("Your final puzzle is a Wordle")
while infinite == True:
    enter = input("Enter your 5 letter guess: ")
    if enter == word:
        infinite = False
        print("The word is DEBUG! Congrats!!!")
    elif len(enter) != len(word):
        print("Must be 5 letter word")
    elif len(enter) == len(word):
        lettertry = []
        for letter in range(len(enter)):
            if enter[letter] == word[letter]:
                print(enter[letter], "is correct and in the right spot")
                lettercorrect.append(enter[letter])
            elif enter[letter] in word and enter[letter] not in lettercorrect and enter[letter] not in lettertry:
                lettertry.append(enter[letter])
        for wrong_letter in lettertry:
            print(wrong_letter, "is correct but in the wrong spot")
        for letter in range(len(enter)):
            if enter[letter] is not in word:
                print(enter[letter], "is not in the word")



""" class book():
    def __init__(self, word, )
        self. = 
        self. = 
    def guess(word,) """