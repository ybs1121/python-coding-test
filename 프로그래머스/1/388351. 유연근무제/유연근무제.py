def limit_schedule(schedule):
    hours = schedule // 100
    minutes = (schedule % 100) + 10

    if minutes >= 60:
        minutes = minutes % 60
        hours = hours + 1
    return hours * 100 + minutes


def is_holiday(date):
    if date == 6 or date == 7:
        return True
    else:
        return False


def solution(schedules, timelogs, startday):
    answer = 0

    logs = [[False] * 5 for _ in range(len(schedules))]

    # 목표한 시간에 도착 했냐
    for i in range(len(schedules)):
        time = limit_schedule(schedules[i])
        day = startday

        for j in range(len(timelogs[i])):
            if is_holiday(day):
                day += 1
                if day > 7:
                    day = 1
            else:
                if timelogs[i][j] <= time:
                    logs[i][day - 1] = True
                day += 1

    # print(logs)

    for log in logs:
        if False not in log:
            answer += 1

    return answer