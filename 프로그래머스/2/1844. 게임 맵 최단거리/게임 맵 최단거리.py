from collections import deque

def solution(maps):
    answer = 0
    x_size = len(maps)
    y_size = len(maps[0])
    visited = [[False for _ in range(y_size)] for _ in range(x_size)]
    nx = [-1, 1, 0, 0]
    ny = [0, 0, -1, 1]
    
    queue = deque()
    queue.append((0,0))
    
    while queue:
        x,y = queue.popleft()
        visited[x][y] = True
        for i in range(4):
            dx = x + nx[i]
            dy = y + ny[i]
            
            if 0 <= dx < x_size and 0 <= dy < y_size and visited[dx][dy] == False and maps[dx][dy] == 1:
                queue.append((dx,dy))
                maps[dx][dy] = maps[x][y] + 1
        
        
    if maps[x_size - 1][y_size - 1] == 1:
        answer = -1
    else:
        answer = maps[x_size - 1][y_size - 1]
    return answer