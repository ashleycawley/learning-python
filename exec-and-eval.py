# exec (execute) and eval (evaluate) are dangerous as used wrong they can be leveraged to run
# code provided by the user (if you're taking input from them etc.)

# Example:

import os # Just pretending this was imported for other reasons higher up in the script
math = input('Do some math:')
print(eval(math))

# The user could then provide input / commands like the following:
# os.system('ls')
# os.system('rm -f file.txt')
#
# To mitigate against this, the scope of what eval can access can be limited with:
print(eval(math, {}))
# The {} limits its access and prevents it from using functions from other imports