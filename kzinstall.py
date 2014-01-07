#!/usr/bin/env python

import optparse, shutil, os
import lib.kuanzaproto as kuanzaproto
import lib.kuanzapackage as kuanzapackage
import lib.kuanzarefresh


def main():
    parser = optparse.OptionParser()
    parser.add_option('-p','--package', default='Default')
    parser.add_option('--remove', action='store_true', default=False)
    options, args = parser.parse_args()

    if( options.remove ):
        for arg in args:
            uninstall( options.package, arg)
    else:
        for arg in args:
            install( options.package, arg )

    lib.kuanzarefresh.refreshPackageData()

def uninstall( packagename, protoname ):

    if not checkPackage(packagename):
        return
    package = kuanzapackage.KuanzaPackage.findByName(packagename)

    if not kuanzaproto.KuanzaProto.exists( package, protoname ):
        print('Prototype %s not found' % protoname)
        return
    prototype = kuanzaproto.KuanzaProto.findByPackageAndName(package, protoname)
    
    print( 'Are you sure you want to remove prototype named [%s]? y/N' % protoname )
    response = input()

    if response.upper() == 'Y':
        prototype.close()
        os.remove( prototype.getPath() )
        print( 'Prototype successfully uninstalled')
    else:
        print( 'Not removing')
    

def install( packagename, protofile ):
    name = verifyProto(protofile)
    if name == None:
        return

    if not checkPackage(packagename):
        return
    package = kuanzapackage.KuanzaPackage.findByName(packagename)

    if canInstall( package, protofile, name ):        
        shutil.copyfile( protofile, os.path.join( package.getPath(), protofile ) )
        print('Prototype %s successfully installed in the %s package' % (name, packagename))


def checkPackage(packagename):
    if not kuanzapackage.KuanzaPackage.exists(packagename):
        print('Package [%s] not found. Aborting.' % packagename )
        return False
    return True


def verifyProto( protofile ):
    try:
        proto = kuanzaproto.KuanzaProto( protofile )
        print( 'Verifying prototype [%s]' % proto.getName() )
        return proto.getName()
        proto.close()
    except Exception as e:
        print('There is an error with your prototype file:')
        print(e)
        return None

def canInstall(package, protofile, name ):
    prototypeName  = os.path.basename( protofile )    

    if os.path.exists( os.path.join( package.getPath(), prototypeName ) ) :
        print('There already is a prototype with the same filename installed in the [%s] package ' % package.getName())
        return False

    if kuanzaproto.KuanzaProto.exists(package, name):
        print('There already is a prototype with the same name installed in the [%s] package' % package.getName())
        return False

    return True


if __name__ == '__main__':
    main()