fName = input("Enter file name:")

if fName == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    quit()

try:
    fh = open(fName)
except:
    print("File could not be opened")
    quit()


lCount = 0
lSum = 0
for l in fh:
    ls = l.rstrip()
    if ls.startswith("X-DSPAM-Confidence:"):
        lCount += 1
        colonPos = ls.find(":")
        num = ls[colonPos+1:]
        numS = num.strip()

        lSum += float(numS)

print("Average spam confidence:", lSum / lCount)

