# livecell=[[livePower,resttime]]
# 처음 restime을 할당할 때 livepower에 -1을 곱한 값을 할당함
# 이후 time에 1씩 더하는 방식으로
# 전체 셀을 만들어서 livecell에서 비교하도록 설정
# 해당 방향에 이미 줄기세포가 있으면 못가게 하기
# 두 세포의 성장 index가 동일하면, 생명력 수치로 비교해서 정하기

T = int(input())
for a in range(T):
    N, M, K = list(map(int, input().split()))
    boardlist = [list(map(int, input().split())) for _ in range(N)]
    livecell = []
    growlist = {}
    nowtime = 0
    global thistimegrow
    thistimegrow = []
    for b in range(N):
        for c in range(M):
            if boardlist[b][c] != 0:
                # livecell=[[livePower,resttime,indx]]
                livecell.append([boardlist[b][c], -1*boardlist[b][c], [b, c]])
                growlist[f'{[b,c]}'] = boardlist[b][c]

    def growroute(idx, lifepower):
        dc = [0, 0, 1, -1]
        dr = [1, -1, 0, 0]
        for d in range(4):
            if f'{[idx[0]+dc[d], idx[1]+dr[d]]}' not in growlist:
                for h in range(len(thistimegrow)):
                    if thistimegrow[h][:2] == [idx[0]+dc[d], idx[1]+dr[d]]:
                        if thistimegrow[h][2] < lifepower:
                            thistimegrow.pop(h)
                            thistimegrow.append(
                                [idx[0]+dc[d], idx[1]+dr[d], lifepower])
                        break
                else:
                    thistimegrow.append(
                        [idx[0]+dc[d], idx[1]+dr[d], lifepower])

                # index가 겹치면, livepower가 더 큰 것으로 바꾸기

    for e in range(K+1):
        for f in range(len(livecell)-1, -1, -1):

            if 0 < livecell[f][1] <= livecell[f][0]:
                growroute(livecell[f][2], livecell[f][0])

        for j in range(len(thistimegrow)):
            growlist[f'{[thistimegrow[j][0],thistimegrow[j][1]]}'] = thistimegrow[j][2]
            livecell.append([thistimegrow[j][2], -1*thistimegrow[j][2],
                            [thistimegrow[j][0], thistimegrow[j][1]]])
        thistimegrow = []
        for f in range(len(livecell)-1, -1, -1):
            livecell[f] = [livecell[f][0], livecell[f][1]+1, livecell[f][2]]
            if livecell[f][1] == livecell[f][0]+1:
                livecell.pop(f)

    print(f'#{a+1} {len(livecell)}')
