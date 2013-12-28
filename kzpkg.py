#!/usr/bin/env python

import optparse, os
import lib.protoservice as protoservice
import json, shutil

def main():
    parse = optparse.OptionParser()
    parse.add_option('--new', action='store_true', default=False)
    parse.add_option('--desc', action='store_true', default=False)
    parse.add_option('--purge', action='store_true', default=False)
    options, args = parse.parse_args()

    if options.new:
        createPackage( args )
    if options.desc:
        editDescription( args )
    if options.purge:
        purgePackage( args )


def createPackage(args):
    if len(args) == 0:
        print('No name was given. Aborting')
        return
    elif len(args) == 1:
        print('WARNING: No description given.')
        writePackage( args[0], 'No description given')
    else:
        writePackage( args[0], args[1])

def writePackage( name, description ):
    if name in protoservice.getInstalledPackageNames():
        print( 'There already is a package named [%s]' % name)
        return
    packagesPath = protoservice.getPackagesPath()
    newPackagePath = os.path.join( packagesPath, name )
    os.mkdir( newPackagePath )
    writePackageInfo( newPackagePath, name, description )
    print('Package created')

def writePackageInfo(path, name, description):
    infoPath = os.path.join( path, 'package.info' )
    with open(infoPath, 'w') as infoFile:
        info = { 'name': name, 'description': description }
        infoFile.write( json.dumps(info, sort_keys=True, indent=4) )

def editDescription(args):
    if len(args) == 0:
        print('No package was specified. Aborting.')
        return
    elif len(args) == 1:
        print('No description was specified. Aborting.')
        return
    else:
        writeDescription( args[0], args[1] )

def writeDescription(name, description):
    if name not in protoservice.getInstalledPackageNames():
        print( 'Package [%s] not found' % name)
        return

    infoPath = os.path.join( protoservice.findPackagePathByName(name), 'package.info' )
    infoData = None
    with open(infoPath) as infoFile:
        infoData = json.load(infoFile)

    if infoData != None:
        infoData['description'] = description
        with open(infoPath, 'w') as infoFile:
            infoFile.write( json.dumps(infoData, sort_keys=True, indent=4) )
    print('Description updated')

def purgePackage(args):
    if len(args) == 0:
        print('No name was given. Aborting.')
        return
    else:
        name = args[0]
        if not packageExists(name):
            print('Package %s not found' % name)
        elif confirmPurge(name):
            removePackageFolder(name)

def packageExists(name):
    if name in protoservice.getInstalledPackageNames():
        return True
    return False

def confirmPurge(name):
    print('Are you sure you want to remove the %s package and ALL its prototypes? y/N' % name)
    response = input()
    if response.upper() == 'Y':
        print('Are you sure? This operation cannot be undone. y/N')
        confirm = input()
        return confirm.upper() == 'Y'
    return False

def removePackageFolder(name):
    prototypePath = protoservice.findPackagePathByName(name)
    shutil.rmtree( prototypePath )
    print( 'Prototype successfully purged' )


if __name__ == '__main__':
    main()