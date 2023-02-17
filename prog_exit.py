import os

def prog_exit():
    os.system('cls')
    print('This will exit the program, are you sure you want to exit?')
    choice = input('(Y/N): ')
    
    if choice == 'y' or choice == 'Y':
        return exit
    else:
        print("Invalid choice. Please try again.")
        return prog_exit()
    
prog_exit()

