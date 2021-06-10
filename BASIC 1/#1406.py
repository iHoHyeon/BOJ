import sys
stack = list(sys.stdin.readline().strip())
M = int(sys.stdin.readline())
now = len(stack)
Ls = stack
Rs = []
for _ in range(M):
  order = sys.stdin.readline().strip()
  if order[0] == 'P' :
    Ls.append(order[2])
  if order[0] == 'L' and len(Ls) != 0 :
    Rs.append(Ls.pop())

  if order[0] == 'D' and len(Rs) != 0:
    Ls.append(Rs.pop())
  if order[0] =='B' and len(Ls) != 0:
    Ls.pop()

print(''.join(Ls+list(reversed(Rs))))
