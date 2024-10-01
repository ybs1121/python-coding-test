n = int(input())
stores = list(map(int, input().split()))

d = [0] * 100

d[0] = stores[0]
d[1] = max(stores[0], stores[1])

for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + stores[i])

print(d[n - 1])
