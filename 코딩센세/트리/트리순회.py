N = int(input())

grahp = [[] for _ in range(130)]

for _ in range(N):
    a, b, c = map(str, input().split())
    # 아스키 코드로 치환
    a = ord(a)
    b = ord(b)
    c = ord(c)

    grahp[a].append(b)
    grahp[a].append(c)


def recur(node):
    if node == 46:
        return
    print(chr(node))
    recur(grahp[node][0])
    recur(grahp[node][1])


recur(65)
