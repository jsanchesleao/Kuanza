import os
import json

class KuanzaPackage:

    def __init__(self, packagepath):
        self.path = packagepath
        with open( os.path.join(packagepath, 'package.info') ) as packinfo:
            self.info = json.load( packinfo )

    def getName(self):
        return self.info['name']

    def getDescription(self):
        return self.info['description']
