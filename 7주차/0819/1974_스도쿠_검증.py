caseNum = int(input())
for k in range(caseNum):
    nowList = [list(map(int,input().split())) for _ in range(9)]
    allDiff = True
    for p in range(9):
        if len(set(nowList[p])) !=9:
            allDiff = False
            break

        columnList=[]
        for q in range(9):
            columnList.append(nowList[q][p])
        if len(set(columnList)) !=9:
            allDiff = False
            break
        boxList = []
        startIdx = [0, 3, 6]
        endIdx = [0,3,6]
        for a in range(3):
            for b in range(3):
                for c in range(3):
                    for d in range(3):
                        boxList.append(nowList[c+startIdx[a]][d+endIdx[b]])
                if len(set(boxList)) !=9:
                    allDiff = False
                    break
    if not allDiff:
        print(f'#{k+1} 0')
    else:
        print(f'#{k+1} 1')