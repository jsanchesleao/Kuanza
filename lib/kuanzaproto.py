from zipfile import ZipFile
import shutil, json, os
import tempfile
import lib.filewalker
import lib.interpreter

class KuanzaProto:
    def __init__(self, zipfile):
        self.zipfile = zipfile
        zip = ZipFile(zipfile)
        self.zip = zip
        self.info = json.loads( zip.read( 'prototype.info' ).decode('utf-8') )

    def extract(self, projectname, projectVariables, inline=False):
        print('extracting files')

        tempdir = tempfile.mkdtemp()
        for file in self.zip.namelist():
            if( file.startswith('prototype/') ):
                if( file.endswith('/') ):
                    newdir = os.path.join(tempdir, file )
                    os.makedirs( newdir )
                else:
                    self.zip.extract(file, tempdir)

        files = lib.filewalker.FileWalker(tempdir)
        files.each( lambda filename: lib.interpreter.Interpreter(filename).interpret(projectVariables) )


        temppath = os.path.join(tempdir, 'prototype');

        if inline:
            self._copyinline( temppath )
        else:
            self._copy( temppath, projectname)    

        shutil.rmtree( tempdir )

    def _copyinline(self, temppath):
        files = lib.filewalker.FileWalker( temppath )
        files.each( lambda filename: shutil.copy(filename, os.getcwd() ) )

    def _copy( self, temppath, projectname ):
        shutil.move( temppath, projectname )

    def close(self):
        self.zip.close()

    def getName(self):
        return self.info['name']

    def getPath(self):
        return self.zipfile

    @staticmethod
    def checkIntegrity( filepath ):
        result = False
        proto = None
        try:
            proto = KuanzaProto( filepath )
            if proto.getName() != None:
                result = True
        except:
            result = False
        finally:
            if proto != None:
                proto.close()

        return result

    @staticmethod
    def findByPackage(package):
        for zipfile in os.listdir( package.getPath() ):
            if zipfile.endswith('.zip'):
                yield KuanzaProto(  os.path.join( package.getPath(), zipfile ) )

    @staticmethod
    def exists( package, name ):
        return KuanzaProto.findByPackageAndName(package, name) != None

    @staticmethod
    def findByPackageAndName(package, name):
        for proto in KuanzaProto.findByPackage(package):
            if proto.getName() == name:
                return proto
        return None