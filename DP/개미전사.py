n = int(input())
storage = list(map(int, input().split()))

d = [0] * 1001
d[0] = storage[0]
d[1] = max(storage[0],storage[1])
## 최대한 많이 털어 가는게 좋겠죠
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + storage[i])
    print(d[i])
print(d[:n+1])