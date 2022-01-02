## 별찍기 - 8 ##
n = int(input())

for line in range(1, n+1):
    for i in range(n*2):
        if line <= i < n*2 - line:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for line in range(1, n+1):
    for i in range(n*2):
        if n-line <= i < n + line:
            print(' ', end='')
        else:
            print('*', end='')
    print()
