# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def ad1(num1,num2):
    num4=num1+num2
    print(num4)

def afunction(num3,ary=[1,2,5]):
    ary.append(num3)
    return ary

def rndfun(numlist=[0,1,2,3,4,5,6,7,8,9]):

    choosednum = random.sample(numlist,4)
    print(choosednum)
    rndlist.append(choosednum)
    return rndlist

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    #ad1(9,3)
    rndlist = []
    #print(afunction(3))
    print(rndfun())
    #Gamersname = 'John'
    #print(Gamersname[3])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
