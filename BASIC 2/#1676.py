N = int(input())
cnt1, cnt2 = 0,0

for i in range(2,N+1):
  while((i%2 == 0) or (i%5 == 0)):
    if i%2 == 0:
      cnt1 += 1
      i = i/2
    if i%5 == 0:
      cnt2 += 1
      i = i/5
print(min(cnt1,cnt2))