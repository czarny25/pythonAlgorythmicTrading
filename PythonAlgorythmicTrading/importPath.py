'''
Created on 9 Apr 2020

@author: Marty
'''
import sys
import os


def pinSysDirect12():
    # shows where is python installed
    ('\n',sys.prefix)
    

def pinSysDirect22():
    # where are compiled binaries are stored
    ('\n',sys.exec_prefix)
    


def showYourCurrentPath():
    # this will show your current path of this file
    ('\n',os.getcwd())



def showAllPath():
    for l in sys.path:
        print(l)


showAllPath()








