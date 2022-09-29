T = int(input())
for k in range(T):
    N,M  = list(map(int,input().split()))
    teamlist = list(map(int,input().split()))
    pairlist = [[] for _ in range(N)]
    count = 0
    for a in range(len(teamlist)//2):
        nowIdx = 0
        while True:
            if teamlist[a*2] in pairlist[nowIdx]:
                pairlist[nowIdx].append(teamlist[a * 2 + 1])
                break
            elif teamlist[a*2+1] in pairlist[nowIdx]:
                pairlist[nowIdx].append(teamlist[a * 2])
                break
            elif len(pairlist[nowIdx])!=0:
                nowIdx+=1
            else:
                pairlist[nowIdx].append(teamlist[a*2])
                pairlist[nowIdx].append(teamlist[a * 2+1])
                break
    print(pairlist)
    for b in range(len(pairlist)):
        if len(pairlist[b])>0:
            count+=1
    for b in range(1,N+1):
        if b not in teamlist:
            count+=1
    print(f'#{k+1} {count}')

