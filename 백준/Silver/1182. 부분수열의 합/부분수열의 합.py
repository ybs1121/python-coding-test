N, S = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
# print(arr)
result = 0

def comb(arr, n):
    result = []

    if n > len(arr):
        return result

    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr) - n + 1):
            for j in comb(arr[i+1 :], n - 1):
                result.append([arr[i]] + j)
    return result

for i in range(1,N+1):
    temp = comb(arr,i)

    for i in range(len(temp)):
        if S == sum(temp[i]):
            result += 1
print(result)



