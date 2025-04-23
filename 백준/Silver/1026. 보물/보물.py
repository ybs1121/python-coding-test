n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A 는 작은 순서대로
A.sort()
# B는 큰 순서대로
B.sort(reverse=True)

answer = 0

for i in range(n):
    answer += A[i] * B[i]

print(answer)
