def validInput(usrInput):
    try:
        input(usrInput)
        print('working')
    except(TypeError, ValueError):
        print('Not a valid input...')

def main():
    validInput('Enter your name: ')

if __name__ == '__main__':
    main()
