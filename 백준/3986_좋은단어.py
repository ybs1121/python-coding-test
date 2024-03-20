N = int(input())
result = 0
for i in range(N):
    arr = str(input())

    if len(arr) % 2 != 1:
        stack = []
        for j in arr:
            if len(stack) == 0:
                stack.append(j)

            else:
                letter = stack.pop()

                if letter != j:
                    stack.append(letter)
                    stack.append(j)

        if len(stack) == 0:
            result += 1
print(result)

