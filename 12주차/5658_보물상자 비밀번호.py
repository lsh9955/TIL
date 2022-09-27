T = int(input())
for k in range(T):
    N,K = list(map(int,input().split()))
    listPassword = list(input())
    changeNum = {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
    numList = []
    for a in range((N//4)):
        for b in range(4):
            #중복되지 않게 숫자 입력
            if "".join(listPassword[b*(N//4):b*(N//4)+(N//4)]) not in numList:
                numList.append("".join(listPassword[b*(N//4):b*(N//4)+(N//4)]))
        #회전하면서 새로 숫자 배열 생성
        willAppendIdx = listPassword.pop()
        listPassword.insert(0,willAppendIdx)
    for c in range(len(numList)):
        thisNum = numList[c]
        nowNum = 0
        for d in range((N//4)):
            #16진법을 10진법으로 변환
            if thisNum[d] in changeNum:
                nowNum+=(16**((N//4-1)-d))*changeNum[thisNum[d]]
            else:
                nowNum+=(16**((N//4-1)-d))*(int(thisNum[d]))
        numList[c] = nowNum
    #해당 숫자들을 정렬해서 K번째의 수를 출력함
    numList.sort()
    print(f'#{k+1} {numList[-K]}')

