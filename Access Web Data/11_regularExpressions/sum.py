# The basic outline of this problem is to read the file: regex_sum_42.txt (There are 90 values with a sum=445833)
filehandle = open('regex_sum_455221.txt')

# import the regular expressions library
import re

# create an empty list
numbers = list()

# loop through each line
for line in filehandle : 
    # look for integers using the re.findall(), looking for a regular expression of '[0-9]+'
    numbers += re.findall('[0-9]+', line)

# converting the extracted strings to integers
count = 0
while count < len(numbers) :
    numbers[count] = int(numbers[count])
    count += 1

# summing up the integers
print(sum(numbers))