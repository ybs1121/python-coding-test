n = int(input())
data = []
for i in range(n):
    split = input().split()
    data.append((str(split[0]),int(split[1])))


data.sort(key=lambda stduent: stduent[1])

print(data)
