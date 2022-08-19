paperNum = int(input())
nowP = [list(map(int, input().split())) for _ in range(paperNum)]
filledList = {}
countLi = [0 for _ in range(paperNum)]
for k in range(paperNum):
    for a in range(nowP[k][0], nowP[k][0] + nowP[k][2]):
        for b in range(nowP[k][1], nowP[k][1] + nowP[k][3]):
            filledList[f'{a},{b}'] = k
for k in filledList:
    countLi[filledList[k]] += 1
for i in range(paperNum):
    print(countLi[i])
#42점따리