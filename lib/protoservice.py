import os
from lib.kuanzaproto import KuanzaProto

def getInstalledPrototypeNames():
    for proto in getInstalledPrototypeFiles():
        yield loadPrototypeObject(proto).getName()

def getInstalledPrototypeFiles():
    for proto in os.listdir(  getPrototypesPath() ):
        if( proto.endswith('.zip') ):
            yield proto

def getPrototypesPath():
    return os.path.join(  os.environ['KUANZA_HOME'], 'prototypes')

def getPrototypePath(prototypeName):
    return os.path.join( os.environ['KUANZA_HOME'], 'prototypes', findZipFileByPrototypeName( prototypeName ) )

def loadPrototypeObject(zipfile):
    return KuanzaProto( os.path.join(getPrototypesPath(), zipfile) )


def findZipFileByPrototypeName(name):
    for proto in getInstalledPrototypeFiles():
        if( name == loadPrototypeObject(proto).getName() ):
            return proto
    return None