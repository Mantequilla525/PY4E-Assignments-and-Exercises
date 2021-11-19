#calculate gross pay
hrs = float(input("Please enter hours worked: "))
rate = float(input("Enter rate: "))
pay = hrs * rate
pay = round(pay, 2)
print("Pay: " + str(pay))