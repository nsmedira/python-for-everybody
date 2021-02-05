fileHandle = open('mbox.txt')
for line in fileHandle:
    line = line.rstrip()

    # skip the lines that don't start with "From:"
    #if not line.startswith('From:') :
    #    continue

    # skip lines where the from address isn't University of Cape Town in South Africa
    if line.find('@uct.ac.za') == -1:
        continue

    print(line)