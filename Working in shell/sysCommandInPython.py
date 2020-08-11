#!/usr/bin/env python3

'''A system command line that check whether or not the command is executed
This can check the return value for commands that don't show outputs.'''

#some examples
import subprocess

print(subprocess.run(["date"]))
print(subprocess.run(["sleep",'2']))
result = subprocess.run(['ls','file_doesn\'t_exist'])
print(result.returncode)


#The following capture_output parameter can be used only above Python 3.7
print(subprocess.run(["host","8.8.8.8"]).stderr)

try:
    print(subprocess.run(["host","8.8.8.8"], capture_output=True).stdout)

except:
    print("ERROR")
