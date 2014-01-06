import os, json, shutil
import lib.kuanzapackage as kuanzapackage

class PackageManager:
    def __init__(self, name):
        self.name = name

    def writePackage( self, packageInfo ):
        if kuanzapackage.KuanzaPackage.exists( self.name ):
            return False
        os.mkdir( self._packagePath() )
        self._writePackageInfo( packageInfo )
        return True

    def _packagePath(self):
        packagesPath = kuanzapackage.KuanzaPackage.basepath()
        newPackagePath = os.path.join( packagesPath, self.name )
        return newPackagePath

    def _writePackageInfo(self, packageInfo):
        infoPath = os.path.join( self._packagePath(), 'package.info' )
        with open(infoPath, 'w') as infoFile:
            packageInfo['name'] = self.name
            infoFile.write( json.dumps(packageInfo, sort_keys=True, indent=4) )

    def purgePackage( self ):
        shutil.rmtree( kuanzapackage.KuanzaPackage.findByName( self.name ).getPath() )
