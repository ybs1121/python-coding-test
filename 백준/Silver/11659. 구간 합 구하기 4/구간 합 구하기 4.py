import sys
input = sys.stdin.readline

line, n = map(int, input().split())

nums = list(map(int, input().split()))

cumulative = [0]
total = 0
for i in range(line):
    total += nums[i]
    cumulative.append(total)

for i in range(n):
    st, ed = map(int, input().split())
    print(cumulative[ed] - cumulative[st - 1])
