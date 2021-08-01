import sys

N = int(sys.stdin.readline())

L = list(map(int, sys.stdin.readline().split()))

cL = list(sorted(set(L)))
cL =  {cL[i]:i for i in range(len(cL))}

print(*[cL[i] for i in L])
