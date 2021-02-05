# write a program to read through a file and print the contents of the file (line by line) all in upper case
filename = input('Enter the filename:')

# try to open the file
try :
    fileHandle = open(filename)
except :
    print('Invalid file name.')
    exit()

# loop through the lines, printing each line converted to upper case
for line in fileHandle :
    print(line.rstrip().upper())