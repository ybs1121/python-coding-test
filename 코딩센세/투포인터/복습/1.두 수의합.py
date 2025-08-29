n = int(input())
arr = list(map(int, input().split()))
target = int(input())


arr.sort()

st = 0
ed = n - 1
answer = 0
while st < ed:
    if arr[st] + arr[ed] == target:
        answer += 1
        st += 1
    if arr[st] + arr[ed] < target:
        st += 1
    else:
        ed -= 1

print(answer)