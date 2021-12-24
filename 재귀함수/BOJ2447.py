## BO2447 별찍기 - 10 ##
## 오늘은 이거 푼다... -크리스마스 이브에-

global count
count = 0

def r(n):
    r1(n)
    r2(n)
    r1(n)


def r1(n):
    global count
    if n == 0:
        print('*', end='')
        count += 1
        if count == n * 3:
            print()
            count = 0
        return
    else:
        for _ in range(n*3):
            r1(n//3)



def r2(n):
    r1(n//3)
    g(n//3)
    r1(n//3)



def g(n):
    global count
    if n == 0:
        print(' ', end='')
        count += 1
        if count == n * 3:
            print()
            count = 0
        return
    else:
        for _ in range(n*3):
            g(n//3)

r(3)