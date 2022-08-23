arr = ['a', 'b', 'c', 'd']
sel = [0, 0, 0, 0]


def findLi(level, sel):
    for i in range(4):
        if level == 1:
            if sel[i] == 0:
                nowSel = sel[:]
                nowSel[i] = 1
                for k in range(4):
                    if nowSel[k] == 1:
                        print(arr[k], end="")
                print()
        else:
            if sel[i] == 0:
                nowSel = sel[:]
                nowSel[i] = 1
                findLi(level + 1, nowSel)


findLi(0, sel)
