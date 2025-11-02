import sys

input = sys.stdin.readline

n = int(input())
scores = list(map(int, input().split()))

m = max(scores)

summary = 0

for score in scores:
    summary += (score / m) * 100

print(summary / n)
