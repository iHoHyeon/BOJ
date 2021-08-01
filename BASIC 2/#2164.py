
N = int(input())
L = [i for i in range(1,N+1)]
while len(L)>1:
  if  len(L)%2:
    L = [L[-1]] + L[1::2]
  else :
    L = L[1::2]
print(L[0])

