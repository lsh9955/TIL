import sys
from traceback import print_tb
sys.stdin = open("input (9).txt", "r")
T = int(input())
for k in range(T):
    N = int(input())
    numList = list(map(int,input().split()))
    sortNum = numList[:]
    sortNum.sort()
    maxNum=0
    print(sortNum)
    # for a in range(N):
    #     if len(sortNum)==0:
    #         break
    #     elif numList[a]>=sortNum[-1]:
    #         thisNum = sortNum[-1]
    #         while len(sortNum)>0 and sortNum[-1] == thisNum:
    #             if len(sortNum)==0:
    #                 break
    #             else:
    #                 sortNum.pop()
    #     else:
    #         maxNum+=sortNum[-1]-numList[a]
    print(f'#{k+1} {maxNum}')

