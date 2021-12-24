## BO2447 별찍기 - 10 ##
## 오늘은 이거 푼다... -크리스마스 이브에-


def r(n):
    r1(n)
    r2(n)
    r1(n)


def r1(n):
    if n == 1:
        for _ in range(3):
            print('*', end='')
        return
    else:
        for _ in range(n*3):
            r1(n//3)
        print()
        for _ in range(n*3):
            r2(n//3)
        print()
        for _ in range(n*3):
            r1(n//3)
        print()


def r2(n):
    if n == 1:
        print('* *', end='')
        return
    else:
        for _ in range(n//3):
            r1(n//3)
            g(n//3)
            r1(n//3)
        print()
        for _ in range(n//3):
            r2(n//3)
            g(n//3)
            r2(n//3)
        print()
        for _ in range(n//3):
            r1(n//3)
            g(n//3)
            r1(n//3)
        print()



def g(n):
    if n == 1:
        print('   ', end='')
    else:
        for _ in range(n//3):
            g(n//3)
    print()

r(9)