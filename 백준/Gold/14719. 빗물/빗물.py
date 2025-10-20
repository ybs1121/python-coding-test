h, w = map(int, input().split())
rains = list(map(int, input().split()))

answer = 0

for i in range(1, w - 1):
    left = max(rains[:i])
    right = max(rains[i+1:])
    
    water = min(left,right)
    
    if water > rains[i]:
        answer += water - rains[i]
print(answer)