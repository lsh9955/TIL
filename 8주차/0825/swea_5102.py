caseNum = int(input())
for k in range(caseNum):
    #노드 개수와 간선 정보를 입력받음
    V, E = list(map(int, input().split()))
    #해당 노드와 연결된 노드를 저장하는 리스트 생성
    graphList = [[] for _ in range(V + 1)]
    for p in range(E):
        #해당 노드의 인덱스에 연결된 노드의 번호를 입력
        fir, sec = list(map(int, input().split()))
        graphList[fir].append(sec)
        graphList[sec].append(fir)
    #시작 노드와 끝나는 노드를 입력
    start, end = list(map(int, input().split()))
    #방문한 노드 리스트
    visitList = [0 for _ in range(V + 1)]
    visitList[start] = 1
    #몇 번 이동해야 도달할 수 있는지를 받는 변수
    #답이 9999로 나오면 이동이 불가능한 것이므로 나중에 답으로 0 출력
    connect = 9999


    def find(nowV, visit, countNum):
        #해당 노드가 end와 연결되어 있다면 connect에 개수를 대입
        global connect
        if end in graphList[nowV]:
            if connect > countNum + 1:
                connect = countNum + 1
        else:
            #아직 방문하지 않은 노드가 있다면, 해당 노드를 방문하고 다시 BFS함수 실행
            for q in range(len(graphList[nowV])):
                if visit[graphList[nowV][q]] == 0:
                    nowVisit = visit[:]
                    nowVisit[graphList[nowV][q]] = 1
                    find(graphList[nowV][q], nowVisit, countNum + 1)

    #초기값을 넣어 BFS실행
    find(start, visitList, 0)
    #9999로 나오면 불가능한 것이므로 0 출력, 아니라면 해당 개수를 출력
    if connect == 9999:
        print(f"#{k + 1} 0")
    else:
        print(f"#{k + 1} {connect}")
