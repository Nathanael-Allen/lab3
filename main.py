import valid
from valid import *

def main():
    on = True
    while on:
        validFloatInput('Item price: ')
        if(not validYN('More items? y/n: ')):
            on = False   
    

if __name__ == '__main__':
    main()