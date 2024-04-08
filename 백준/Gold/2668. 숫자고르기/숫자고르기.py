def dfs(v, start):
    global cnt, ans
 
    visited[v] = 1
 
    # 다시 시작점으로 돌아왔을 경우
    if v == start:
        cnt += 1
        ans.append(start)
        return
 
    # 앞으로 갈 곳이 방문하지 않은 곳이라면
    if visited[g[v]] == 0:
        dfs(g[v], start)
 
 
# 그래프에서 사이클의 갯수 구하기
n = int(input())
# 숫자당 간선이 하나이므로 1차원 배열 활용
g = [0]
for i in range(1, n + 1):
    g.append(int(input()))
 
cnt = 0
ans = []
# 모든 숫자를 순회
for i in range(1, n + 1):
    # 방문 처리 배열 초기화
    visited = [0] * (n + 1)
    dfs(g[i], i)
 
print(cnt)
for i in ans:
    print(i)