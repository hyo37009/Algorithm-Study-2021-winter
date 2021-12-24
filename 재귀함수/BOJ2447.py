## BO2447 별찍기 - 10 ##
## 오늘은 이거 푼다... -크리스마스 이브에-



def star(n):
    if n == 1:
        print('*', end='')
    else:
        for _ in range(3):
            star(n - 1)
        print()
        star(n - 1)
        star2(n - 1)
        star(n - 1)
        print()
        for _ in range(3):
            star(n - 1)
        print()


def star2(n):
    if n == 1:
        print(' ', end='')
    else:
        for _ in range(3):
            for _ in range(3):
                star2(n - 1)
            print()


star(3)
