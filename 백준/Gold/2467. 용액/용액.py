N = int(input())

liquid_list = list(map(int,input().split()))

liquid = 1e10
start = 0
end = len(liquid_list) - 1
result_b = 0

while start < end:


    temp_liquid = liquid_list[start] + liquid_list[end]
    if temp_liquid == 0:
        result_a = start
        result_b = end
        break

    if abs(temp_liquid) < abs(liquid):
        # 새로운 용액이 더 0에 가까움
        result_a = start
        result_b = end
        liquid = temp_liquid

    if temp_liquid < 0:
        start += 1
    elif temp_liquid > 0:
        end -= 1


print(liquid_list[result_a], liquid_list[result_b], sep= " ")

