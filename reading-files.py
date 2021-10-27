
## Reading Files
# The file I'm going to be working with:
my_file_path = '/home/acawley/Documents/Programming/Python/learning-python/file.txt'
# /home/acawley/Documents/python/learning-python/file.txt

## Four Methods:

## 1) This one is for older python and is a bit more cumbersome:
file = open('/home/acawley/Documents/Programming/Python/learning-python/file.txt', 'r')
for line in file:
    print(line)
file.close()

## NOTE: in subsequent example I've going to replace the full path in '' with my path in a variable instead.

## 2) This one puts each line into a list, even blank lines will be stored as items in the list like '\n'
file = open(my_file_path, 'r')
lines =file.readlines()
print(lines)
file.close()


## 3) This prints the text as just a block of text
file = open(my_file_path, 'r')
text = file.read()
print(text)
file.close()

## 4) With this method you do not have to close the file with file.close() because this method
# has in-built clean-up. This is called a "Context Manager"
with open(my_file_path, 'r') as file:
    for line in file:
        print(line)

## Reading X number of bytes uses file.read()
with open(my_file_path, 'r') as file:
    content = file.read(10) # Reads only the first 10 bytes of the file
    print(content)

## Reading X number of lines uses file.readlines()
with open(my_file_path, 'r') as file:
    content = file.readlines(5) # Reads the first 5 lines in the file
    print(content)