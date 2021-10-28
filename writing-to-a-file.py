# Writing to a file

## Four methods or modes when opening a file:
# r - read
# w - write
# a - append
# rb - read binary file (.gif, .exe etc.)

# NOTE: You have to be careful when opening files for writing in Python, even if you do
# nothing with the file like this example below it will effectively ERASE the contents:

with open('file2.txt', 'w') as file:
    print('not doing anything')

with open('file2.txt', 'w') as file:
    content = 'This will be my first line.\n'
    file.write(content)

    more_content = 'This will be my second line.\n'
    file.write(more_content)


## file.writelines() - For writing multiple lines in one go:
with open('file2.txt', 'w') as file:
    content = ['line one\n', 'line two\n', 'line three\n']
    file.writelines(content)

## Appending to the end of a file is done with the 'a' mode:
with open('file2.txt', 'a') as file:
    content = ['line one\n', 'line two\n', 'line three\n']
    file.writelines(content)