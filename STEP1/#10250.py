from math import ceil

T = int(input())
for _ in range(T):
  H,W,N = map(int,input().split())
  j = N%H if N%H != 0 else H
  i = ceil(N/H) 
  print(100*j+i)