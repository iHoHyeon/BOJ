while (1):
  a,b,c = map(int,input().split())
  if max(a,b,c) == 0 : 
    break
  print("right" if 2*(max(a,b,c)**2) == (a**2+b**2+c**2) else "wrong")