
'''The useful script to count the words in your essay'''
import re
Words = []
count = 0
File = str(input("Input the file location or file name: "))
with open(File,'r') as f:
    Words = (f.read().split()) #add in the list for more accessible features
    count = len(Words)
    print("The total numbers of words are "+ str(count))
