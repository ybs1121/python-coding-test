# 모든 소인수가 100만보다 크면 적절한 비밀번호다.

N = int(input())

nums = []

for i in range(N):
    nums.append(int(input()))

# 나눌 수 있는 약수를 찾는다

end_num = 1_000_001
for num in nums:
    for i in range(2, end_num):
        if num % i == 0:
            print("NO")
            break
        if i == 1_000_000:
            print("YES")
            break


