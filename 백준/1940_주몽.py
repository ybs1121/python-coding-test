n = int(input())
m = int(input())
arr = list(map(int, input().split()))
arr.sort()

start = 0
end = n - 1
result = 0
while start < end:

    temp = arr[start] + arr[end]

    if temp < m:
        start += 1
    elif temp > m:
        end -= 1
    else:
        result += 1
        start += 1
        end -= 1

print(result)
