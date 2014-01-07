#!/usr/bin/env python

import json, os
import lib.kuanzapackage
import lib.kuanzaproto


def refreshPackageData():
    packages = {}
    for package in lib.kuanzapackage.KuanzaPackage.findAll():
        packages[ package.getName() ] = getPackageData(package)

    output = json.dumps( packages, indent=4, sort_keys=True )

    packagesinfo = os.path.join( lib.kuanzapackage.KuanzaPackage.basepath(), 'packages.info' )

    with open(packagesinfo, 'w') as infofile:
        infofile.write(output)


def getPackageData(package):
    data = {
        'path': package.getPath(),
        'desc': package.getDescription(),
        'prototypes': {}
    }
    for prototype in lib.kuanzaproto.KuanzaProto.findByPackage(package):
        data['prototypes'][ prototype.getName() ] = prototype.getPath()

    return data