candy = int(input())

answer = 0
for i in range(1, candy + 1):
    A = i
    for j in range(A, candy + 1):
        B = j
        C = candy - A - B

        case_1 = A + 2 <= B
        case_2 = A + B + C == candy
        case_3 = C % 2 == 0
        case_4 = A > 0 and B > 0 and C > 0

        if case_1 and case_2 and case_3 and case_4:
            answer += 1

print(answer)
