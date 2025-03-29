import time
import os
def root():

# Loop through 9 colors
 for a in range(5):
  for i in range(2):    
     os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
     print(f"  \033[1;3{i}m               __            __                      ")
     print(f"                |  \          |  \                     ")
     print(f"   __   __   __  \$$ _______  | $$  ______    ______   ")
     print(f"  |  \ |  \ |  \|  \|       \ | $$ /      \  /      \  ")
     print(f"  | $$ | $$ | $$| $$| $$$$$$$\| $$|  $$$$$$\|  $$$$$$\ ")
     print(f"  | $$ | $$ | $$| $$| $$  | $$| $$| $$    $$| $$   \$$ ")
     print(f"  | $$_/ $$_/ $$| $$| $$  | $$| $$| $$$$$$$$| $$        ")
     print(f"   \$$   $$   $$| $$| $$  | $$| $$ \$$     \| $$        ")
     print(f"    \$$$$$\$$$$  \$$ \$$   \$$ \$$  \$$$$$$$ \$$        ")
     print("")
     print(f"                    \033[1;37mVersion:[0.0.2]")
     print("")
     print("                    DEV:[n0nex03]")
     time.sleep(0.5)  # Delay between color changes
