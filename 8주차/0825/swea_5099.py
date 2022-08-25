# N개의 피자를 구울 수 있음
# 한바퀴 돌면 C->C//2로 감소
# 1번부터 M까지 순서대로 화덕에 넣음
# 1번위치에서만 넣거나 뺄 수 있음

caseNum = int(input())
for k in range(caseNum):
    #화덕에 넣을 수 있는 피자 양과 구워야 할 피자 개수를 입력
    N, M = list(map(int, input().split()))
    #각 피자에 해당하는 치즈 양을 입력
    Ci = list(map(int, input().split()))
    #현재 피자가 오븐에 넣어졌으면 1, 아직 굽지 않았으면 0으로 하는 리스트 생성
    inputList = [0 for _ in range(M)]
    #[현재 피자의 번호, 현재 피자의 치즈 양]을 가지는 오븐의 상태를 나타내는 리스트 생성
    ovenList = [[0,0] for _ in range(N)]
    #화덕의 1번 위치를 나타내는 인덱스
    firIdx = 0
    #몇 개가 만들어졌는지를 세는 변수
    countMade = 0
    while True:
        #리스트에 있는 피자가 이미 만들어진 것이 아니라면, 1번 위치로 돌아온 피자의 치즈 양을 절반으로 줄임
        if ovenList[firIdx][1] != -1:
            ovenList[firIdx][1] = ovenList[firIdx][1]//2
        #리스트에 있는 피자가 다 만들어졌다면, 새로운 피자를 넣음
        if ovenList[firIdx][1] == 0:
            for p in range(M):
                #아직 넣지 않은 피자가 있다면, firIdx에 해당 피자의 번호와 치즈 양을 입력
                #다 만들어졌으므로 countMade를 1추가
                if inputList[p] ==0:
                    ovenList[firIdx] = [p+1,Ci[p]]
                    inputList[p] = 1
                    countMade +=1
                    break
            else:
                #피자가 다 만들어졌으면, countmade에 1을 추가하고 다시 세는 것을 방지하기 위해 치즈양을 -1로 바꿈
                if ovenList[firIdx][1] != -1:
                    countMade+=1
                    ovenList[firIdx][1] = -1
        #1번위치가 계속 돌아간다고 생각
        #1번 위치가 마지막 인덱스에 다다르면, 다시 0으로 초기화
        if firIdx==N-1:
            firIdx=0
        else:
            firIdx+=1
        #처음에 화덕 내부에 0으로 이루어진 리스트들이 존재해, N개가 더 만들어진다고 세어지게 됨
        #따라서 원래 세어야 하는 개수는 M-1이나, N을 더해 M+N-1이 되면 빠져나옴
        if countMade == M+N-1:
            break
    #아직 남아있는 피자의 인덱스를 찾아, 해당 피자의 번호를 출력
    for i in range(N):
        if ovenList[i][1] != -1:
            print(f'#{k+1} {ovenList[i][0]}')
            break





