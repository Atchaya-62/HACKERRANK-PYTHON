from collections import namedtuple


N = int(input())
headers = input().split()
Student = namedtuple('Student', headers)

total_marks = 0
for i in range(N):
    student_data = input().split()
    student = Student(*student_data)
    total_marks += int(student.MARKS)

average = total_marks / N
print(f"{average:.2f}")
