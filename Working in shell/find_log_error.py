#!/usr/bin/env python3

import os
import re
import sys

'''This script searches the specific error type from log files.'''

# function to find the error
def error_search(log_file):
    error = input('What is the error? ')
    returned_error =[]
    with open(log_file,encoding='UTF-8')as file:
        for log in file.readlines():
            error_patterns = ['error']
            for i in range(len(error.split(' '))):
                error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
            if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
                returned_errors.append(log)
        file.close()
    return returned_errors


# function to output the log file
def file_output(returned_errors):
    # address the log file
    with open(os.path.expanduser('~')+'/data/errors_found.log', 'w') as file:
        for error in returned_errors:
            file.write(error)
        file.close()


# main function
if __name__ == '__main__':
    log_file = sys.argv[1]
    returned_errors = error_search(log_file)
    file_output(returned_errors)
    sys.exit(0) # used to exit from Python
