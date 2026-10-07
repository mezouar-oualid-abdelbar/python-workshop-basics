students = ["Alice", "Bob", "Charlie", "David", "Eve"]

grades = [85, 90, 78, 92, 90]

unique_grades = {i for i in grades}

highest_grade = max(grades)

student_grades = dict(zip(students,grades))

top_students ={k:student_grades[k] for k in student_grades if student_grades[k] == highest_grade}

print("Student Grades Dictionary:", student_grades)
print("Unique Grades Set:", unique_grades)
print("Highest Grade:", highest_grade)
print("Top Student(s):", top_students)

