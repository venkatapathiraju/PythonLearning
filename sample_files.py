# Complete the function below.

import sys
import os
import io
import re

zenPython = '''
    The Zen of Python, by Tim Peters
    
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may no55.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!
    '''
#print(zenPython)
fp = io.StringIO(zenPython) 
zenlines=fp.readlines()
zenlines = [line.strip() for line in zenlines ]
#print(zenlines)
#m = re.search('-(.+?)-'
for line in zenlines:
    m=re.search('(-/*)(.+?)(-/*)',line)
    if m:
        print(m.group(1))
            

         



