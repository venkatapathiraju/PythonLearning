
import sys
import os
import subprocess
import inspect

# Define 'writeTo' function below, such that 
# it writes input_text string to filename.
def writeTo(filename, input_text):
    with open(filename,'w') as fp:
        fp.write(input_text)
    
# Define the function 'archive' below, such that
# it archives 'filename' into the 'zipfile'
def archive(zfile, filename):
    with zipfile.ZipFile(zfile,'w') as myzip:
        myzip.write(filename)

def run_process(cmd_args):
    with subprocess.Popen(cmd_args,stdout = subprocess.PIPE)  as fp:
        return fp.communicate()[0]


test  = ['python', '-c', 'print("Hello")']
res = run_process(test)
print(res)

