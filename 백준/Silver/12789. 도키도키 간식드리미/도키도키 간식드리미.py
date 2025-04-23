import sys
from collections import deque
input = sys.stdin.readline

# 입력
n = int(input())
arr = list(map(int, input().split()))

stack = deque()
waitingNum = 1

stack = deque()
waitingNum = 1 # 간식을 받을 차례의 대기번호

for x in arr:
    stack.append(x)
    while stack and stack[-1] == waitingNum: # 빈 스택이 아니고 & 스택 맨 위랑 대기번호가 같을 때
        stack.pop()
        waitingNum += 1 # 대기번호 증가시켜주기

if len(stack) == 0: # 빈 스택이라면 Nice
    print('Nice')
else: # 아니라면 Sad
    print('Sad')