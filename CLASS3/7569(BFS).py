
M, N, H = map(int, input().split())
queue = []
non = set()
for h in range(H):
    for n in range(N):
        temp = list(map(int, input().split()))
        for m in range(M):
            if temp[m] == 1:
                queue.append((h, n, m))
            elif temp[m] == 0:
                non.add((h, n, m))

day = -1
dx = [0, 0, -1, 1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def BFS(queue):
    new_queue = []
    while queue:
        (z, y, x) = queue.pop()
        for i in range(6):
            X = x + dx[i]
            Y = y + dy[i]
            Z = z + dz[i]
            if (Z, Y, X) in non:
                non.remove((Z, Y, X))
                new_queue.append((Z, Y, X))
    return new_queue


while queue:
    queue = BFS(queue)
    day += 1

print(day if non == set() else -1)
