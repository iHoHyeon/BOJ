def check(map,a,b):
  cnt1, cnt2  = 0 , 0
  for i in range(8):
    for j in range(8):
      if (i+j)%2 == 0:
        if map[a+i][b+j] == 'B' :
         cnt1 += 1
      else :
        if map[a+i][b+j] == 'W':
          cnt1 += 1
  for i in range(8):
   for j in range(8):
       if (i+j)%2 == 0:
         if map[a+i][b+j] == 'W' :
          cnt2 += 1
       else :
         if map[a+i][b+j] == 'B':
          cnt2 += 1
  return min(cnt1,cnt2)

N,M = map(int,input().split())
L =[]
for i in range(N):
  L.append(list(map(str,input())))
cnt = []
for i in range(N-7):
  for j in range(M-7):
    cnt.append(check(L,i,j))
print(min(cnt))