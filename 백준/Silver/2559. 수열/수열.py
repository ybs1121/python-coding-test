
n, k = map(int, input().split())
temperature = list(map(int, input().split()))

answer = sum(temperature[0:k])
temp = sum(temperature[0:k])
for i in range(k, n):
    temp = temp - temperature[i - k] + temperature[i]
    answer = max(answer, temp)

print(answer)
