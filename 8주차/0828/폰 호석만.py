chamNum = int(input())
direction = []
landLen = []
#해당 직선의 방향과 길이를 따로 입력받음
for i in range(6):
    nowDir, nowLen = list(map(int, input().split()))
    direction.append(nowDir)
    landLen.append(nowLen)
widthHeight = []
for k in range(6):
    #해당 직선이 한번만 나오면 분리되지 않은(나눠지지 않은) 직선이므로, 전체 구역의 가로,세로 길이가 됨
    if direction.count(direction[k])==1:
        widthHeight.append(landLen[k])
        #1 3 1 3과 같이 중복되는 구역에서 중심에 있는 3 1이 빼야 할 가상의 구역이 됨
        #[1 3 ... 1 3]인 경우도 있으므로 이를 방지하기 위해 direction의 길이를 2배로 함
direction = direction * 2
delList = []

for k in range(9):
    #해당 인덱스에서 1만큼 넘어간 값이 그 다음 인덱스에서 1개만큼 더 간 값과 같다면, 해당 값을 곱해서 제거
    #direction에서 2를 곱해줘서 6의 나머지로 처리해줘야 인덱스가 정상적으로 됨
    if direction[k:k + 2] == direction[k + 2:k + 4]:
        delList = [(k + 1) % 6, (k + 2) % 6]
        break
        #위에서 구한 전체 구역의 가로 세로를 곱하고, 가상의 구역의 가로 세로를 곱해서 뺀 후 참외의 개수를 곱함
print((widthHeight[0]*widthHeight[1]-(landLen[delList[0]]*landLen[delList[1]]))*chamNum)
