## 2007년 ##

num = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
dic = {}
n = 0

for i in range(12): # 무슨 요일으로 시작하는지 인덱스로 기록
    if i == 0:
        dic[i+1] = n
    else:
        n += num[i-1] % 7
        if n >= 7:
            n -= 7
        dic[i + 1] = n

x, y = map(int, input().split(' '))

y %= 7
y += dic[x]
if y >= 7:
    y -= 7
print(day[y - 1])