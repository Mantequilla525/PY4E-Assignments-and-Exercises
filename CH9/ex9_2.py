fName = "mbox-short.txt"
fh = open(fName)


dow = dict()
for line in fh:
    if line.startswith("From "):
        fs = line.split()
        dowStr = fs[2]
        dow[dowStr] = dow.get(dowStr, 0) + 1

print(dow)