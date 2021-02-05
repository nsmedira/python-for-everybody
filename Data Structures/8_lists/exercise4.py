# open the file romeo.txt
try :
    filehandle = open('romeo.txt')
except :
    print('Error opening file.')
    exit()

# create a variable to hold all the words in romeo.txt in a list
list_words = []

# read it line by line
for line in filehandle :

    # for each line, split the line into a list of words using the split function
    words = line.split()
    #print(words)

    # for each word, check to see if the word is already in a list
    for line in words :

        # if a word is not in the list, add it to the list
        if not ( line in list_words ) :
            list_words.append(line)
            #print(list_words)

# when the program completes, sort and print the resulting words in alphabetical order
list_words.sort()
print(list_words)