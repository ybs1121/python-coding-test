# input
# a1 -> 2
# c2 -> 6
point = input()

# 좌표 치환
x = int(point[1]) - 1
y = ord(point[0]) - 97


# 나이트가 움직을 수 있는 방법
nx = [-2, -2, -1, -1, 2, 2, 1, 1]
ny = [1, -1, 2, -2, 1, -1, 2, -2]

answer = 0

print(x,y)

for i in range(8):
    dx = x + nx[i]
    dy = y + ny[i]

    if 0 <= dx < 8 and 0 <= dy < 8:
        answer += 1

print(answer)

