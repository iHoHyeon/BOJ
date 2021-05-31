T = int(input())

def pt(a):
  if a == 1:
    return 0
  for i in range(2,int(a**(0.5))+1):
    if a%i == 0 :
      return 0
  return 1

plist = []
for i in range(1,10000):
  if pt(10000-i) :
    plist.append(10000-i)

for _ in range(T):
  n = int(input())
  for i in plist:
    if i >n/2 :
      continue
    if (n-i) in plist:
      print(i,n-i)
      break
# T = int(input())

# def pt(a):
#   if a == 1:
#     return 0
#   for i in range(2,int(a**(0.5))+1):
#     if a%i == 0 :
#       return 0
#   return 1

# plist = []
# for i in range(10000,-1,-1):
#   if pt(i) :
#     plist.append(i)

# for _ in range(T):
#   n = int(input())
#   n_li = [i for i in plist if i<=n/2]
#   for i in n_li:
#     if n-i in plist:
#       print(i,n-i)
#       break