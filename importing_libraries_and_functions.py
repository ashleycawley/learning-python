import random # Imports a library called 'random' which will have functions within it.

# import xyz is usually done at the top and is best to do that to take precedence.

print(random.random()) # random.random() uses a function (random) within a library called random.

# Functions from within libraries can also be imported in and relabelled if desired, for example:
from math import fsum as madnumbers

# ^^^ > The function 'fsum' was imported from the 'math' library and fsum was re-labelled to 'madnumbers'

# And is used here:
print(madnumbers( [ 12 + 12 ] ))