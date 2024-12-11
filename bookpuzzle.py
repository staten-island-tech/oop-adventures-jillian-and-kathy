import time
""" import pygame """
import sys

word = "debug"
infinite = True
print("Your final puzzle is a Wordle")
while infinite == True:
    enter = input("Enter your 5 letter guess: ")
    if enter == word:
        infinite = False
        print("The word is DEBUG! Congrats!!!")


""" class book():
    def __init__(self, word, )
        self. = 
        self. = 
    def guess(word,) """