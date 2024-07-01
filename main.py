from valid import *
from calc import *
from receipt import *

def main():
    running = True
    items = []
    total = 0

    print(f'{(20 * '*')}\n   TIP CALCULATOR\n{(20 * '*')}')
    while running:
        newItem = {
            'item': validString('Input item name: '),
            'cost': validFloatInput('Input item cost: ')
        }
        items.append(newItem)

        if(validYN('More items? y/n: ') == False):
            printReceipt(total, 0, items)
            # print(items[0]['item'])
            running = False
            

if __name__ == '__main__':
    main()