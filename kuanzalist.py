#!/usr/bin/env python

import os
from lib.kuanzaproto import KuanzaProto

def main():
    for proto in getInstalledPrototypeNames():
        print( proto )

def getInstalledPrototypeNames():
    for proto in zipfiles():
        yield getPrototype(proto).getName()

def getPrototypesPath():
    return os.path.join(  os.environ['KUANZA_HOME'], 'prototypes')

def getPrototypePath(prototypeName):
    return os.path.join( os.environ['KUANZA_HOME'], 'prototypes', find( prototypeName ) )

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