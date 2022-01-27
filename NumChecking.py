def checkinput(userinput):
    isDigits = userinput.isdigit()
    lenofdigits = len(userinput)
    # print('digits',isDigits)
    if(isDigits and lenofdigits==4):
        print(f'Your input is', userinput)
        return 0
    elif(isDigits and lenofdigits!=4):
        print(f'Your input', userinput, 'should be 4 digits of number, please re-enter')
        return 1
    elif(isDigits==False):
        print(f'Your input', userinput, 'isn\'t number, please re-enter')
        return 1
