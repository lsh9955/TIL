for k in range(10):
    N = int(input())
    inputList = [list(input().split()) for _ in range(N)]
    idx=["" for _ in range(N+1)]
    r=[0 for _ in range(N+1)]
    l=[0 for _ in range(N+1)]
    calList =["+","-","/","*"]
    for p in range(N):
        if len(inputList[p]) == 4:
            idx[int(inputList[p][0])] = inputList[p][1]
            r[int(inputList[p][0])] = int(inputList[p][2])
            l[int(inputList[p][0])] = int(inputList[p][3])
        else:
            idx[int(inputList[p][0])] =  int(inputList[p][1])
    while len(idx)>2:
        secNum = idx.pop()
        firNum = idx.pop()
        calIdx = ""
        calNum = 0
        for q in range(len(idx)-1,-1,-1):
            if idx[q] in calList:
                calIdx = idx[q]
                idx.pop(q)
                break
        if calIdx == "+":
            calNum = firNum + secNum
        elif calIdx == "-":
            calNum = firNum - secNum
        elif calIdx == "/":
            calNum = firNum//secNum
        elif calIdx == "*":
            calNum = firNum*secNum
        idx.insert(-1,calNum)
    print(idx[0])