import initlist

x = initlist.listinitiation()
n = len(x)

print('정렬 전 :', x)

print('버블 정렬 시작')
n = len(x)
for i in range(n-1):
    for j in range(n-1, i, -1):
        if x[j-1] > x[j]:
            x[j-1], x[j] = x[j], x[j-1]
    print(f'현재({i}) :', x)

print('정렬 후 :', x)