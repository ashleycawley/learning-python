import os

os.system('whoami')

# Run a command on a remote system over SSH
os.system('ssh -p 7669 pi@einkPi uptime') # This example assumes that SSH key-based auth is already in place

# It is good to specify full paths to binaries but obviously they can vary in different environments, in bash
# we would typically use the "which" command to locate the path of a binary, we can do a similar thing in Python
# using the "shutil" module and "shutil.which()" sub-module:
import shutil

ping_path = shutil.which("ping")

# That could then be used to run a process in the more modern way using the "subprocess" module:
import subprocess
subprocess.run([shutil.which("ping"), "-c 20", "bbc.co.uk"])

# NOTE: To run a command in the *background* and let the rest of the script proceed then use "subprocess.Popen([])"
# instead of the "subprocess.run([])"
subprocess.Popen([shutil.which("ping"), "-c 20", "bbc.co.uk"])