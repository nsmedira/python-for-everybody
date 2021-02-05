def count(string, letter) :
    count = 0
    for index in string :
        if index == letter :
            count = count + 1
    return count

print(count('Mississippi','M'))