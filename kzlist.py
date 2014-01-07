#!/usr/bin/env python

import os, optparse
import lib.kuanzapackage

def main():

    parse = optparse.OptionParser()
    parse.add_option('-a', '--all', action='store_true', default=False)
    options, args = parse.parse_args()

    print('Installed Modules and Prototypes: \n')

    packagesData = lib.kuanzapackage.KuanzaPackage.getPackagesData()

    for packageName, packageData in packagesData.items():
        names = []
        for prototypeName in packageData['prototypes'].keys():
            names.append( prototypeName )
        if len(names) == 0:
            if not options.all:
                continue

        print('  %s' % packageName )
        print('  (%s)' % packageData['desc'] )
        print('  |')
        for name in names:
            print('  |--%s' % name)
        print('')

if __name__ == '__main__':
    main()