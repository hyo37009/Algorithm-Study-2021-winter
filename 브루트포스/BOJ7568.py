## BOJ7568 덩치 ##
# 큰 덩치의 사람만 세서 등수를 매김.
import operator

n = int(input())
people = []
bigger = {}
rank = []

for _ in range(n): #입력
    people.append(list(map(int, input().split())))
    bigger[_] = 0
    rank.append(0)

for i in range(n):
    for j in range(n):
        if i == j:
            continue

        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            bigger [i] += 1


for i in range(n):
    print(bigger[i]+1, end=' ')
