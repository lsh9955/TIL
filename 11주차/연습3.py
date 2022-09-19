T = int(input())
for k in range(T):
    numList = list(input())
    outputList = []
    upList = ["A","B","C","D","E","F"]
    alList = {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
    passwordPattern = {"001101":"0","010011":"1","111011":"2","110001":"3","100011":"4","110111":"5","001011":"6","111101":"7","011001":"8","101111":"9"}
    allBit = ""
    secList = [[]]
    allFourList =[]
    for p in range(len(numList)):
        thisNum = 0
        if numList[p] in upList:
            thisNum = alList[numList[p]]
        else:
            thisNum = int(numList[p])
        fourList = [0,0,0,0]
        for i in range(3,-1,-1):
            fourList[i]=str(thisNum%2)
            thisNum = thisNum//2
        allBit+="".join(fourList)
    a=0
    while True:
        if allBit[a:a+6] in passwordPattern:
            outputList.append(passwordPattern[allBit[a:a+6]])
            a=a+6
            if a>len(allBit)-7:
                break
        else:
            a=a+1
    print(" ".join(outputList))