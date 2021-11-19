import re

exp = input("Enter a regular expression:")

fh = open("mbox-short.txt")

count = 0
for line in fh:
    line = line.rstrip()
    if re.search(exp, line):
        count += 1

print(count)