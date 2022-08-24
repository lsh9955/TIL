from collections import deque
for k in range(10):
    #현재 케이스의 번호와 리스트를 받아옴
    thisCase=int(input())
    nowList = list(map(int,input().split()))
    deq = deque(nowList)
    #뺄 숫자를 변수로 지정
    subtractNum =1

    while deq[-1] > 0:
        #rotate를 하면 [1,2,3,4] => [2,3,4,1] 로 됨
        deq.rotate(-1)
        #맨 마지막 요소가 0보다 작거나 같으면 0으로 지정하고 빠져나옴
        if deq[-1]-subtractNum <= 0:
            deq[-1] = 0
            break
        else:
            #subtracNum이 5가 되면 1로 바꾸고, 아니면 계속 1을 더해나감
            deq[-1]-=subtractNum
            if subtractNum == 5:
                subtractNum = 1
            else:
                subtractNum+=1
    print(f'#{thisCase} {" ".join(map(str,deq))}')

