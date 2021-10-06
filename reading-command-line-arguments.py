
## Reading Command Line Arguements

# This program is designed to take arguements written like:
#                python3 reading-command-line-arguments.py apple 9 1.20

import sys
import json

filename = sys.argv[0]
arguements = sys.argv[1:]

food = arguements[0]
quantity = int(arguements[1])
cost = float(arguements[2])

total = quantity * cost
print("You are buying {} {} for £{}".format(food,quantity,total))

json.loads