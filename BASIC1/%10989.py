import sys

N = int(input())

cnt = [0]*10000

for _ in range(N):
  i = int(sys.stdin.readline())
  cnt[i-1] += 1

for i in range(10000) :
  if cnt[i]== 0 :
    continue
  for _ in range(cnt[i]):
    print(i+1)
  