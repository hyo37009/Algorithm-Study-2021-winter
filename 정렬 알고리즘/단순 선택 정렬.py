import initlist

x = initlist.listinitiation()
n = len(x)

print('정렬 전 :', x)
for i in range(n - 1):
    min = i
    for j in range(i + 1, n):
        if x[j] < x[min]:
            min = j
    x[i], x[min] = x[min], x[i]
    print(x)
print('정렬 후 :', x)