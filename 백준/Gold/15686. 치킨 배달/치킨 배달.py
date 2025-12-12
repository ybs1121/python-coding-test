import sys

input = sys.stdin.readline

N, M = map(int, input().split())
maps = []
for i in range(N):
    maps.append(list(map(int, input().split())))

# 집과 치킨집을 분리할까
houses = []
chickens = []

for i in range(N):
    for j in range(N):
        if maps[i][j] == 1:
            houses.append([i, j])
        if maps[i][j] == 2:
            chickens.append([i, j])

# i의 치킨집을 폐업 시킬지 말지
visited = [0] * len(chickens)

answer = sys.maxsize


def dfs(idx, cnt):
    global N, M, answer

    if cnt == M:

        tmp_sum = 0
        for i in range(len(houses)):
            distance = sys.maxsize
            for j in range(len(visited)):
                if visited[j]:
                    check_num = abs(houses[i][0] - chickens[j][0]) + abs(houses[i][1] - chickens[j][1])
                    distance = min(distance, check_num)
            tmp_sum += distance

        answer = min(answer, tmp_sum)
        return

    for i in range(idx, len(chickens)):
        if visited[i] == 0:
            visited[i] = 1
            dfs(i + 1, cnt + 1)
            visited[i] = 0

    return


dfs(0, 0)

print(answer)
