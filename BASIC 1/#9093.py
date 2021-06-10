T = int(input())

for _ in range(T):
  L = list(input().split())
  print(*[i[::-1] for i in L])