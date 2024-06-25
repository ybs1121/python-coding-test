def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        if visited[i] == False:
            dfs(n,computers,i,visited)
            answer += 1
    return answer

def dfs(n, computers, now, visited):
    visited[now] = True
    for i in range(n):
        if visited[i] == False and computers[i][now] == 1:
            dfs(n,computers,i,visited)