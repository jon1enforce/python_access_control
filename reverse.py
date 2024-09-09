#command line 
#pipdeptree --freeze --warn silence | grep -P '^[\w0-9-=.]+' > reverse.txt
#command line
import os
import sys
if sys.platform[:5] == 'linux':
    from landlock import Ruleset
if sys.platform[:7] == 'openbsd':
    import openbsd

def reverse():
    import sysconfig
    #exmaple imports..
    #imports = ['sys', 'itertools', 'datetime', 'os']
    my_file = open("reverse.txt", "r")
    data = my_file.read()
    imports_source = data.replace('-', '_').split("\n")
    imports = []
    for i in imports_source:
        x = i.split('==')
        imports.append(x[0])

    my_file.close()
    all_modules = []
    modules = {}
    path = []
    for x in imports:
        if x == None or x == '' or x == ' ':
            continue
        try:
            modules[x] = __import__(x)
            print ("Successfully imported ", x, '.')
        except ImportError:
            print("Error importing ", x, '.')
            continue
        all_modules.append(modules[x])
    module_path = []
    for i in all_modules:
        i = str(i)
        x = i.split('from')
        if len(x)==2:
            x[1].replace(' ', '')
            x[1] = x[1][:-1]
            print(x[1], '\n')
            module_path.append(x[1])
    return module_path
#test on setup.py .. during app install ..
if __name__=='__main__':
    j = '/namespace'
    list = reverse()
    print(list)
    try:
        rs = Ruleset()
        for i in list:
            try:
                j = str(i.replace('__init__.py', '').replace(' ', '').replace("'", ''))
                s = '"' + j + '"'
                print(s)
                rs.allow(s)
            except:
                print('error..')
        rs.apply()
        print('..reverse..on..setup.py..set..linux-landlock')
        if sys.platform == 'openbsd':
            openbsd.unveil('/*', 'r')
            openbsd.unveil('.', 'rwx')
            for i in list:
                openbsd.unveil(os.path.abspath(i))
            print('..reverse..on..setup.py..set..openbsd..unveil')
    except:
        print('no suitable OS, try linux or openbsd')
        sys.exit()
#use the absolute path for access control
