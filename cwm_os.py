#! /usr/bin/python
"""

$Id$

Operating systems built-ins for cwm
http://www.w3.org/2000/10/swap/string.py

See cwm.py and the os module in python

"""

from thing import *
import thing

import os

OS_NS_URI = "http://www.w3.org/2000/10/swap/os#"



###############################################################################################
#
#                              O P E R A T I N G   S Y T E M   B U I L T - I N s
#
#
#   Light Built-in classes

# Read Operating sytem environment lookup - read-only
#
# Not fatal if not defined
class BI_environ(LightBuiltIn, Function):
    def evaluateObject(self, store, context, subj, subj_py):
        if thing.verbosity() > 80: progress("os:environ input:"+`subj_py`+ " has value "+os.environ[subj_py])
        if type(subj_py) == type(''):
            return store._fromPython(context, os.environ.get(subj_py, None))
        progress("os:environ input is not a string: "+`subj_py`)
# Command line argument: read-only
#  The command lines are passed though cwm using "--with" and into the RDFStore when init'ed.
# Not fatal if not defined
class BI_argv(LightBuiltIn, Function):
    def evaluateObject(self, store, context, subj, subj_py):
        if thing.verbosity() > 80: progress("os:argv input:"+`subj_py`)
        if type(subj_py) == type('') and store.argv:  # Not None or []
            try:
                argnum = int(subj_py) -1
            except ValueError:
                if thing.verbosity() > 30:
                    progress("os:argv input is not a number: "+`subj_py`)
                return None
            if argnum < len(store.argv):
                return store._fromPython(context, store.argv[argnum])


#  Register the string built-ins with the store

def register(store):
    str = store.internURI(OS_NS_URI[:-1])
    str.internFrag("environ", BI_environ)
    str.internFrag("argv", BI_argv)

# ends

