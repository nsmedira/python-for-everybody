filename = input('Enter the file name: ')
try:
    filehandle = open(filename)
except:
    print('File cannot be opened:', filename)
    exit()
count = 0
for line in filehandle :
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', filename)