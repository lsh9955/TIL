nodeNum = int(input())
#방문 노드와 [해당 노드, 연결된 노드]를 리스트로 갖는 nodeList 생성
visitList = [0 for _ in range(nodeNum)]
inputList = list(map(int,input().split()))
nodeList=[[_+1] for _ in range(nodeNum)]
for i in range(len(inputList)//2):
    nodeList[inputList[2*i]-1].append(inputList[2*i+1])
output = []
#탐색해 나갈 요소드를 삽입, 삭제하는 리스트 생성
stackList = [nodeList[0]]

while len(stackList) != 0:
    #맨 위의(마지막의) 요소를 기준으로
    targetNode = stackList[-1]
    #두 개의 자식 노드를 가지면, 현재 노드를 출력하고 왼쪽, 오른쪽 순서대로 리스트에 저장
    if len(targetNode) == 3:
        visitList[targetNode[0] - 1] = 1
        output.append(str(targetNode[0]))
        stackList.pop()
        stackList.append(nodeList[targetNode[2] - 1])
        stackList.append(nodeList[targetNode[1] - 1])
        #자식 노드가 하나라면, 현재 노드를 출력하고 자식 노드를 리스트에 저장
    elif len(targetNode) == 2:
        visitList[targetNode[0] - 1] = 1
        output.append(str(targetNode[0]))
        stackList.pop()
        stackList.append(nodeList[targetNode[1] - 1])
        #말단 노드라면 현재 노드를 출력하고 pop
    else:
        visitList[int(targetNode[0]) - 1] = 1
        output.append(str(targetNode[0]))
        stackList.pop()
print(" ".join(output))