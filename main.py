import os

# List of Python files to run
python_files = [
    'EscapeRoom.py',
    'app.py',
    'EscapeRoom3.py'
]

# Class definition for User
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

inventory.clear_storage()


current_directory = os.getcwd()

# Iterate over the list of Python files
for python_file in python_files:
    # Construct the full path to the Python file
    file_path = os.path.join(current_directory, python_file)
    
    # Check if the file exists
    if os.path.isfile(file_path):
        print(f"Running {file_path}")
        # Execute the Python file
        os.system(f"python \"{file_path}\"")
        inventory.add_storage("Key")
        inventory.show_storage()
    else:
        print(f"{file_path} does not exist")


