# Slicing Lists

letters = list('abcdefghijklmnop')

print(letters)

# How do I get the letters 'c' through 'f'?
selected = letters[2:6] # NOTE: It shows the begining number 2 which represents
# 'c' in this case, so the first number in the range is "inclusive" *BUT* the
# last number "6" it does NOT show, so you actually have to set the ending number
# one higher than is naturally intuative.

print('Selected: ', selected)

# How do I get every other letter from the list?
every_other = letters[0:len(letters):2]
# RECAP on declaring the range [0:len(letters):2]
# The first part declares the START, then the STOP, then the STEP.
# [0:len(letters):2] === Start:Stop:Step
print('Every Other: ', every_other)

# Worth noting with: [0:len(letters):2] the 0 value is implied so can be left
# out if you want, so is the lenth in the middle, so:
# [0:len(letters):2]
# Can become:
# [::2]
# And it still does the same job:
every_other2 = letters[::2]
print('Every Other: ', every_other2)
# That approach is only suitable really if you want to start at the begining
# of the list and finish at the end.

# Reverse with Slicing
reverse_letters = letters[::-1]
print('Reversed Letters: ', reverse_letters)

# Every other one reversed would be: letters[::-2]
