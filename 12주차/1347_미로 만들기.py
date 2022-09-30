N = int(input())
honglist = input()
dir = 3
nowidx= [0,0]
alllist = [[0,0]]

for k in range(N):
    if honglist[k]=="L":
        if dir==1:
            dir = 4
        else:
            dir-=1
    elif honglist[k]=="R":
        if dir == 4:
            dir = 1
        else:
            dir+=1
    elif honglist[k]=="F":
        if dir==1:
            nowidx[0]+=1
        elif dir==2:
            nowidx[1]+=1
        elif dir==3:
            nowidx[0]-=1
        elif dir==4:
            nowidx[1]-=1
        alllist.append(nowidx[:])
print(alllist)
alllist.sort(key=lambda x:x[0])
maxheight = alllist[-1][0]-alllist[0][0]

alllist.sort(key=lambda x:x[1])
maxwidth = alllist[-1][1]-alllist[0][1]
maze = [["#" for _ in range(maxwidth+1)] for x in range(maxheight+1)]

for b in range(len(alllist)):
    maze[alllist[b][0]][alllist[b][1]] = "."
print(maze)

