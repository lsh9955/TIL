#SWEA 7532
inputNum=int(input())
for i in range(inputNum):
#sem력으로 이루어진 연도를 의미하는 리스트 입력
    testCase=list(map(int,input().split()))
#365가 제일 크므로 이 숫자를 기준으로 하였음
    findNum=testCase[0]

    while True:
#365의 배수를 각각의 sem력에서의 값과 같은지 비교함
#24와 29로 나눠준 이유는, 24와 29가 0으로 표현되지 않고 그대로 24로 표현되기 때문에 나머지를 서로 비교할 때 오류가 나기 때문
#모든 경우를 충족한다면 while문을 벗어나서 값 출력
        if findNum%24==testCase[1]%24 and findNum%29==testCase[2]%29:
            break
        else:
            findNum+=365
    print(f'#{i+1} {findNum}')