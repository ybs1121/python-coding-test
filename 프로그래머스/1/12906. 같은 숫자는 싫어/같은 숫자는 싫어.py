def solution(arr):
    answer = []
    
    for i in arr:
        if len(answer) == 0:
            answer.append(i)
        else:
            if not answer[-1] == i:
                answer.append(i)
                
    
    
    return answer