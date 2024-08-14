#command line 
#pipdeptree --freeze --warn silence | grep -P '^[\w0-9-=.]+' > reverse.txt
#command line
def reverse():
    import sysconfig
    #exmaple imports..
    #imports = ['sys', 'itertools', 'datetime', 'os'] 
    my_file = open("reverse.txt", "r") 
    data = my_file.read()  
    imports = data.replace('\n', ' ').split(".")  
    my_file.close() 

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
#returns /usr/local/lib/python3.11/dist-packages at all..
#use the path for access control
