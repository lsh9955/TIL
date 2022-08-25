rowList = [0 for _ in range(5)]
colList = [0 for _ in range(5)]
ru = [[4 - _, _] for _ in range(5)]
ld = [[_, _] for _ in range(5)]
ruList = 0
ldList = 0
bingoList = [list(map(int, input().split())) for _ in range(5)]
bingDict = {}
for a in range(5):
    for b in range(5):
        bingDict[bingoList[a][b]] = [a, b]
checkList = [list(map(int, input().split())) for _ in range(5)]
flag = True
for a in range(5):
    if not flag:
        break
    for b in range(5):
        if bingDict[checkList[a][b]] in ru:
            ruList += 1
        if bingDict[checkList[a][b]] in ld:
            ldList += 1
        colList[bingDict[checkList[a][b]][0]] += 1
        rowList[bingDict[checkList[a][b]][1]] += 1
        row=1 if ruList ==5 else 0
        column = 1 if ldList ==5 else 0
        if colList.count(5)+rowList.count(5)+row+column==3:
            print(a*5+b+1)
            flag=False
            break

