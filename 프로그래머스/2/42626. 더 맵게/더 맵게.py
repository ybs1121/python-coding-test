import heapq

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)
    
    while(len(scoville) >= 2):
        fs = heapq.heappop(scoville)
        sd = heapq.heappop(scoville)
        
        if fs >= K:
            break
            
        answer += 1
        scv = fs + (sd * 2)
        heapq.heappush(scoville, scv)
    
    if len(scoville) == 1:
        if not scoville[0] >= K:
            answer = -1
        
    return answer