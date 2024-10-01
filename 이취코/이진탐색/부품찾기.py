n = int(input())
parts = list(map(int, input().split()))
parts.sort()
m = int(input())
req_parts = list(map(int, input().split()))

answer = []
def binary_search(start, end, target, parts):
    while start <= end:
        # 인덱스
        mid = (start + end) // 2

        if parts[mid] == target:
            return "yes"

        elif parts[mid] < target:
            start = mid + 1
        elif parts[mid] > target:
            end = mid - 1

    return "no"


for req_part in req_parts:
    answer.append(binary_search(0, n, req_part, parts))


for a in answer:
    print(a, end=" ")