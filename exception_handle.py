try:
    text = input('enter:')
except EOFError:
    print('why')
except KeyboardInterrupt:
    print('You cancelled the operation.')
else:
    print('You entered {}'.format(text))
   