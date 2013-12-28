#!/usr/bin/env python

import optparse, os
from lib.prototypemaker import PrototypeMaker

def main():
    parser = optparse.OptionParser()
    parser.add_option('--name', '-n')
    options, arguments = parser.parse_args()

    if len(arguments) != 1:
        print('Exactly one folder must be specified. %s given ' % len(folders))
        return

    folder = arguments[0]

    if not os.path.isdir( folder ):
        print( 'There is a problem with you folder. Aborting.' )
        return

    name = options.name
    if not name:
        print ('No name given by -n option. Entering in interactive mode.')
        print ('Enter prototype name:')
        name = input()

    PrototypeMaker( folder, name ).pack()
    print('Prototype zipfile successfully created.')



if __name__ == '__main__':
    main()