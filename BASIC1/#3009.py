X = []
Y = []

for _ in range(3):
  x,y = map(int,input().split())
  X.append(x)
  Y.append(y)
print(min(X, key =X.count),min(Y, key =Y.count),sep=' ')

# max or min 는 key를 이용할 수 있다.