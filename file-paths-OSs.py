# File Paths on different OS's

# Python provides a tool to help build file paths (converting the slashes) to be correct on either Windows or UNIX
# That tool is: os.path.join()

import os
folder_path = os.path.join("home", "acawley", "Documents", "Python")
print(folder_path)  # This will output the following:
                    # On Linux: home/acawley/Documents/Python
                    # On Windows: home\acawley\Documents\Python
                    # NOTE: The path is not absolute, it is relative, there is no leading C:\ or /
## If you wish to add a learing C:\ or / then you can use the os.sep inside of the os.path.join:
folder_path = os.path.join(os.sep, "home", "acawley", "Documents", "Python")
print(folder_path)