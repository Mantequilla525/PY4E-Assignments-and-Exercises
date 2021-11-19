fname = input("Please enter a file name:")
fh = open(fname)

for line in fh:
    linex = line.rstrip()
    lineup = linex.upper()
    print(lineup)