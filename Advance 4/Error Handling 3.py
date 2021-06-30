while True:
    try:
        age = int(input('what is your age?'))
        10/age
    except ValueError:
        print('please enter a number')
        continue
    except ZeroDivisionError:
        print('please enter a number heigher then 0')
        break
    else:
        print('thank you!')
        break
    finally:
        print('ok! finally i m done')
    print('can you hear me')
