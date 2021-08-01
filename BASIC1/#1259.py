while(1):
  N = list(input())
  if N == ['0'] : break
  print("yes" if N == N[::-1] else "no")
