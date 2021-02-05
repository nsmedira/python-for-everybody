# Write a program to read through the mbox-short.txt
filehandle = open('mbox-short.txt')

distribution = dict()

# figure out the distribution by hour of the day for each of the messages. 
for line in filehandle :
    if line.startswith("From") and not line.startswith("From:") :

        # You can pull the hour out from the 'From ' line by finding the time
        # From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
        time = line.split()[5]

        # split the string a second time using a colon
        hour = time.split(":")[0]
        distribution[hour] = distribution.get(hour,0) + 1

# sort the dictionary by hour ascending
# create a list (which are sortable) to put the key value tuples into
listOfTuples = list()
for key, value in list(distribution.items()) :
    listOfTuples.append((key, value))

listOfTuples.sort()

for key, value in listOfTuples :
    print(key, value)