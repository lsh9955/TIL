# 연습 1
T = int(input())
for k in range(T):
    numList = list(map(int,input()))
    outputList = []
    for p in range(len(numList)//7):
        thisNum = 0
        nowIdx = 2**6
        for q in range(7):
            if numList[p*7+q] == 1:
                thisNum += nowIdx
            nowIdx = nowIdx //2
        outputList.append(str(thisNum))
    print(" ".join(outputList))
