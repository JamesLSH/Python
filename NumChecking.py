def checkinput(userinput):
    isDigits = userinput.isdigit()
    lenofdigits = len(userinput)
    # print('digits',isDigits)
    if(isDigits and lenofdigits==4):
        print(f'Your input is', userinput)
        # return 1
    elif(isDigits and lenofdigits!=4):
        print(f'Your input', userinput, 'should be 4 digits of number, please re-enter')
        # return -1
    elif(isDigits==False):
        print(f'Your input', userinput, 'isn\'t number, please re-enter')
        # return -2

    # while(checkinput(userinput)!=1):
    #     break
    #     if (checkinput(userinput)==1):
    #         print(f'Your input is', userinput)
    #     elif(checkinput(userinput)==-1):
    #         print(f'Your input',userinput,'should be 4 digits of number, please re-enter')
    #     elif (checkinput(userinput) == -2):
    #         print(f'Your input', userinput, 'isn\'t number, please re-enter')