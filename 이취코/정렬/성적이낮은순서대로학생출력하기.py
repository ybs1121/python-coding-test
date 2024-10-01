n = int(input())

students = []
for i in range(n):
    name, score = input().split()
    students.append([name, score])

sorted_students = sorted(students, key=lambda s: s[1])

for i in sorted_students:
    print(i[0], end=" ")
