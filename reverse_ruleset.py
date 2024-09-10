import os
import sys
import time



def main():
    file = open('./setting.txt', 'r')
    lines = file.readlines()
    try:
        if sys.platform[:5] == 'linux':
            from landlock import Ruleset
            rs = Ruleset()
            count = 0
            for line in lines:
                try:
                    count = count + 1
                    line = str(line)
                    j = line.replace('__init__.py', '').replace(' ', '').replace("\n", "")
                    print(count)
                    print(j)
                    if j.endswith("/'") and j.startswith("'/"):
                        print('xxx')
                        rs.allow(j)
                        time.sleep(0.5)
                except:
                    print('error..')
            rs.apply()
            print('..reverse..on..setup.py..set..linux-landlock')
        elif sys.platform[:7] == 'openbsd':
            import openbsd
            openbsd.unveil('/*', 'r')
            openbsd.unveil('.', 'rwx')
            for i in list:
                openbsd.unveil(os.path.abspath(i))
            print('..reverse..on..setup.py..set..openbsd..unveil')
    except:
        print('no suitable OS, try linux or openbsd')
        sys.exit()
#use the absolute path for access control
if __name__=='__main__':
    main()
