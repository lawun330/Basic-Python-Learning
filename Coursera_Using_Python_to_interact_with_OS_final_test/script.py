#!/usr/bin/env python3

'''using python script to create CSV files for errors and users from system log errors and infos'''

import re
import operator
import csv

error_msgs = {}   #error_file : number of occurence
user_msg   = {}   #user : total number of INFO and ERROR
user_name  = ''
error_name = ''
with open('syslog.log') as file: #can change the name here
    for line in file.readlines():
        user = re.search(r"ticky: (INFO|ERROR):* ([\w ']*)(\[[#\d]*\])*.*\(([a-zA-Z\. ]+)\)",line)
        if user:
            user_name = user.group(4)
            if user_name not in user_msg:
                user_msg[user_name] = [0,0] #initialize new user

            if user.group(1) == 'INFO':
                user_msg[user_name][0] += 1
            elif user.group(1) == 'ERROR':
                user_msg[user_name][1] += 1

        if user.group(1) == 'ERROR':
            error_name = user.group(2)
            if error_name not in error_msgs:
                error_msgs[error_name] = 0
            error_msgs[error_name] += 1

user_list=sorted(user_msg.items()) #sort alphabetically
error_list=sorted(error_msgs.items(), key = operator.itemgetter(1), reverse = True) #sort from most common to least common

#create new user list in tuples inside list for csv header
new_user_list = []
for i in range (len(user_list)):
    new_user_list.append((user_list[i][0],user_list[i][1][0],user_list[i][1][1]))

#create csv file for errors
with open("error_message.csv",'w+') as csvErrorFile:
    fieldnames = ["Error", "Count"]
    writer = csv.DictWriter(csvErrorFile, fieldnames=fieldnames)
    writer.writeheader()
    writer = csv.writer(csvErrorFile)
    writer.writerows(error_list)

#create csv file for users
with open("user_statistics.csv",'w+') as csvUserFile:
    fieldnames = ["Username","INFO","ERROR"]
    writer = csv.DictWriter(csvUserFile, fieldnames=fieldnames)
    writer.writeheader()
    writer = csv.writer(csvUserFile)
    writer.writerows(new_user_list)
