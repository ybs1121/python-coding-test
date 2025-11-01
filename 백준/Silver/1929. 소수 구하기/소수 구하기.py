import math

def is_prime_number(num):
    if num == 0 or num == 1:
        return False

    if num == 2:
        return True

    if num % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    else:
        return True


M, N = map(int, input().split())

for i in range(M, N + 1):
    if is_prime_number(i):
        print(i)