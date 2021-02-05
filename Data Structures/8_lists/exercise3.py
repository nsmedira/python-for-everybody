# figure out which line of the above program is still not properly guarded. see if you can construct a text file which causes the program to fail and then modify the program so that the line is properly guarded and test it to make sure it handles your new text file

filehandle = open('mbox-short.txt')
count = 0
for line in filehandle :

    words = line.split()

    # the conditions we want to avoid
    if len(words) == () or words[0] != 'From' : continue

    print(words[2])