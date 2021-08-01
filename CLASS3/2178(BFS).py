from collections import deque

N, M = map(int, input().split())
Map = []
for _ in range(N):
    Map.append(list(map(int, input())))
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]
            if (0 <= X < N) and (0 <= Y < M):
                if Map[X][Y] == 1:
                    Map[X][Y] = Map[x][y] + 1
                    queue.append((X, Y))


BFS(0, 0)
print(Map[N-1][M-1])

# while queue:
#     x, y = queue[0][0], queue[0][1]
#     del queue[0]
#     for i in range(4):
#         X = x + dx[i]
#         Y = y + dy[i]
#         if 0 <= X < N and 0 <= Y < M and Map[X][Y] == "1":
#             queue.append([X, Y])
#             Map[X][Y] = Map[x][y] + 1
# print(Map[N-1][M-1])
