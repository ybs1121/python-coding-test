def solution(N, stages):
    people = len(stages)
    fail_list = {}
    for i in range(1, N + 1):
        if people != 0:
            fail_list[i] = stages.count(i) / people
            people -= stages.count(i)
        else:
            fail_list[i] = 0

    return sorted(fail_list, key=lambda i: fail_list[i], reverse=True)