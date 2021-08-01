# BFS 공부하기


dx = [-1,0,0,1]
dy = [0,-1,1,0]

def bfs(x,y):
  queue = [[x,y]]
  while queue:
    a, b =queue[0][0],queue[0][1]
    del queue[0]
    for i in range(4):
      q = a + dx[i]
      w = b + dy[i]
      if 0<= q < N and 0<= w < M and L[q][w] == 1:
        L[q][w] = 0
        queue.append([q,w])

T = int(input())
for _ in range(T):
  M, N, K = map(int,input().split())
  cnt = 0
  L = [[0 for _ in range(M)] for _ in range(N)]

  for _ in range(K):
    x, y = map(int,input().split())
    L[y][x] = 1
  
  for i in range(N):
    for j in range(M):
      if L[i][j] == 1 :
        bfs(i,j)
        L[i][j] = 0
        cnt += 1
  print(cnt)
