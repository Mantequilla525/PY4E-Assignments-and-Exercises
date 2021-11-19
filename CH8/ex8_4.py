fname = input("Please enter a file name:")

try:
    fh = open(fname)
except:
    print("File could not be opened")
    quit()

uniqueWords = list()

fRead = fh.read()
fSplit = fRead.split()

for word in fSplit:
    if word not in uniqueWords:
        uniqueWords.append(word)

uniqueWords.sort()
print(uniqueWords)