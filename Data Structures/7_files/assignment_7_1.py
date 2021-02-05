# Write a program that prompts for a file name
# Use the file words.txt and convert to upppercase
# You can download the sample data at http://www.py4e.com/code3/words.txt
filename = input("Enter file name: ")

# then opens that file
filehandle = open(filename)

# reads through the file
for line in filehandle :

    # print the contents of the file in upper case. 
    print(line.rstrip().upper())