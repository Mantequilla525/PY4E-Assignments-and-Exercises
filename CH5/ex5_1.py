count = 0
total = 0

while True :
    sInp = input("Please enter a number or done:")
    if sInp == "done":
        break
    try:
        fInp = float(sInp)
    except:
        print("Invalid input")
        continue
    # print(fInp)
    count += 1
    total += fInp

print('Complete')
print(count, total, total / count)