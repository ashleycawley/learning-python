# Using Tripple quotes for a "doc-strings for functions"
# A simple explination of what a function does, IDE's pickup and use this:
# Lets setup a simple example function:
def my_function(value):
    """Takes a value and prints it to the screen"""
    print(f"{value} is a nice value")
    return

# In an editor now like VS Code when you start typing the function name: my_func....
# It pops up with a on-screen sugestion of the value along with the "doc-string" mentioned
# above in the tripple quotes.