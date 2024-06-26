from collections import deque
def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    
    for word in words:
        if word  == begin:
            words.remove(word)

    
    q = deque()
    
    q.append((begin,0))

    while q:
        next_word,cnt = q.popleft()
        
        if next_word == target:
            answer = cnt
            break
        
        for word in words:
            diff_cnt = 0 
            for a,b in zip(next_word, word):
                if a != b:
                    diff_cnt += 1
            if diff_cnt == 1:
                q.append((word,cnt + 1))
    
    if next_word == target:
        return answer
    else:
        return 0
 