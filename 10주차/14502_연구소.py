import copy
N,M = list(map(int,input().split()))
roadMap = [list(map(int,input().split())) for _ in range(N)]
emptyCell = []
corona = []
maxEmpty = 0

def maxNum(fir,sec,tir):
    global nowNum
    global thisRoad
    thisRoad = copy.deepcopy(roadMap)
    nowNum = len(emptyCell)-3
    thisRoad[emptyCell[fir][0]][emptyCell[fir][1]]=1
    thisRoad[emptyCell[sec][0]][emptyCell[sec][1]]=1
    thisRoad[emptyCell[tir][0]][emptyCell[tir][1]]=1
    def findempty(nowIdx):
        global nowNum
        r = [0,0,1,-1]
        l = [1,-1,0,0]
        for i in range(4):
            if nowIdx[0]+r[i]>=0 and nowIdx[0]+r[i]<=N-1 and nowIdx[1]+l[i]>=0 and nowIdx[1]+l[i]<=M-1 and thisRoad[nowIdx[0]+r[i]][nowIdx[1]+l[i]]==0:
                nowNum-=1
                thisRoad[nowIdx[0]+r[i]][nowIdx[1]+l[i]]=3
                findempty([nowIdx[0]+r[i],nowIdx[1]+l[i]])
    for p in range(len(corona)):
        findempty(corona[p])
    return nowNum

for a in range(N):
    for b in range(M):
        if roadMap[a][b] == 0:
            emptyCell.append([a, b])
        elif roadMap[a][b] == 2:
            corona.append([a, b])

for a in range(len(emptyCell)-2):
    for b in range(a+1,len(emptyCell)-1):
        for c in range(b+1,len(emptyCell)):
            thisNum = maxNum(c,b,a)
            if maxEmpty<thisNum:
                maxEmpty = thisNum
print(maxEmpty)

