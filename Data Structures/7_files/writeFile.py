# need to include 'w' for 'write'
fileOut = open('output.txt', 'w')

#print(fileOut)

line1 = "First, I went to the liquor store."
line2 = "Then, I got positively fucked up."

fileOut.write(line1)
fileOut.write('\n' + line2)

fileOut.close