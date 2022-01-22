'''
출처 : 이취코파 유튜브
문제 :
    N x M 크기의 얼음틀이 있다. 구멍이 뚫린 부분은 0, 칸막이가 존재하는 부분은 1이다.
    구멍이 뚫려있는 부분끼리 상, 하, 좌, 우로 붙어있는 경우 서로 연결되어 있는 것으로 간주한다.
    이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하라.
    조건 - 난이도 별1.5/3, 풀이시간 30분, 시간제한 1초, 메모리 제한 128MB
    입력 조건:
        -첫번째 줄에 얼음 틀의 세로 길이 N과 길이 M이 주어진다. (1 <= N, M <= 1000)
        -두 번째 줄 부터 N+1번쨰 줄까지 얼음 틀의 형태가 주어진다
        -이 때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1이다.
    출력 조건 :
        -한 번에 만들 수 있는 아이스크림의 개수를 출력한다.
'''
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0: #방문하지 않은 노드만 검사한다.
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상 하 좌 우 재귀적 호출
        dfs(x - 1, y)
        dfs(x, y-1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


n, m = map(int, input().split())
graph = [list(input()) for i in range(m)]
visit = [[0] * n] * m

result = 0
for i in range(n):
    for j in range(m):
        #현재 위치에서 dfs 수행
        if dfs(i, j): #방문처리가 된 노드라면 False가 반환되므로 굳이 신경 쓸 필요가 없다
            result += 1
print(result)
