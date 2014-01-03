#!/usr/bin/env python

import optparse
import lib.filewalker
import lib.kuanzapackage
import re, zipfile


def main():
    parser = optparse.OptionParser()
    options, args = parser.parse_args()

    if len(args) == 0:
        print('No packages specified. Aborting')
        return

    for packagename in args:
        export(packagename)

def export( packagename ):
    print('Exporting package %s' % packagename)
    if lib.kuanzapackage.KuanzaPackage.exists(packagename) :
        package = lib.kuanzapackage.KuanzaPackage.findByName( packagename )
        zipname =  treat(packagename)
        zipfolder( package.getPath(), zipname )
        print('Created %s backup file.' % zipname)
    else:
        print('Cannot find package named %s' % packagename )

def treat(packagename):
    return re.sub('[^\d\w]', '_', packagename)


def zipfolder(folder, targetname): 
    zip = zipfile.ZipFile('%s.zip' % targetname, 'w')
    for file in lib.filewalker.FileWalker( folder ).list():
        arcname = file.replace( folder, '', 1)
        zip.write( file, arcname )
    
    zip.close()


if __name__ == '__main__':
    main()