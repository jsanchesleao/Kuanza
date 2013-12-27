#!/usr/bin/env python

import unittest
import os
from lib import protoservice

class TestProtoService(unittest.TestCase):

    def test_can_list_prototype_names(self):
        prototypes = protoservice.getInstalledPrototypeNames()
        self.assertTrue( 'ExpressJSEmpty' in prototypes )

    def test_can_list_prototype_files(self):
        prototypes = protoservice.getInstalledPrototypeFiles()
        self.assertTrue( 'expressjsempty.zip' in prototypes )

    def test_find_zipfile_path_given_prototype_name(self):
        filepath = protoservice.getPrototypePath( 'ExpressJSEmpty' )
        expectedpath = os.path.join( os.environ['KUANZA_HOME'] , 'prototypes', 'expressjsempty.zip')
        self.assertEqual( expectedpath , filepath )

    def test_get_prototype_object_given_name(self):
        proto = protoservice.loadPrototypeObject( 'expressjsempty.zip' )
        self.assertEqual( proto.getName(), 'ExpressJSEmpty' )

    def test_find_zipfile_name_given_prototype_name(self):
        filename = protoservice.findZipFileByPrototypeName( 'ExpressJSEmpty' )        
        self.assertEqual( 'expressjsempty.zip' , filename )


if __name__ == '__main__':
    unittest.main()
