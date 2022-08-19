countLand=[]
inputLand = [list(map(int,input().split())) for _ in range(4)]
for i in range(4):
    for a in range(inputLand[i][0],inputLand[i][2]):
        for b in range(inputLand[i][1],inputLand[i][3]):
            if [a,b] not in countLand:
                countLand.append([a,b])
print(len(countLand))
