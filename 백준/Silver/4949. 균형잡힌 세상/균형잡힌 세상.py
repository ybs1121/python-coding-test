while True:
    str = input()
    check = []  # 괄호를 체크하기 위한 배열
    answer = 'yes'
    if str == '.':
        break
    stack = []

    for s in str:
        # print("-")
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if len(stack) == 0:
                answer = 'no'
                break
            pop_str = stack.pop()
            if pop_str == '(':
                continue
            else:
                answer = 'no'
                break
        elif s == ']':

            if len(stack) == 0:
                answer = 'no'
                break
            pop_str = stack.pop()
            if pop_str == '[':
                continue
            else:
                answer = 'no'
                break
        elif s == '.':
            if len(stack) != 0:
                answer = 'no'

            break
    print(answer)

