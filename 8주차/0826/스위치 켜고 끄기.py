sNum = int(input())
sList = list(map(int, input().split()))
pNum = int(input())
for i in range(pNum):
    student = list(map(int, input().split()))
    cardNum = student[1]
    #해당 학생이 남학생이라면, 전체 길이까지 배수만큼 건너뛰면서 해당 인덱스의 숫자를 바꿈
    if student[0] == 1:
        thisCard = cardNum
        while thisCard <= sNum:
            if sList[thisCard - 1] == 0:
                sList[thisCard - 1] = 1
            else:
                sList[thisCard - 1] = 0
            thisCard += cardNum
    else:
        #해당 학생이 여학생이라면, 현재 인덱스는 무조건 숫자를 바꿈
        #옆으로 퍼져나가며(minNum이 현재 인덱스에서 건너간 횟수) 서로 같다면 숫자를 바꿈
        cardIdx = cardNum - 1
        minNum = 1
        sList[cardNum - 1] = 1 if sList[cardNum - 1] == 0 else 0
        while cardIdx - minNum >= 0 and cardIdx + minNum <= sNum - 1:
            if sList[cardIdx - minNum] == sList[cardIdx + minNum]:
                if sList[cardIdx - minNum] == 0:
                    sList[cardIdx - minNum] = 1
                    sList[cardIdx + minNum] = 1
                else:
                    sList[cardIdx - minNum] = 0
                    sList[cardIdx + minNum] = 0

                minNum += 1
            else:
                break
                #20개가 넘으면 다음줄에 출력되도록 함
for i in range(sNum):
    if (i+1)%20 == 0 or i==sNum-1:
        print(sList[i])
    else:
        print(sList[i], end=" ")
