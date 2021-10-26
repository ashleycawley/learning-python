# Input and Output

### Manipulting Print Output
# Print has a "end" value which defaults to "\n" but it can be changed:
# Lets say we want to displays 100 lines horizontally, not veritcally:
for i in range(100):
    print(i, end=' ') # Changes \n to just a space instead.

# A basic way of writing to a file BUT a better way of doing this exists
# that uses a "Context Manager", but still this is one way:
file = open('test-test.txt', 'w') # Creates "file" object, specifies its name and read (r) or write (w) mode.
file.write('Hello World!\n') # Writes data to the file
file.close() # Important to close the file afterwards.

file = open('test-test.txt', 'r') # Opens the file in read mode
print(file.readlines()) # reads all lines / words into a list.
file.close()