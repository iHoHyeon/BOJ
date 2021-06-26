import sys
K, N = map(int,sys.stdin.readline().split())
L = [int(sys.stdin.readline()) for _ in range(K)] 

start , end = 1, max(L) 

while start <= end :
  mid = (start+end)//2
  lines = 0
  for i in L:
    lines += i//mid
  
  if lines >= N :
    start = mid + 1
  else : 
    end = mid - 1
print(end)

#이분탐색