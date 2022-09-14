N,M = list(map(int,input().split()))
robot = list(map(int,input().split()))
roadMap = [list(map(int,input().split())) for _ in range(N)]
roboDir = [0,3,2,1]
nowIdx = [robot[0],robot[1]]
#처음에 할당된 부분도 청소함
roadMap[robot[0]][robot[1]] = 2
nowDir = robot[2]
cleanNum = 0

while True:

    r=[0,1,0,-1]
    l=[-1,0,1,0]
    wallCount = 0
    backWall = False
    backIdx=[]
    for p in range(4):
        thisR = nowIdx[0]+r[p]
        thisL = nowIdx[1]+l[p] 
        if thisR>=0 and thisR<=N-1 and thisL>=0 and thisL<=M-1:
            if roadMap[thisR][thisL] != 0:
                wallCount +=1
    if nowDir == 0:
        thisR = nowIdx[0]+r[1]
        thisL = nowIdx[1]+l[1]
    elif nowDir == 1:
        thisR = nowIdx[0]+r[0]
        thisL = nowIdx[1]+l[0]
    elif nowDir == 2:
        thisR = nowIdx[0]+r[3]
        thisL = nowIdx[1]+l[3]
    elif nowDir == 3:
        thisR = nowIdx[0]+r[2]
        thisL = nowIdx[1]+l[2]

    if thisR>=0 and thisR<=N-1 and thisL>=0 and thisL<=M-1:
        backIdx = [thisR,thisL]
        if roadMap[thisR][thisL] == 1:
            backWall = True

    if wallCount == 4 and backWall:
        break
    elif wallCount == 4:
        nowIdx = backIdx
    else:

        if nowDir == 0:
            thisR = nowIdx[0]+r[0]
            thisL = nowIdx[1]+l[0]
            nowDir = 3
            if thisR>=0 and thisR<=N-1 and thisL>=0 and thisL<=M-1:
                if roadMap[thisR][thisL] == 0:
                    nowIdx = [thisR,thisL]
                    roadMap[thisR][thisL] = 2
                    cleanNum+=1

        elif nowDir == 1:
            thisR = nowIdx[0]+r[3]
            thisL = nowIdx[1]+l[3]
            nowDir = 0
            if thisR>=0 and thisR<=N-1 and thisL>=0 and thisL<=M-1:
                if roadMap[thisR][thisL] == 0:
                    nowIdx = [thisR,thisL]
                    roadMap[thisR][thisL] = 2
                    cleanNum+=1
        elif nowDir == 2:
            thisR = nowIdx[0]+r[2]
            thisL = nowIdx[1]+l[2]
            nowDir = 1
            if thisR>=0 and thisR<=N-1 and thisL>=0 and thisL<=M-1:
                if roadMap[thisR][thisL] == 0:
                    nowIdx = [thisR,thisL]
                    roadMap[thisR][thisL] = 2
                    cleanNum+=1

        elif nowDir == 3:
            thisR = nowIdx[0]+r[1]
            thisL = nowIdx[1]+l[1]
            nowDir = 2
            if thisR>=0 and thisR<=N-1 and thisL>=0 and thisL<=M-1:
                if roadMap[thisR][thisL] == 0:
                    nowIdx = [thisR,thisL]
                    roadMap[thisR][thisL] = 2
                    cleanNum+=1
print(cleanNum+1)