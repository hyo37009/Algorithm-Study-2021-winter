import random

n = random.randrange(5, 15)
x = []
for i in range(n):
    x.append(random.randrange(1, 25))

print(f'n = {n}')
print('정렬 전:', x)
i = 0
while i < n - 1:
    last = n-1
    for j in range(n - 1, i, -1):
        if x[j - 1] > x[j]:
            x[j - 1], x[j] = x[j], x[j - 1]
            last = j
    i = last
    print(f'i = {i}, x =', x)
print(f'n-1 = {n-1}')
print('정렬 후:', x)
