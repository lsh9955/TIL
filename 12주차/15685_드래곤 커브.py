# y = -x축에 대해 그 뭐냐 그걸 하면 됨
N = int(input())
dragon = [list(map(int,input().split())) for _ in range(N)]
curvelist = []
dir = 0
for a in range(N):
    x,y,d,g = dragon[a]
    firlist =[]
    if d == 0:
        firlist = [[0, 0],[1,0]]
    elif d == 1:
        firlist = [[0,0],[0,-1]]
    elif d == 2:
        firlist = [[0,0],[-1,0]]
    elif d == 3:
        firlist = [[0, 0], [0, 1]]
    while g>0:
        endidx = [firlist[-1][0],firlist[-1][1]]
        nowlen = len(firlist)
        addlist = []
        for b in range(len(firlist)):
            addlist.append(- [firlist[b][1],-firlist[b][0]])
        nowend = [addlist[-1][0],addlist[-1][1]]
        willadd = [endidx[0]-nowend[0],nowend[1]-endidx[1]]
        for c in range(len(addlist)):
            addlist[c][0]+=willadd[0]
            addlist[c][1]+=willadd[1]
        for d in range(len(addlist)-2,-1,-1):
            firlist.append(addlist[d])
        g-=1
    print(firlist)

