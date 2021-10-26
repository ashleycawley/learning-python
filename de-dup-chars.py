# This script is designed to take a list of words or passwords and reduces them down to a unique character set.
input_filename = 'char-dict.txt'
output_filename = 'unique-characters.txt'

with open(input_filename, 'r') as file:
    char_list = list(file.read()) # Converts string into a list.
    char_list = set(char_list) # Reduces the list to unique characters only.
    char_list = sorted(char_list) # Sorts alphabetically, may be unnessasary but pretty.
    char_list.remove('\n') # Removes \n new line.

print('There are', len(char_list), 'unique characters which are being written to', output_filename)

for char in char_list:
    with open(output_filename, 'a') as file:
        file.write(char) # If you want all chars next to each other on one line
        # file.write(char + '\n') # If you want each char on its own line (vertical list)