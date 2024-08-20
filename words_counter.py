'''The useful script to count the words in your essay.'''

words = []
count = 0

file = str(input("Input the file location or file name: "))

with open(file) as f:
    words = (f.read().split()) # add to the list
    count = len(words)
    print(words)
    print("The total numbers of words are " + str(count) + '.')
