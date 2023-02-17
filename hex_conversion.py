import os

def hex_conversion():
    os.system('cls')
    print('''
Enter the integers of the PLDT WiFi located in your WiFi SSID.

example: PLDTWIFI12345

only input the integer.\n
          ''')
    
    hex_dict = {
        "0" : "f",
        "1" : "e",
        "2" : "d",
        "3" : "c",
        "4" : "b",
        "5" : "a",
        "6" : "9",
        "7" : "8",
    }
    
    ssid = input("Enter the integer from your WiFi SSID: ")
    
    passKey = []
    invalid_character = []
    for char in ssid:
        passKey.append(hex_dict[char])
        
        if passKey != hex_dict:
            invalid_character.append(passKey)
    
            
    
    if invalid_character:
        return "Invalid input: character '{}'".format(", ".join(invalid_character))    
        
    return passKey


print(hex_conversion())