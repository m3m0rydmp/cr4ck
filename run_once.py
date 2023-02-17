import os


def hex_conversion():
    os.system('cls')
    print('''
    Enter the integers of the PLDT WiFi located in your WiFi SSID.

    example: PLDTWIFI12345

    only input the integer.\n
    
    Refer to the Dictionary for conversion.
    
    0 : f,
    1 : e,
    2 : d,
    3 : c,
    4 : b,
    5 : a,
    6 : 9,
    7 : 8,
    8 : 7,
    9 : 6,
    a : 5,
    b : 4,
    c : 3,
    d : 2,
    e : 1,
    f : 0,
    
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
    "8" : "7",
    "9" : "6",
    "a" : "5",
    "b" : "4",
    "c" : "3",
    "d" : "2",
    "e" : "1",
    "f" : "0",
    }
    
    ssid = input("Enter the integer from your WiFi SSID: ")
    
    if ssid in hex_dict:
        result = hex_dict[ssid]
        
    else:
        
        for key, value in hex_dict.items():
            if value == ssid:
                result = key
                break
            
            else:
                for char in ssid:
                    if char not in hex_dict:
                        result = "Error: Invalid input - character '{}' is not in the dictionary".format(char)
                        break
                else:
                    result = "Error: Invalid input."
    
    print("PLDT WiFi Password is: ", result)
    
hex_conversion()