for k in range(10):
    caseNumber, caseLength = map(int, input().split())              #케이스의 현재 순서와 길이를 입력
    inputLi = list(map(int, input().split()))                       #현재 케이스의 문자 리스트를 입력

    AdjList = [[0] * 100 for _ in range(100)]                       #0~99까지 100개의 배열이며, 1부터 시작하지 않기 때문에 길이를 100으로 지정
    for q in range(caseLength):
        AdjList[inputLi[q * 2]][inputLi[q * 2 + 1]] = 1             #2개마다 쌍으로 이루어져 있어, 인자 2개를 하나의 배열로 생각해 해당 인덱스에 1을 표시

    global foundAns
    foundAns = False                                                #가능한 경우가 있다면 True, 아니라면 False를 반환하는 foundAns 변수 생성


    def findRoute(thisV, thisVisited):
        global foundAns
        for i in range(100):                                        #nowIndex는 인자로 받은 해당 위치에서 다른 위치로 이동할 수 있는지를 파악
            nowIdx = AdjList[thisV][i]                              #nowIdx가 1이면 갈 수 있고, 0이면 갈 수 없음
            if i == 99 and nowIdx == 1:                             #99가 목적지이므로, 이동이 가능하다면 True로 foundAns 변경
                foundAns = True
                break
            elif nowIdx == 1 and i not in thisVisited:              #1이지만 아직 방문하지 않았다면, 해당 위치로 이동하고 visited처리 후
                nextVisit = thisVisited[:]                          #재귀로 다시 탐색
                nextVisit.append(i)
                findRoute(i, nextVisit)

    findRoute(0, [0])                                               #처음 시작은 0 이고, 0은 방문한 상태이므로 0,[0]에서 시작
    print(f'#{k+1} {1 if foundAns else 0}')                         #True,False값에 따라 결과를 출력