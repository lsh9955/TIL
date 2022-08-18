caseNum = int(input())                                  #케이스 개수를 입력받음
for k in range(caseNum):
    nowLetter = input()                                 #현재 케이스 문자를 입력
    inputStack = []                                     #중복을 제거한 문자들을 stack으로 쌓을 inputStack 생성
    while True:
        inputStack = []
        for i in range(len(nowLetter)):                 #inputStack에 아무것도 없다면 문자를 넣고,
            if len(inputStack) == 0:
                inputStack.append(nowLetter[i])         #맨 마지막 문자와 중복된다면 pop을 이용해 제거
            elif inputStack[-1] == nowLetter[i]:
                inputStack.pop()
            else:
                inputStack.append(nowLetter[i])         #중복되지 않는 문자라면 inputStack에 문자를 입력
        if len(nowLetter) == len(inputStack):           #중복되는 것이 없다면, 빠져나옴
            break
        else:
            nowLetter="".join(inputStack)
    print(f'#{k+1} {len(inputStack)}')                  #중복되지 않는 문자의 개수를 출력