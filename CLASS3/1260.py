##DFS and BFS
N, M, V = map(int,input().split())
matrix = [[0]*(N+1) for _ in range(N+1)]
## 행렬의 (a,b) = 1이면 a,b는 연결되어있다
for _ in range(M):
  x,y = map(int,input().split())
  matrix[x][y] = 1
  matrix[y][x] = 1

def DFS(visit, start_node):
  visit += [start_node]
  for i in range(len(matrix[start_node])):
    if matrix[start_node][i] == 1 and (i not in visit):
      DFS(visit,i)      
  return visit

def BFS(start_node):
  visit = [start_node]
  queue = [start_node]
  while queue:
    n = queue.pop(0) ##들어온 순서대로 pop
    for i in range(len(matrix[n])):
      if matrix[n][i] == 1 and (i not in visit) :
        queue.append(i)
        visit.append(i)
  return visit

print(*DFS([],V))
print(*BFS(V))