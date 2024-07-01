from valid import *

def main():
    on = True
    total = 0

    print(f'{(20 * '*')}\n   TIP CALCULATOR\n{(20 * '*')}')
    while on:
        total += validFloatInput('Item price: ')
        if(not validYN('More items? y/n: ')):
            print(total)
            on = False   
    

if __name__ == '__main__':
    main()