A, B, C, D, E, F = map(int, input().split())

for x in range(-10_000, 10_001):
    for y in range(-10_000, 10_001):
        f1 = A * x + B * y == C
        f2 = D * x + E * y == F

        if f1 and f2:
            print(x, y)
            break
