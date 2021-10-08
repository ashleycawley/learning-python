## User Cancelling Execution
import time

try:
    print('one')
    time.sleep(30)
    print('two')
except KeyboardInterrupt as e:
    print('You have cancelled the programs execution. \n Performing cleanup...')
    exit(1)

print('Save my progress')

# except Exception as e: <--- is an example of a bad, generic catch-all exception/error handling.