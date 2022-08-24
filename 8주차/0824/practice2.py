#2. 사탕 나눠주기
candy = int(input())
QList = [0]*99
front,rear = -1,-1
totalMan = 1
#삽입
def enQueue(item):
    global rear
    if Full():
        print("Queue Full")
    else:
        rear = rear + 1
        QList[rear] = item
#삭제
def deQueue():
    global front
    global rear
    if isEmpty():
        print("Queue Empty")
    else:
        front = front+1
        return QList[front]
#큐가 비었는지, 가득 찼는지를 확인하는 함수
def isEmpty():
    return front == rear
def Full():
    return rear == len(QList) -1
#큐의 변경 없이 맨 첫번째 인자만 return함
def Qpeek():
    if isEmpty():
        print("Queue Empty")
    else:
        return QList[front+1]

#데이터를 큐에 삽입
enQueue([1,1])
while candy>0:
    #사탕받을 사람을 빼서 받아야할 사탕 개수만큼 전체에서 뺌
    candyMan = deQueue()
    candy -= candyMan[1]
    #사탕이 음수이면 다 받은것이므로 현재 사탕받는 사람을 출력 후 break
    if candy<=0:
        print(candyMan[0])
        break
    else:
        #되돌아가는 사람은 사탕을 하나 더 받으므로 추가해주고 다시 큐에 삽입
        #큐에 새로운 사람을 추가
        candyMan[1] += 1
        enQueue(candyMan)
        totalMan+=1
        enQueue([totalMan,1])


