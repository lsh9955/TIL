caseNum = int(input())
for i in range(caseNum):
    nowWidth = int(input())
    maxSquarePaperNum = nowWidth // 20

    tenPaperNum = (nowWidth - maxSquarePaperNum * 20) // 10
    totalCount = 0
    while maxSquarePaperNum >= 0:
        if tenPaperNum >= maxSquarePaperNum:
            firCount = 1
            secCount = 1
            for k in range(maxSquarePaperNum):
                firCount *= (tenPaperNum + 1 - k)
                secCount *= (maxSquarePaperNum - k)

            totalCount += (firCount // secCount)*(2**(maxSquarePaperNum+1))
        else:
            firCount = 1
            secCount = 1
            for k in range(tenPaperNum):
                firCount *= (maxSquarePaperNum + 1 - k)
                secCount *= (tenPaperNum - k)

            totalCount += (firCount // secCount)*(2**(maxSquarePaperNum+1))
        maxSquarePaperNum -= 1
    print(totalCount)