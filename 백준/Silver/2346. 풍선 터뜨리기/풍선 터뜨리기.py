from collections import deque
N = int(input())  
bal = list(map(int, input().split())) 
que = deque(enumerate(bal, start=1))
res = []
cur, m = que.popleft()
res.append(cur)
while que:
    if m > 0:
        que.rotate(-(m - 1))
    else:
        que.rotate(-m)
    cur, m = que.popleft()
    res.append(cur)
print(" ".join(map(str, res)))