import sys

N = int(sys.stdin.readline())
Q = []

for _ in range(N):
  com = sys.stdin.readline().split()
  if com[0] == "push" :
    Q.append(com[1])
  elif com[0] == "pop":
    print(Q.pop(0) if len(Q) != 0 else -1)
  elif com[0] == "size" :
    print(len(Q))  
  elif com[0] == "empty" :
    print(1 if len(Q)==0 else 0)  
  elif com[0] == "front" :
    print(Q[0] if len(Q) != 0 else -1)
  elif com[0] == "back" :
    print(Q[-1] if len(Q) != 0 else -1)


# Q != [] 보다 len(Q) != 0 이 빠르다