caseNum = int(input())
for k in range(caseNum):
    N = int(input())
    mazeList = [list(map(int, input())) for _ in range(N)]
    startIdx = [0, 0]
    xList = [0, 0, 1, -1]
    yList = [1, -1, 0, 0]
    find = 0
    for a in range(N):
        flag=False
        for b in range(N):
            if mazeList[a][b] == 3:
                startIdx = [a,b]
                flag = True
                break
        if flag:
            break
    routeStack = [startIdx[:]]
    forbiddenStack = []
    while len(routeStack) != 0:
        nowX = routeStack[-1][1]
        nowY = routeStack[-1][0]
        for i in range(4):
            if 0 <= nowY + yList[i] <= N - 1 and 0 <= nowX + xList[i] <= N - 1:
                if mazeList[nowY + yList[i]][nowX + xList[i]] == 2:
                    find = 1
                    routeStack = []
                    break
        if find == 1:
            break
        else:
            for i in range(4):
                if 0 <= nowY + yList[i] <= N - 1 and 0 <= nowX + xList[i] <= N - 1:
                    if mazeList[nowY + yList[i]][nowX + xList[i]] == 0 and [nowY + yList[i],
                                                                            nowX + xList[i]] not in forbiddenStack and [
                        nowY + yList[i], nowX + xList[i]] not in routeStack:
                        routeStack.append([nowY + yList[i], nowX + xList[i]])
                        break
            else:
                forbiddenStack.append(routeStack.pop())
    print(f'#{k + 1} {find}')