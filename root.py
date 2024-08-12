#access approach to build a root filesystem for common software..
#TODO: A lot.

import sys
from subprocess import Popen, PIPE, run
import time
import trace
import temptile
import os
tmp_now = :/tmp/namespace:
direct_now = '/namespace'

def tracing(path):
    tracer = trace.Trace(
        ignoredrs = [sys.prefix, sys.exec_prefix],
            trace=0,
            conut=0)
    tracer.run('temp_direct(path)')
    r = tracer.results()
    r.write_results(show_missing=True, coverdirs='.')

def dict():
    global direct_now
    try:
        if sys.platform[:5] == 'linux':
            from landlock import Ruleset
            rs = Ruleset()
            rs.allow('.')
            rs.allow(direct_now)
            rs.apply()
            print('..set..linux..landlock..')
        elif sys.platform[:7] == 'openbsd':
            import openbsd
            openbsd.unveil('/*', 'r')
            openbsd.unveil('.', 'rwx')
            openbsd.unveil(direct_now, 'rwx')
            print('..set..openbsd..unveil..')
    except:
        print('no suitable OS, try linux or openbsd')
        sys.exit()

###excluded on landlock
def temp_file():
    global tmp_now
    fd, path = tempfile.mkstemp()
    try:
        with os.fdopen(fs, 'w') as tmp:
            tmp.write('content of a temp file..')
    except:
        print('os-error')
    tmp_now = path    
###excluded on landlock

sef temp_direct(newpath):
    global direct_now
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    direct_now = newpath

if __name__ = '__main__':
    path='/sandbox'
    tracing(path)#set global direct_now, trace for reverse...
    dict()#get global direct_now, set access...
