A=int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

min_price = price[0] #최소 가격을 첫 번째 인덱스로 설정
answer = 0

for i in range(A-1): #마지막 인덱스 제외하고 반복문 수행
  if min_price>price[i]: #현재 인덱스값이 최솟값보다 작으면 min_price 바꿔줌
    min_price = price[i]
  answer+=min_price*distance[i] #현재 인덱스 거리값과 최솟값을 곱해줌
print(answer)