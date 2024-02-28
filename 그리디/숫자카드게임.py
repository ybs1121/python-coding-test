n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

result = -1
for i in range(n):
    arr[i].sort()
    if result < arr[i][0]:
        result = arr[i][0]

print(result)



for i in range(n):
    min_val = min(arr[i])
    result = max(min_val, result)
print(result)