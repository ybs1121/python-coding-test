# 15649

N, M = map(int, input().split())

answer = []


def find(val, output):
    if val == M:
        print(output)
        return

    for i in range(1, N + 1):
        find(val + 1, output + str(i) + " ")


find(0, "")
