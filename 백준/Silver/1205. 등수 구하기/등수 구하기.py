N, S, P = map(int, input().split())
if N > 0:
    arr = list(map(int, input().split()))
else:
    arr = []

arr.sort(reverse=True)

if len(arr) == 0:
    print(1)
else:
    rank = 1
    k = 0
    for i in range(len(arr)):
        k = i
        if S < arr[i]:
            rank += 1
        elif S > arr[i]:
            k = k - 1
            break

    if k < P - 1:
        print(rank)
    else:
        print(-1)
