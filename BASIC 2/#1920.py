import sys
N = int(sys.stdin.readline())
A = set(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int,sys.stdin.readline().split()))

for i in B:
  print(1 if i in A else 0)

# list의 in 탐색 : O(n)
# 이분탐색 : O(log n)
# set,dictionary의 in 탐색 : O(1)

def binary(start,end,An,i):
  if start > end :
    return 0 
  mid = (start+end)//2
  if i == An[mid]:
    return 1
  elif i < An[mid]:
    return binary(start,mid-1,An,i)
  else :
    return binary(mid+1,end,An,i)
  
import sys
N = int(sys.stdin.readline())
A = sorted(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int,sys.stdin.readline().split()))

for i in B :
  start = 0
  end = len(A) - 1
  print(binary(start,end,A,i))