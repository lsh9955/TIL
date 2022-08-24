#1. 큐의 규현
N =  int(input())
inputList = list(map(int,input()))
QList = [0]*N
front,rear = -1,-1
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
for i in range(N):
    enQueue(inputList[i])
#큐에서 데이터를 차례로 꺼내 출력
for i in range(N):
    print(deQueue())
    print(QList)
#input
#3
#123
#outPut
#1
#2
#3