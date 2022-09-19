T = int(input())
for k in range(T):
    numList = list(input())
    outputList = []
    upList = ["A","B","C","D","E","F"]
    alList = {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
    secList = [[]]
    allFourList =[]
    for p in range(len(numList)):
        thisNum = 0
        if numList[p] in upList:
            thisNum = alList[numList[p]]
        else:
            thisNum = int(numList[p])
        fourList = [0,0,0,0]
        for i in range(3,-1,-1):
            fourList[i]=thisNum%2
            thisNum = thisNum//2
        allFourList+=fourList
    for x in range(len(allFourList)):
        if len(secList[-1])==7:
            secList.append([])
        secList[-1].append(allFourList[x])
    


    for a in range(len(secList)):
        thisNum = 0
        nowIdx = 1
        for b in range(len(secList[a])-1,-1,-1):
            if secList[a][b] == 1:
                thisNum += nowIdx
            nowIdx = nowIdx *2
        outputList.append(str(thisNum))
    print(" ".join(outputList))
