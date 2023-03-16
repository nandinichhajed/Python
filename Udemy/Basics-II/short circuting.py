# case 1
is_Friend = True
is_User = True

if is_Friend and is_User:
    print('Best Friend Forever')
else:
    print('Not such good friends')

if is_Friend or is_User:
    print('Best Friend Forever')
else:
    print('Not such good friends')

# case 2
is_Friend = False
is_User = True

if is_Friend and is_User:
    print('Best Friend Forever')
else:
    print('Not such good friends')

if is_Friend or is_User:
    print('Best Friend Forever')
else:
    print('Not such good friends')

# case 3
is_Friend = True
is_User = False

if is_Friend and is_User:
    print('Best Friend Forever')
else:
    print('Not such good friends')

if is_Friend or is_User:
    print('Best Friend Forever')
else:
    print('Not such good friends')

# case 4
is_Friend = False
is_User = False

if is_Friend and is_User:
    print('Best Friend Forever')
else:
    print('Not such good friends')

if is_Friend or is_User:
    print('Best Friend Forever')
else:
    print('Not such good friends')
