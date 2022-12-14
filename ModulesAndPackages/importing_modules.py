#!/usr/bin/env python3

# NOTE: dir() - Shows you what modules or objects are currently imported into the current "name space" or "symbol table"
dir()

# When you ask to import a module the Python interpreter will check in a few places:
# 1) the current working directory, so if you started python3 in a directory that contained: mod.py
#    And you ran: import mod it would import it in. Note: you didn't have to specify the .py file extention.
# 2) Other paths that are checked can by seen by using:
import sys
print(sys.path)

# Multiple modules can be imported on one line like:
import abc, ast, base64

# To see the available objects/modules *within* a module like base64 you can run:
dir(base64)

# Lets add a new path to the existing sys.path which are checked, we do this by appending a path with:
sys.path.append(r'/home/acawley/Documents/Python/learning-python/ModulesAndPackages/new_path') # The 'r' stands for raw path

import new # This module lives within the path which was recently brought in above
print(new.more_data) # Pulls data from that 'new' imported moduled from the new path

# Checking where a module is being loaded from: new.__file__
print(new.__file__)

# Importing things into current Namespace:
# if mod.py contained friend_list and we did a: import mod, when we called it we would need to:
# print(mod.friend_list)
# But we can drop the mod. if we:
from mod import friend_list
print(friend_list)

# Conflicting names - if something you want to import has a conflicting name that clashes with something in your code
# you can rename it when you import it:
from mod import friend_list as friends
print(friends)

# Import a module but give it a different name:
import base64 as b64

# Checking what modules or objects are now imported into the current name space / symbol table before we leave.
dir()