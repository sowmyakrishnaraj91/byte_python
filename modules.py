
import sys

print('Command line arguments are:')

for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is', sys.path, '\n')

import os
print(os.getcwd())


print(__name__)