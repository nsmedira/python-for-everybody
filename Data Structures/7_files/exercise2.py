filename = input('Enter file name: ')

# try opening the file
try :
    filehandle = open(filename)
except :
    print('Invalid file name.')
    exit()

count = 0
total = 0.0

for line in filehandle :
    if line.startswith('X-DSPAM-Confidence:') :
        count = count + 1
        position = line.find(':')
        value = float(line[position + 2:])
        total = total + value
        # print(count, value, total)

print('Average spam confidence:',total/count)