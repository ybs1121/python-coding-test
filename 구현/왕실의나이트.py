input_list = input()
print(input_list)

x = int(input_list[1]) - 1
y = ord(input_list[0]) - 97

print(x, y)

## 수평 2 수직 1  ## 수평 1 수직 1

dx = [1, 1, -1, -1, 2, 2, -2, -2]
dy = [2, -2, 2, -2, 1, -1, 1, -2]

count = 0

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx <= 7 and 0 <= ny <= 7:
        count += 1

print(count)
