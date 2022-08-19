roundNum = int(input())
for i in range(roundNum):
    ACard = [0, 0, 0, 0]
    BCard = [0, 0, 0, 0]
    aList = list(map(int, input().split()))
    bList = list(map(int, input().split()))
    winner = ""
    for p in range(1, aList[0]):
        ACard[aList[p] - 1] += 1
    for p in range(1, bList[0]):
        BCard[bList[p] - 1] += 1
    if ACard[3] != BCard[3]:
        if ACard[3] > BCard[3]:
            winner = "A"
        else:
            winner = "B"
    elif ACard[2] != BCard[2]:
        if ACard[2] > BCard[2]:
            winner = "A"
        else:
            winner = "B"
    elif ACard[1] != BCard[1]:
        if ACard[1] > BCard[1]:
            winner = "A"
        else:
            winner = "B"
    elif ACard[0] != BCard[0]:
        if ACard[0] > BCard[0]:
            winner = "A"
        else:
            winner = "B"
    else:
        winner = "D"
    print(winner)
