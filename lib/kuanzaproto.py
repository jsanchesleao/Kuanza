from zipfile import ZipFile
import shutil, json, os
import tempfile

class KuanzaProto:
    def __init__(self, zipfile):
        zip = ZipFile(zipfile)
        self.zip = zip
        self.info = json.loads( zip.read( 'prototype.info' ).decode('utf-8') )

    def extract(self, projectname):
        print('extracting files')

        tempdir = tempfile.mkdtemp()
        for file in self.zip.namelist():
            if( file.startswith('prototype/') ):
                if( file.endswith('/') ):
                    newdir = os.path.join(tempdir, file )
                    os.makedirs( newdir )
                else:
                    self.zip.extract(file, tempdir)

        shutil.move( os.path.join(tempdir, 'prototype'), projectname )
        shutil.rmtree( tempdir )

    def close(self):
        self.zip.close()

    def getName(self):
        return self.info['name']

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