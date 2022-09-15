N,L = list(map(int,input().split()))
routeMap = [list(map(int,input().split())) for _ in range(N)]
countRoute = 0
for a in range(N):
    diffList = []
    flag = True
    for b in range(N-1):
        if routeMap[a][b] == routeMap[a][b+1]:
            pass
        elif routeMap[a][b] != routeMap[a][b+1] and abs(routeMap[a][b+1]-routeMap[a][b]) == 1:
            if len(diffList) == 0:
                if routeMap[a][b+1]-routeMap[a][b] == 1:
                    if b+1<L:
                        flag = False
                        break
                    else:
                        diffList.append([b,routeMap[a][b],routeMap[a][b+1]])
                elif routeMap[a][b+1]-routeMap[a][b] == -1:
                    diffList.append([b,routeMap[a][b],routeMap[a][b+1]])
            else:
                if diffList[-1][1]==routeMap[a][b+1] and routeMap[a][b+1]-routeMap[a][b] == 1:
                    if b-diffList[-1][0]<L*2:
                        flag = False
                        break
                elif  diffList[-1][1]==routeMap[a][b+1] and routeMap[a][b+1]-routeMap[a][b] == -1:
                    diffList.append([b,routeMap[a][b],routeMap[a][b+1]])
                    pass
                else:
                    if b-diffList[-1][0]<L:
                        flag = False
                        break
                    else:
                        diffList.append([b,routeMap[a][b],routeMap[a][b+1]])
        else:
            flag = False
            break
    if len(diffList) == 0:
        pass
    elif routeMap[a][N-1]-diffList[-1][1] == 1:
        pass
    elif routeMap[a][N-1]-diffList[-1][1] == -1:
        if N-1-diffList[-1][0]<L:
            flag = False
    if flag:
        countRoute+=1
def rotated(arr):
    rotateList = zip(*arr[::-1])
    return [list(_) for _ in rotateList]
routeMap=rotated(routeMap)
for a in range(N):
    diffList = []
    flag = True
    for b in range(N-1):
        if routeMap[a][b] == routeMap[a][b+1]:
            continue
        elif routeMap[a][b] != routeMap[a][b+1] and abs(routeMap[a][b+1]-routeMap[a][b]) == 1:
            if len(diffList) == 0:
                if routeMap[a][b+1]-routeMap[a][b] == 1:
                    if b+1<L:
                        flag = False
                        break
                    else:
                        diffList.append([b,routeMap[a][b],routeMap[a][b+1]])
                elif routeMap[a][b+1]-routeMap[a][b] == -1:
                    diffList.append([b,routeMap[a][b],routeMap[a][b+1]])
            else:
                if diffList[-1][1]==routeMap[a][b+1] and routeMap[a][b+1]-routeMap[a][b] == 1:
                    if b-diffList[-1][0]<L*2:
                        flag = False
                        break
                elif  diffList[-1][1]==routeMap[a][b+1] and routeMap[a][b+1]-routeMap[a][b] == -1:
                    diffList.append([b,routeMap[a][b],routeMap[a][b+1]])
                    continue
                else:
                    if b-diffList[-1][0]<L:
                        flag = False
                        break
                    else:
                        diffList.append([b,routeMap[a][b],routeMap[a][b+1]])
        else:
            flag = False
            break
    if len(diffList) == 0:
        pass
    elif routeMap[a][N-1]-diffList[-1][1] == 1:
        continue
    elif routeMap[a][N-1]-diffList[-1][1] == -1:
        if N-1-diffList[-1][0]<L:
            flag = False
    if flag:
        countRoute+=1



print(countRoute)

