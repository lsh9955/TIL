T = int(input())
for k in range(T):
    N,M,R,C,L = list(map(int,input().split()))
    roadList = [list(map(int,input().split())) for _ in range(N)]
    nowIdx = [R,C]
    amountTime = L-1
    nowPipe = roadList[R][C]
    global connectRoad
    global checkRoad
    connectRoad = [[R,C,0]]
    checkRoad = [nowIdx]
    def findRoute(thisIdx,thisPipe,nowTime):
        y = thisIdx[0]
        x = thisIdx[1]
        if thisPipe == 1:
            if x-1>=0:
                if roadList[y][x-1] != 0:
                    if [y,x-1] not in checkRoad:
                        connectRoad.append([y,x-1,nowTime])
                        checkRoad.append([y,x-1])
                        findRoute([y,x-1],roadList[y][x-1],nowTime+1)
                    else:
                        compareTime=0
                        popIdx=0
                        for p in range(len(connectRoad)):
                            if connectRoad[p][0]==y and connectRoad[p][1]==x-1:
                                compareTime=connectRoad[p][2]
                                popIdx = p
                        if compareTime>nowTime:
                            connectRoad.pop(popIdx)
                            connectRoad.append([y,x-1,nowTime])
                            findRoute([y,x-1],roadList[y][x-1],nowTime+1)
                            
            if x+1<=M-1:
                if roadList[y][x+1] != 0:
                    if [y,x+1] not in checkRoad:
                        connectRoad.append([y,x+1,nowTime])
                        checkRoad.append([y,x+1])
                        findRoute([y,x+1],roadList[y][x+1],nowTime+1)
                    else:
                        compareTime=0
                        popIdx=0
                        for p in range(len(connectRoad)):
                            if connectRoad[p][0]==y and connectRoad[p][1]==x+1:
                                compareTime=connectRoad[p][2]
                                popIdx = p
                                break
                        if compareTime>nowTime:
                            connectRoad.pop(popIdx)
                            connectRoad.append([y,x+1,nowTime])
                            findRoute([y,x+1],roadList[y][x+1],nowTime+1)
            if y+1<=N-1:
                if roadList[y+1][x] != 0:
                    if [y+1,x] not in checkRoad:
                        connectRoad.append([y+1,x,nowTime])
                        checkRoad.append([y+1,x])
                        findRoute([y+1,x],roadList[y+1][x],nowTime+1)
                    else:
                        compareTime=0
                        popIdx=0
                        for p in range(len(connectRoad)):
                            if connectRoad[p][0]==y+1 and connectRoad[p][1]==x:
                                compareTime=connectRoad[p][2]
                                popIdx = p
                                break
                        if compareTime>nowTime:
                            connectRoad.pop(popIdx)
                            connectRoad.append([y+1,x,nowTime])
                            findRoute([y+1,x],roadList[y+1][x],nowTime+1)
            if y-1>=0:
                if roadList[y-1][x] != 0:
                    if [y-1,x] not in checkRoad:
                        connectRoad.append([y-1,x,nowTime])
                        checkRoad.append([y-1,x])
                        findRoute([y-1,x],roadList[y-1][x],nowTime+1)
                    else:
                        compareTime=0
                        popIdx=0
                        for p in range(len(connectRoad)):
                            if connectRoad[p][0]==y-1 and connectRoad[p][1]==x:
                                compareTime=connectRoad[p][2]
                                popIdx = p
                                break
                        if compareTime>nowTime:
                            connectRoad.pop(popIdx)
                            connectRoad.append([y-1,x,nowTime])
                            findRoute([y-1,x],roadList[y-1][x],nowTime+1)
        elif thisPipe == 2:
            if y-1>=0:
                if roadList[y-1][x] != 0:
                    if [y-1,x] not in checkRoad:
                        connectRoad.append([y-1,x,nowTime])
                        checkRoad.append([y-1,x])
                        findRoute([y-1,x],roadList[y-1][x],nowTime+1)
                    else:
                        compareTime=0
                        popIdx=0
                        for p in range(len(connectRoad)):
                            if connectRoad[p][0]==y-1 and connectRoad[p][1]==x:
                                compareTime=connectRoad[p][2]
                                popIdx = p
                                break
                        if compareTime>nowTime:
                            connectRoad.pop(popIdx)
                            connectRoad.append([y-1,x,nowTime])
                            findRoute([y-1,x],roadList[y-1][x],nowTime+1)
            if y+1<=N-1:
                if roadList[y+1][x] != 0:
                    if [y+1,x] not in checkRoad:
                        connectRoad.append([y+1,x,nowTime])
                        checkRoad.append([y+1,x])
                        findRoute([y+1,x],roadList[y+1][x],nowTime+1)
                    else:
                        compareTime=0
                        popIdx=0
                        for p in range(len(connectRoad)):
                            if connectRoad[p][0]==y+1 and connectRoad[p][1]==x:
                                compareTime=connectRoad[p][2]
                                popIdx = p
                                break
                        if compareTime>nowTime:
                            connectRoad.pop(popIdx)
                            connectRoad.append([y+1,x,nowTime])
                            findRoute([y+1,x],roadList[y+1][x],nowTime+1)
        elif thisPipe == 3:
            if x+1<=M-1:
                if roadList[y][x+1] != 0:
                    if [y,x+1] not in checkRoad:
                        connectRoad.append([y,x+1,nowTime])
                        checkRoad.append([y,x+1])
                        findRoute([y,x+1],roadList[y][x+1],nowTime+1)
                    else:
                        compareTime=0
                        popIdx=0
                        for p in range(len(connectRoad)):
                            if connectRoad[p][0]==y and connectRoad[p][1]==x+1:
                                compareTime=connectRoad[p][2]
                                popIdx = p
                                break
                        if compareTime>nowTime:
                            connectRoad.pop(popIdx)
                            connectRoad.append([y,x+1,nowTime])
                            findRoute([y,x+1],roadList[y][x+1],nowTime+1)
            if x-1>=0:            
                if roadList[y][x-1] != 0:
                    if [y,x-1] not in checkRoad:
                        connectRoad.append([y,x-1,nowTime])
                        checkRoad.append([y,x-1])
                        findRoute([y,x-1],roadList[y][x-1],nowTime+1)
                    else:
                        compareTime=0
                        popIdx=0
                        for p in range(len(connectRoad)):
                            if connectRoad[p][0]==y and connectRoad[p][1]==x-1:
                                compareTime=connectRoad[p][2]
                                popIdx = p
                                break
                        if compareTime>nowTime:
                            connectRoad.pop(popIdx)
                            connectRoad.append([y,x-1,nowTime])
                            findRoute([y,x-1],roadList[y][x-1],nowTime+1)
        elif thisPipe == 4:
            if y-1>=0:
                if roadList[y-1][x] != 0:
                    if [y-1,x] not in checkRoad:
                        connectRoad.append([y-1,x,nowTime])
                        checkRoad.append([y-1,x])
                        findRoute([y-1,x],roadList[y-1][x],nowTime+1)
                    else:
                        compareTime=0
                        popIdx=0
                        for p in range(len(connectRoad)):
                            if connectRoad[p][0]==y-1 and connectRoad[p][1]==x:
                                compareTime=connectRoad[p][2]
                                popIdx = p
                                break
                        if compareTime>nowTime:
                            connectRoad.pop(popIdx)
                            connectRoad.append([y-1,x,nowTime])
                            findRoute([y-1,x],roadList[y-1][x],nowTime+1)
            if x+1<=M-1:            
                if roadList[y][x+1] != 0:
                    if [y,x+1] not in checkRoad:
                        connectRoad.append([y,x+1,nowTime])
                        checkRoad.append([y,x+1])
                        findRoute([y,x+1],roadList[y][x+1],nowTime+1)   
                    else:
                        compareTime=0
                        popIdx=0
                        for p in range(len(connectRoad)):
                            if connectRoad[p][0]==y and connectRoad[p][1]==x+1:
                                compareTime=connectRoad[p][2]
                                popIdx = p
                        if compareTime>nowTime:
                            connectRoad.pop(popIdx)
                            connectRoad.append([y,x+1,nowTime])
                            findRoute([y,x+1],roadList[y][x+1],nowTime+1)   
        elif thisPipe == 5:
            if y+1<=N-1:
                if roadList[y+1][x] != 0:
                    if [y+1,x] not in checkRoad:
                        connectRoad.append([y+1,x,nowTime])
                        checkRoad.append([y+1,x])
                        findRoute([y+1,x],roadList[y+1][x],nowTime+1)
                    else:
                        compareTime=0
                        popIdx=0
                        for p in range(len(connectRoad)):
                            if connectRoad[p][0]==y+1 and connectRoad[p][1]==x:
                                compareTime=connectRoad[p][2]
                                popIdx = p
                        if compareTime>nowTime:
                            connectRoad.pop(popIdx)
                            connectRoad.append([y+1,x,nowTime])
                            findRoute([y+1,x],roadList[y+1][x],nowTime+1)
            if x+1<=M-1:
                if roadList[y][x+1] != 0:
                    if [y,x+1] not in checkRoad:
                        connectRoad.append([y,x+1,nowTime])
                        checkRoad.append([y,x+1])
                        findRoute([y,x+1],roadList[y][x+1],nowTime+1) 
                    else:
                        compareTime=0
                        popIdx=0
                        for p in range(len(connectRoad)):
                            if connectRoad[p][0]==y and connectRoad[p][1]==x+1:
                                compareTime=connectRoad[p][2]
                                popIdx = p
                        if compareTime>nowTime:
                            connectRoad.pop(popIdx)
                            connectRoad.append([y,x+1,nowTime])
                            findRoute([y,x+1],roadList[y][x+1],nowTime+1) 
        elif thisPipe == 6:
            if y+1<=N-1:
                if roadList[y+1][x] != 0:
                    if [y+1,x] not in checkRoad:
                        connectRoad.append([y+1,x,nowTime])
                        checkRoad.append([y+1,x])
                        findRoute([y+1,x],roadList[y+1][x],nowTime+1)
                    else:
                        compareTime=0
                        popIdx=0
                        for p in range(len(connectRoad)):
                            if connectRoad[p][0]==y+1 and connectRoad[p][1]==x:
                                compareTime=connectRoad[p][2]
                                popIdx = p
                        if compareTime>nowTime:
                            connectRoad.pop(popIdx)
                            connectRoad.append([y+1,x,nowTime])
                            findRoute([y+1,x],roadList[y+1][x],nowTime+1)
            if x-1>=0:
                if roadList[y][x-1] != 0:
                    if [y,x-1] not in checkRoad:
                        connectRoad.append([y,x-1,nowTime])
                        checkRoad.append([y,x-1])
                        findRoute([y,x-1],roadList[y][x-1],nowTime+1)  
                    else:
                        compareTime=0
                        popIdx=0
                        for p in range(len(connectRoad)):
                            if connectRoad[p][0]==y and connectRoad[p][1]==x-1:
                                compareTime=connectRoad[p][2]
                                popIdx = p
                        if compareTime>nowTime:
                            connectRoad.pop(popIdx)
                            connectRoad.append([y,x-1,nowTime])
                            findRoute([y,x-1],roadList[y][x-1],nowTime+1)  
        elif thisPipe == 7:
            if y-1>=0:
                if roadList[y-1][x] != 0:
                    if [y-1,x] not in checkRoad:
                        connectRoad.append([y-1,x,nowTime])
                        checkRoad.append([y-1,x])
                        findRoute([y-1,x],roadList[y-1][x],nowTime+1)
                    else:
                        compareTime=0
                        popIdx=0
                        for p in range(len(connectRoad)):
                            if connectRoad[p][0]==y-1 and connectRoad[p][1]==x:
                                compareTime=connectRoad[p][2]
                                popIdx = p
                        if compareTime>nowTime:
                            connectRoad.pop(popIdx)
                            connectRoad.append([y-1,x,nowTime])
                            findRoute([y-1,x],roadList[y-1][x],nowTime+1)
            if x-1>=0:
                if roadList[y][x-1] != 0:
                    if [y,x-1] not in checkRoad:
                        connectRoad.append([y,x-1,nowTime])
                        checkRoad.append([y,x-1])
                        findRoute([y,x-1],roadList[y][x-1],nowTime+1)  
                    else:
                        compareTime=0
                        popIdx=0
                        for p in range(len(connectRoad)):
                            if connectRoad[p][0]==y and connectRoad[p][1]==x-1:
                                compareTime=connectRoad[p][2]
                                popIdx = p
                        if compareTime>nowTime:
                            connectRoad.pop(popIdx)
                            connectRoad.append([y,x-1,nowTime])
                            findRoute([y,x-1],roadList[y][x-1],nowTime+1)  
    findRoute(nowIdx,nowPipe,1)
    countRoute = 0
    print(connectRoad)
    for b in range(len(connectRoad)):
        if connectRoad[b][2]<=amountTime:
            countRoute+=1
    print(f'#{k+1} {countRoute}')
