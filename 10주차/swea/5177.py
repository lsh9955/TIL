T = int(input())
for k in range(T):
    N = int(input())
    inputList = list(map(int,input().split()))
    nodeList = [0 for _ in range(N+1)]
    nodeList[1] = inputList[0]
    inputList.pop(0)
    #부모 인덱스는 자식의 //2
    while True:
        thisIdx = 0
        for p in range(1,N+1):
            
