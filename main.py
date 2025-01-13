<<<<<<< HEAD
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
=======
import os

# Target directory
target_dir = 'C:\Users\jillian.weingarten24\Documents\GitHub\oop-adventures-jillian-and-kathy\Room_one\EscapeRoom.py'

# Dictionary of directories to iterate over
directories = {
    'Room_one': 'EscapeRoom.py',
    'Room_two': 'app.py',
    'Escape Room #3': 'EscapeRoom3.py'
}

for directory, python_file in directories.items():
    # Construct the full path to the directory
    path = os.path.join(os.getcwd(), target_dir, directory)
    
    # Check if the path is a valid directory
    if os.path.exists(path) and os.path.isdir(path):
        print(f"Processing {directory}")
        
        # Get the list of Python files in the directory
        python_files = [f for f in os.listdir(path) if f.endswith('.py')]
        
        # Check if the python file we're looking for exists in the directory
        if python_file not in python_files:
            print(f"{directory}: No {python_file} found in the directory")
            continue
        
        # Get the full path to the Python file
        python_file_path = os.path.join(path, python_file)
        
        # Run the Python file
        print(f"Running {python_file_path}")
        os.system(f"python {python_file_path}")
    else:
        print(f"{directory} is not a valid directory")
>>>>>>> 25d6adfaa75e584c5bedba12eb7786bfdcf6f206
