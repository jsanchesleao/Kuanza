import os
import json
import lib.protoservice

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


    @staticmethod
    def createByName(name):
        return KuanzaPackage( lib.protoservice.findPackagePathByName(name) )

    @staticmethod
    def exists(name):
        return name in lib.protoservice.getInstalledPackageNames()