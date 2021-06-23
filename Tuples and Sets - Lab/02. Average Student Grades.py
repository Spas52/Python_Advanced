number = int(input())


def input_students_grades(number):
    students_grades = {}
    for _ in range(number):
        student_name, student_grade = input().split()
        student_grade = float(student_grade)
        if student_name not in students_grades:
            students_grades[student_name] = []
        students_grades[student_name].append(student_grade)
    return students_grades


def calculate_avg(iter):
    return sum(iter) / len(iter)


def print_data(students_grades):
    for student, grade in students_grades.items():
        grades_str = " ".join(map(lambda grade: f"{grade:.2f}", grade))
        avg_grade = calculate_avg(grade)
        print(f'{student} -> {grades_str} (avg: {avg_grade:.2f})')


students_grades = input_students_grades(number)
print_data(students_grades)