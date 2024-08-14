#command line 
#pipdeptree --freeze --warn silence | grep -P '^[\w0-9-=.]+' > reverse.txt
#command line
import os
def reverse():
    import sysconfig
    #exmaple imports..
    #imports = ['sys', 'itertools', 'datetime', 'os'] 
    my_file = open("reverse.txt", "r") 
    data = my_file.read()  
    imports = data.replace('==', '\n').replace('-', '_').split("\n")
    imports = imports[::2]
    
    my_file.close()
    all_modules = []
    modules = {}
    path = []
    for x in imports:
        try:
            modules[x] = __import__(x)
            print ("Successfully imported ", x, '.')
        except ImportError:
            print("Error importing ", x, '.')
            continue
        all_modules.append(modules[x])
        #path.append(str(os.path.abspath(modules[x].__file__)))
    #print(path)
    return path
    
#test
if __name__=='__main__':
    reverse()

    reverse()
#returns /usr/local/lib/python3.11/dist-packages at all..
#use the path for access control
