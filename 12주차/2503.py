N = int(input())
baseball = [list(map(int,input().split())) for _ in range(N)]
baseball.sort(key=lambda x:x[1])
countlist = []
#0을 아무 숫자나 올수 있는 자리로 가정i
for a in range(N):
    if baseball[a][1]==3:
