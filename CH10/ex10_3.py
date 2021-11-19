fh = open("mbox-short.txt")

letterCount = {}
for line in fh:
    ls = line.split()
    for word in ls:
        ws = list(word)
        for letter in ws:
            lowLetter = letter.lower()
            letterCount[lowLetter] = letterCount.get(lowLetter, 0) + 1

print(letterCount)