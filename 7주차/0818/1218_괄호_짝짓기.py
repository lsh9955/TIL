for k in range(10):
    caseLength = int(input())
    caseList=input()
    pairStack = []
    rightList=[")","]","}",">"]
    ansOutput = False
    for i in range(caseLength):
        if caseList[i] in rightList:
            if len(pairStack) == 0:
                break
            elif caseList[i] == ")" and pairStack[-1] == "(":
                pairStack.pop()
            elif caseList[i] == "]" and pairStack[-1] == "[":
                pairStack.pop()
            elif caseList[i] == "}" and pairStack[-1] == "{":
                pairStack.pop()
            elif caseList[i] == ">" and pairStack[-1] == "<":
                pairStack.pop()
            else:
                break
        else:
            pairStack.append(caseList[i])
    if len(pairStack) == 0:
        ansOutput = True
    print(f'#{k+1} {1 if ansOutput else 0}')