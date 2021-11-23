#!/usr/bin/env python3

# Handling Arguements

import sys # Required to access arguements

# Prints the full path and name of this script.
print(sys.argv[0])

# Prints the 1st argument, but if no arg was supplied then it will error
#print(sys.argv[1])

# A "try" and "except" / exception handling routine to check if a argument was
# supplied, if not it prompts the user on correct usage and quits.
try:
    arg = sys.argv[1]
except IndexError:
    print('Error: No argument was supplied.')
    print('Correct usage is:', sys.argv[0], 'cloudabove.com')
    quit()

print('End of script')