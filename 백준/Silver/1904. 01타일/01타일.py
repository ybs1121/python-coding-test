import sys
input = sys.stdin.readline

n = int(input())

answer = [0] * 1000001
if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    answer[1] = 1
    answer[2] = 2

    sum = answer[0] + answer[1]

    for i in range(3,n+1):
            answer[i] += (answer[i-2] + answer[i - 1])%15746



    print(answer[n]%15746)

