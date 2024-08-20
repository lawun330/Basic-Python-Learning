#!/usr/bin/env python3

'''A system command line that checks whether or not the command is executed.
This can check the return value for commands that don't show outputs.'''

# some example module
import subprocess

# print the date
print(subprocess.run(["date"]))

# sleep for 2 seconds
print(subprocess.run(["sleep",'2']))

# check the return code
result = subprocess.run(['ls','file_doesn\'t_exist'])
print(result.returncode)

# print the error
print(subprocess.run(["host","8.8.8.8"]).stderr)

# the parameter 'capture_output' can only be used with Python 3.7 or above
try:
    print(subprocess.run(["host","8.8.8.8"], capture_output=True).stdout)
except:
    print("ERROR")
