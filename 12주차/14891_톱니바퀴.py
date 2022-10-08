magList = [list(map(int,input())) for _ in range(4)]
K = int(input())
rotList = [list(map(int,input().split())) for _ in range(K)]
#시계,반시계 방향으로 돌아가게 하는 함수 생성
def rotateRow(input,rot):
    thisA = input[:]
    if rot == 1:
        willA = thisA.pop()
        thisA.insert(0, willA)
        return thisA
    else:
        willA = thisA.pop(0)
        thisA.append(willA)
        return thisA

for a in range(K):
    #서로 맞닿은 부분이 다른지 파악
    targetMag = rotList[a][0]
    diffList = [0, 0, 0]
    if magList[0][2] != magList[1][6]:
        diffList[0]=1
    if magList[1][2] != magList[2][6]:
        diffList[1]=1
    if magList[2][2] != magList[3][6]:
        diffList[2]=1
    #어떤 톱니바퀴가 돌아가는지에 따라, 맞물린 부분들을 조사하여 해당 부분이 다르면
    #돌아가도록 작성
    #건너뛴 톱니바퀴는 타겟과 같은 방향으로 돌아가야 함
    if targetMag==1:
        if diffList[0]==1:
            magList[1] = rotateRow(magList[1], -rotList[a][1])
            if diffList[1]==1:
                magList[2]=rotateRow(magList[2], rotList[a][1])
                if diffList[2]==1:
                    magList[3] = rotateRow(magList[3], -rotList[a][1])
    elif targetMag==4:
        if diffList[2]==1:
            magList[2] = rotateRow(magList[2], -rotList[a][1])
            if diffList[1]==1:
                magList[1]=rotateRow(magList[1], rotList[a][1])
                if diffList[0]==1:
                    magList[0] = rotateRow(magList[0], -rotList[a][1])
    elif targetMag==2:
        if diffList[1] == 1:
            magList[2] = rotateRow(magList[2], -rotList[a][1])
            if diffList[2] == 1:
                magList[3] = rotateRow(magList[3], rotList[a][1])
        if diffList[0] == 1:
            magList[0] = rotateRow(magList[0], -rotList[a][1])
    elif targetMag==3:
        if diffList[1] == 1:
            magList[1] = rotateRow(magList[1], -rotList[a][1])
            if diffList[0] == 1:
                magList[0] = rotateRow(magList[0], rotList[a][1])
        if diffList[2] == 1:
            magList[3] = rotateRow(magList[3], -rotList[a][1])
    magList[targetMag - 1] = rotateRow(magList[targetMag - 1], rotList[a][1])
sumOutput = 0
for b in range(4):
    if magList[b][0]==1:
        sumOutput+=2**b
print(sumOutput)
