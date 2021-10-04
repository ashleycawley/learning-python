
## Reading Files
# The file I'm going to be working with:
# /home/acawley/Documents/python/learning-python/file.txt

## Four Methods:

# This one is for older python and is a bit more cumbersome:
file = open('/home/acawley/Documents/python/learning-python/file.txt', 'r')
for line in file:
    print(line)
file.close()


# This one puts each line into a list, even blank lines will be stored as items in the list like '\n'
file = open('/home/acawley/Documents/python/learning-python/file.txt', 'r')
lines =file.readlines()
print(lines)
file.close()


# This prints the text as just a block of text
file = open('/home/acawley/Documents/python/learning-python/file.txt', 'r')
text = file.read()
print(text)
file.close()

# With this method you do not have to close the file with file.close() because this method
# has in-built clean-up. This is called a "Context Manager"
with open('/home/acawley/Documents/python/learning-python/file.txt', 'r') as file:
    for line in file:
        print(line)
