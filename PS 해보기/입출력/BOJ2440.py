## 별 찍기 - 3 ##

num = int(input())

while num > 0:
    for _ in range(num):
        print('*', end='')
    print()
    num -= 1