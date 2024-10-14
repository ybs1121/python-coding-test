from collections import deque

n, k = map(int, input().split())
virus_map = []
for i in range(n):
    virus_map.append(list(map(int, input().split())))

s, x, y = map(int, input().split())

# 숫자가 작은 순서 대로 정렬

nx = [1, 0, -1, 0]
ny = [0, 1, 0, - 1]


def bfs(sort_virus, n, s):
    q = deque(sort_virus)
    while q:
        v, x, y, sec = q.popleft()

        if sec > s:
            return

        for i in range(4):

            dx = x + nx[i]
            dy = y + ny[i]
            if 0 <= dx < n and 0 <= dy < n and virus_map[dx][dy] == 0:
                virus_map[dx][dy] = virus_map[x][y]
                q.append((virus_map[dx][dy], dx, dy, sec + 1))


def find_virus(virus_map, n):
    virus = []
    for i in range(n):
        for j in range(n):
            if virus_map[i][j] > 0:
                virus.append((virus_map[i][j], i, j, 1))
    return virus


virus = find_virus(virus_map, n)

sort_virus = sorted(virus, key=lambda x: (x[0], x[1], x[2]))

bfs(sort_virus, n, s)

print(virus_map[x - 1][y - 1])
