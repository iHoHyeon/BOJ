import sys

N = int(input())
L = []
for _ in range(N):
    L.append(list(map(int,sys.stdin.readline().split())))
    
L.sort(key = lambda x : (x[0],x[1]))
for i in L:
    print(i[0],i[1])