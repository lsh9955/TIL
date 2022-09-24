def solution(today, terms, privacies):
    termDict = {}
    for k in range(len(terms)):
        nowTerm = terms[k].split(" ")
        termDict[nowTerm[0]]=int(nowTerm[1])
    isExpired = []
    todayDate = today.split(".")
    todayDate = list(map(int,todayDate))

    for p in range(len(privacies)):
        thisList = privacies[p].split(" ")
        thisday = thisList[0].split(".")
        thisday = list(map(int,thisday))

        addDay = termDict[thisList[1]]+thisday[1]
        addYear = 0
        willaddDay = 0
        if addDay//12==1 and addDay%12 == 0:

            addYear = thisday[0]
            willaddDay = 12
        elif addDay//12>1 and addDay%12 == 0:
            addYear = thisday[0]+addDay//12-1
            willaddDay = 12
        else:
            addYear = thisday[0]+addDay//12
            willaddDay =addDay%12


        willaddDate = thisday[2]
        if thisday[2]==1:

            if willaddDay == 1:

                addYear-=1
                willaddDay = 12
                willaddDate = 28
            else:

                willaddDay-=1
                willaddDate=28
        else:
            willaddDate-=1
        if todayDate[0]>addYear:
            isExpired.append(p+1)

        elif todayDate[0]==addYear and todayDate[1]>willaddDay:
            isExpired.append(p+1)
        elif todayDate[0]==addYear and todayDate[1]==willaddDay and todayDate[2]>willaddDate:
            isExpired.append(p+1)


    answer = isExpired
    return answer

print(solution("2020.01.01",["Z 3", "D 5"],["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))