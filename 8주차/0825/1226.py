for k in range(10):
    caseNum = int(input())
    maze = [list(map(int,input())) for _ in range(16)]
    visited = [[0]*16 for _ in range(16)]
    flag = True
    startIdx = [0,0]
    #몇 번 이동해야 도달할 수 있는지를 받는 변수
    #답이 9999로 나오면 이동이 불가능한 것이므로 나중에 답으로 0 출력
    count = 99999
    #해당 좌표를 방문하였는지를 파악하는 리스트 생성
    viList = [[0]*16 for _ in range(16)]
    r = [0,0,-1,1]
    l = [1,-1,0,0]
    #처음 출발하는 좌표 찾기
    for a in range(16):
        if not flag:
            break
        for b in range(16):
            if maze[a][b] == 2:
                startIdx = [a,b]
                break
    def BFS(nowIdx,visitList,nowCount):
        global count
        c, d = nowIdx[0], nowIdx[1]
        # 해당 좌표에서 상하좌우 중 3이 있으면, 현재 count를 출력하고, 아니면 방문하지 않고, 통로인 지점을 찾아
        # 계속 탐색
        for p in range(4):
            if (c + r[p] >= 0 and c + r[p] <= 15) and (d + l[p] >= 0 and d + l[p] <= 15):
                if maze[c + r[p]][d + l[p]] == 3:
                    if count > nowCount:
                        count = nowCount
                elif maze[c + r[p]][d + l[p]] == 0 and visitList[c + r[p]][d + l[p]] == 0:
                    visitList[c + r[p]][d + l[p]] = 1
                    BFS([c + r[p], d + l[p]], visitList, nowCount + 1)
    BFS(startIdx,visited,0)
    if count == 99999:
        print(f"#{k+1} 0")
    else:
        print(f"#{k+1} 1")