answer = 0 

def search(k, dungeons, visited, cnt):
    global answer 
    answer = max(cnt, answer)
    
    for i in range(len(dungeons)):
        if visited[i] == False and k >= dungeons[i][0]:
            visited[i] = True
            search(k - dungeons[i][1], dungeons, visited, cnt + 1)
            visited[i] = False
    
def solution(k, dungeons):
    visited = [False] * k
    search(k,dungeons, visited, 0)
    return answer