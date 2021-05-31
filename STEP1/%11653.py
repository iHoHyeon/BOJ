N = int(input())
now = 2
while(N != 1):
  if N%now == 0:
    print(now)
    N /=now
  else : now += 1

  # while의 조건문을 활용해서 시간초과 방지
