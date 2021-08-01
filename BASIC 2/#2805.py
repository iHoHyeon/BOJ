import sys
N,M = map(int,sys.stdin.readline().split())
L = list(map(int,sys.stdin.readline().split()))
H = max(L)-1
S = 1
while S <= H : 
  mid = (S+H)//2
  sum = 0
  for i in L:
    if i > mid:
      sum += i-mid
  if sum >= M :
    S = mid +1
  elif sum < M :
    H = mid -1

print(H)