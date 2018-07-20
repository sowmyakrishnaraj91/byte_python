#break
while True:
    a=input('enter comething:')

    if a == 'quit':
        break

    else:
        print('length of entered string:',len(a))

print('Done')

#continue
while True:
    b=input('enter comething:')

    if b == 'quit':
        break

    if len(b) <3:
        print('string too small')
        continue

