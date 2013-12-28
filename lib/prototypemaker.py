from lib.filewalker import FileWalker
import zipfile, tempfile, json, os


class PrototypeMaker:
    def __init__(self, folder, name):
        self.folder = folder
        self.name = name

    def pack(self): 
        zip = zipfile.ZipFile('%s.zip' % self.name, 'w')
        self._writeFiles( zip )
        self._writeDescriptor( zip )
        zip.close()

    def _listFiles(self):
        files = []
        FileWalker( self.folder ).each( files.append )
        return files

    def _writeFiles(self, zip):
        for file in self._listFiles():
            arcfile = file.replace(self.folder, 'prototype/', 1)
            zip.write( file, arcfile)

    def _writeDescriptor(self, zip):
        fh, path = tempfile.mkstemp()
        descriptor = os.fdopen( fh, 'w')
        descriptor.write( json.dumps({ 'name': self.name }, sort_keys=True, indent=4) )
        descriptor.close()
        zip.write( path, 'prototype.info' )
        os.remove( path )