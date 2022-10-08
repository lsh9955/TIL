for k in range(10):
    caseNum = int(input())
    mazeList = [list(map(int,input())) for _ in range(16)]
    findRoute = [[1,1]]
    flag = 0
    while len(findRoute)>0:
        d=[0,0,1,-1]
        l=[1,-1,0,0]
        nowIdx = findRoute.pop()
        mazeList[nowIdx[0]][nowIdx[1]]=4
        thisFlag = False
        for a in range(4):
            if mazeList[nowIdx[0]+d[a]][nowIdx[1]+l[a]]==0:
                findRoute.append([nowIdx[0] + d[a],nowIdx[1] + l[a]])
            elif mazeList[nowIdx[0]+d[a]][nowIdx[1]+l[a]]==3:
                flag = 1
                thisFlag = True
                break
        if thisFlag:
            break
    print(f'#{caseNum} {flag}')