N = int(input())
L =[]
for _ in range(N):
  L.append(list(map(int,input().split())))

for i in range(N):
  rank = 1
  for j in range(N):
    if L[i][0] < L[j][0] and L[i][1] < L[j][1]:
       rank += 1
  print(rank,end=' ')