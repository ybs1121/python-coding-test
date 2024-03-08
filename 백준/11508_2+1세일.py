n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

### 무조건 3개씩 사는게 이득
arr.sort(reverse=True)

pay_amt = []
last_run_idx = -1

for i in range(0, n, 3):
    pay_amt.append(arr[i:i+3])

result = 0

for i in pay_amt:
    if len(i) < 3:
        result += sum(i)
    else:
        result += sum(i) - min(i)
print(result)
