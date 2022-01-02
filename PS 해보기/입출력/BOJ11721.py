## 열 개씩 끊어 출력하기 ##

a = input()
n = 0

for i in range(len(a)):
    print(a[i], end='')
    if (i + 1) % 10 == 0 : #왠지 and로 합치면 동작을 안한다...
        if i == 0:
            continue
        print()