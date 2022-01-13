## 별찍기 - 5 ##

n = int(input())

for line in range(n):
    for _ in range(n - line - 1):
        print(' ', end='')
    for _ in range((line + 1) * 2 - 1):
        print('*', end='')
    print()
