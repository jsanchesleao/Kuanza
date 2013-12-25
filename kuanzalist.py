#!/usr/bin/env python

import os
from lib.kuanzaproto import KuanzaProto

def main():
    for proto in zipfiles():
        print( getPrototype(proto).getName() )

            

def getPrototypesPath():
    return os.path.join(  os.environ['KUANZA_HOME'], 'prototypes')

def getPrototype(name):
    return KuanzaProto( os.path.join(getPrototypesPath(), name) )

def zipfiles():
    for proto in os.listdir(  getPrototypesPath() ):
        if( proto.endswith('.zip') ):
            yield proto


def find(name):
    for proto in zipfiles():
        if( name == getPrototype(proto).getName() ):
            return proto
    return None

if __name__ == '__main__':
    main()