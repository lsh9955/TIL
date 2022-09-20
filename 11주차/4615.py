T = int(input())
for k in range(T):
    N,M = list(map(int,input().split()))
    board = [[0 for _ in range(N)] for _ in range(N)]
    board[N//2-1][N//2-1] = 2
    board[N//2-1][N//2] = 1
    board[N//2][N//2-1] = 1
    board[N//2][N//2] = 2
    blackCount = 0
    whiteCount = 0
    for a in range(M):
        x,y,stone = list(map(int,input().split()))          
        x = x-1
        y = y-1
        board[y][x] = stone
        dirX = [-1,0,1,1,1,0,-1,-1]
        dirY = [1,1,1,0,-1,-1,-1,0]
        for b in range(8):
            thisCount = 1
            while (y+dirY[b]*thisCount>=0 and y+dirY[b]*thisCount<=N-1 and x+dirX[b]*thisCount>=0 and x+dirX[b]*thisCount<=N-1):
                if board[y+dirY[b]*thisCount][x+dirX[b]*thisCount]== 0:
                    break
                elif board[y+dirY[b]*thisCount][x+dirX[b]*thisCount]== stone:
                    for c in range(thisCount):
                        if board[y+dirY[b]*c][x+dirX[b]*c] != stone:
                            board[y+dirY[b]*c][x+dirX[b]*c] = stone
                    break
                else:
                    thisCount+=1

    for d in range(N):
        for e in range(N):
            if board[d][e] ==1:
                blackCount+=1
            elif board[d][e] ==2:
                whiteCount+=1
    print(f'#{k+1} {blackCount} {whiteCount}')
