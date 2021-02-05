# write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements
list_cars = ['acura mdx','honda civic','jeep wrangler']

def chop(list_input) :
    del list_input[0]
    del list_input[len(list_input)-1]
    return None

def middle(list_input) :
    return list_input[1:len(list_input)-1]

# chop(list_cars)

newList = middle(list_cars)

print(newList)
print(list_cars)