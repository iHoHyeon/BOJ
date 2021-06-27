T = int(input())

for _ in range(T):
  N,M = map(int,input().split())
  imp = list(map(int,input().split()))
  now = [0]*N
  now[M] = 1

  cnt = 0
  if N ==1 :
    print(1)
    continue
  
  while True:
    if imp[0]>=max(imp):
      if now[0]==1:
        print(cnt+1)
        break
      else:
        imp = imp[1:]
        now = now[1:]
        cnt += 1
    
    else:
        imp = imp[1:] + [imp[0]]
        now = now[1:] + [now[0]]    


