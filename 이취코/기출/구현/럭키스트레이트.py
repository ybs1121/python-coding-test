n = str(input())

if len(n) % 2 == 0:

    mid_idx = len(n) // 2

    front = 0

    end = 0

    for i in n[:mid_idx]:
        front += int(i)
    for i in n[mid_idx:]:
        end += int(i)
    if front == end:
        print("LUCKY")
    else:
        print("READY")
else:
    print("READY")
