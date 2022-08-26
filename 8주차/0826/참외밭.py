chamNum = int(input())
direction = []
landLen = []
for i in range(6):
    nowDir, nowLen = list(map(int, input().split()))
    direction.append(nowDir)
    landLen.append(nowLen)
widthHeight = []
for k in range(6):
    if direction.count(direction[k])==1:
        widthHeight.append(landLen[k])
direction = direction * 2
delList = []

for k in range(9):
    if direction[k:k + 2] == direction[k + 2:k + 4]:
        delList = [(k + 1) % 6, (k + 2) % 6]
        break
print((widthHeight[0]*widthHeight[1]-(landLen[delList[0]]*landLen[delList[1]]))*chamNum)
