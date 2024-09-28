n, k = map(int, input().split())

# 나눌 수 있으면 나누는 것이 횟수를 최소화 하는 것이다.
answer = 0

while n > 1:
    if n % k == 0:
        n = n // k
    else :
        n = n - 1

    answer += 1

print(answer)
