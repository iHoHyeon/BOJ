import math

def pt(a):
  for i in range(1,math.floor(math.sqrt(a))+1):
    if i == 1:
      continue
    if a%i == 0 :
      return 1
    else : 
      return 0

print(pt(5))