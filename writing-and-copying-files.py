
## Writing and Copying Files
# The file I'm going to be working with:
# /home/acawley/Documents/python/learning-python/file.txt

## Writing a File

# NOTE: 'w' stands for write and it blanks the file when starting
output_filename = 'output.txt'
with open(output_filename, 'w') as file:
    file.write('hello world \n')

# Append
with open(output_filename, 'a') as file:
    file.write('hello world \n')
# 'a' makes it append to the end of the file.

# Copying a file

with open('data.txt', 'r') as input_file:
    with open(output_filename, 'w') as output:
        for line in input_file:
            output.write(line)
            
# The same statement can also be written as:
with open('data.txt', 'r') as input_file, open(output_filename, 'w') as output:
        for line in input_file:
            output.write(line)

# Parsing and removing a line from a file when copying, so this looks at a hw.txt file which has:
# hello
# new
# world
# And it outputs a new file called parsed.txt without the middle "new" line:
with open('hw.txt', 'r') as input_file, open('parsed.txt', 'w') as output:
        for line in input_file:
            if line != 'new\n':
                output.write(line)

with open('txt/one.txt', 'r') as input_file, open('txt/three.txt', 'w') as output:
        for line in input_file:
            if line != 'new\n':
                output.write(line)

# Just my own little side-quest: I wanted to set myself the challenge of parsing ALL files within
# a sub-directory, copying those files to new files BUT parsing-out any lines that just said "new"
import os
my_path = '/home/acawley/Documents/python/learning-python/txt/'
file_list = os.listdir(my_path)
print(file_list)

for file in file_list:
   with open(my_path+file, 'r') as input_file, open(my_path+file+file, 'w') as output:
       for line in input_file:
           if line != 'new\n':
               output.write(line)
