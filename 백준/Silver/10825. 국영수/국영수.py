n = int(input())
students = []

for i in range(n):
    name, korean, english, math = map(str, input().split())
    students.append([name, int(korean), int(english), int(math)])

sorted_students = sorted(students, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for student in sorted_students:
    print(student[0])
