import sys

_ = int(sys.stdin.readline()) 
N = sorted(map(int,sys.stdin.readline().split()))
_ = int(sys.stdin.readline())
M = list(map(int,sys.stdin.readline().split()))

hashmap ={}
for i in N:
  if i in hashmap:
    hashmap[i] += 1
  else :
    hashmap[i] = 1

print(' '.join(str(hashmap[m]) if m in hashmap else '0' for m in M))
