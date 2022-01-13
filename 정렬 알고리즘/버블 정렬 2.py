import initlist

x = initlist.listinitiation()
n = len(x)

print(f'n = {n}')
print('정렬 전 :', x)
for i in range(n):
    chan = 0
    for j in range(n-1, i, -1):
        if x[j-1] > x[j]:
            x[j-1], x[j] = x[j], x[j-1]
            chan += 1
    print(f'{i}번째 :', x)
    if chan == 0:
        break
print('정렬 후:', x)