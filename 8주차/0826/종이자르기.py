column,row = list(map(int,input().split()))
divideNum = int(input())
rowList = [0,row]
colList = [0,column]
for k in range(divideNum):
    dir,idx = list(map(int,input().split()))
    if dir == 0:
        for p in range(len(rowList)-1):
            if rowList[p]<idx<rowList[p+1]:
                rowList.insert(p+1,idx)
    else:
        for p in range(len(colList)-1):
            if colList[p]<idx<colList[p+1]:
                colList.insert(p+1,idx)
rowMax=0
colMax=0
for a in range(len(rowList)-1):
    if rowMax<rowList[a+1]-rowList[a]:
        rowMax=rowList[a+1]-rowList[a]
for a in range(len(colList)-1):
    if colMax<colList[a+1]-colList[a]:
        colMax=colList[a+1]-colList[a]
print(rowMax*colMax)