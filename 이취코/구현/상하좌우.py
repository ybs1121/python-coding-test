#input
# 5
# R R R U D D

n = int(input())
commands = list(map(str, input().split()))

x, y = 0, 0

# R, L , U, D
nx = [0, 0, -1, 1]
ny = [1, -1, 0, 0]
for command in commands:
    dx = -1
    dy = -1

    if command == "R":
        dx = x + nx[0]
        dy = y + ny[0]

    elif command == "L":
        dx = x + nx[1]
        dy = y + ny[1]

    elif command == "U":
        dx = x + nx[2]
        dy = y + ny[2]

    elif command == "D":
        dx = x + nx[3]
        dy = y + ny[3]

    if 0 <= dx < n and 0 <= dy < n:
        x = dx
        y = dy

print(x + 1, end=" ")
print(y + 1, end=" ")
