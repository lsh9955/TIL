caseNum = int(input())
for k in range(caseNum):
    nowNum = int(input())
    board = [[0] * nowNum for _ in range(nowNum)]
    start = [0, 0]
    count = []


    def find(visitList, appendList, nowCount):
        global count
        for a in range(nowNum):
            for b in range(nowNum):
                if visitList[a][b] == 0:
                    thisAppendList = appendList[:]
                    thisAppendList.append(a)
                    thisAppendList.append(b)
                    nowList = visitList[:]
                    nowList[a][b] = 1

                    for p in range(nowNum):
                        nowList[a][p] = 0
                        nowList[p][b] = 0
                    l=[1,1,-1,-1]
                    r=[1,-1,1,-1]
                    for q in range(4):
                        c,d=a,b
                        while True:
                            if (c+l[q]>=0 and c+l[q]<=nowNum-1) and (d+r[q]>=0 and d+r[q]<=nowNum-1):
                                nowList[c+l[q]][d+r[q]]=0
                                c=c+l[q]
                                d=d+r[q]
                            else:
                                break

                    if nowCount == nowNum + 1:
                        count.append(thisAppendList)
                    else:
                        find(nowList, thisAppendList, nowCount + 1)
    find(board,[],0)
    print(count)