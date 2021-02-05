# write a program to read through a mail log

# ask for a filename
# filename = input('Enter a filename: ')
filename = "mbox-short.txt"

# try opening the file
try :
    filehandle = open(filename)
except :
    print('Invalid filename.')
    quit()

count_messages = dict()

# build a histogram using a dictionary to count how many messages have come from each email address
for line in filehandle :

    # skip over the lines that don't begin with "from"
    if line.startswith("From") :
        address = line.split()[1]
        count_messages[address] = count_messages.get(address,0) + 1

# print the dictionary
print (count_messages)