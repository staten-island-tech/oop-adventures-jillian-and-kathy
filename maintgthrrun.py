import time
import pygame
import sys
from Escape_room3 import EscapeRoom3
from Escape_room3 import bookpuzzle




class User:
    def __init__(self, keys):
        self.keys = keys
        self.storage = []

    def add_storage(self, key):
        self.storage.append(key)
        print(f"You have gained 1 {key}")
    
    def clear_storage(self):
        self.storage = []
        print(f"Your {self.keys} storage was cleared")

    def show_storage(self):
        print(f"This is your {self.keys} inventory: {self.storage}")

inventory = User("Escape Keys")

inventory.add_storage("Room 1 Key")

inventory.add_storage("Room 2 Key")

inventory.add_storage("Room 3 Key")

inventory.show_storage()

inventory.clear_storage()

inventory.show_storage()