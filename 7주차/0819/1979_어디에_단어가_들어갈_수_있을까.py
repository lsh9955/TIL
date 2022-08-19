caseNum = int(input())
for k in range(caseNum):
    N, K = map(int, input().split())                                            #배열의 길이인 N,찾고자 하는 단어의 길이 K를 입력
    puzzleList = [list(map(int, input().split())) for _ in range(N)]            #해당 리스트를 입력
    wordLenList = []                                                            #연속해서 글자를 쓸 수 있는 크기들을 입력받을 리스트 생성
    for p in range(N):
        rowNum = 0                                                              #한 행과 열에서 연속되는 1의 값을 찾기 위해 변수 생성
        columnNum = 0
        for q in range(N):
            if puzzleList[p][q] == 1 and q == N - 1:                            #해당 칸이 1이고 맨 끝이라면 지금까지의 크기를 배열에 입력
                wordLenList.append(rowNum + 1)
            elif puzzleList[p][q] == 1:                                         #해당 칸이 1이면 개수에 추가
                rowNum += 1
            elif puzzleList[p][q] == 0:                                         #해당 칸이 0이면 지금까지의 개수를 추가, 맨 마지막 인덱스가 0이더라도
                wordLenList.append(rowNum)                                      #어차피 개수를 추가해주면 되기 때문에 따로 if문으로 분리하진 않았음
                rowNum = 0
            if puzzleList[q][p] == 1 and q == N - 1:                            #행, 열 모두 동일하게 진행
                wordLenList.append(columnNum + 1)
            elif puzzleList[q][p] == 1:
                columnNum += 1
            elif puzzleList[q][p] == 0:
                wordLenList.append(columnNum)
                columnNum = 0

    print(f'#{k+1} {wordLenList.count(K)}')                                     #wordLenList 중 K값에 해당하는 값들의 개수를 세어 출력
