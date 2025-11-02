import sys

input = sys.stdin.readline

n = int(input())
answer = 0
for i in range(n):
    word = input()
    prev = word[0]
    for j in range(0, len(word) - 1):
        if prev == word[j + 1]:
            continue
        else:
            if prev in word[j + 1:]:
                break
            else:
                prev = word[j + 1]
    else:
        answer += 1

print(answer)
