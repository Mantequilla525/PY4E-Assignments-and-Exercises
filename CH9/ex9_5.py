fh = open('mbox-short.txt')

count = dict()
for line in fh:
    if line.startswith("From "):
        ls = line.split()
        emAd = ls[1]
        school = emAd.split("@")
        schoolHandle = school[1]
        count[schoolHandle] = count.get(schoolHandle, 0) + 1
        print(schoolHandle)

# Find which school has sent the most emails
schoolName = None
schoolNameCount = None

for a,b in count.items():
    if schoolNameCount is None or b > schoolNameCount:
        schoolName = a
        schoolNameCount = b
print("Most emails from:", schoolName,schoolNameCount)