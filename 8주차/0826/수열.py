N,K = list(map(int,input().split()))
tempList = list(map(int,input().split()))
#첫 인덱스와 마지막 인덱스를 변수로 생성
fir,sec = 0,K-1
#가장 큰 수와, 현재의 수를 변수로 생성
maxNum = 0
thisNum = 0
#첫번째 경우의 수를 현재 수에 대입
for i in range(K):
    thisNum+=tempList[i]
maxNum = thisNum
#인덱스를 앞으로 이동시키며, 다음 인덱스를 더하고 현재의 맨 처음 인덱스를 빼며 이동함
#총 합계를 max값과 비교하며 지금 합계가 더 크다면, 합계를 max에 대입
for i in range(1,N-K+1):
    sec+=1
    thisNum = thisNum-tempList[fir]+tempList[sec]
    if thisNum>maxNum:
        maxNum = thisNum
    fir += 1
print(maxNum)