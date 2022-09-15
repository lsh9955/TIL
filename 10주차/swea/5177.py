T = int(input())
for k in range(T):
    N = int(input())
    inputList = list(map(int,input().split()))
    nodeList = [0 for _ in range(N+1)]
    nodeList[1] = inputList[0]
    inputList.pop(0)
    #부모 인덱스는 자식의 //2

    for a in range(N-1):
        parentNode = 0
        thisIdx = 0
        thisNode = inputList.pop(0)
        for p in range(1,N+1):
            if nodeList[p] ==0:
                nodeList[p]=thisNode
                parentNode = p//2
                thisIdx = p
                break
        while nodeList[parentNode]>thisNode:
            nodeList[parentNode],nodeList[thisIdx]=nodeList[thisIdx],nodeList[parentNode]
            thisIdx = parentNode
            parentNode = parentNode//2
            if parentNode == 0:
                break
        lastIdx = N//2
        parentSum = 0
        while lastIdx>0:
            parentSum +=nodeList[lastIdx]
            lastIdx = lastIdx//2
    print(f"#{k+1} {parentSum}")    




            
