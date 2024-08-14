
imports = ['sys', 'itertools', 'datetime', 'os']
modules = {}
for x in imports:
    try:
        modules[x] = __import__(x)
        print "Successfully imported ", x, '.'
    except ImportError:
        print "Error importing ", x, '.'
