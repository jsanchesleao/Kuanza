import os
from lib.kuanzaproto import KuanzaProto
from lib.kuanzapackage import KuanzaPackage

def getInstalledPackageNames():
    for packagepath in getInstalledPackagePaths():
        yield KuanzaPackage( packagepath ).getName()

def checkPrototypeIsInstalled(packagename, prototype):
    if not packagename in getInstalledPackageNames():
        return False
    if not prototype in getInstalledPrototypeNames( packagename ):
        return False
    return True

def getInstalledPackages():
    for packagepath in getInstalledPackagePaths():
        yield KuanzaPackage( packagepath )

def getInstalledPackagePaths():
    for packfolder in os.listdir( getPackagesPath() ):
        yield os.path.join( getPackagesPath(), packfolder )

def getInstalledPrototypeNames(packagename):
    packagePath = findPackagePathByName(packagename)
    for proto in getInstalledPrototypeFiles(packagename):
        yield loadPrototypeObject( packagePath, proto ).getName()

def getInstalledPrototypeFiles(packagename):
    for proto in os.listdir(  findPackagePathByName(packagename) ):
        if( proto.endswith('.zip') ):
            yield proto

def getPackagesPath():
    return os.path.join(  os.environ['KUANZA_HOME'], 'prototypes')

def loadPrototypeObject(packagepath, zipfile):
    return KuanzaProto( os.path.join( packagepath, zipfile ) )

def findZipFileByPrototypeName(packagename, name):

    packagepath = findPackagePathByName( packagename )

    for proto in getInstalledPrototypeFiles(packagename):
        if( name == loadPrototypeObject( packagepath, proto ).getName() ):
            return os.path.join( findPackagePathByName(packagename), proto )
    return None

def findPackagePathByName(packagename):
    for path in getInstalledPackagePaths():
        if KuanzaPackage(path).getName() == packagename:
            return path
    return None