T = int(input())

for _ in range(T):
  x,y = map(int,input().split())
  k = 1
  L = y-x
  while(1):
    if k*(k+1) >= L:
      if L > k*(k+1)-k:
        print(2*k)
        break
      else : 
        print(2*k-1)
        break
    k+=1
