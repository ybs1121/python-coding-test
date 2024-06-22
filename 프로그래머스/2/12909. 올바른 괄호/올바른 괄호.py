def solution(s):
    answer = True
    
    temp_stack = []
    for i in s:
        if len(temp_stack) == 0:
            if i == '(':
                temp_stack.append(i)
            else:
                return False
        else:
            if i == ')':
                if temp_stack[-1] == '(':
                    temp_stack.pop()
            else:
                temp_stack.append(i)
    if len(temp_stack) > 0:
        return False
    return True