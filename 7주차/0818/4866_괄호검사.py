caseNum = int(input())                                                      #테스트 개수 입력
for k in range(caseNum):
    letter = input()                                                        #괄호인지, 왼쪽, 오른쪽 괄호인지를 판단하기 위해 리스트 생성
    pairList = ["(", ")", "{", "}"]                                         #괄호를 담을 리스트 생성
    leftList = ["(", "{"]                                                   #괄호검사는 크게 3가지의 경우로 나뉘어짐
    rightList = [")", "}"]                                                  #1.오른쪽 괄호가 먼저 오는 경우
    stackPair = []                                                          #2.왼쪽 괄호가 오는 경우
    for i in range(len(letter)):                                            #3.왼쪽 괄호가 있을 때 오른쪽 괄호가 오는 경우
        if letter[i] in pairList:
            if letter[i] in rightList and len(stackPair) == 0:              #stack에 아무것도 없는데 닫는 괄호가 먼저 온다면 짝이 맞지 않으므로 0 출력
                print(f'#{k + 1} 0')
                break
            elif letter[i] in leftList:                                     #왼쪽 괄호는 배열에 추가
                stackPair.append(letter[i])
            elif letter[i] in rightList:                                    #오른쪽 괄호인 경우, 짝을 이루는 개수가 맞다 하더라도
                if letter[i] == rightList[0] and stackPair[-1] == leftList[0]:
                    stackPair.pop()                                         #"{" 이후에 ")" 가 올 수 없으므로, 이것을 파악하여 짝이 맞는지를 파악
                elif letter[i] == rightList[1] and stackPair[-1] == leftList[1]:
                    stackPair.pop()
                else:                                                       #짝이 맞지 않으면 break
                    print(f'#{k + 1} 0')
                    break
    else:                                                                   #왼쪽 괄호가 남는지 여부를 검사하여, 남지 않으면 1을 출력
        if len(stackPair) == 0:
            print(f'#{k + 1} 1')
        else:
            print(f'#{k + 1} 0')                                            #남으면 짝이 맞지 않는 것이므로 0을 출력

