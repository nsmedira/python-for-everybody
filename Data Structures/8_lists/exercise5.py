# open mailbox data file
try :
    filehandle = open('mbox-short.txt')
except :
    print('invalid input')
    exit()

count_fromLines = 0

# when you find a line that starts with "From", you will split the line into words using the split function
for line in filehandle :
    if line.startswith('From') and not line.startswith('From:') :

        # parse the From line and print out the second word for each From line
        # we are interested in who sent the message, which is the second word on the "From" line
        print(line.split()[1])
        
        # you will also count the number of From (not From:) lines and print out a count at the end. 
        count_fromLines = count_fromLines + 1