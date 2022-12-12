from collections import deque
import sys

input = sys.stdin.readline
n,m = map(int, input().split())
graph = [list(map(str, input().strip())) for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()

    for i in range(m):
        for j in range(n):
            if graph[i][j] == "J":
                queue.append((i,j))
            if graph[i][j] == "F":
                queue.append((i,j))
    # 불 사람 불 사람
    while queue:
        x, y = queue.popleft() # J 좌표
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 pass
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            # 벽 pass
            if graph[nx][ny] == "#":
                continue
            # 불 확산
            if graph[x][y] == "F" and graph[nx][ny] == ".":
                graph[nx][ny] = graph[x][y]
                queue.append((nx, ny))
            # 도망가
            if graph[x][y] == "J" and graph[nx][ny] == ".":
                graph[nx][ny] = "J"
                queue.append((nx, ny))  
    return graph
'''
    for index, row in enumerate(graph):
        if index == 0 and "J" in row:
            return turn
        if index < (len(graph) -1) and row[0] == "J" or row[-1] == "J":
            return turn
        if index == (len(graph) -1) and "J" in row:
            return turn
'''

print(bfs())