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