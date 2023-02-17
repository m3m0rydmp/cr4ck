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

def convert_string(s):
    # Check if the input string is in the hex_dict
    if s in hex_dict:
        # If it is, return the corresponding value from the hex_dict
        return hex_dict[s]
    else:
        # If it is not, check if the input string is a value in the hex_dict
        for key, value in hex_dict.items():
            if value == s:
                # If it is, return the corresponding key from the hex_dict
                return key
        # If the input string is not in the hex_dict at all, check each character in the input string
        for char in s:
            if char not in hex_dict:
                # If any of the characters are not in the hex_dict, return an error message
                return "Error: invalid input - character '{}' is not in the dictionary".format(char)
        # If none of the characters are not in the hex_dict, return an error message
        return "Error: invalid input"

# Prompt the user for input
input_string = input("Enter a string to convert: ")

# Convert the input string and print the result
result = convert_string(input_string)
print(result)
