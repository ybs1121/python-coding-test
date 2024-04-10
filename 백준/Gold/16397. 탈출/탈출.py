# import sys
# sys.setrecursionlimit(10**6)
from collections import deque

N, T, G = map(int, input().split())

# N이 G보다 자리수가 크면 탈출 못할거 같은데
# 가지치기로 쭉 탐색하다가 가장 적은 애가 나오면 멈춰?
# result_list = []
#
# def find(cnt, num):
#     global T
#     global G
#
#     cnt += 1
#
#     if cnt > T:
#         return
#
#         # A버튼
#
#     A_num = num + 1
#     if A_num == G:
#         result_list.append(cnt)
#         return
#     find(cnt, A_num)
#
#     if num * 2 > 99999:
#         return
#
#     digit = len(str(num * 2)) # 자리수
#     B_num = num * 2 - (10 ** (digit - 1))
#
#     # B버튼
#     if B_num == G:
#         result_list.append(cnt)
#         return
#
#
#     find(cnt, B_num)
#
#
# if len(str(N)) > len(str(G)):
#     print("ANG")
#
# else:
#     find(0, N)
#     if len(result_list) == 0:
#         print("ANG")
#     else:
#         print(min(result_list))




visit = [False for _ in range(100001)]

queue = deque([(N,0)])
visit[N] = True
result_list = []
while queue:

    v,cnt = queue.popleft()
    if cnt > T:
        continue

    if v == G:
        result_list.append(cnt)
        break



    A_num = v + 1
    if A_num > 99999:
        continue
    if not visit[A_num]:
        queue.append((A_num,cnt+1))
        visit[A_num] = True

    if (v * 2) > 99999:
        continue

    digit = len(str(v * 2))  # 자리수
    B_num = (v * 2) - (10 ** (digit - 1))
    if B_num < 0:
        continue

    if not visit[B_num]:
        queue.append((B_num,cnt+1))
        visit[B_num] = True



if len(result_list) == 0:
    print("ANG")
else:
    print(min(result_list))



