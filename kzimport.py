#!/usr/bin/env python

import optparse
import shutil, tempfile, zipfile, os, json
import lib.packagemanager
import lib.kuanzapackage
import lib.kuanzaproto
import lib.kuanzarefresh


def main():
    parser = optparse.OptionParser()
    parser.add_option('-n', '--name')
    options, args = parser.parse_args()

    if len(args) == 0:
        print('No zipfile was specified. Aborting.')
        return
    if len(args) > 1:
        print('More than one file was specified. Aborting.')
        return

    file = args[0]
    if not os.path.exists(file):
        print('Cannot find file %s. Aborting.' % file)
        return

    
    tempdir = tempfile.mkdtemp()
    try:        
        zip = zipfile.ZipFile( args[0] )
        zip.extractall(tempdir)
        doImport( tempdir, options )
        zip.close()
    except Exception as e:
        print('There was an unknown error. %s' % e)
    finally:
        shutil.rmtree(tempdir)

    lib.kuanzarefresh.refreshPackageData()


def doImport(dirname, options):
    info = {}
    try:
        with open( os.path.join(dirname, 'package.info') ) as infofile:
            info = json.load( infofile )
    except:
        print('There was a problem with package.info file. Aborting.')
        return
    if options.name:
        info['name'] = options.name

    packagemanager = lib.packagemanager.PackageManager( info['name'] )
    if packagemanager.writePackage( info ):
        package = lib.kuanzapackage.KuanzaPackage.findByName( info['name'] )
        install_prototypes(dirname, package)
    else:
        print('Could not import package.')
        return

def install_prototypes(dirname, package):
    for file in os.listdir(dirname):
        if( file.endswith('.zip') ):
            try:
                fullpath = os.path.join( dirname, file )
                proto = lib.kuanzaproto.KuanzaProto(fullpath)
                print('Installing prototype %s' % proto.getName())
                proto.close()
                shutil.copy( fullpath, package.getPath() )
            except Exception as e:
                print('There was an error with file %s' % file)
                print(e)


if __name__ == '__main__':
    main()