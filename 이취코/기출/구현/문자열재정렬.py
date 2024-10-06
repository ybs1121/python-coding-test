n = str(input())

alpha_list = []
digit_list = []

for i in n:
    if i.isdigit():
        digit_list.append(int(i))
    else:
        alpha_list.append(i)


alpha_list.sort()

for i in alpha_list:
    print(i, end='')
print(sum(digit_list))