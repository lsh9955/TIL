caseNum = int(input())
for k in range(caseNum):
    N, M = map(int, input().split())                                        #NxN리스트의 N값과, MxM 리스트의 M 값을 입력
    flyList = [list(map(int,input().split())) for _ in range(N)]            #NxN리스트를 입력
    maxFly = 0                                                              #최대로 많이 잡을 수 있는 파리의 수를 입력받기 위해 변수로 생성

    def findMax(thisLen, startIdx):                                         #M의 값과 시작인덱스를 함수에서 받아
        totalFly = 0
        for p in range(thisLen):                                            #해당 지점에서부터 M만큼 가면서 모든 파리의 수를 합침
            for q in range(thisLen):
                totalFly += flyList[startIdx[0] + p][startIdx[1] + q]
        return totalFly                                                     #모든 파리의 수를 출력

    for a in range(N-M+1):                                                  #파리채의 크기가 있으므로 N-M+1만큼 파리채가 갈 수 있음
        for b in range(N-M+1):
            if findMax(M,[a,b])>maxFly:                                     #maxFly값보다 현재 파리채로 잡은 수가 더 많다면 maxFly값에 대입
                maxFly = findMax(M,[a,b])
    print(f'#{k+1} {maxFly}')                                               #maxFly 값 출력