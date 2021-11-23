#!/usr/bin/env python3

# When you ask to import a module the Python interpreter will check in a few places:
# 1) the current working directory, so if you started python3 in a directory that contained: mod.py
#    And you ran: import mod it would import it in.
# 2) Other paths that are checked can by seen by using:
import sys
print(sys.path)

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