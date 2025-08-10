N = int(input())
guess = []
answer = 0
for i in range(1, N + 1):
    guess.append(list(map(str, input().split())))  # 숫자, 스트라이크, 불

for x in range(0, 10):
    for y in range(0, 10):
        for z in range(0, 10):
            if x == y or y == z or x == z:
                continue
            grading = [False] * N
            i = 0
            for g in guess:

                strick = 0
                ball = 0

                # 스트라이크인 경우
                if str(x) == g[0][0]:
                    strick = strick + 1
                if str(y) == g[0][1]:
                    strick = strick + 1
                if str(z) == g[0][2]:
                    strick = strick + 1

                # 볼인 경우
                if str(x) == g[0][1] or str(x) == g[0][2]:
                    ball = ball + 1
                if str(y) == g[0][0] or str(y) == g[0][2]:
                    ball = ball + 1
                if str(z) == g[0][0] or str(z) == g[0][1]:
                    ball = ball + 1
                if int(g[1]) == strick and int(g[2]) == ball:
                    grading[i] = True
                i = i + 1

            if sum(grading) == N:
                answer = answer + 1
print(answer)

