import sys

N = int(input())
L = []
for _ in range(N):
  L.append(list(sys.stdin.readline().split()))

L.sort(key = lambda x : int(x[0]))

for i in L : 
  print(i[0],i[1])

