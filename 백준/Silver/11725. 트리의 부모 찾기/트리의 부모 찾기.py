import sys
 
N = int(sys.stdin.readline())
 
# 그래프 생성
graph = [[] for i in range(N+1)]
for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
 
# 방문 여부, 각 인덱스를 노드로 사용해 방문했으면 0을 지우고, 부모 노드를 저장한다.
visited = [0]*(N+1) 
 
'''dfs - 스택으로 구현'''
def dfs(graph,node):
 
    stack = [node]
    while stack:
        top = stack.pop()
        for adj in graph[top]:
            if visited[adj] == 0: # 방문한 적이 없다면
                visited[adj] = top # 해당 노드를 부모 노드로 저장
                stack.append(adj)
    
    return visited
 
dfs(graph,1)
# 첫번째 예시라면 visited = [0, 4, 4, 6, 1, 3, 1, 4]
 
for x in range(2, N+1):
    print(visited[x]) # 각 인덱스(노드)에 저장된 부모 노드 가져오기