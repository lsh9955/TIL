def babyGin(target):
    isBabyGin=False
    inputStr =list(str(target))
    input = list(map(int, inputStr))
    for a in range(4):
        if isBabyGin:
            break
        for b in range(a+1,5):
            if isBabyGin:
                break
            for c in range(b+1,6):
                firList = [input[a],input[b],input[c]]
                secList =[]
                for d in range(6):
                    if d !=a and d != b and d != c:
                        secList.append(input[d])
                firList.sort()
                secList.sort()

                fir = False
                sec = False
                if firList[0]==firList[1]==firList[2] or firList[0]+1==firList[1] and firList[1]+1==firList[2]:
                    fir = True
                if secList[0]==secList[1]==secList[2] or secList[0]+1==secList[1]and secList[1]+1==secList[2]:
                    sec = True
                if fir and sec :
                    isBabyGin = True
                    break
    if isBabyGin:
        print("True")
    else:
        print("False")
babyGin(124783)
babyGin(667767)
babyGin("054060")
babyGin(101123)
#False
#True
#True
#False













