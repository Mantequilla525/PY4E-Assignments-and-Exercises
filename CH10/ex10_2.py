fh = open("mbox-short.txt")

count = dict()
for line in fh:
    if line.startswith("From "):
        ls = line.split()
        ts = ls[5]
        tss = ts.split(":")
        hr = tss[0]
        count[hr] = count.get(hr, 0) + 1

countList = list()
for a,b in count.items():
    countList.append((a,b))

countList = sorted(countList)

for a,b in countList:
    print(a,b)