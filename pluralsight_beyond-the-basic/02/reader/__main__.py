# __main__.py enable executable directory or zip file

# run from console #
# -------------------
# python reader test.gz
# python reader.zip test.gz

import sys
import reader

print('inside main --> executing __main__.py with name {}'.format(__name__))
print()
r = reader.Reader(sys.argv[1])
try:
    print(r.read())
finally:
    r.close()

