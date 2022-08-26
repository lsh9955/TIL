sNum = int(input())
sList = list(map(int, input().split()))
pNum = int(input())
for i in range(pNum):
    student = list(map(int, input().split()))
    cardNum = student[1]
    if student[0] == 1:
        thisCard = cardNum
        while thisCard <= sNum:
            if sList[thisCard - 1] == 0:
                sList[thisCard - 1] = 1
            else:
                sList[thisCard - 1] = 0
            thisCard += cardNum
    else:
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
for i in range(sNum):
    if (i+1)%20 == 0 or i==sNum-1:
        print(sList[i])
    else:
        print(sList[i], end=" ")
