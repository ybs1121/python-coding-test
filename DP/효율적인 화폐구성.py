n, m = map(int, input().split())

coins = []
for i in range(n):
    coins.append(int(input()))
INF = 100000000
d = [INF] * 1001

for i in range(n):
    d[coins[i]] = 1

for i in range(1, m + 1):

    for j in range(1, i):
        end_idx = i - j
        start_idx = j
        if d[end_idx] != INF and d[start_idx] != INF:  ## 인덱스에 방법이 잇을때
            d[i] = min(d[i], (d[start_idx] + d[end_idx]))

    if i % 2 == 0:
        if d[i // 2] != INF:  ## 인덱스에 방법이 잇을때
            d[i] = min(d[i], d[i // 2] * 2)

print(d[m])
