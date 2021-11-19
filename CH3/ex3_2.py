hrs = input("Please enter hours worked: ")
rate = input("Please enter pay rate: ")

try:
    h = float(hrs)
    r = float(rate)

    
    if h < 40:
     pay = h * r
    else:
        hrs_ot = h - 40
        pay = (40 * r) + (hrs_ot * (r * 1.5))

    print(str(round(pay, 2)))
except:
    print("Error, please enter numeric input")