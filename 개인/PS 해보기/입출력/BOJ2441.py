## 별찍기 - 4 ##

num = int(input())
tem = num

while tem > 0:
    for i in range(num):
        if i < num - tem:
            print(' ', end='')
        else:
            print('*', end='')
    print()
    tem -= 1