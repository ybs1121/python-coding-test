import sys
import heapq

input = sys.stdin.readline

n = int(input())
nums = []

for i in range(n):
    num = int(input())
    if num <= 0:
        if not nums:
            print(0)
        else:
            print(-heapq.heappop(nums))
    else:
        heapq.heappush(nums, -num)


