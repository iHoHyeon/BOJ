def pt(a):
  if a == 1:
    return 0
  for i in range(2,int(a**(0.5))+1):
    if a%i == 0 :
      return 0
  return 1

plist=[2]
for i in range(2,123456+1):
  if pt(2*i-1):
    plist.append(2*i-1)
while True:
  n = int(input())
  if n == 0:
    break
  print(len([i for i in plist if n<i<=2*n]))
#시간초과를 피해야함
#[i for i in List if (조건)] 기억하기