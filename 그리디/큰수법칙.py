n, m, k = map(int, input().split())

arr = list(map(int,input().split()))

arr.sort(reverse=True)

dupCnt = 0
answer = 0

for i in range(m):
    if dupCnt < k:
        answer += arr[0]
        dupCnt += 1
    else:
        answer += arr[1]
        dupCnt = 0
print(answer)

###### 2안 ####
first = arr[0]
second = arr[1]

count = int (m/(k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first
result += (m - count) *second

print(result)

