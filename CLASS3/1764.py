import sys

N, M = map(int, sys.stdin.readline().split())

D = []
DB = []

for _ in range(N):
    D.append(sys.stdin.readline())

Ds = set(D)

for _ in range(M):
    temp = sys.stdin.readline()
    if temp in Ds:
        DB.append(temp)

print(len(DB))
DB.sort()
print(''.join(map(str, DB)))
