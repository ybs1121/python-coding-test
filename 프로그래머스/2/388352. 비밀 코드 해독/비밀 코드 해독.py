def finder(nums, start, end, ans, test_cases, counter):
    if len(nums) == 5:
        flag = True
        for i in range(len(test_cases)):
            cc = len(set(nums) & set(test_cases[i]))
            if cc != ans[i]:
                flag = False
                break
        if flag:
            counter[0] += 1  
        return

    for i in range(start, end):
        nums.append(i)
        finder(nums, i + 1, end, ans, test_cases, counter)
        nums.pop()

def solution(n, q, ans):
    counter = [0]  
    finder([], 1, n + 1, ans, q, counter)
    return counter[0]
