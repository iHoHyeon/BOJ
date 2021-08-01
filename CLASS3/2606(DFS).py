def dfs(visit, node):
    visit.append(node)

    for i in range(len(net[node])):
        if net[node][i] == 1 and (i not in visit):
            dfs(visit, i)
    return visit


N = int(input())
T = int(input())
net = [[0]*(N+1) for _ in range(N+1)]
for _ in range(T):
    x, y = map(int, input().split())
    net[x][y] = 1
    net[y][x] = 1
visit = []
print(len(dfs(visit, 1))-1)
