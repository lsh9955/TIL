import copy
def solution(game_board, table):
    newgame = copy.deepcopy(game_board)
    blocklist = []
    count = 0
    def thisroute(x,y,e,f):
        blocklist[-1].append([e,f])
        newgame[x][y]=1
        d=[0,0,-1,1]
        l=[1,-1,0,0]
        for p in range(4):
            if 0<=x+d[p]<=len(newgame)-1 and 0<=y+l[p]<=len(newgame)-1:
                if newgame[x+d[p]][y+l[p]]==0:
                    thisroute(x+d[p],y+l[p],e+d[p],f+l[p])

    for a in range(len(newgame)):
        for b in range(len(newgame)):
            if newgame[a][b]==0:
                blocklist.append([])
                thisroute(a,b,0,0)
    newtable=copy.deepcopy(table)
    realidx = []
    tableidx = []
    def tableroute(x,y,e,f,n):
        tableidx[-1].append([e,f])
        realidx[-1].append([x,y])
        newtable[x][y]=n+1
        d=[0,0,-1,1]
        l=[1,-1,0,0]
        for p in range(4):
            if 0<=x+d[p]<=len(newtable)-1 and 0<=y+l[p]<=len(newtable)-1:
                if newtable[x+d[p]][y+l[p]]==n:
                    tableroute(x+d[p],y+l[p],e+d[p],f+l[p],n)
    def rotate_90(m):
        N = len(m)
        ret = [[0] * N for _ in range(N)]
        for r in range(N):
            for c in range(N):
                ret[c][N-1-r] = m[r][c]
        return ret


    for a in range(len(newtable)):
        for b in range(len(newtable)):
            if newtable[a][b]==1:
                realidx.append([])
                tableidx.append([])
                tableroute(a,b,0,0,1)

    for c in range(len(tableidx)):
        if tableidx[c] in blocklist:
            blocklist.pop(blocklist.index(tableidx[c]))
            count+=len(tableidx[c])
            for d in range(len(tableidx[c])):
                newtable[realidx[c][d][0]][realidx[c][d][1]]=0
    realidx = []
    tableidx = []
    newtable = rotate_90(newtable)
    
    
    for a in range(len(newtable)):
        for b in range(len(newtable)):
            if newtable[a][b]==2:
                realidx.append([])
                tableidx.append([])
                tableroute(a,b,0,0,2)

    for c in range(len(tableidx)):
        if tableidx[c] in blocklist:
            blocklist.pop(blocklist.index(tableidx[c]))
            
            count+=len(tableidx[c])
            for d in range(len(tableidx[c])):
                newtable[realidx[c][d][0]][realidx[c][d][1]]=0
    realidx = []
    tableidx = []
    newtable = rotate_90(newtable)
    for a in range(len(newtable)):
        for b in range(len(newtable)):
            if newtable[a][b]==3:
                realidx.append([])
                tableidx.append([])
                tableroute(a,b,0,0,3)

    for c in range(len(tableidx)):
        if tableidx[c] in blocklist:
            blocklist.pop(blocklist.index(tableidx[c]))
            
            count+=len(tableidx[c])
            for d in range(len(tableidx[c])):
                newtable[realidx[c][d][0]][realidx[c][d][1]]=0
    realidx = []
    tableidx = []
    newtable = rotate_90(newtable)
    for a in range(len(newtable)):
        for b in range(len(newtable)):
            if newtable[a][b]==4:
                realidx.append([])
                tableidx.append([])
                tableroute(a,b,0,0,4)

    for c in range(len(tableidx)):
        if tableidx[c] in blocklist:
            blocklist.pop(blocklist.index(tableidx[c]))
            
            count+=len(tableidx[c])
            for d in range(len(tableidx[c])):
                newtable[realidx[c][d][0]][realidx[c][d][1]]=0
    


    answer = count
    return answer
print(solution([[0,0,0],[1,1,0],[1,1,1]],[[1,1,1],[1,0,0],[0,0,0]]))