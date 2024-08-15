#command line 
#pipdeptree --freeze --warn silence | grep -P '^[\w0-9-=.]+' > reverse.txt
#command line
import os
def reverse():
    import sysconfig
    #imports_example = ['sys', 'itertools', 'datetime', 'os'] 
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
    print(all_modules)
    return all_modules
#test
if __name__=='__main__':
    reverse()
#returns /usr/local/lib/python3.11/dist-packages at all..
