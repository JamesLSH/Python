# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import NumCompare
import NumChecking

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# def afunction(num3,ary=[1,2,5]):
#     ary.append(num3)
#     return ary

def rndfun(numlist=[0,1,2,3,4,5,6,7,8,9]):
    choosednum = random.sample(numlist,4)
    # print(f'random choosed numbers',choosednum)
    return choosednum

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    hidennum=rndfun()
    # print('random 4 numbers list is', hidencode)
    flag=0
    while flag==0:
        userinput = input("Please input 4 digits of number: ")
        if (NumChecking.checkinput(userinput)==0):
            flag=1

    print('chosen number is ',hidennum)
    print('user input number is ', userinput)
    # userinputlist=[]
    # userinputlist=userinput.split(' ')
    # print('userinputlist is ',userinputlist)
    # NumCompare.compare(userinput,hidennum,0,0)

def testFun():
    printf("it's just empty function")



    # NumCompare.compare(userinput,hidencode)
    #Gamersname = 'John'
    #print(Gamersname[3])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
