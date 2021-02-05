filename = input('Enter file name: ')

# easter egg
if filename == 'na na boo boo' :
    print('NA NA BOO BOO TO YOU - You have been punk\'d')
    exit()

# try opening the file
try :
    filehandle = open(filename)
except :
    print('Invalid filename.')
    exit()

count = 0
total = 0.0

for line in filehandle :
    if line.startswith('X-DSPAM-Confidence:') :
        count = count + 1
        position = line.find(':')
        value = float(line[position + 2:])
        total = total + value
        print(count, value, total)

print('Average spam confidence:',total/count)