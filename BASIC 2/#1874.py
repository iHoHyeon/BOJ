N = int(input())
stack = [1]
seq =[]
for _ in range(N):
  seq.append(int(input()))

command = ['+']
now = 2

for i in range(N):
  if stack == []:
    stack.append(now)
    command.append('+')
    now += 1

  while(stack[len(stack)-1] != seq[i]):
    if now == N+1 :
      break
    
    stack.append(now)
    command.append('+')
    now += 1

  if stack[len(stack)-1] == seq[i] :
    stack.pop()
    command.append('-')
  else : break

if (stack == []) and (now == N+1):
  print('\n'.join(command))
else : print('NO')
