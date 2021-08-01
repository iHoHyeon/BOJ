import sys

S = set()
M = int(sys.stdin.readline())
for _ in range(M):
    com = sys.stdin.readline().rstrip().split()
    if com[0] == 'all':
        S = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
             12, 13, 14, 15, 16, 17, 18, 19, 20}
        continue
    if com[0] == 'empty':
        S = set()
        continue
    x = int(com[1])
    if com[0] == 'add':
        S.add(x)
    elif com[0] == 'remove':
        S.discard(x)
    elif com[0] == 'check':
        print(1 if x in S else 0)
    elif com[0] == 'toggle':
        if x in S:
            S.discard(x)
        else:
            S.add(x)
