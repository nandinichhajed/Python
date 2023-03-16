# printing our own errors

while True:
    try:
        age = int(input('what is your age?'))
        10/age

        raise ValueError('Hey! cut it out')
        raise Exception('Hey! cut it out')
        raise ZeroDivisionError('Hey! cut it out')

        print('thank you!')
        break
    finally:
        print('ok! finally i m done')
    print('can you hear me')
