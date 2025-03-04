import time
import os
def root():

# Loop through 9 colors
 for a in range(3):
  for i in range(2):    
     os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
     print(f"  \033[1;3{i}m                          ⣼⣿⢿⣿⣟⣿⣿⣻⣿⣟⡿⠿⢯⡿⠿⢿⣽⣿⣿⣻⣿⢿⣻⣿⣿⣧           ")
     print(f"                            ⡿⣿⣿⣿⣻⣿⠿⠛⠉⠀⠀⢀⣴⣷⣀⠀⠀⠉⠛⠿⣿⣿⣿⣿⣻⣿                 ")
     print(f"                            ⣿⣿⣿⣽⠟⠁⠀⠀⠀⢀⣴⣿⣿⣿⠟⠁⠀⡀⠀⠀⠈⠻⣿⣽⣿⡿                 ")
     print(f"                            ⡿⣷⣿⠃⠀⠀⠀⢀⣴⣿⣿⣿⠟⠁⠀⠀⣠⣷⣄⠀⠀⠀⠘⣿⣿⣿                 ")
     print(f"                            ⣿⣿⠃⠀⡀⠀⠘⢿⣿⣿⣿⣅⠀⠀⣠⣾⣿⣿⣿⣷⣄⠀⠀⠘⣿⣷    ▒▒▒╔╗▒▒▒▒▒▒▒▒▒")
     print(f"                            ⣽⡟⠀⢠⣧⡀⠀⠀⠙⢿⣿⣿⣷⣾⣿⣿⡿⠻⣿⣿⣿⣷⣄⠀⢹⣿    ╔╦╦╬╬═╦╦╗╔═╦╦╗")
     print(f"                            ⣿⡇⠰⣿⣿⣿⣦⡀⠀⠀⣹⣿⣿⣿⣿⣏⠀⠀⠈⠻⣿⣿⣿⡗⢸⣿    ║║║║║║║║╚╣╩╣╔╝")
     print(f"                            ⣾⣧⠀⠈⢻⣿⣿⣿⣦⣾⣿⣿⡿⢿⣿⣿⣷⣄⠀⠀⠈⠻⠃⠀⣸⣿    ╚══╩╩╩═╩═╩═╩╝▒")
     print(f"                            ⡿⣿⡄⠀⠀⠈⢻⣿⣿⣿⡿⠋⠀⠀⢙⣿⣿⣿⣷⡄⠀⠀⠀⢠⣿⣿                  ")
     print(f"                            ⣿⣿⣿⡄⠀⠀⠀⠈⠿⠋⠀⠀⢀⣴⣿⣿⣿⠿⠃⠀⠀⠀⢠⣿⣿⣿                  ")
     print(f"                            ⣿⣾⣿⣿⣦⡀⠀⠀⠀⠀⠀⣴⣿⣿⣿⡟⠋⠀⠀⠀⢀⣴⣿⣿⣿⡿                  ")
     print(f"                            ⣿⣿⣷⣿⣿⣿⣷⣤⣀⠀⠀⠈⠻⡟⠋⠀⠀⣀⣤⣾⣿⣿⣿⣿⡿⣿                  ")
     print(f"                            ⣿⢿⣻⣿⣯⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣻⣷⣿⣿                  ")
     print("")
     print(f"                                 \033[1;37mVersion:[0.0.1]")
     print("")
     print("                                  DEV:[lose_sec]")
     time.sleep(0.5)  # Delay between color changes
