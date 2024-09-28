N, M, K = map(int, input().split())
nums = list(map(int, input().split()))

# 정렬
nums.sort(reverse=True)

# 0번 인덱스를 더 하고 횟수가 초과하면 1번 인덱스를 더한다
answer = 0
cnt = 0
for i in range(M):
    if cnt == K:
        answer += nums[1]
        cnt = 0
    else:
        answer += nums[0]
        cnt += 1

print(answer)

