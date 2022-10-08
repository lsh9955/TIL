import sys
sys.setrecursionlimit(10**6)
moving = [[-2, 1], [-2, -1], [-1, 2],
          [-1, -2], [2, 1], [2, -1], [1, 2], [1, -2]]
T = int(input())
for a in range(T):
    l = int(input())
    nowidx = list(map(int, input().split()))
    willmoveidx = list(map(int, input().split()))
    chessboard = [[0]*l for _ in range(l)]
    chessboard[nowidx[0]][nowidx[1]] = 1
    global findcount
    findcount = 99999

    def findroute(idx, count):
        global findcount
        for b in range(8):
            if 0 <= idx[0]+moving[b][0] <= l-1 and 0 <= idx[1]+moving[b][1] <= l-1:
                if [idx[0]+moving[b][0], idx[1]+moving[b][1]] == willmoveidx:
                    if findcount > count+1:
                        findcount = count+1
                    break
                elif chessboard[idx[0]+moving[b][0]][idx[1]+moving[b][1]] == 0:
                    chessboard[idx[0]+moving[b][0]][idx[1]+moving[b][1]] = 1
                    findroute(
                        [idx[0]+moving[b][0], idx[1]+moving[b][1]], count+1)

    findroute(nowidx, 0)

    print(findcount)
