import sys
sys.stdin = open('input.txt')
# 1. 입력 데이터에서 2진 암호코드 읽어내기 (뒤에서 부터 읽기)
# 2. 읽어낸 2진 암호코드를 숫자 암호코드로 변경하기 (딕셔너리 활용)
# 3. 암호코드가 정상적인 암호코드인지 확인하기
# 4. 결과출력하기

code_dic = {
    (3, 2, 1, 1): 0,
    (2, 2, 2, 1): 1,
    (2, 1, 2, 2): 2,
    (1, 4, 1, 1): 3,
    (1, 1, 3, 2): 4,
    (1, 2, 3, 1): 5,
    (1, 1, 1, 4): 6,
    (1, 3, 1, 2): 7,
    (1, 2, 1, 3): 8,
    (3, 1, 1, 2): 9
}
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = [list(map(int, input())) for _ in range(N)]


    # 데이터에서 2진 암호코드 읽어오기

    # 뒤에서 부터 읽어올거고
    # 마지막이 1로 끝나니까....
    # 연속된 1읽어오고, 0읽어오고, 1읽어오고, 0읽기(7자리) >> 숫자하나 다 읽음
    # 8번 반복


    for i in range(N):
        # 코드의 길이가 56이니까 최소한 55번에서는 코드가 나와야 한다.
        for j in range(M - 1, 54, -1):
            # 코드가 나왔는지 확인!
            if data[i][j] == 1:  # 코드를 찾음!
                # 코드를 찾았으니, 코드를 읽으면 됩니다.
                # 우리는 0과 1의 패턴의 개수를 알아야 한다.
                # 코드는 0101이 반복되니까...
                # 1의 개수 세고, 0의 개수세고, 1의 개수 세고, 0개수 세기
                r, c = i, j  # 시작점 변수 저장\
                result = []
                for i in range(8):  # 숫자가 8개라서 8번 반복
                    n1 = n2 = n3 = n4 = 0  # 개수를 세기위한 변수선언
                    while data[r][c] == 1:  # 1의 개수 세기
                        n4 += 1
                        c -= 1  # 옆으로 한 칸 이동
                    while data[r][c] == 0:  # 0의 개수 세기
                        n3 += 1
                        c -= 1  # 옆으로 한 칸 이동
                    while data[r][c] == 1:  # 1의 개수 세기
                        n2 += 1
                        c -= 1  # 옆으로 한 칸 이동
                    n1 = 7 - n2 - n3 - n4
                    c -= n1  # n1의 크기만큼 옆으로 이동
                    print(n1,n2,n3,n4)
                    result.append(code_dic[(n1, n2, n3, n4)])
                result.reverse()
                result_odd = 0
                result_even = 0
                result_sum = 0
                for i in range(8):
                    if i % 2 == 0:  # 홀수
                        result_odd += result[i]
                    if i % 2 == 1:  # 짝수
                        result_even += result[i]
                if (result_odd * 3 + result_even) % 10 == 0:
                    result_sum = result_odd + result_even
                else:
                    result_sum = 0



    print(f"#{tc}{result_sum}")