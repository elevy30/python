import bz2
import sys

print('inside bzip --> name {}'.format(__name__))
opener = bz2.open

if __name__ == '__main__':
    f = bz2.open(sys.argv[1], mode='wt', encoding='utf-8')
    f.write(' '.join(sys.argv[2:]))
    f.close()
