#SWEA 6808
inputNum = int(input())

for i in range(inputNum):
    global nowList, winCount, loseCount
    # 현재 규영이의 리스트,이긴 횟수와 진 횟수를 변수로 생성
    nowList = list(map(int, input().split()))
    InYoungList = []
    winCount = 0
    loseCount = 0
    #인영이의 리스트는 규영이의 카드를 제외한 숫자들로 생성
    for k in range(1, 19):
        if k not in nowList:
            InYoungList.append(k)

    #라운드를 진행하는 함수를 생성
    def gaming(targetList, nowCount, KyuScore, InYoungScore):
        global winCount, loseCount
        #아직 9회 미만이면 게임을 진행
        if nowCount <= 8:
            for q in range(9):
                #아직 뽑지 않은 카드가 있다면, 뽑아서 게임을 진행
                if targetList[q] != 0:
                    nowTarget = targetList[:]
                    # 이부분을 0으로 했었는데 else나 if 둘 중 하나만 거치게 되므로 0으로 초기화가 되어버림. 기존의 스코어를 받는 게 맞음
                    changeInYoungScore = InYoungScore
                    changeKyuScore = KyuScore
                    #인영의 카드 숫자가 규영 카드 숫자보다 크다면 인영 스코어에 점수를 더함
                    if nowTarget[q] > nowList[nowCount]:
                        changeInYoungScore = InYoungScore + nowTarget[q] + nowList[nowCount]
                    #규영의 카드 숫자가 인영쓰의 카드 숫자보다 크다면 규영 스코어에 점수를 더함
                    else:
                        changeKyuScore = KyuScore + nowTarget[q] + nowList[nowCount]
                    #뽑은 카드이므로 0으로 바꿈
                    nowTarget[q] = 0
                    #게임을 계속 진행
                    gaming(nowTarget, nowCount + 1, changeKyuScore, changeInYoungScore)
        #모든 게임이 끝났다면 스코어를 비교하여 패,승을 입력
        else:
            if KyuScore > InYoungScore:
                winCount += 1
            elif InYoungScore > KyuScore:
                loseCount += 1

    #초기값을 0으로 하고 게임을 진행
    gaming(InYoungList, 0, 0, 0)
    #결과값 출력
    print(f'#{i + 1} {winCount} {loseCount}')