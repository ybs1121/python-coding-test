import sys

input = sys.stdin.readline
n = int(input())

meetings = []

for i in range(n):
    meetings.append(list(map(int, input().split())))

meetings.sort(key=lambda x: (x[1],x[0]))

# print(meetings)

answer = 1

end_time = meetings[0][1]

for i in range(1, n):
    if meetings[i][0] >= end_time:
        answer += 1
        end_time = meetings[i][1]
print(answer)
