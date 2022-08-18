for k in range(10):
    caseNumber, caseLength = map(int, input().split())
    inputLi = list(map(int, input().split()))

    AdjList = [[0] * 100 for _ in range(100)]
    for q in range(caseLength):
        AdjList[inputLi[q * 2]][inputLi[q * 2 + 1]] = 1

    stack = [0]
    visited = [0]

    global foundAns
    foundAns = False


    def findRoute(thisV, thisVisited):
        global foundAns
        for i in range(100):
            nowIdx = AdjList[thisV][i]
            if i == 99 and nowIdx == 1:
                foundAns = True
                break
            elif nowIdx == 1 and i not in thisVisited:
                nextVisit = thisVisited[:]
                nextVisit.append(i)
                findRoute(i, nextVisit)

    findRoute(0, [0])
    print(f'#{k+1} {1 if foundAns else 0}')