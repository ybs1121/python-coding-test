n = int(input())

result = 0

hh = 0
mm = 0
ss = 0

for i in range(n+1):
    print(i)
    for j in range(60):
        for k in range(60):
            times = str(i) + str(j) + str(k)
            if '3' in times:
                result += 1


print(result)