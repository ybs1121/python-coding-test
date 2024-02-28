n, m = map(int, input().split())

result = n

count = 0

while result != 1:
    count += 1
    if result % m == 0:
        result /= m
    else:
        result -= 1
print(count)