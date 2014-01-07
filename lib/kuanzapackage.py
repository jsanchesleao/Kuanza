import os, json

class KuanzaPackage:

    def __init__(self, packagepath):
        self.path = packagepath
        with open( self._infoFilePath() ) as packinfo:
            self.info = json.load( packinfo )

    def _infoFilePath(self):
        return os.path.join(self.path, 'package.info')

    def getName(self):
        return self.info['name']

    def getDescription(self):
        return self.info['description']

    def setDescription(self, description):
        self.info['description'] = description

    def save(self):
        with open(self._infoFilePath(), 'w') as infoFile:
            infoFile.write( json.dumps(self.info, sort_keys=True, indent=4) )

    def getPath(self):
        return self.path


    @staticmethod
    def exists(name):
        for pack in KuanzaPackage.findAll():
            if name == pack.getName():
                return True
        return False

    @staticmethod
    def findAll():
        for path in os.listdir( KuanzaPackage.basepath() ):
            fullpath = os.path.join( KuanzaPackage.basepath(), path )
            if os.path.isdir( fullpath ):
                yield KuanzaPackage( fullpath )

    @staticmethod
    def findByName(name):
        for pack in KuanzaPackage.findAll():
            if name == pack.getName():
                return pack
        return None

    @staticmethod
    def basepath():        
        return os.path.join( os.environ['KUANZA_HOME'], 'prototypes' )

    @staticmethod
    def getPackagesData():
        path = os.path.join( KuanzaPackage.basepath(), 'packages.info' )
        info = {}
        with open( path ) as infofile:
            info = json.load( infofile )
        return info
