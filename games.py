import os
import random
import subprocess
import shutil
import sys
import logo
import guess

# Display logo (Make sure you have a 'logo' module with the 'root()' function)
logo.root()

os.system('cls' if os.name == 'nt' else 'clear')


def main():
    print("[1] Guess the number game (Windows version) and create .exe")
    print("[2] Encrypt files (WIP)")
    print("")

    x = input("Please select your option: ")

    if x == "1":
        guess.create_exe()
        guess.one_option()
    elif x == "2":
        print("File encryption feature is under development.")
    else:
        print("Invalid option. Please try again.")


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


