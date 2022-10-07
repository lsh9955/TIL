T = int(input())
for k in range(T):
    nowList = list(map(int, input().split()))
    firList = []
    secList = []
    winner = 0
    for a in range(6):
        firList.append(nowList[a*2])
        secList.append(nowList[a*2+1])
        if len(firList) >= 3:
            firwinner = 0
            secWinner = 0
            firList.sort()
            secList.sort()
            for c in range(len(firList)-2):
                if firList[c] == firList[c+1] == firList[c+2]:
                    firwinner = 1
                    break
                elif firList[c]+1 == firList[c+1] and firList[c+1]+1 == firList[c+2]:
                    firwinner = 1
                    break
            for d in range(len(secList)-2):
                if secList[d] == secList[d+1] == secList[d+2]:
                    secWinner = 1
                    break
                elif secList[d]+1 == secList[d+1] and secList[d+1]+1 == secList[d+2]:
                    secWinner = 1
                    break
            if firwinner == 1 and secWinner == 1:
                winner = 0
                break
            elif firwinner == 1 and secWinner == 0:
                winner = 1
                break
            elif firwinner == 0 and secWinner == 1:
                winner = 2
                break
    print(f'#{k+1} {winner}')
