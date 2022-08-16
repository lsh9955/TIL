#swea 3143.가장 빠른 문자열 타이핑
#테스트 개수 입력
testNum=int(input())
for i in range(testNum):
		#A와 B를 입력받음
    targetStr, saveStr = map(str,input().split())
		#A의 길이에서, B문자열에 1을 뺀 값을 B가 A에 나오는 갯수만큼 뺌
    print(f'#{i+1} {len(targetStr) - (len(saveStr)-1)*(targetStr.count(saveStr))}')


#swea 4861.회문
#테스트케이스 개수 입력
inputNum = int(input())
for k in range(inputNum):
		#테스트케이스의 길이(N)와 찾고자 하는 길이(M)를 입력받음
    letterLen, caseNum = map(int, input().split())
		#NxN개의 2차원 배열을 받음
    boardList = [input() for _ in range(letterLen)]
		#가로로 길이가 M인 문자열을 탐색 
    for p in range(letterLen):
        for e in range(letterLen-caseNum+1):
            nowLetter = boardList[p][e:e + caseNum]
						#문자열을 뒤집어도 동일하다면 해당 문자열을 출력
            if nowLetter == nowLetter[::-1]:
                print(f'#{k + 1} {nowLetter}')
                break
    else:
				#세로로 문자열을 변환한 리스트를 생성
        columnList = list(zip(*boardList))
        for p in range(letterLen):
						#세로로 길이가 M인 문자열을 탐색 
            for e in range(letterLen - caseNum + 1):
								#문자열을 뒤집어도 동일하다면 해당 문자열을 출력
                nowLetter = columnList[p][e:e + caseNum]
                if nowLetter == nowLetter[::-1]:
                    print(f'#{k + 1} {"".join(nowLetter)}')

#swea 4864. 문자열 비교
caseNum = int(input())
for i in range(caseNum):
    str1=input()
    str2=input()
		# str1이 str2에 포함되면 1을, 아니면 0을 출력
    if str1 in str2:
        print(f'#{i+1} 1')
    else:
        print(f'#{i+1} 0')

#swea 4865.글자수
inputNum = int(input())
for k in range(inputNum):
    #str1,str2입력
    str1 = list(set(input()))
    str2 = input()
    #최대값을 저장할 변수 생성
    count = 0
    for p in range(len(str1)):
        #str2에서 str1의 특정 문자의 개수가 count보다 크면 그 값을 count에 저장
        if str2.count(str1[p]) > count:
            count = str2.count(str1[p])
    print(f'#{k + 1} {count}')

#swea 1216.회문2
for k in range(10):
    #회문 최소값은 1이므로 최대값을 받을 변수의 기본 값을 1로 설정
    maxNum = 1
    #현재 케이스의 순서 입력
    nowCase = int(input())
    #100x100 케이스를 2차원 배열로 입력받음
    testList = [input() for _ in range(100)]
    for i in range(100):
        for j in range(100):
            #가장 큰 길이(100)에서부터 행에서 모든 경우의 수를 구하여
            for p in range(100, 1, -1):
                thisWord = testList[i][j:j + p]
                #거꾸로 뒤집은 경우에도 문자열이 같고 maxNum보다 길이가 길다면 maxNum을
                #thisWord의 길이값으로 바꿈
                if thisWord == thisWord[::-1] and len(thisWord) > maxNum:
                    maxNum = len(thisWord)
                    break
    #세로로도 회문이 가능하므로 세로로 변환시킨 문자열을 만듦
    for i in range(100):
        colStr = ""
        for p in range(100):
            colStr += testList[p][i]
        #가장 큰 길이(100)에서부터 행에서 모든 경우의 수를 구하여
        for j in range(100):
            for q in range(100, 1, -1):
                thisWord = colStr[j:j + q]
                #거꾸로 뒤집은 경우에도 문자열이 같고 maxNum보다 길이가 길다면 maxNum을
                #thisWord의 길이값으로 바꿈
                if thisWord == thisWord[::-1] and len(thisWord) > maxNum:
                    maxNum = len(thisWord)
                    break
    #가장 긴 회문의 길이값을 출력
    print(f'#{k+1} {maxNum}')

#swea 5356.의석이의 세로로 말해요
#케이스 개수를 입력
caseNum = int(input())
for k in range(caseNum):
    #모든 케이스를 담을 배열과, 가장 긴 배열의 길이를 담을 변수 생성
    caseList = []
    maxNum = 0
    outPutLetter = ""
    for p in range(5):
        #각 input마다 길이를 측정하여 가장 긴 배열의 길이를 찾음
        nowinput = input()
        if len(nowinput) > maxNum:
            maxNum = len(nowinput)
        caseList.append(nowinput)
    #길이가 현재 i보다 작은 리스트는 넘기고, 현재 i보다 크거나 같은 리스트에서 글자를 가져와 결합
    for i in range(maxNum):
        for q in range(5):
            if len(caseList[q]) >= i + 1:
                outPutLetter += caseList[q][i]
    print(f'#{k + 1} {outPutLetter}')