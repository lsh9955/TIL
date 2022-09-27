T = int(input())
for k in range(T):
    D, M, tM, Y = list(map(int, input().split()))
    monthPlan = list(map(int, input().split()))
    tMPlan = [0 for _ in range(12)]
    addAmount = 0
    DMPlan = [0 for _ in range(12)]
    allNum = 0
    outPutNum=0
    for a in range(12):
        DMPlan[a] = min(D*monthPlan[a],M)
        allNum+=min(D*monthPlan[a],M)
    outPutNum = allNum
    #3이 하나 있을 떄
    #하나의 길이가 3이므로 최대로 갈 수 있는 index는 9까지(9 10 11)
    for b in range(10):
        thisNum = allNum
        if outPutNum>thisNum+tM-DMPlan[b]-DMPlan[b+1]-DMPlan[b+2]:
            outPutNum = thisNum+tM-DMPlan[b]-DMPlan[b+1]-DMPlan[b+2]
    # 3이 두개 있을 떄
    #두 개가 모두 끝에 몰려있다고 생각하면, 첫 번째 요소의 최대 인덱스는 6(6,7,8), 두 번째 요소의 최대 인덱스는 9(9,10,11)
    #범위를 제대로 설정을 안해서 3시간을 날렸
    #기본 문법부터 다시 공부하기
    for a in range(7):
        for b in range(a+3,10):
            thisNum = allNum
            if outPutNum>thisNum+2*tM-DMPlan[b]-DMPlan[b+1]-DMPlan[b+2]-DMPlan[a]-DMPlan[a+1]-DMPlan[a+2]:
                outPutNum=thisNum + 2 * tM - DMPlan[b] - DMPlan[b + 1] - DMPlan[b + 2] - DMPlan[a] - DMPlan[a + 1] - DMPlan[a + 2]
    # 3이 3개 있을 떄
    for a in range(4):
        for b in range(a+3,7):
            for c in range(b+3,10):
                thisNum = allNum
                if outPutNum>thisNum+3*tM-DMPlan[b]-DMPlan[b+1]-DMPlan[b+2]-DMPlan[a]-DMPlan[a+1]-DMPlan[a+2]-DMPlan[c]-DMPlan[c+1]-DMPlan[c+2]:
                    outPutNum=thisNum + 3 * tM - DMPlan[b] - DMPlan[b + 1] - DMPlan[b + 2] - DMPlan[a] - DMPlan[a + 1] - DMPlan[a + 2] - DMPlan[c] - DMPlan[c + 1] - DMPlan[c + 2]
    # 3이 4개 있을 떄
    if outPutNum>4*tM:
        outPutNum=4*tM
    # 모든 경우의 수와 연간권 비교
    if outPutNum>Y:
        outPutNum=Y
    print(f'#{k+1} {outPutNum}')
    # for a in range(12):
    #     if tMPlan[a] == 0:
    #         if a == 10:
    #             leastDayMonth = min(D*monthPlan[10],M)+min(D*monthPlan[11],M)
    #             if tM<leastDayMonth:
    #                 addAmount+=tM
    #                 break
    #             else:
    #                 addAmount+=min(D * monthPlan[10], M)
    #         elif a == 11:
    #             leastDayMonth = min(D * monthPlan[11], M)
    #             if tM < leastDayMonth:
    #                 addAmount += tM
    #                 break
    #             else:
    #                 addAmount += leastDayMonth
    #                 break
    #         else:
    #             leastDayMonth = min(D * monthPlan[a], M) + min(D * monthPlan[a+1], M)+ min(D * monthPlan[a+2], M)
    #             if tM < leastDayMonth:
    #                 addAmount += tM
    #                 tMPlan[a], tMPlan[a + 1], tMPlan[a + 2] = 1, 1, 1
    #             else:
    #                 addAmount += min(D * monthPlan[a], M)
    #     print(tMPlan)
    # if addAmount>Y:
    #     print(f'#{k+1} {Y}')
    # else:
    #     print(f'#{k+1} {addAmount}')

