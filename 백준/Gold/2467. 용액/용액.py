import sys

input = sys.stdin.readline

N = int(input())
liquids = list(map(int, input().split()))

answer_a = liquids[0]
answer_b = liquids[-1]

start = 0
end = len(liquids) - 1

answer = abs(answer_a + answer_b)

while start < end:

    mix_liquids = liquids[start] + liquids[end]

    if mix_liquids == 0:
        answer_a = liquids[start]
        answer_b = liquids[end]
        break
    elif answer >= abs(mix_liquids):
        answer = min(answer, abs(mix_liquids))
        answer_a = liquids[start]
        answer_b = liquids[end]
        if mix_liquids < 0:
            start += 1
        else:
            end -= 1
    else:
        if mix_liquids < 0:
            start += 1
        else:
            end -= 1

liquids = [answer_a, answer_b]
liquids.sort()
print(liquids[0], liquids[-1])
