T = int(input())
for _ in range(T):
  N,M = map(int,input().split())
  L = list(map(int,input().split()))
  L.reverse()
  while(1):
    if max(L)==