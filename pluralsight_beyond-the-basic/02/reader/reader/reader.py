import os
from .compressed import gzipped
from .compressed import bzipped

print('inside reader --> name {}'.format(__name__))
extension_map = {
    '.bz2': bzipped.opener,
    '.gz': gzipped.opener
}


class Reader:
    def __init__(self, filename):
        extension = os.path.splitext(filename)[1]
        # the second args in map.get() 'open' is a default option
        opener = extension_map.get(extension, open)
        self.filename = filename
        self.f = opener(self.filename, 'rt', encoding='utf-8', errors='ignore')

    def close(self):
        self.f.close()

    def read(self):
        return self.f.read()

