def solution(n, times):
    answer = 0
    end = n * max(times)
    start = 1 
    
    while start <= end:
        mid = (start + end ) // 2
        possible_total = 0
        for time in times:
            possible_total += (mid//time)
            
            if possible_total >= n:
                break
            
        if possible_total >= n :
            answer = mid
            end = mid-1
        else:
            start = mid+1
    
    return answer