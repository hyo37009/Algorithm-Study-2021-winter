'''
내가 가지고 있는 고등학교 수학 지식으로 구현한 코드이다.
reverse의 사용법이 헷갈린다. [::-1]이 편하다.
'''

def two(num):
    list = []
    while num >= 2:
        list.append(str(num%2))
        num //= 2
    list.append(str(num))

    return (''.join(list))[::-1]

def eight(num):
    list = []

    while num >= 8:
        list.append(str(num%8))
        num //= 8
    list.append(str(num))

    return (''.join(list))[::-1]

def sth(num):
    numlist = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f']
    list = []

    while num >= 16:
        list.append(str(numlist[num%16]))
        num //= 16
    list.append(str(numlist[num%16]))

    return (''.join(list))[::-1]

n = 846

#확인용으로 내장함수와 함께 출력한다.
print('0b' + two(n))
print(bin(n))
print('0o' + eight(n))
print(oct(n))
print('0x' + sth(n))
print(hex(n))
