### SWEA 9480

```python
import sys
sys.stdin = open("input.txt", "r")
caseNum=int(input())
for i in range(caseNum):
    thisNum=int(input())
    wordList=[]
    outputList=[]
    def findSet(inputWord,checkList):
        for q in range(len(checkList)):
            nowCheckList=checkList[:]
            if nowCheckList[q]==0:
                addWord=inputWord+wordList[q]
                nowCheckList[q]=1
                if len(set(addWord))==26:
                    outputList.append(nowCheckList)
                findSet(addWord,nowCheckList)
    for k in range(thisNum):
        nowWord=input()
        wordList.append(nowWord)

    for w in range(thisNum):
        targetWord=wordList[w]
        targetList=[0]*thisNum
        targetList[w]=1
        findSet(targetWord,targetList)
    print(len(set(list(map(tuple,outputList)))))
```

### SWEA 6913

````python
import sys
sys.stdin = open("input.txt", "r")
caseNum=int(input())
for i in range(caseNum):
    N,M=map(int,input().split())
    MaxCase=0
    MaxCount=0
    for k in range(N):
        nowVal=list(map(str,input().split())).count("1")
        if nowVal>MaxCase:
            MaxCase = nowVal
            MaxCount = 1
        elif nowVal==MaxCase:
            MaxCount +=1
    print("".join(["#",str(i+1)," ",str(MaxCount)," ",str(MaxCase)]))
    ```
````
