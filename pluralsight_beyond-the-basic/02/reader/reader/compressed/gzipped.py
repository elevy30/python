import gzip
import sys

print('inside gzip --> name {}'.format(__name__))
opener = gzip.open

if __name__ == '__main__':
    f = gzip.open(sys.argv[1], mode='wt', encoding='utf-8')
    f.write(' '.join(sys.argv[2:]))
    f.close()

