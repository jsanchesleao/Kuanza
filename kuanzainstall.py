#!/usr/bin/env python

import optparse, shutil, os
from lib.kuanzaproto import KuanzaProto
import kuanzalist

def main():
    parser = optparse.OptionParser()
    parser.add_option('--remove', action='store_true', default=False)
    options, args = parser.parse_args()

    if( options.remove ):
        for arg in args:
            uninstall(arg)
    else:
        for arg in args:
            install( arg )

def uninstall( protoname ):
    protofile = kuanzalist.find( protoname )
    print( 'Are you sure you want to remove prototype named [%s]? y/N' % protoname )
    response = input()

    if response.upper() == 'Y':
        fullpath = os.path.join(kuanzalist.getPrototypesPath(), protofile)
        os.remove( fullpath )
        print( 'Prototype successfully uninstalled')
    else:
        print( 'Not removing')
    

def install( protofile ):
    name = verifyProto(protofile)
    verifyIfCanInstall( protofile, name )
    shutil.copyfile( protofile, os.path.join( kuanzalist.getPrototypesPath(), protofile ) )
    print('Prototype %s successfully installed' % name)


def verifyProto( protofile ):
    try:
        proto = KuanzaProto( protofile )
        print( 'Verifying prototype [%s]' % proto.getName() )
        return proto.getName()
        proto.close()
    except:
        print('There is an error with your prototype file')
        exit(-1)

def verifyIfCanInstall( protofile, name ):
    prototypesPath = kuanzalist.getPrototypesPath()
    prototypeName  = os.path.basename( protofile )
    if os.path.exists( os.path.join(prototypesPath, prototypeName) ) :
        print('There already is a prototype with the same filename installed')
        exit(-1)

    if name in kuanzalist.getInstalledPrototypeNames():
        print('There already is a prototype with the same name installed')
        exit(-1)


if __name__ == '__main__':
    main()