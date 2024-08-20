#!/usr/bin/env python3

import os

'''This script gets environment variables.

You can type 'env' in the command shell to get all env-variables.
This script uses an 'os' module to automate that via a Python script.

If an env-variable doesn't exist, use 'export' keyword to set it.
    Example: 'export FRUIT=pineapple' '''

print("HOME: "  + os.environ.get("HOME", ""))
print("SHELL: " + os.environ.get("SHELL", ""))
print("FRUIT: " + os.environ.get("FRUIT", ""))
