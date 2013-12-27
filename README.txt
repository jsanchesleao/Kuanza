Install kuanza by simply extracting it and pointing a system variable named KUANZA_HOME to that directory
It needs python 3

To create an instance of a prototype, use the kzcreate tool as follows:
    $>kzcreate.py [-p <PACKAGE_NAME>] <PROTOTYPE_NAME> [<INSTANCE_NAME>]

For a list of installed prototypes and their packages, use kzlist tool:
    $>kzlist.py


Prototypes must be zip files inside a package dir.

It must have the following structure:

/
    -prototype/
        -files
        -of
        -your
        -prototype
    prototype.info


prototype.info is a JSON formatted file which contains meta data for the package.
Currently the accepted format is:

{
    "name": "<NAME OF THE PROTOTYPE>"
}


A Package is a group of relates prototypes, and they are directories inside the prototypes installation dir
They must hold a JSON formatted file named package.info.
Currently the accepted format is:

{
    "name": "<NAME OF THE PACKAGE>",
    "description": "<Brief description of the contents of the package>"
}



create a prototype zip with the kzpack util as follows:
    $> kzpack.py --name <PROTO_NAME> <PROTO_DIR>


to install a prototype zip use the kzinstall util as follows:
    $> kzinstall.py [-p <TARGET_PACKAGE>] <PROTO_ZIP>

to uninstall a prototype, find it's name with kzlist.py and remove as follows:
    $> kzinstall.py --remove [-p <TARGET_PACKAGE>] <PROTO_NAME>
    