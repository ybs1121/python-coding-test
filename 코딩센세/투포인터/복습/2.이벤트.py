n, x = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

# 만약 최대 용량보다 크거나 같다면 그냥 cnt + 1
# 두 개의 남은 용랭을 합쳐서 만약 반 이상이면 두병 제거 후 cnt + 1
st = 0
ed = n - 1

remain = 0
cnt = 0

while st <= ed:

    if arr[ed] == x:
        cnt += 1
        ed -= 1
        continue

    if st == ed:
        remain += 1

    if arr[st] + arr[ed] >= x / 2:
        cnt += 1
        st += 1
        ed -= 1
    else:
        st += 1
        remain += 1

print(cnt + remain // 2)
