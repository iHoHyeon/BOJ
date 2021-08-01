import sys 

N = int(input())
s = 0
cnt = [0]*8001

for _ in range(N):
  i = int(sys.stdin.readline())
  cnt[i+4000] += 1
  s += i
j = 1
while(1):
  if sum(cnt[:j]) >= N//2 +1:
    mid = j-1
    break
  j += 1


print(round(s/N))
print(mid-4000)

m = []
c = 0
for i in range(len(cnt)):
  if cnt[i] == max(cnt):
    m.append(i)
    c += 1
    if c==2: break

if len(m) == 1:
  print(m[0]-4000)
else :
  print(m[1]-4000)

for i in range(8002):
  if cnt[i] != 0:
    mi = i-4000
    break
for i in range(8000,-1,-1):
  if cnt[i] != 0:
    ma = i - 4000
    break

print(ma-mi)
