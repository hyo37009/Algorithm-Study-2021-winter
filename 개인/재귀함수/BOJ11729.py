## BOJ11729 하노이 탑 이동순서 ##
tot = 0
list = []
def hnoi(f, t, n):
    list.append("{} {}".format(f, t)) #가장 큰 것 목표호 옮김
    for i in [1,2,3]:
        if i not in [f, t]:



hnoi(1, 3, 3)
print(tot)
