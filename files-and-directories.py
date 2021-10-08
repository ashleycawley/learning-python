import os
# Lets say we want to build a full path to a file located at: /home/acawley/git/learning-python/parsed.txt
# There is two methods, one more error prone than the other, firstly:
current_directory = os.getcwd()
path_to_file = (current_directory + '/parsed.txt') # This method is more error prone apparently.

# A better method is to use:
better_path_to_file = os.path.join(current_directory, 'parsed.txt') # This function adds or removes slashes
# for you to make sure the path is correct so should be better.

meta_data = os.stat(current_directory + '/parsed.txt') # os.stat

directory_files = os.listdir()
print("My working directory: ", current_directory)
print("Files: ", directory_files)
print("parsed.txt information: ", meta_data)

os.chdir('mail') # Change directory (goes into a "mail" sub-folder)
print(os.listdir())