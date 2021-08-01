from itertools import combinations
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
members = [i for i in range(N)]
Pteam = []

for team in list(combinations(members, N//2)):
    Pteam.append(team)

statGap = 1000000000
for i in range(len(Pteam)//2):
    team = Pteam[i]
    A = 0
    for j in range(N//2):
        member = team[j]
        for k in team:
            A += S[member][k]

    team = Pteam[-i-1]
    B = 0
    for j in range(N//2):
        member = team[j]
        for k in team:
            B += S[member][k]

    statGap = min(statGap, abs(A - B))

print(statGap)
