from collections import deque
for k in range(10):
    thisCase=int(input())
    nowList = list(map(int,input().split()))
    deq = deque(nowList)
    subtractNum =1
    while deq[-1] > 0:
        deq.rotate(-1)
        if deq[-1]-subtractNum <= 0:
            deq[-1] = 0
            break
        else:
            deq[-1]-=subtractNum
            if subtractNum == 5:
                subtractNum = 1
            else:
                subtractNum+=1
    print(f'#{thisCase} {" ".join(map(str,deq))}')

