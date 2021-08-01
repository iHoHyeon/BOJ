import sys

K = int(sys.stdin.readline())
L = []
for _ in range(K):
  temp = int(sys.stdin.readline())
  if temp == 0:
    L.pop()
  else : 
    L.append(temp)
  
print(sum(L))