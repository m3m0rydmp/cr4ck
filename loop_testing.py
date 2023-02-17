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

def convert_string():
    # Prompt the user for input
    input_string = input("Enter a string to convert: ")

    # Check if the input string is in the hex_dict
    if input_string in hex_dict:
        # If it is, return the corresponding value from the hex_dict
        result = hex_dict[input_string]
    else:
        # If it is not, check if the input string is a value in the hex_dict
        for key, value in hex_dict.items():
            if value == input_string:
                # If it is, return the corresponding key from the hex_dict
                result = key
                break
        else:
            # If the input string is not in the hex_dict at all, check each character in the input string
            for char in input_string:
                if char not in hex_dict:
                    # If any of the characters are not in the hex_dict, return an error message
                    result = "Error: invalid input - character '{}' is not in the dictionary".format(char)
                    break
            else:
                # If none of the characters are not in the hex_dict, return an error message
                result = "Error: invalid input"

    # Print the result
    print(result)

convert_string()
