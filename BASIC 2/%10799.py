# L = list(input())
# now = 0
# cnt = 0
# tag = 0 
# for i in L:
#   if now == 0:
#     if i =='(' :
#       now += 1
#       tag = 0
#   else :
#     if i == '(' :
#       if tag == 0:
#         now += 1
#       else :
#         now += 1
#         tag = 0
#     elif i ==')' :
#       if tag == 0:
#         now -= 1
#         cnt += now
#         tag = 1
#       else :
#         now -= 1
#         cnt += 1
#         tag = 1

# print(cnt)

L = list(input())
stack = []
cnt = 0
for i in range(len(L)):
  if L[i] == '(':
    stack.append(1)
  
  else :
    if L[i-1] == '(':
      stack.pop()
      cnt += len(stack)
    else :
      stack.pop()
      cnt += 1
print(cnt)