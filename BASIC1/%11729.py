N = int(input())

def HN(i,a,b,c):
  if i==1:
    print(a,c)
  else:
    HN(i-1,a,c,b) 
    #i-1 개를 1에서 2로 이동
    print(a,c) 
    #1에 남은 1개를 3으로 이동
    HN(i-1,b,a,c) 
    #2에 올려있는 i-1개를 3으로 이동 
cnt =  1
for i in range(N-1):
  cnt = cnt*2 +1
  # N번째는 N-1개를 두번 이동하고 1개를 한번 이동시킨다

print(cnt)
HN(N,1,2,3)