import heapq
import sys
n = int(input())
heap = []
for i in range(n):
    x = int(sys.stdin.readline())  ## input() 은 느려서 한줄 씩 사용하는 거면 이게 이득이다.

    if x == 0 : ## 출력
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, x)

