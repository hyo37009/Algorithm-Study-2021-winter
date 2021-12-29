## BOJ1018 체스판 다시 칠하기 ##
# 적당히 칠해진 판을 8*8로 잘라 체스판처럼 지그제그로 다시 칠하는데,
# 체스판 모양으로 만들기 위해 가장 최소로 칠하는 수를 찾는 문제

n, m = map(int, input().split(" "))
board = []
chess = [0, 0, 0, 0, 0, 0, 0, 0]
now = 0
less = 32  # 최댓값

for _ in range(n):
    board.append(input())

for i in range(n - 7): #줄검사
    for j in range(m - 7):
        for tem in range(8):
            chess[tem] = list(board[tem][j:j+8])
        for a in range(8):
            for b in range(7):
                if a != 0 & b == 0:
                    if chess[a - 1][0] == chess[a][0]:
                        now += 1
                        chess[a][0] = 'B' if chess[a - 1][0] != 'B' else 'W'
                if chess[a][b] == chess[a][b + 1]:
                    now += 1
                    chess[a][b + 1] = 'B' if chess[a][b + 1] != 'B' else 'W'
        if now < less: less = now
        now = 0

print(less)
