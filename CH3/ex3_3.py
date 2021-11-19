score = input("Enter Score: ")

try:
    s = float(score)
except:
    "Error, please enter a number between 0 and 1.0"
    quit()

if s < 0.6:
    grade = "F"
elif s < 0.7:
    grade = "D"
elif s < 0.8:
	grade = "C"
elif s < 0.9:
	grade = "B"
else:
    grade = "A"

print(grade)