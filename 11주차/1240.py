T = int(input())
for k in range(T):
    N,M = list(map(int,input().split()))
    bitList = [input() for _ in range(N)]
    targetList = []
    for c in range(len(bitList)):
        if "1" in bitList[c]:
            targetList = bitList[c]  

    outputList = []
    passwordPattern = {"0001101":"0","0011001":"1","0010011":"2","0111101":"3","0100011":"4","0110001":"5","0101111":"6","0111011":"7","0110111":"8","0001011":"9"}
    a=0
    firIdx = 0
    nextTo = True
    while True:
        if not nextTo:
            a = firIdx +1
            nextTo = True
        if a !=0 and targetList[a:a+7] in passwordPattern and firIdx==0:
            firIdx = a
            outputList.append(int(passwordPattern[targetList[a:a+7]]))
            a=a+7
        elif targetList[a:a+7] in passwordPattern:
            outputList.append(int(passwordPattern[targetList[a:a+7]]))
            a=a+7
        else:
            nextTo = False
        if a>len(targetList)-8:
            break
    print(outputList)
    evenNum =0
    oddNum = 0
    for p in range(len(outputList)):
        if p%2 == 0:
            evenNum+=outputList[p]
        else:
            oddNum +=outputList[p]
    if (evenNum*3+oddNum)%10 == 0:
        print(f'#{k+1} {sum(outputList)}')
    else:
        print(f'#{k+1} 0')