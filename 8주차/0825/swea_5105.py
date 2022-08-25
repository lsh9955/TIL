caseNum = int(input())
for k in range(caseNum):
    #현재 케이스의 너비를 입력
    size = int(input())
    #입력받은 미로 정보에 따라 리스트 생성
    maze = [list(map(int,input())) for _ in range(size)]
    flag = True
    startIdx = [0,0]
    #몇 번 이동해야 도달할 수 있는지를 받는 변수
    #답이 9999로 나오면 이동이 불가능한 것이므로 나중에 답으로 0 출력
    count = 99999
    #해당 좌표를 방문하였는지를 파악하는 리스트 생성
    viList = [[0]*size for _ in range(size)]
    r = [0,0,-1,1]
    l = [1,-1,0,0]
    #처음 출발하는 좌표 찾기
    for a in range(size):
        if not flag:
            break
        for b in range(size):
            if maze[a][b] == 2:
                startIdx = [a,b]
                break

    def find(nowIdx,visitList,nowCount):
        global count
        c,d = nowIdx[0],nowIdx[1]
        #해당 좌표에서 상하좌우 중 3이 있으면, 현재 count를 출력하고, 아니면 방문하지 않고, 통로인 지점을 찾아
        #계속 탐색
        for p in range(4):
            if (c+r[p]>=0 and c+r[p]<=size-1) and (d+l[p]>=0 and d+l[p]<=size-1):
                if maze[c+r[p]][d+l[p]]==3:
                    if count > nowCount:
                        count = nowCount
                elif maze[c+r[p]][d+l[p]]==0 and visitList[c+r[p]][d+l[p]] ==0:
                    nowVi = visitList[:]
                    nowVi[c+r[p]][d+l[p]] = 1
                    find([c+r[p],d+l[p]],nowVi,nowCount+1)
    #초기값을 넣어 BFS실행
    find(startIdx,viList,0)
    #99999로 나오면 불가능한 것이므로 0 출력, 아니라면 해당 개수를 출력
    if count == 99999:
        print(f"#{k+1} 0")
    else:
        print(f"#{k+1} {count}")
