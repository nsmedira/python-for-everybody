# write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards

string = 'titillate'
index = len(string) - 1

while index >= 0 :
    print(string[index])
    index = index - 1