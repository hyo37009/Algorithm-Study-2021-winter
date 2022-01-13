## BOJ2798 블랙잭 ##

# 규칙 : 카드 합이 21을 넘지 않는 한도 내에서 가장 크게 만들기
# 규칙+ : 카드에는 양의 정수. 딜러는 N장의 카드를 펼치고 숫자 M을 외침.
#        M을 넘지 않는 선에서 M과 가장 가깝게 만들기 (3합 출력)

n, m = map(int, input().split())
card = list(map(int, input().split()))

card.sort()
close = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if close < (card[i] + card[j] + card[k]) <= m:
                close = card[i] + card[j] + card[k]

print(close)
