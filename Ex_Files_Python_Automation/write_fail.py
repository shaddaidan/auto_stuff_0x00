# first you open the file and read it
file = open('inputFile.txt', 'r')
fail = open('fail.txt', 'w')

# then you write into the file

for line in file:
    if line.split()[2] == 'F':
        fail.write(line)


file.close()
fail.close()

# Reopen 'fail.txt' in read mode and print its content
fail = open('fail.txt', 'r')
print(fail.read())
fail.close()