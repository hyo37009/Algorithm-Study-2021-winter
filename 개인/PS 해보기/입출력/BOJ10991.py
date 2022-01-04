## 별 찍기 - 16 ##
'''
난이도 : 하
쉬워서 금방 했다
'''

num = int(input())

for line in range(1, num+1):
    for _ in range(num - line):
        print(' ', end='')
    for _ in range(line):
        print('* ', end='')
    print()
