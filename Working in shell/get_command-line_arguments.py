#!/usr/bin/env python3

import sys

'''This script returns the arguments you have passed into the command line.
Example - ./command-line-args.py arg1 arg2.
This is helpful than writing function(arg1,arg2) in command line.'''

arguments = sys.argv

def show_argument(args):
	string = f"The arguments you have passed are {args}."
	return string

print(show_argument(arguments))
