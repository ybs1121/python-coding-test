n = list(map(int, input().split()))[0]  # Convert map object to list and access the first element
data = list(map(str, input().split()))

nx = [1, -1, 0, 0]
ny = [0, 0, -1, 1]
ways = ['D', 'U', 'L', 'R']

result_x = 1
result_y = 1

for i in data:
    index = ways.index(i)
    if (nx[index] + result_x) < 1 or (nx[index] + result_x) > n:
        continue
    if (ny[index] + result_y) < 1 or (ny[index] + result_y) > n:
        continue

    result_x += nx[index]
    result_y += ny[index]

    print(result_x, result_y, sep=" ")


print(result_x, result_y, sep=" ")