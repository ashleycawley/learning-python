
# Convert a string to a integer
fav_num = '7' # string var
fav_num = int(fav_num) # Uses the int function to convert str > int
print('The type for the fav_num is ', type(fav_num))

# Convert integer to string
age = 12 # integer var
age_str = str(age) # Converts integer to string
print("The type for age_str is: ", type(age_str))

# Convert integer to floating point
age_float = float(age)
print("age_float: ", age_float)
print("The type for age_float is: ", type(age_float))

# Converting a long float into a integer
mad_float = 4.932893425783
print("mad_float :", mad_float)
print("Integer: ", int(mad_float))

# Round the float to the nearesr whole integer
print("Rounded: ", round(mad_float))

# Boolean
likes_cheese = 'False' # This is a string because it has ''
print('as boolean: ', bool(likes_cheese)) # Will report as true because it contains text
