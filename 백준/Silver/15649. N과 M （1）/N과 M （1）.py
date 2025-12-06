import sys
input = sys.stdin.readline

N, M = map(int, input().split())
kinds = []
visited = [0] * (N + 1)

def finder(target):
    if len(target) == M:
        kinds.append(target)
        return

    for num in range(1, N + 1):
        if not visited[num]:
            visited[num] = 1          
            finder(target + [num])    
            visited[num] = 0          

finder([])

kinds.sort()
for kind in kinds:
    print(*kind)
