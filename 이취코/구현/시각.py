# input
# 5

n = int(input())
cnt = 0
for h in range(n + 1):  # 시
    for m in range(0, 60):  # 분
        for s in range(0, 60):  # 초
            if '3' in str(h) + str(m) + str(s):
                cnt += 1

print(cnt)
