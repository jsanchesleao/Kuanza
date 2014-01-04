=============================
Kuanza
=============================


Cross Platform prototype engine, for start new projects


Status
------

It's still under development, but currently the following features are working good:

* Creation of project based on installed prototype
* List of installed packages and prototypes
* Create, manage and remove packages
* Pack arbitrary folder into prototype
* Install and uninstall custom prototypes
* Export installed packages
* Import packages


Quick Manual
------------

To create an instance of a prototype, use the kzcreate tool as follows:
    $>kzcreate.py [-p <PACKAGE_NAME>] [--inline] <PROTOTYPE_NAME> [<INSTANCE_NAME>]

    The inline option does not create a directory for the new project, but use the current working directory instead

To list of installed prototypes and their packages, use kzlist tool:
    $>kzlist.py [-a] #use -a flag to show even empty packages

To create an empty package, use kzpkg tool as follows:
    $>kzpkg.py --new <PACKAGE_NAME> [<DESCRIPTION>]

To edit a package's description, use kzpkg tool as follows:
    $>kzpkg.py --desc <PACKAGE_NAME> <NEW_DESCRIPTION>

To create a prototype zip with the kzpack util as follows:
    $> kzpack.py --name <PROTO_NAME> <PROTO_DIR>

To install a prototype zip use the kzinstall util as follows:
    $> kzinstall.py [-p <TARGET_PACKAGE>] <PROTO_ZIP>

To uninstall a prototype, find it's name with kzlist.py and remove as follows:
    $> kzinstall.py --remove [-p <TARGET_PACKAGE>] <PROTO_NAME>

To export packages, use kzexport tool:
    $> kzexport.py <PACKAGE_NAME> [<OTHER_PACKAGES>, ]
    #this will generate zip files containing the packages' data

To import a package zip data, use kzimport tool:
    $> kzimport.py <ZIPDATA_FILE> [--name <PACKAGE_NAME>]

Credits
-------

* Binary file recognition powered by binaryornot package by Audrey Roy
* https://github.com/audreyr/binaryornot