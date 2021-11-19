fh = open('mbox-short.txt')

count = dict()
for line in fh:
    if line.startswith("From "):
        ls = line.split()
        emAd = ls[1]
        count[emAd] = count.get(emAd, 0) + 1

tList = list()
for k,v in count.items():
    temp = (v, k)
    tList.append(temp)

tList = sorted(tList, reverse=True)
print(tList)
print("Most commits:", tList[0])