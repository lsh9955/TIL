# N개의 피자를 구울 수 있음
# 한바퀴 돌면 C->C//2로 감소
# 1번부터 M까지 순서대로 화덕에 넣음
# 1번위치에서만 넣거나 뺄 수 있음

caseNum = int(input())
for k in range(caseNum):
    # 화덕에 넣을 수 있는 피자 양과 구워야 할 피자 개수를 입력
    N, M = list(map(int, input().split()))
    # 각 피자에 해당하는 치즈 양을 입력
    Ci = list(map(int, input().split()))
    # 현재 피자가 오븐에 넣어졌으면 1, 아직 굽지 않았으면 0으로 하는 리스트 생성
    pizzaList = [[_+1, Ci[_] // 2 + Ci[_] % 2] for _ in range(M)]
    nowOven = [pizzaList[i] for i in range(N)]
    makePizza = N

    print(min(nowOven))
    while makePizza <= M - 1:
        minNum, minIdx = 99999, 0
        print(nowOven)
        for p in range(N):
            if nowOven[p][1] < minNum:
                minNum = nowOven[p][1]
                minIdx = p
            elif nowOven[p][1] == minNum:
                if p<minIdx:
                    minIdx = p
        nowOven[minIdx] = [pizzaList[makePizza][0], pizzaList[makePizza][1] + nowOven[minIdx][1]]
        makePizza += 1
    maxNum,maxIdx=0,0
    for p in range(N):
        if nowOven[p][1]>maxNum:
            maxNum=nowOven[p][1]
            maxIdx=nowOven[p][0]
    print(nowOven)
    print(f"#{k + 1} {maxIdx}")
