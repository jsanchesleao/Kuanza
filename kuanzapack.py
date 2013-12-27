#!/usr/bin/env python

import optparse
from lib.filewalker import FileWalker
import zipfile
import tempfile, json, os

def main():
    parser = optparse.OptionParser()
    parser.add_option('--name', '-n')
    options, folders = parser.parse_args()

    if len(folders) != 1:
        print('Exactly one folder must be specified. %s given ' % len(folders))
        exit(-1)

    name = options.name
    if not name:
        print ('No name given by -n option. Entering in interactive mode.')
        print ('Enter prototype name:')
        name = input()

    pack( folders[0], name)


def pack( folder, name ):
    files = []
    try:        
        FileWalker(folder).each( files.append )
    except IOError as e:
        print(e)
        exit(-1)

    zip = zipfile.ZipFile('%s.zip' % name, 'w')
    copyPrototype(zip, folder, files)
    writeDescriptor( zip, name )
    zip.close()

def copyPrototype(zip, folder, filelist):
    for file in filelist:
        arcfile = file.replace(folder, 'prototype/', 1)
        zip.write( file, arcfile)

def writeDescriptor(zip, name):
    fh, path = tempfile.mkstemp()
    descriptor = os.fdopen( fh, 'w')
    descriptor.write( json.dumps({ 'name': name }, sort_keys=True, indent=4) )
    descriptor.close()
    zip.write( path, 'prototype.info' )
    os.remove( path )


if __name__ == '__main__':
    main()