#

n = int(input())
scores = list(map(int, input().split()))


max_score = max(scores)

if max_score == 0:
    print(0)

else:
    prefix_sum = 0
    for i in range(n):
        prefix_sum += scores[i] / max_score * 100

print(prefix_sum/n)