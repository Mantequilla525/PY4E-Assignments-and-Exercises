hrs = float(input("Please enter hours worked: "))
rate = float(input("Please enter pay rate: "))

if hrs < 40:
    pay = hrs * rate
else:
    hrs_ot = hrs - 40
    pay = (40 * rate) + (hrs_ot * (rate * 1.5))

pay = round(pay, 2)

print(str(pay))