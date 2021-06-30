is_magic = False
is_expert = True

# check if magic and expert: print 'You are a master magician'
if is_magic and is_expert:
    print('You are a master magician')
# check if magic but not an expert: print 'atlist you are getting there'
elif is_magic and not is_expert:
    print('atlist you are getting there')
#  if you are not magician magic: print 'you need magic powers'
elif not is_magic:
    print('you need magic powers')
