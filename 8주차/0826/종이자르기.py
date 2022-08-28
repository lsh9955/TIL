column,row = list(map(int,input().split()))
divideNum = int(input())
rowList = [0,row]
colList = [0,column]
for k in range(divideNum):
    dir,idx = list(map(int,input().split()))
    #가로 세로에 따라 리스트에 넣음. 숫자에 따라 들어가야 하는 위치를 지정해서 insert
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
#앞의 인수와 현재 인수의 차이만큼이 길이 이므로, 그 중 가장 긴 세로, 가로 길이를 구함
#모든 세로 가로는 겹치기 때문에 한 번은 만나므로, 가장 긴 세로와 가로의 길이를 곱해서 출력함
for a in range(len(rowList)-1):
    if rowMax<rowList[a+1]-rowList[a]:
        rowMax=rowList[a+1]-rowList[a]
for a in range(len(colList)-1):
    if colMax<colList[a+1]-colList[a]:
        colMax=colList[a+1]-colList[a]
print(rowMax*colMax)