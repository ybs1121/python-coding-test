import sys

input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
kind_cards = list(map(int, input().split()))

dic = {}

for i in kind_cards:
    dic[i] = 0

for card in cards:
    if dic.get(card) is None:
        continue
    else:
        dic[card] = dic[card] + 1

for i in kind_cards:
    print(dic[i], end=' ')
