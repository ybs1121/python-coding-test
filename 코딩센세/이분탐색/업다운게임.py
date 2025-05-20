N = int(input())
arr1 = sorted(list(map(int, input().split())))

M = int(input())
arr2 = list(map(int, input().split()))

for num in arr2:
    s = 0
    e = N - 1

    mid = (s + e) // 2
    flag = False
    while s < e:

        if arr1[mid] > num:
            e = mid - 1
        elif arr1[mid] < num:
            s = mid + 1
        else:
            flag = True
            break

    if flag:
        print(1, end=" ")
    else:
        print(0, end=" ")
