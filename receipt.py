def printReceipt(total, tip, items):
    print('-' * 10)
    print('RECEIPT')
    print('-' * 10)

    for item in items:
        print(f'{item['item']}: ${item['cost']:.2f}')
        print('-' * 10)

    print(f'Tip: ${tip:.2f}')
    print(f'Total: ${total:.2f}')