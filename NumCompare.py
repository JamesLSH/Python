def compare(userinput,hidenlist,numA,numB):
    userinputlist=[]

    for x in hidenlist:
        for y in userinput:
            if (x == int(y)):
                print('we found 1')

    for x in {0,1,2,3}:
        userinputlist[x]= (list)(userinput)

        if (userinputlist[x]==hidenlist[x]):
            print('userinputlist[',x,'] is ',userinput[x])
            print('hidenlist[', x, '] is ', hidenlist[x])
