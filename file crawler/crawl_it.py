'''
Created on Oct 16, 2012

@author: tbp
'''
'''
crawl through some folders and print the names and size of the files.
root folder given through argument'''

import os,sys

def crawlIt(path):
    index = 1
    for directory, _, fileName in os.walk(path): # got all the directories, paths and so on
        filesToCheck = [(os.path.join(directory, name)) for name in fileName]
        for files in filesToCheck:
            try:
                print '{0:>7}. {1:<100} {2:>10} kB'.format(str(index), os.path.abspath(files) + ' ,',os.path.getsize(files))
                index += 1
            except:
                pass

if len(sys.argv) != 2:
    currentPath = './'
else:
    currentPath = sys.argv[1]


crawlIt(currentPath)