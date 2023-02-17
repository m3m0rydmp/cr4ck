# Define the mapping between input and output characters
mapping = {
    "f": "0",
    "1": "e",
    "2": "d",
    # Add more entries for other input characters
}

# Get the user input
user_input = input("Enter a string: ")

# Convert each character in the input string to the corresponding output character
output = ""
for char in user_input:
    mapped_char = mapping.get(char)
    if mapped_char is not None:
        output += mapped_char
    else:
        output += char

# Print the output string
print(output)
