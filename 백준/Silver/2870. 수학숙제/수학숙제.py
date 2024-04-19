

M = int(input())
result = []
for _ in range(M):
    stack = []

    s = input()
    # print(s)

    for i in s:
        if i.isdigit():
            stack.append(i)
        else:
            if len(stack) > 0:
                num_str = "".join(stack)
                result.append(int(num_str))
                stack = []

    if len(stack) > 0:
        num_str = "".join(stack)
        result.append(int(num_str))



result.sort()

for i in result:
    print(i)

