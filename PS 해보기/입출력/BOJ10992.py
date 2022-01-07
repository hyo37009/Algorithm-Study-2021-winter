## 별 찍기 - 17 ##
"""
난이도 : 하
별찍기 16 응용이라 쉬움
출력형식을 어디까지 맞춰야하나 싶어서 헷갈림
"""

num = int(input())

for line in range(1, num+1):
    for _ in range(num - line):
        print(' ', end='')
    if line == num:
        for _ in range(num * 2 - 1):
            print('*', end='')
    elif line == 1:
        print('*', end='')
    else:
        print('*', end='')
        for _ in range((line-1)*2-1):
            print(' ', end='')
        print('* ', end='')
    print()
