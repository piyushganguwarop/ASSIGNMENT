
student_marks = {
    "Zoro": 85,
    "Luffy": 78,
    "Igris": 92,
    "Jaideep": 88,
    "Bhoomi": 76
}

student_name = input("Enter the student's name: ")


if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print(f"Student '{student_name}' not found in the records.")
