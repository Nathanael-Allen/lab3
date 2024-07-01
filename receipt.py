def printReceipt(total, tip, items):
    print('RECEIPT')
    print('-' * 10)

    for item in items:
        for name, cost in item.items():
            print(f'{name}: {cost}')
        print('-' * 10)

    print(f'Tip: {tip}')
    print(f'Total: {total}')