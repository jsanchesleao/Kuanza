#!/usr/bin/env python

import os, optparse
from lib.kuanzaproto import KuanzaProto
import lib.protoservice as protoservice

def main():

    parse = optparse.OptionParser()
    parse.add_option('-a', '--all', action='store_true', default=False)
    options, args = parse.parse_args()

    print('Installed Modules and Prototypes: \n')
    for package in protoservice.getInstalledPackages():
        names = []
        for name in protoservice.getInstalledPrototypeNames(package.getName()):
            names.append( name )
        if len(names) == 0:
            if not options.all:
                continue

        print('  %s' % package.getName() )
        print('  (%s)' % package.getDescription() )
        print('  |')
        for name in names:
            print('  |--%s' % name)
        print('')


if __name__ == '__main__':
    main()