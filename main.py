import os

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
    
    # Check if the file exists
    if os.path.isfile(file_path):
        print(f"Running {file_path}")
        os.system(f"python {file_path}")
    else:
        print(f"{file_path} does not exist")