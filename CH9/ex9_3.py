fh = open('mbox-short.txt')

count = dict()
for line in fh:
    if line.startswith("From "):
        ls = line.split()
        emAd = ls[1]
        count[emAd] = count.get(emAd, 0) + 1

print(count)