to_write = '''Line to file
Line 2 to write
Line 3 to write'''

f = open('dummy.txt','w')
f.write(to_write)
f.close()

f = open('dummy.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break

    print(line, end='')
f.close()