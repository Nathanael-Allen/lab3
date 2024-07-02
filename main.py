# Author: Nathanael Allen
# Assignment: Lab 3
# Date: 07/01/24
# Description: This program asks users for a list of items and there costs, 
# then a tip percent and calculates the total with tip and prints a receipt.

# Input: items -> string, item cost -> float, tip -> float
# Outputs: a list of items with costs and total


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
        total += newItem['cost']
        items.append(newItem)

        if(validYN('More items? y/n: ') == False):
            tipPercentage = validFloatInput('What percentage would you like to tip? use whole numbers e.g. 15, 20, 25: ')
            tip = calculateTip(total, tipPercentage)
            finalTotal = total + tip
            printReceipt(finalTotal, tip, items)
            running = False
    if(validYN('Run again? y/n: ')):
        main()
        
if __name__ == '__main__':
    main()