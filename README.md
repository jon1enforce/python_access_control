# python_access_control
overhead of python code; with [M]andatory [A]ccess [C]ontrol
# something stupid:
https://www.youtube.com/watch?v=UNRnSaXajC4
# framework description:
FIRST install with reserve.sh (reserver.py)
..on setup.py
SECOND just trace and set access rules.. with root.py (overhead code must be expanded)
# universal access control approach is not always suitable..
A suitable access control needs adjustments to software... But iam searching for such an example;
a kind of setup.py  modification on the entry point. But anything seems more complicated since python3; like setuptools and..
# try on an example..
1) mkdir /home/user/pybuild
2) python3 setup.py build --build-base .
3) other resources must be reversed with trace.
4) another Resource: Python egg is an older version of the Python wheel package containing the metadata and installation information about a particular python package. 
5) reverse.py needs a frozen modules fix..landlock does not work as expected, maybe because of frozen landlock or so..
