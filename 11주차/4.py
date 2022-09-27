# 맨밑 1
# 3 2 3 1 3 2 3
# 3이 1인데 2가 0이면 안됨
# 가운데는 무조건 1
# 개수는 무조건 1+2**n
# 4 3 4 2 4 3 4 1 4 3 4 2 4 3 4

def solution(numbers):
    answer = []
    for k in range(len(numbers)):
        targetNum = numbers[k]
        secList = []
        while targetNum>0:
            secList.insert(0,targetNum%2)
            targetNum //=2

        thisLen = len(secList)-1
        countSec = 1
        while True:
            if thisLen-2**countSec==0:
                thisLen=0
                break
            elif thisLen-2**countSec>0:
                thisLen -= 2 ** countSec
            elif thisLen-2**countSec<0:
                willAdd = 2**countSec-thisLen
                thisLen = willAdd
                break
            countSec+=1
        findLi = [0 for _ in range(thisLen)]+secList
        layerLi = []
        for a in range(countSec+1):
            layerLi.append([])
            for b in range(len(findLi)-1,-1,-1):
                if b%2==0:
                    layerLi[-1].append(findLi[b])
                    findLi.pop(b)
            layerLi[-1].reverse()
        flag = False
        ispossible = 1
        if numbers[k]==1:
            answer.append(1)
        else:
            for a in range(countSec):
                if flag:
                    break
                for b in range(len(layerLi[a+1])):
                    if layerLi[a+1][b]==0 and (layerLi[a][b*2]==1 or layerLi[a][b*2+1]==1):
                        flag = True
                        ispossible = 0
                        break
            answer.append(ispossible)

    return answer
print(solution([1,2,3,4,5,6,7,8,9,10]))