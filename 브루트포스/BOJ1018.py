## BOJ1018 체스판 다시 칠하기 ##
# 적당히 칠해진 판을 8*8로 잘라 체스판처럼 지그제그로 다시 칠하는데,
# 체스판 모양으로 만들기 위해 가장 최소로 칠하는 수를 찾는 문제
def chess(now=[])->int:
    stWhi = 0  # 화이트로 시작하는 체스판 검사
    stBla = 64  # 블랙으로 시작하는 체스판 검사
    pre = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]  # 체스판 설정(흰색 시작)

    # 검사 시작
    for a in range(8):
        for b in range(8):
            if now[a][b] != pre[a][b]:
                stWhi += 1
                stBla -= 1

    return stWhi if stWhi < stBla else stBla


n, m = map(int, input().split(" "))
board = []
less = 32
nowlist = []

for k in range(n):
    board.append(input())
    board[k] = list(board[k])

for i in range(n-7):
    for j in range(m-7):
        for k in range(8):
            nowlist.append(board[i+k][j:j+9])
        nowless = chess(nowlist)
        if less > nowless:
            less = nowless
        nowlist = []

print(less)