for k in range(10):
    #방문한 노드를 기록하는 리스트와, 각 노드의 리스트를 입력받는 리스트를 생성
    nodeNum = int(input())
    visitList=[0 for _ in range(nodeNum)]
    nodeList = [list(input().split()) for i in range(nodeNum)]
    output=''
    #스택을 이용하여 다음 탐색 노드를 파악
    stackList = [nodeList[0]]

    while len(stackList) !=0:
        targetNode = stackList[-1]
        #자식 노드가 2개라면
        if len(targetNode) == 4:
            #왼쪽 자식을 탐색했다면, 해당 노드를 출력하고 오른쪽 자식을 탐색
            if visitList[int(targetNode[2])-1] == 1:
                visitList[int(targetNode[0])-1] = 1
                output += targetNode[1]
                stackList.pop()
                stackList.append(nodeList[int(targetNode[3])-1])
            #왼쪽 자식을 탐색하지 않았다면, 왼쪽 자식을 탐색
            else:
                visitList[int(targetNode[2]) - 1] = 1
                stackList.append(nodeList[int(targetNode[2]) - 1])
        #자식이 하나라면
        elif len(targetNode) == 3:
            #자식을 탐색하였다면 해당 노드를 출력
            if visitList[int(targetNode[2]) - 1] == 1:
                visitList[int(targetNode[0]) - 1] = 1
                output += targetNode[1]
                stackList.pop()
                #자식을 탐색하지 않았다면 계속 탐색
            else:
                stackList.append(nodeList[int(targetNode[2]) - 1])
        #자식이 없다면, 해당 노드를 출력하고 pop
        else:
            visitList[int(targetNode[0]) - 1] = 1
            output += targetNode[1]
            stackList.pop()
    #합쳐진 글자를 출력
    print(f'#{k+1} {output}')
