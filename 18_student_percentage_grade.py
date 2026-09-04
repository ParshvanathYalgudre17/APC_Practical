def student_result(m1, m2, m3, m4, m5):
    total = m1 + m2 + m3 + m4 + m5
    percentage = total / 5

    if percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "Fail"

    return percentage, grade

marks = []
for i in range(5):
    marks.append(float(input("Enter marks: ")))

percentage, grade = student_result(*marks)
print("Percentage =", percentage)
print("Grade =", grade)
