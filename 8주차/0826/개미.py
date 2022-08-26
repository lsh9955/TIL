w,h=list(map(int,input().split()))
firIdx = list(map(int,input().split()))
t = int(input())
antRoute = [firIdx]
nowIdx=firIdx[:]
thisDir=0
r = [1, 1, -1, -1]
c = [1, -1, 1, -1]
while True:
    print(nowIdx)
    print(thisDir)
    if (nowIdx[0]+r[thisDir]<w and nowIdx[0]+r[thisDir]>0) and (nowIdx[1]+c[thisDir]<h and  nowIdx[1]+c[thisDir]>0):
        nowIdx=[nowIdx[0]+r[thisDir],nowIdx[1]+c[thisDir]]
        antRoute.append(nowIdx)
    elif nowIdx[0]+r[thisDir]==w and nowIdx[1]+c[thisDir]<h and nowIdx[1]+c[thisDir]>0:
        nowIdx = [nowIdx[0] + r[thisDir], nowIdx[1] + c[thisDir]]
        antRoute.append(nowIdx)
        if thisDir ==0:
            thisDir = 2
        elif thisDir == 1:
            thisDir = 3
    elif nowIdx[0]+r[thisDir]==0 and nowIdx[1]+c[thisDir]<h and nowIdx[1]+c[thisDir]>0:
        nowIdx = [nowIdx[0] + r[thisDir], nowIdx[1] + c[thisDir]]
        antRoute.append(nowIdx)
        if thisDir == 2:
            thisDir = 0
        elif thisDir == 3:
            thisDir = 1
    elif nowIdx[0]+r[thisDir]<w and nowIdx[0]+r[thisDir]>0 and nowIdx[1]+c[thisDir]==h:
        nowIdx = [nowIdx[0] + r[thisDir], nowIdx[1] + c[thisDir]]
        antRoute.append(nowIdx)
        if thisDir == 2:
            thisDir = 3
        elif thisDir == 0:
            thisDir = 1

            # r = [1, 1, -1, -1]
            # c = [1, -1, 1, -1]
    elif nowIdx[0]+r[thisDir]<w and nowIdx[0]+r[thisDir]>0 and nowIdx[1]+c[thisDir]==0:
        nowIdx = [nowIdx[0] + r[thisDir], nowIdx[1] + c[thisDir]]
        antRoute.append(nowIdx)
        if thisDir == 3:
            thisDir = 2
        elif thisDir == 1:
            thisDir = 0
    #모서리에 부딪힐 때
    else:
        print("di")
        antRoute.append(nowIdx)
        #nowIdx는 안바뀜
        if thisDir == 0:
            thisDir = 3
        elif thisDir == 1:
            thisDir =2
        elif thisDir == 2:
            thisDir = 3
        elif thisDir == 3:
            thisDir = 0
        nowIdx = [nowIdx[0] + r[thisDir], nowIdx[1] + c[thisDir]]
        antRoute.append(nowIdx)
    if len(antRoute)>1 and antRoute[-1] ==firIdx:
        if antRoute[-1] != antRoute[-2]:
            break
antRoute.pop()
print(antRoute)
if t<=len(antRoute)-1:
    print(antRoute[t])
else:
    print(antRoute[(t+1)%len(antRoute)])
