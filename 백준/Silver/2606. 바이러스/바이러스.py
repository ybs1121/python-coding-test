import sys

input = sys.stdin.readline

V = int(input())
E = int(input())

graph = []

for i in range(E):
    graph.append(list(map(int,input().split())))


# print("V " + str(V))
# print("E " + str(E))

graph.sort()
# print("grahp ")
# print(graph)
# print("--------------------------------------")

connect = [[] for _ in range(V + 1)]


for i in graph:
    connect[i[0]].append(i[1])
    connect[i[1]].append(i[0])
#
# print(connect)
#
# print("연결 확인 끝!")

# 방문확인 리스트
chk =[False for _ in range(V + 1)]




#DFS 구현

def dfs(chk, i, connect):

    if chk[i] == False:
        chk[i] = True


        for k in connect[i]:
            if chk[k] == False:
                result[0] += 1
                dfs(chk,k,connect)




#결과값 변수 선언
result = [0]
dfs(chk, 1, connect)
print(result[0])

# print("-==========================")
# print(chk)
# print(result)

