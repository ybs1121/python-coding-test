# 알파벳이 한번 나왔다가 다른 알파벳으로 바꼈다가 다시 나올 수 없다.

n = int(input())
words = []
for i in range(n):
    word = input()
    words.append(word)
answer = 0


for word in words:
    use_chars = []
    flag = True
    for char in word:
        if not use_chars or use_chars[-1] == char:
            use_chars.append(char)
        elif char in use_chars or 97 > ord(char)  or ord(char) > 127:
            flag = False
            break
        else:
            use_chars.append(char)

    if flag:
        answer += 1

print(answer)
