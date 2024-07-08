def printReceipt(total, tip, items):
    print('-' * 15)
    print('RECEIPT')
    print('-' * 15)

    for item in items:
        print(f'{item["item"]}: ${item["cost"]:.2f}')
        print('-' * 15)

    print(f'Tip: ${tip:.2f}')
    print(f'Total: ${total:.2f}')