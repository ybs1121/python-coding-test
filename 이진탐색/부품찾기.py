import time
n = int(input())
data = list(map(int, input().split()))

m = int(input())
needs = list(map(int, input().split()))

data.sort()
print(data)
start = 0
end = n
result = []
for need in needs:
    flag = False
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2
        if need == data[mid]:
            flag = True
            result.append("YES")
            break

        elif data[mid] > need:
            end = mid - 1

        elif data[mid] < need:

            start = mid + 1


        print(mid)
        time.sleep(1)

    print("out")
    if not flag:
        result.append("NO")


print(result, sep = " ")





