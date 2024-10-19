import sys

input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))  # +, -, *, //

maximum = -1e9
minimum = 1e9


def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)


dfs(1, num[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)

n = int(input())
nums = list(map(int, input().split()))
operator = list(map(int, input().split()))

max_num = - 1_000_000_001
min_num = 1_000_000_001


def how_to_cal(option, n1, n2):
    if option == 0:
        return n1 + n2
    elif option == 1:
        return n1 - n2
    elif option == 2:
        return n1 * n2
    elif option == 3:
        return int(n1 / n2)


max_idx = len(nums)


def cal(num, operator, next_num_idx):
    global max_num
    global min_num

    if sum(operator) == 0 or next_num_idx >= max_idx:  ## 사용 다했으면
        max_num = max(max_num, num)
        min_num = min(min_num, num)
        return

    for i in range(4):
        if operator[i] > 0:
            cal_num = how_to_cal(i, num, nums[next_num_idx])
            operator[i] = operator[i] - 1
            cal(cal_num, operator, next_num_idx + 1)
            operator[i] = operator[i] + 1


cal(nums[0], operator, 1)

print(max_num)
print(min_num)

