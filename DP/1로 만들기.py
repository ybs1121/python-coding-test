n = int(input())

arrays = []


def calculation(n, cnt):
    if n == 1:
        arrays.append(cnt)
        return
    if n % 5 == 0:
        next_n = n // 5
        calculation(next_n, cnt + 1)
    if n % 3 == 0:
        next_n = n // 3
        calculation(next_n, cnt + 1)

    if n % 2 == 0:
        next_n = n // 2
        calculation(next_n, cnt + 1)

    next_n = n - 1
    calculation(next_n, cnt + 1)


calculation(n, 0)
print(min(arrays))

####DP로 풀기
result = [0] * 30001

for i in range(2, n + 1):
    result[i] = result[i - 1] + 1

    if i % 5 == 0:
        result[i] = min(result[i], result[i // 5] + 1)
    if i % 3 == 0:
        result[i] = min(result[i], result[i // 3] + 1)
    if i % 2 == 0:
        result[i] = min(result[i], result[i // 2] + 1)

print(result[n])
