import sys

N= int(sys.stdin.readline())

A = list(map(int,sys.stdin.readline().split()))

for i in range(N):
  L = A[i+1:] +[0]
  for j in L:
    if max(L) <= A[i]:
      print(-1, end=' ')
      break
    if A[i] < j:
      print(j,end =' ')
      break

