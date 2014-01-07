#!/usr/bin/env python

import optparse
from lib.kuanzapackage import KuanzaPackage
from lib.packagemanager import PackageManager
import lib.kuanzarefresh

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

    
    lib.kuanzarefresh.refreshPackageData()


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
    if KuanzaPackage.exists(name):
        print( 'There already is a package named [%s]' % name)
        return

    packageManager = PackageManager(name)
    packageManager.writePackage( {'description': description} )
    print('Package created')

def editDescription(args):
    if len(args) == 0:
        print('No package was specified. Aborting.')
        return
    elif len(args) == 1:
        print('No description was specified. Aborting.')
        return

    name = args[0]
    description = args[1]
    if not KuanzaPackage.exists( name ):
        print ('There is no package [%s] installed. Aborting.' % name)
        return
    else:
        writeDescription( name, description )
        print('Description successfully altered.')

def writeDescription(name, description):
    package = KuanzaPackage.findByName( name )
    package.setDescription( description )
    package.save()

def purgePackage(args):
    if len(args) == 0:
        print('No name was given. Aborting.')
        return
    else:
        name = args[0]
        if not KuanzaPackage.exists(name):
            print('Package %s not found' % name)
        elif confirmPurge(name):
            PackageManager(name).purgePackage()
            print( 'Package successfully purged' )

def confirmPurge(name):
    print('Are you sure you want to remove the %s package and ALL its prototypes? y/N' % name)
    response = input()
    if response.upper() == 'Y':
        print('Are you sure? This operation cannot be undone. y/N')
        confirm = input()
        return confirm.upper() == 'Y'
    return False




if __name__ == '__main__':
    main()