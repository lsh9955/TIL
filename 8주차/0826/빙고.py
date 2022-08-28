rowList = [0 for _ in range(5)]
colList = [0 for _ in range(5)]
#대각선의 index를 배열에 넣음. 값이 속해있는 인덱스와 비교하여 대각선을 만족하는지를 비교함
ru = [[4 - _, _] for _ in range(5)]
ld = [[_, _] for _ in range(5)]
ruList = 0
ldList = 0
bingoList = [list(map(int, input().split())) for _ in range(5)]
bingDict = {}
#해당 숫자와 인덱스를 쌍으로 하는 딕셔너리 생성
for a in range(5):
    for b in range(5):
        bingDict[bingoList[a][b]] = [a, b]
#사회자가 부르는 값을 입력받는 리스트 생성
checkList = [list(map(int, input().split())) for _ in range(5)]
flag = True
for a in range(5):
    if not flag:
        break
    #대각선에서 해당 인덱스에 숫자가 속해 있으면 1을 더함
    for b in range(5):
        if bingDict[checkList[a][b]] in ru:
            ruList += 1
        if bingDict[checkList[a][b]] in ld:
            ldList += 1
        #가로와 세로줄에서, 해당 줄에 숫자가 있다면 그 인덱스에 1을 더함
        colList[bingDict[checkList[a][b]][0]] += 1
        rowList[bingDict[checkList[a][b]][1]] += 1
        #대각선에 5개 모두 숫자가 속했으면 1, 아니면 0을 대입
        row = 1 if ruList == 5 else 0
        column = 1 if ldList == 5 else 0
        #3개 이상의 빙고가 만족한다면 현재 횟수를 출력
        if colList.count(5) + rowList.count(5) + row + column >= 3:
            print(a * 5 + b + 1)
            flag = False
            break
