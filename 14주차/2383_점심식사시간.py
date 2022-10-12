#기다리는 것 vs 다른 계단을 가는 것 중 어떤게 더 빠를지를 비교?
#빠르게 계단에 도착할 수 있는 사람 순서대로
#1분+계단갯수
#계단 개수는 무조건 2개
T = int(input())
for a in range(T):
    N = int(input())
    mapinfo = [list(map(int,input().split())) for _ in range(N)]
    stairidx = []
    personidx = []
    firstir=[]
    secstir=[]
    for b in range(N):
        for c in range(N):
            if mapinfo[b][c] > 1:
                stairidx.append([b,c,  mapinfo[b][c]])
            elif mapinfo[b][c] == 1:
                personidx.append([b,c])
    #personidx= [y좌표,x좌표, 0번계단까지 거리,1번계단까지 거리]
    for b in range(len(personidx)):
        yidx = personidx[b][0]
        xidx = personidx[b][1]
        if abs(stairidx[0][0]-yidx)+abs(stairidx[0][1]-xidx) < abs(stairidx[1][0]-yidx)+abs(stairidx[1][1]-xidx):
            personidx[b].append(abs(stairidx[0][0]-yidx)+abs(stairidx[0][1]-xidx))
            personidx[b].append(abs(stairidx[1][0] - yidx) + abs(stairidx[1][1] - xidx))
            firstir.append(personidx[b])
        else:
            personidx[b].append(abs(stairidx[0][0]-yidx)+abs(stairidx[0][1]-xidx))
            personidx[b].append(abs(stairidx[1][0] - yidx) + abs(stairidx[1][1] - xidx))
            secstir.append(personidx[b])
    firstir.sort(key=lambda x:x[2])
    secstir.sort(key=lambda x:x[3])
    finfo=[]
    sinfo=[]
    ftime=0
    stime=0
    # 시간을 어떻게 측정을 할지?
    while len(firstir) !=0 or len(secstir) !=0:
        compairtime=0
        if len(firstir) !=0 and len(secstir) !=0:
            if len(finfo)==0:
                if firstir[0][2]+stairidx[0][2]>firstir[0][3]+stairidx[1][2]:
                    if 


