# Reading from one file and writing to another
with open('file2.txt', 'r') as source_file, open('new_file.txt', 'w') as destination_file:
    content = source_file.readlines()
    destination_file.writelines(content)