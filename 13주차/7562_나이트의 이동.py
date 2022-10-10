from collections import deque
#체스의 움직일 수 있는 위치
moving = [[-2, 1], [-2, -1], [-1, 2],
          [-1, -2], [2, 1], [2, -1], [1, 2], [1, -2]]
T = int(input())
for a in range(T):
    l = int(input())
    nowidx = list(map(int, input().split()))
    willmoveidx = list(map(int, input().split()))
    #체스판 생성
    chessboard = [[0]*l for _ in range(l)]
    #현재 말 위치를 1로 지정
    chessboard[nowidx[0]][nowidx[1]] = 1

    def findroute(idx):
        global findcount
        idxlist = deque()
        idxlist.append(idx)
        #시작점부터 탐색 시작
        while idxlist:
            searchidx = idxlist.popleft()
            #다음에 말이 도착하는 지점에 현재 지점에서의 수보다 1을 더해, 탐색 횟수를 지정함
            addnum = chessboard[searchidx[0]][searchidx[1]]+1
            #도착 지점에서의 좌표가 목표 좌표와 같다면 해당 수(탐색횟수)를 return
            if searchidx[0] == willmoveidx[0] and searchidx[1] == willmoveidx[1]:
                return chessboard[searchidx[0]][searchidx[1]]
                #총 8개의 경우의 수가 있으므로, 탐색 좌표가 0이면 해당 좌표를 idxlist에 넣고 
                #해당 좌표에다 탐색 횟수를 적음
            for b in range(8):
                if 0 <= searchidx[0]+moving[b][0] <= l-1 and 0 <= searchidx[1]+moving[b][1] <= l-1:
                    if chessboard[searchidx[0]+moving[b][0]][searchidx[1]+moving[b][1]] == 0:
                        idxlist.append(
                            [searchidx[0]+moving[b][0], searchidx[1]+moving[b][1]])
                        chessboard[searchidx[0]+moving[b][0]
                                   ][searchidx[1]+moving[b][1]] = addnum
    #탐색 좌표와 출발 좌표가 같은 경우도 있으므로, 이때는 움직이지 않아도 되니 0을 return
    if nowidx == willmoveidx:
        print(0)
    else:
        # 처음 시작할 때 1을 더했으므로
        print(findroute(nowidx)-1)
