# 어쨌든 다 탐색해봐야 하지 않을까?
import copy
T = int(input())
for a in range(T):

    N, W, H = list(map(int, input().split()))
    bricklist = [list(map(int, input().split())) for _ in range(H)]
    visitidx = []
    global minrestbrick
    minrestbrick = 99999
    # 현재 벽돌 상태,탐색 횟수

    def findroute(thisbricks, nowcount, restbrick):
        if nowcount == 0:
            if minrestbrick > restbrick:
                minrestbrick = restbrick
        else:
            for b in range(W):
                global nowbrick
                global boomlist
                nowbrick = copy.deepcopy(thisbricks)
                hitidx = []
                boomlist = []

                def boomfind(idx):
                    nownum = nowbrick[idx[0]][idx[1]] - 1
                    if nownum != 0:
                        dc = [1, -1, 0, 0]
                        dr = [0, 0, 1, -1]
                        for d in range(4):
                            for e in range(1, nownum+1):
                                if 0 <= idx[0]+dc[d]*e <= W-1 and 0 <= idx[1]+dr[d]*e <= W-1:
                                    if [idx[0]+dc[d]*e, idx[1]+dr[d]*e] not in boomlist:
                                        boomlist.append(
                                            [idx[0]+dc[d]*e, idx[1]+dr[d]*e])
                                        findroute(
                                            [idx[0]+dc[d]*e, idx[1]+dr[d]*e])

                for c in range(H):
                    if nowbrick[c][b] != 0:
                        hitidx = [c, b]
                        break
                boomfind(hitidx)
                for g in range(len(boomlist)):
                    nowbrick[boomlist[g][0]][boomlist[g][1]] = 0
                for h in range(W):
                    notZero = []
                    for j in range(H):
                        if nowbrick[j][h] != 0:
                            notZero.append(nowbrick[j][h])
                    for j in range(len(notZero)):
                        nowbrick[j+len(notZero)-1][h] = notZero[j]
                findroute(nowbrick, nowcount-1, restbrick-len(boomlist))
    findroute(bricklist,N,0)
    print(f'#{a+1} {minrestbrick}')