marks = 40

if marks < 40:
    print("Failed")
else:
    print("Passed")

"""
marks 1 to 39 : F
marks 40 to 49 : D
marks 50 to 59 : C
marks 60 to 69 : B
marks 70 to 79 : A-
marks 80 to 89 : A
marks 90 to 100 : A+
"""

marks = int(input("Marks: "))

if 0 <= marks <= 39:
    print("Grade: F")
elif 40 <= marks <= 49:
    print("Grade: D")
elif 50 <= marks <= 59:
    print("Grade: C")
elif 60 <= marks <= 69:
    print("Grade: B")
elif 70 <= marks <= 79:
    print("Grade: A-")
elif 80 <= marks <= 89:
    print("Grade: A")
elif 90 <= marks <= 100:
    print("Grade: A+")
else:
    print("Invalid Marks")
