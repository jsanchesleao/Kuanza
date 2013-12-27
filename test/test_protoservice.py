#!/usr/bin/env python

import unittest
import os
from lib import protoservice

class TestProtoService(unittest.TestCase):

    def test_can_list_installed_prototype_packages(self):
        packages = protoservice.getInstalledPackageNames()
        self.assertTrue( 'ExpressJS' in packages )

    def test_can_list_installed_prototype_folder_paths(self):
        packages = protoservice.getInstalledPackagePaths()
        expectedpath = os.path.join( os.environ['KUANZA_HOME'] , 'prototypes', 'node')
        self.assertTrue( expectedpath in packages )

    def test_can_list_prototype_names(self):
        prototypes = protoservice.getInstalledPrototypeNames('ExpressJS')
        self.assertTrue( 'ExpressJSEmpty' in prototypes )

    def test_can_list_prototype_files(self):
        prototypes = protoservice.getInstalledPrototypeFiles('ExpressJS')
        self.assertTrue( 'expressjsempty.zip' in prototypes )

    def test_find_zipfile_path_given_prototype_name_and_package_name(self):
        filepath = protoservice.findZipFileByPrototypeName('ExpressJS', 'ExpressJSEmpty' )
        expectedpath = os.path.join( os.environ['KUANZA_HOME'] , 'prototypes', 'node', 'expressjsempty.zip')
        self.assertEqual( expectedpath , filepath )

    def test_get_prototype_object_given_name(self):
        packagepath = os.path.join( os.environ['KUANZA_HOME'], 'prototypes', 'node' )
        proto = protoservice.loadPrototypeObject(  packagepath, 'expressjsempty.zip' )
        self.assertEqual( proto.getName(), 'ExpressJSEmpty' )


if __name__ == '__main__':
    unittest.main()
