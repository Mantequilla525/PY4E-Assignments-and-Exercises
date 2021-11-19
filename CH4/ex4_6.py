hrs = input("Please enter hours worked: ")
rate = input("Please enter pay rate: ")

try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

def computepay(hr, py):
    if h < 40:
     pay = h * r
    else:
        hrs_ot = h - 40
        pay = (40 * r) + (hrs_ot * (r * 1.5))
    return pay

total_pay = computepay(h, r)

print(total_pay)