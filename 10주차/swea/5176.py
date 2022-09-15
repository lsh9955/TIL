T = int(input())
for k in range(T):
    N = int(input())
    targetNum = N
    addNum = []
    for q in range(10):
        if 2**q<targetNum:
            addNum.append(2**q)
            targetNum-=2**q
        else:
            addNum.append(targetNum)
            break
    addList = [_ for _ in range(1,N+1)]
    orderList = []
    while True:
        if len(addList) == 1:
            orderList.insert(0,addList[0])
            break
        else:
            for b in range(addNum[-1]-1,-1,-1):

                orderList.insert(0,addList[2*b])
                addList.pop(2*b)
            addNum.pop()
    print(f'#{k+1} {orderList[0]} {orderList[N//2-1]}')
