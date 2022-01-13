## BOJ2231 분해합 ##

# 분해합 : n + n을 이루는 각 자리수의 합

n = int(input())
num = 0

while num < n:
    tem = 0
    for i in str(num):
        tem += int(i)
    tem += num

    if tem == n:
        print(num)
        break
    if num + 1 == n:
        print(0)
    num += 1

