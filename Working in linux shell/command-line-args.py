#!/usr/bin/env python3
#Test in linux
import sys

'''returns the arguments you have passed into the command line
Example - ./command-line-args.py arg1 arg2.
This is helpful than writing function(arg1,arg2) in command line.'''

arguments = sys.argv

def show_argument(args):
	string = "The arguments you have passed are {}".format(args)
	return string

print(show_argument(arguments))

