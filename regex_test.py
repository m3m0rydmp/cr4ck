import re

#Define a string to SEARCH
string = "The quick brown fox jumps over the lazy dog"

#Define a regular expression to search for the word "fox"
pattern = "fox"

#Use the 'search' function to search for the pattern in the string
match = re.search(pattern, string)
#(pattern, string) defines the word "fox" to look in the var string

#If a match is found, print the match
if match:
    print(match.group())