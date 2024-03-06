### 시간조과
# T = int(input())
# result = []
# for i in range(T):
#     n = int(input())
#     stock_price = list(map(int, input().split()))
#     diff_amt = 0
#     for i in range(n):
#         max_diff = -1
#         for j in range(i + 1, n):
#             if stock_price[i] < stock_price[j]:
#                 # print(stock_price[j])
#                 max_diff = max(max_diff, stock_price[j] - stock_price[i])
#         if max_diff > 0:
#             diff_amt += max_diff
#
#     result.append(diff_amt)
#
# for i in result:
#     print(i)

###
# T = int(input())
# result = []
# for i in range(T):
#     n = int(input())
#     stock_price = list(map(int, input().split()))
#     temp = []
#     diff_amt = 0
#     # print("--")
#     for j in range(1, n):
#         if stock_price[j - 1] <= stock_price[j]:
#             temp.append(stock_price[j - 1])
#             # print(temp)
#         else:
#             # print(stock_price[j - 1])
#             temp.append(stock_price[j - 1])
#             # print(temp)
#             for k in temp[:-1]:
#                 diff_amt += (temp[-1] - k)
#
#             temp = []
#             # temp.append(stock_price[j])
#
#
#     temp.append(stock_price[-1])
#     if len(temp) > 0:
#         for k in temp[:-1]:
#             if temp[-1] >= temp[-2]:
#                 diff_amt += (temp[-1] - k)
#     result.append(diff_amt)
#
# for i in result:
#     print(i)
    #  반례
    # 1
    # 6
    # 1 2 3 2 4 1


T = int(input())
result = []
for i in range(T):
    n = int(input())
    stock_price = list(map(int, input().split()))
    diff_amt = 0
    # print(n)
    # print("-")
    max_value = max(stock_price)
    # print(max_value)
    for j in range(n-1):
        # print(max_value)
        # print(stock_price[j])
        # print("-")
        if stock_price[j] < max_value:
            diff_amt += (max_value - stock_price[j])
        else:
            max_value = max(stock_price[j + 1:])
        # print(max_value)
        # print(diff_amt)
    # print("-----------")
    result.append(diff_amt)
    # print(result)

for i in result:
    print(i)