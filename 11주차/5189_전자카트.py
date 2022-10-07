T = int(input())
for k in range(T):
    N = int(input())
    roadList = [list(map(int, input().split())) for _ in range(N)]
    checked = [1]+[0 for _ in range(N-1)]
    global minNum
    minNum = 99999

    def findRoute(before, checkLi, amount):
        global minNum
        if 0 in checkLi:
            for p in range(N):
                nowCheck = checkLi[:]
                if nowCheck[p] == 0:
                    nowCheck[p] = 1
                    addamount = roadList[before][p]
                    findRoute(p, nowCheck, amount+addamount)
        else:
            outPut = amount+roadList[before][0]
            minNum = outPut if minNum > outPut else minNum
    findRoute(0, checked, 0)
    print(f'#{k+1} {minNum}')
