with open('inputFile.txt', 'r') as file:

    for line in file:
        if line.split()[2] == 'F':
            print(line)
