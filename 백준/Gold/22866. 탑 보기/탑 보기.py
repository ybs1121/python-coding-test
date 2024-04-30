# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# buildings = list(map(int, input().split()))
#
#
# result = []
# for i in range(n):
#
#     left_stack = []
#     right_stack = []
#     for j in range(i-1, 0, -1):
#         # print("left:" + str(j))
#         if len(left_stack) == 0 and buildings[i] < buildings[j]:
#             left_stack.append([buildings[j], j+1])
#         elif len(left_stack) > 0:
#             if left_stack[-1][0] < buildings[j]:
#                 left_stack.append([buildings[j], j+1])
#     for k in range(i+1, n):
#         # print("right:" + str(k))
#         if len(right_stack) == 0 and buildings[i] < buildings[k]:
#             right_stack.append([buildings[k], k+1])
#         elif len(right_stack) > 0:
#             if right_stack[-1][0] < buildings[k]:
#                 right_stack.append([buildings[k], k+1])
#     # print("-")
#     cnt = len(left_stack) + len(right_stack)
#     if cnt == 0:
#         result.append([0])
#     else:
#         if len(left_stack) > 0 and len(right_stack) > 0:
#             left = left_stack[0][1]
#             right = right_stack[0][1]
#
#             result.append([cnt, min(left, right)])
#         elif len(right_stack) == 0:
#             result.append([cnt, left_stack[0][1]])
#         else:
#             result.append([cnt, right_stack[0][1]])
#
# for i in result:
#     print(*i)
# 문제링크: https://www.acmicpc.net/problem/22866
import sys

# sys.stdin = open("input.txt", "r")

input = sys.stdin.readline
INT_MAX = sys.maxsize

# 건물의 개수
n = int(input())

# 빌딩의 높이들
buildings = list(map(int, input().split()))

# 각 빌딩에서 볼 수 있는 빌딩의 숫자
building_count = [0] * n

# 볼 수 있는 건물중 가장 가까운 빌딩
near_building = [INT_MAX] * n

# 왼쪽 -> 오른쪽으로 탐색하면서 현재 빌딩의 높이보다 큰 빌딩들은 담는 stack
left_stack = []

for i, height in enumerate(buildings):
    # 스택에 요소들이 있고 현재 높이보다 낮은 빌딩들은 모두 제거
    while left_stack and buildings[left_stack[-1]] <= height:
        left_stack.pop()

    building_count[i] += len(left_stack)

    # 가장 가까이에 있는 빌딩 갱신
    if left_stack:
        if abs(i - left_stack[-1]) < abs(near_building[i] - i):
            near_building[i] = left_stack[-1]

    left_stack.append(i)

# 오른쪽 -> 왼쪽으로 탐색하면서 현재 빌딩의 높이보다 큰 빌딩을 담는 스택
right_stack = []

for i in range(n - 1, -1, -1):
    height = buildings[i]

    # 스택에 요소들이 있고 현재 높이보다 낮은 빌딩들은 모두 제거
    while right_stack and buildings[right_stack[-1]] <= height:
        right_stack.pop()

    building_count[i] += len(right_stack)

    # 가장 가까이에 있는 빌딩 갱신
    if right_stack:
        if abs(i - right_stack[-1]) < abs(near_building[i] - i):
            near_building[i] = right_stack[-1]

    right_stack.append(i)

for i in range(n):
    # 볼 수 있는 빌딩이 있는 경우
    if building_count[i]:
        print(building_count[i], near_building[i] + 1)
    else:
        print(0)