from collections import deque

def solution(progresses, speeds):

    answer = []
    progresses_deque = deque(progresses)
    speeds_deque = deque(speeds)
    while  progresses_deque:
        cnt = 0
        for i in range(len(progresses_deque)):
            t_pro = progresses_deque.popleft()
            t_sp = speeds_deque.popleft()
            progresses_deque.append(t_pro + t_sp)
            speeds_deque.append(t_sp)
            
        
        while progresses_deque:
            t_dev = progresses_deque.popleft()
            if t_dev >= 100:
                speeds_deque.popleft()
                cnt += 1
            else:
                progresses_deque.appendleft(t_dev)
                break
        
        if cnt > 0 :
            answer.append(cnt)
            
    
    
    return answer