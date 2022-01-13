import initlist

x = initlist.listinitiation()
n = len(x)

print('정렬 전 :', x)
left = 0
right = n - 1
last = right

while left<right:
    for j in range(right, left, -1):
        if x[j-1]>x[j]:
            x[j-1], x[j] = x[j], x[j-1]
            last = j
    left = last

    print(x)

    for j in range(left, right):
        if x[j] > x[j+1]:
            x[j], x[j+1] = x[j+1], x[j]
            last = j
    right = last

    print(x)

print('정렬 후 :', x)
