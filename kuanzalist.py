#!/usr/bin/env python

import os

def main():
    prototypesFolder = os.listdir(  os.path.join(  os.environ['KUANZA_HOME'], 'prototypes') )
    for proto in prototypesFolder:
        print( proto )

if __name__ == '__main__':
    main()