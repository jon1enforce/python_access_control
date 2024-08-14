#command line 
#pipdeptree --freeze --warn silence | grep -P '^[\w0-9-=.]+' > reverse.txt
#command line
def reverse():
    import sysconfig
    imports = ['sys', 'itertools', 'datetime', 'os']
    modules = {}
    for x in imports:
        try:
            modules[x] = __import__(x)
            print ("Successfully imported ", x, '.')
        except ImportError:
            print("Error importing ", x, '.')
    all_modules = []
    for i in imports:
        all_modules.append(str(sysconfig.get_path('purelib')))
    print(all_modules)    
    return all_modules
    
#test
if __name__=='__main__':
    reverse()
