import sys

N = int(input())
L = []
for _ in range(N):
    L.append(list(map(int,sys.stdin.readline().split())))
    
L.sort(key = lambda x : (x[1],x[0]))
for i in L:
    print(i[0],i[1])