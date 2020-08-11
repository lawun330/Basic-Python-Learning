#!/usr/bin/env python3

import os

'''Get the environment varible.
NOTE - Type 'env' in the command shell to get all env-variables.
This is just using os module to get the env-var from Python script.'''

print("HOME: "  + os.environ.get("HOME", ""))
print("SHELL: " + os.environ.get("SHELL", ""))
print("FRUIT: " + os.environ.get("FRUIT",""))

'''if env-var doesn't exist, use export keyword to set it.
Example - 'export FRUIT=pineapple'. '''
