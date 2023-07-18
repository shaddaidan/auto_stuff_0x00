# open files

file = open('inputFile.txt', 'r')
Pass = open('pass.txt', 'w')

# loopty loop time

for line in file :
    if line.split()[2] == 'P':
        Pass.write(line)

file.close()
Pass.close()

Pass = open('pass.txt', 'r')
print(Pass.read())
Pass.close()