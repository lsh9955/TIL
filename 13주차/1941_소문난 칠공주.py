stulist = [list(map(str, input())) for _ in range(5)]
sidxlist = []
for a in range(19):
    for b in range(a+1, 20):
        for c in range(b+1, 21):
            for d in range(c+1, 22):
                for e in range(d+1, 23):
                    for f in range(e+1, 24):
                        for g in range(f+1, 25):
                            # 모든 경우의 수를 구함
                            # 해당 요소들의 index를 구함
                            peoplelist = [[a//5, a % 5], [b//5, b % 5], [c//5, c % 5],
                                          [d//5, d % 5], [e//5, e % 5], [f//5, f % 5], [g//5, g % 5]]
                            scount = 0
                            # 4명 이상인 경우에만 추가적인 계산 수행
                            for h in range(7):
                                if stulist[peoplelist[h][0]][peoplelist[h][1]] == "S":
                                    scount += 1
                            if scount >= 4:
                                # 4명 이상이라면 bfs 사용하여, 모든 수들이 붙어 있는지 파악
                                dr = [0, 0, 1, -1]
                                dc = [1, -1, 0, 0]
                                flag = True
                                thisidx = peoplelist.pop()

                                def findroute(idx):
                                    for j in range(4):
                                        if [idx[0]+dr[j], idx[1]+dc[j]] in peoplelist:
                                            nowidx = peoplelist.pop(peoplelist.index(
                                                [idx[0]+dr[j], idx[1]+dc[j]]))
                                            findroute(nowidx)
                                findroute(thisidx)
                                # 다 붙어 있다면, 해당 배열을 입력
                                if len(peoplelist) == 0:
                                    if [a, b, c, d, e, f, g] not in sidxlist:
                                        sidxlist.append([a, b, c, d, e, f, g])
print(len(sidxlist))
