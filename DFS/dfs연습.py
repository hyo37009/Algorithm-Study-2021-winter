def DFS(v):
    '''
    :param v: vertex, 노드
    :return:
    '''
    if v > 7:
        return
    else: # 밑 양쪽 노드 호출
        print(v)
        DFS(v * 2)
        DFS(v * 2 + 1)

if __name__ == '__main__':
    DFS(1)