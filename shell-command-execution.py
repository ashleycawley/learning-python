import os

os.system('whoami')

# Run a command on a remote system over SSH
os.system('ssh -p 7669 pi@einkPi uptime') # This example assumes that SSH key-based auth is already in place