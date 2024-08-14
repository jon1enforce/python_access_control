def reverse():
    import sysconfig
    imports = ['sys', 'itertools', 'datetime', 'os']
    modules = {}
    for x in imports:
        try:
            modules[x] = __import__(x)
            print "Successfully imported ", x, '.'
        except ImportError:
            print "Error importing ", x, '.'
    all_modules = []
    for i in imports:
        all_modules.append(str(sysconfig.get_path('purelib')))
    
