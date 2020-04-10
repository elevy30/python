from ..compressed.bzipped import opener as bz2_opener
from ..compressed.gzipped import opener as gz_opener

print('inside compressed init --> name {}'.format(__name__))

# __all__ limiting what 'names' we exposed from a module
# locals() will show all teh exposed name
__all__ = ['bz2_opener', 'gz_opener']

