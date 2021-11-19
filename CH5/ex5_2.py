largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    
    try:
        iNum = int(num)
    except:
        print("Invalid input")
        continue
    
    if largest is None or iNum:
        largest = iNum
    elif iNum > largest:
        largest = iNum
    if smallest is None:
        smallest = iNum
    elif iNum < smallest:
        smallest = iNum

print("Maximum is", largest)
print("Minumum is", smallest)