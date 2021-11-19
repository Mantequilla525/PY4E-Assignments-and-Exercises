import re

fh = open("mbox-short.txt")

count = []
for line in fh:
    line = line.rstrip()
    x = re.findall('^New .*:\s(.*)', line)
    if len(x) > 0:
        for n in x:
            n = float(n)
            count.append(n)

print(sum(count) / len(count))