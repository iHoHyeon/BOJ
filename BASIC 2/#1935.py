N = int(input())
L = list(input())
num = []
for i in range(N):
  num.append(int(input()))
stack = []
li = []
for i in L:
  if ord('A')<=ord(i)<=ord('Z') :
  
    stack.append(num[ord(i)-ord('A')])

  else:
    li.append(stack.pop())
    li.append(i)
    li.append(stack.pop())
    stack.append(eval(''.join(map(str,li[::-1]))))
    li = []


print(f"{stack[0]:.2f}")
