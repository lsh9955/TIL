caseNum = int(input())
for k in range(caseNum):
    #N개의 숫자와 M번 작업의 개수를 입력
    N, M = list(map(int, input().split()))
    numList = list(map(int, input().split()))
    #M번 작업을 했을 때, M//N만큼 진행했을 때 다시 원래의 리스트와 동일해짐
    #맨 앞에 있는 숫자는, M%N만큼 앞으로 간 인덱스와 동일하므로 해당 인덱스의 값을 출력
    print(f'#{k + 1} {numList[M % N]}')
