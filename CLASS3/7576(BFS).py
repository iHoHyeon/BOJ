M, N = map(int, input().split())

queue = []
non = set()

for n in range(N):
    temp = list(map(int, input().split()))
    for m in range(M):
        if temp[m] == 1:
            queue.append((n, m))
        elif temp[m] == 0:
            non.add((n, m))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(queue):
    new_queue = []
    while queue:
        (y, x) = queue.pop()
        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]
            if (Y, X) in non:
                new_queue.append((Y, X))
                non.remove((Y, X))
    return new_queue


day = -1
while queue:
    queue = bfs(queue)
    day += 1

print(day if non == set() else -1)
