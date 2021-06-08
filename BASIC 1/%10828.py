import sys

stack = []
N = int(sys.stdin.readline())

for _ in range(N):
  com = list(sys.stdin.readline().split())
  
  if com[0] == 'push' :
    stack.append(com[1])
  if com[0] == 'pop':
    if stack == []:
      print(-1)
    else :
      print(stack[len(stack)-1])
      stack.pop()
  if com[0] == 'size' :
    print(len(stack))
  if com[0] == 'empty' :
    if stack == [] :
      print(1)
    else :
      print(0)
  if com[0] == 'top':
    if stack == []:
      print(-1)
    else :
      print(stack[len(stack)-1])