x,y = map(int,input().split())
days = ['MON','TUE','WED','THU','FRI','SAT','SUN']
i,j = 1,1
cnt = 0
while(j!=y):
    cnt += 1
    j += 1
while(i!=x):
  if i in (1,3,5,7,8,10,12):
    cnt += 31
  elif  i == 2 :
    cnt += 28
  else :
    cnt += 30
  i += 1
print(days[cnt%7])
