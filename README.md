# python_access_control
overhead of python code; with [M]andatory [A]ccess [C]ontrol
# NOTICE
setup.py is just a testcase, and must be substitute! Try to put spyder-IDE in a sandbox, or try another app!
# something stupid:
https://www.youtube.com/watch?v=UNRnSaXajC4
# framework description: REVERSE on SETUP.PY, and SET RULES
FIRST install an app -- with reverse.sh (reverse.py), and set the access allowed on all dependencies
..listed at setup.py. All others are DENIED! -- or only read, not write!
# framework description: TRACE and SET RULES
SECOND just trace and set access rules.. with root.py (overhead code must be expanded)
# universal access control approach is not always suitable..
A suitable access control needs adjustments to software... But iam searching for such an example;
a kind of setup.py  modification on the entry point. But anything seems more complicated since python3; like setuptools and..
# try on an example..
1) try reverse on setup.py (example-code, must be substituted)
2) reverse.py needs a frozen modules fix..landlock does not work as expected, maybe because of frozen landlock or so..
3) root.py is just an overhead!
