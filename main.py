from valid import *

def main():
    running = True
    total = 0

    print(f'{(20 * '*')}\n   TIP CALCULATOR\n{(20 * '*')}')
    while running:
        total += validFloatInput('Item price: ')

        if(validYN('More items? y/n: ') == False):
            print(total)
            running = False       

if __name__ == '__main__':
    main()