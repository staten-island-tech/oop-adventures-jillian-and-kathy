import os

<<<<<<< HEAD
# List of Python files to run
python_files = [
    'EscapeRoom.py',
    'app.py',
    'EscapeRoom3.py'
]

# Iterate over the list and run each file
for file in python_files:
    # Construct the absolute path to the Python file
    file_path = os.path.join(os.getcwd(), file)
=======
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

# Target directory
target_dir = 'C:\Users\jillian.weingarten24\Documents\GitHub\oop-adventures-jillian-and-kathy\Room_one\EscapeRoom.py'

# Dictionary of directories to iterate over
directories = {
    'EscapeRoom.py',
    'app.py',
    'EscapeRoom3.py'
}

for directory, python_file in directories.items():
    # Construct the full path to the directory
    path = os.path.join(os.getcwd(), target_dir, directory)
>>>>>>> f3c83b75e17e21a3e458241c975afaf52041a289
    
    # Check if the file exists
    if os.path.isfile(file_path):
        print(f"Running {file_path}")
        os.system(f"python {file_path}")
    else:
<<<<<<< HEAD
        print(f"{file_path} does not exist")
=======
        print(f"{directory} is not a valid directory")
>>>>>>> f3c83b75e17e21a3e458241c975afaf52041a289
