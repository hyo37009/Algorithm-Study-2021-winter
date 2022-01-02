## 별 찍기 - 12 ##
'''
체감난이도 : 쉬움
이 전에 2521번을 풀었기 때문에 금방 풀 수 있었다.
'''

n = int(input())

for line in range(1, n+1):
    for i in range(n):
        if i < n - line:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for line in range(1, n):
    for i in range(n):
        if i < line:
            print(' ', end='')
        else:
            print('*', end='')
    print()