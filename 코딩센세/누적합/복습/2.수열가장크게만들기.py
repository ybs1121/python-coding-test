N = int(input())
arr = list(map(int, input().split()))

prefix = [0 for i in range(N + 1)]
for i in range(N):
    prefix[i + 1] = max(prefix[i] + arr[i], arr[i])

print(*prefix)
