import re

fh = open("regex.txt")

count = list()
for line in fh:
    line.rstrip()
    x = re.findall("[0-9]+", line)
    if len(x) > 0:
        for n in x:
            n = float(n)
            count.append(n)

print(sum(count))