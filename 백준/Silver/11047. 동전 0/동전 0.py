import sys

input = sys.stdin.readline

n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

answer = 0

coins.sort(reverse=True)
rest = k
for coin in coins:
    answer += (rest // coin)
    rest = rest % coin


print(answer)

