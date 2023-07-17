# step 1 open book
book = open('inputFile.txt', 'r' )

# step 2 loop through book
count = 1
for line in book:
    if line.split()[2] == 'P':
        print(line)

book.close()

   