import sys

input = sys.stdin.readline

N, M = map(int, input().split())

answer = []


def finder(arr, idx):
    global N, M

    if len(arr) == M:
        answer.append(arr)
        return

    for i in range(idx, N):
        arr.append(i + 1)
        finder(arr + [], i + 1)
        arr.pop()


finder([], 0)

for a in answer:
    print(*a)
