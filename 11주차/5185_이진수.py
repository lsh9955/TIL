T = int(input())
for k in range(T):
    numLen,numList = list(input().split())
    outputList = []
    upList = ["A","B","C","D","E","F"]
    alList = {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
    allFourList =[]
    for p in range(len(numList)):
        thisNum = 0
        if numList[p] in upList:
            thisNum = alList[numList[p]]
        else:
            thisNum = int(numList[p])
        fourList = [0,0,0,0]
        for i in range(3,-1,-1):
            fourList[i]=str(thisNum%2)
            thisNum = thisNum//2
        allFourList+=fourList
    print(f'#{k+1} {"".join(allFourList)}')
