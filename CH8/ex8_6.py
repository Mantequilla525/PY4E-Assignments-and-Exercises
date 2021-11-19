nums = list()
while True :
    sInp = input("Please enter a number or done:")
    if sInp == "done":
        break
    try:
        fInp = float(sInp)
    except:
        print("Invalid input")
        continue
    nums.append(fInp)

print('Complete')
print("Maximum:", max(nums))
print("Minumum:", min(nums))