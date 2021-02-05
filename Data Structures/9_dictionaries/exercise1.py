# write a program that reads the words in words.txt
filehandle = open('words.txt')
allWords = dict()

# store the words as keys in a dictionary
for line in filehandle :
    words = line.split()

    # use the in operator as a fast way to check whether a string is in the dictionary
    for line in words :
        if not line in allWords :

            # it doesn't matter what the values are
            allWords[line] = "placeholder"

string = input('Enter a word: ')

if string in allWords :
    print('This word is in the dictionary.')
else :
    print('This word is not in the dictionary.')