import sys
sys.setrecursionlimit(10000)

N, M = map(int, sys.stdin.readline().split())
Matrix = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    Matrix[x][y] = 1
    Matrix[y][x] = 1


def DFS(node):
    visit.add(node)
    for j in range(len(Matrix[node])):
        if (Matrix[node][j] == 1) and (j not in visit):
            DFS(j)


cnt = 0
visit = set()
for i in range(1, N+1):
    if i not in visit:
        cnt += 1
        DFS(i)
print(cnt)
