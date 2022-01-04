## BOJ1436 영화감독 숌 ##

num = int(input())

n = 0
all = 0

while all != num:
    n += 1
    count = 0
    nu = list(str(n))
    for i in range(len(nu)):
        if nu[i] != '6':
            count = 0
            continue
        if count != 0:
            if nu[i-1] != nu[i]:
                count == 0
                continue
        count += 1
        if count == 3:
            all += 1
            if all == num:
                print(''.join(nu))
            break

