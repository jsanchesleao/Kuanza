#!/usr/bin/env python

import os, optparse
import lib.kuanzaproto as kuanzaproto
import lib.kuanzapackage as kuanzapackage

def main():

    parse = optparse.OptionParser()
    parse.add_option('-a', '--all', action='store_true', default=False)
    options, args = parse.parse_args()

    print('Installed Modules and Prototypes: \n')
    for package in kuanzapackage.KuanzaPackage.findAll():
        names = []
        for proto in kuanzaproto.KuanzaProto.findByPackage( package ):
            names.append( proto.getName() )
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