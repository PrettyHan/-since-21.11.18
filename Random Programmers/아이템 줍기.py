from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    graph = [[0 for _ in range(50)] for _ in range(50)] # 그래프 50x50
    queue = deque()
    queue.append((characterX, characterY))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in rectangle:
        x1, y1, x2, y2 = i # 좌표
        print("x1:",x1,"y1:",y1,"x2:",x2,"y2:",y2)
        for j in range(x1, x2+1):
            for k in range(y1, y2+1):
                graph[j][k] = 1 # 일단 직사각형 테투리 다 칠해
    while queue:
        x, y = queue.leftpop()
        answer = graph[itemX][itemY]
        break
    print(graph)
    
    return -1