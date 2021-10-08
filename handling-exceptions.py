## Handling Exceptions

# It is best to be explicit about the exception you are handling, for example see the
# line that starts "except ZeroDivisionError" below. As oppose the generic route which
# you may see but is bad practice is people doing: "except Exception as e:" the problem
# with this is that it will catch all errors/exceptions and so your output/print or actions
# may not be customised to the error that is being encountered.
import time, sys
total = 4
count = 2

try:
    average = total / count
    print('Average is: ', average)
    time.sleep(60)
except ZeroDivisionError as e:
    print('Cannot devide by zero.', e)
except NameError as e:
    print('You have a typo.', e)
except KeyboardInterrupt as e:
    print('You have cancelled the programs execution. \n Performing cleanup...')
    sys.exit(1)

print('Save my progress')

# except Exception as e: <--- is an example of a bad, generic catch-all exception/error handling.