score = input("Enter Score: ")

try:
    s = float(score)
except:
    "Error, please enter a number between 0 and 1.0"
    quit()

def computegrade(inp):
    if inp > 1.0:
        print("Error, please enter a value between 0.0 and 1.0")
        quit()
    elif inp >= 0.9:
        grade = "A"
    elif inp >= 0.8:
        grade = "B"
    elif inp >= 0.7:
        grade = "C"
    elif inp >= 0.6:
        grade = "D"
    elif inp < 0.6 and inp >= 0.0:
        grade = "F"
    else:
        print("Error, please enter a value between 0.0 and 1.0")
        quit()
    return grade

letter_grade = computegrade(s)
print(letter_grade)