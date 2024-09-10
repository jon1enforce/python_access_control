#command line 
#pipdeptree --freeze --warn silence | grep -P '^[\w0-9-=.]+' > reverse.txt
#command line
import os
import sys

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
            #print(x[1], '\n')
            module_path.append(x[1])
    return module_path
#test on setup.py .. during app install ..
if __name__=='__main__':
    list = reverse()
    file = open('./setting.txt','w')
    for i in list:
        file.write(i)
        file.write('\n')
    file.close()
