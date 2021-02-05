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
    if line.startswith("From") and not line.startswith("From:") :
        address = line.split()[1]
        count_messages[address] = count_messages.get(address,0) + 1

# print the dictionary
# print(count_messages)

# after all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop to find who has the most messages and print how many messages the person has
# maxKey = max(count_messages, key=count_messages.get)
# print (maxKey, str(count_messages[maxKey]))
maxValue = None
sender = None
for line in count_messages :
    count = count_messages[line]
    if maxValue is None or count > maxValue :
        maxValue = count
        sender = line
print ( sender, maxValue )