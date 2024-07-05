def validFloatInput(question) -> float:
    while True:
        try:
            usrInput = input(question).strip()
            if(not usrInput):
                raise ValueError
            if(float(usrInput) < 0):
                raise ValueError
            return float(usrInput)
        except(Exception):
            print('ERROR: Invalid input')


def validString(question) -> str:
    while True:    
        try:
            usrInput = input(question).strip()
            if(not usrInput):
                raise ValueError
            return usrInput
        except(Exception):
            print('ERROR: Invalid input')


def validYN(question) -> bool:
    while True:
        try:
            usrInput = input(question).strip().lower()
            if(not usrInput):
                raise ValueError
            elif(usrInput == 'y' or usrInput == 'yes'):
                return True
            elif(usrInput == 'n' or usrInput == 'no'):
                return False
            else:
                raise Exception
        except(Exception):
            print('ERROR: Invalid input')