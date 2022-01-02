## 별찍기 - 9 ##
"""
난이도 : 하
그.. 반전시키는게 조금 헷갈린다.
그 외엔 괜찮다.
"""

n = int(input())

for line in range(1, n + 1):
    for i in range(n * 2 - 1):
        if i < line -1 :
            print(' ', end='')
        elif i < n * 2 - line:
            print('*', end='')

    print(' ')

for line in range(1, n):
    for i in range(n * 2 - 1):
        if i < n - line - 1:
            print(' ', end='')
        elif i < n * 2 - n + line:
            print('*', end='')
    print(' ')
