def compare(userinput,hidenlist,numA,numB):


    for x in hidenlist:
        for y in userinput:
            if (x == int(y)):
                print('we found 1')

    for x in {0,1,2,3}:
        if (userinput==hidenlist[x]):
            print('userinput[',x,'] is ',userinput[x])
            print('hidenlist[', x, '] is ', hidenlist[x])
