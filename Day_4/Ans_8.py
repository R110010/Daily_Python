def get_grade(marks):
    grade = {
        range(90, 101): ("A+", "Excellent"),
        range(80, 90): ("A", "Very Good"),
        range(70, 80): ("B", "Good"),
        range(60, 70): ("C", "Average"),
        range(50, 60): ("D", "Needs Improvement"),
        range(0, 50): ("F", "Fail")
    }

    for markRange in grade:
        if marks in markRange:
            return grade[markRange]

    return ("Invalid", "Marks out of range")


marks = int(input("Enter your marks: "))
grade, remarks = get_grade(marks)

print("Grade:", grade)
print("Remarks:", remarks)
