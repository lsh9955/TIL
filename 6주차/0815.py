#백준
#13300 방배정
studentNum,maxNum=list(map(int,input().split()))
roomDict={1:[0,0],2:[0,0],3:[0,0],4:[0,0],5:[0,0],6:[0,0]}
for k in range(studentNum):
    MW,nowGrade=list(map(int,input().split()))
    if MW==0:
        roomDict[nowGrade][0]+=1
    else:
        roomDict[nowGrade][1]+=1
roomCount=0
for i in roomDict:
    roomCount+=roomDict[i][0]//maxNum
    roomCount+=1 if roomDict[i][0] % maxNum !=0 else 0
    roomCount += roomDict[i][1] // maxNum
    roomCount += 1 if roomDict[i][1] % maxNum !=0 else 0
print(roomCount)

#2309 일곱 난쟁이
shortMan=[]
for i in range(9):
    shortMan.append(int(input()))
global answerList
answerList=[]
def findSeven(countList, manList,totalTall):
    global answerList
    if totalTall<100:
        for k in range(9):
            if manList[k]!=0:
                nowLi=manList[:]
                nowTall=totalTall
                nownum=countList[:]
                nowTall+=nowLi[k]
                nownum.append(nowLi[k])
                nowLi[k]=0
                findSeven(nownum,nowLi,nowTall)
    elif totalTall==100:
        answerList.append(countList)
findSeven([],shortMan,0)
for i in range(len(answerList)):
    if len(answerList[i])==7:
        answer=answerList[i].sort()
        for k in range(7):
            print(answerList[i][k])
        break