def solution(players, m, k):
    answer = 0
    sch = dict()

    for i in range(0, 24):
        sch[i] = players[i]



    current_server = 0

    timer = []

    for i in range(0, 24):
        if sch[i] > current_server * m:
            avb = current_server * m  # 가용인원

            extra_server = (sch[i] - avb) // m  # 증설해야하는 수

            current_server += extra_server  # 현재 서버 갯수 추가

            answer += extra_server  # 정답 증가

            for j in range(extra_server):
                timer.append(k)

        # 서버 반납해야하는거 있으면 확인 후 반납
        for i in range(len(timer) - 1, -1, -1):  # 뒤에서 앞
            timer[i] -= 1
            if timer[i] == 0:
                del timer[i]
                current_server -= 1

    return answer


