import heapq

T = int(input())
for _ in range(T):
    K = int(input())
    arrays = list(map(int, input().split()))
    arrays_sum = 0
    heapq.heapify(arrays)
    while len(arrays) > 1:
        a = heapq.heappop(arrays)
        b = heapq.heappop(arrays)
        ab = (a + b)
        arrays_sum += ab
        heapq.heappush(arrays, ab)
    print(arrays_sum)

