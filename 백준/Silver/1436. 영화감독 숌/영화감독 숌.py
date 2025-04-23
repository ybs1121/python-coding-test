n = int(input())

i = 0
cnt = 0
answer = ''
while True:
    i += 1
    if '666' in str(i):
       cnt += 1
    if cnt == n:
        answer = str(i)
        break

print(answer)
        