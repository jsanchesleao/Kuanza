
To create an instance of a prototype, use the kuanzacreate tool as follows:
    $>kuanzacreate.py [-p <PACKAGE_NAME>] <PROTOTYPE_NAME> [<INSTANCE_NAME>]

For a list of installed prototypes and their packages, use kuanzalist tool:
    $>kuanzalist.py


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



create a prototype zip with the kuanzapack util as follows:
    $> kuanzapack.py --name <PROTO_NAME> <PROTO_DIR>


to install a prototype zip use the kuanzainstall util as follows:
    $> kuanzainstall.py [-p <TARGET_PACKAGE>] <PROTO_ZIP>

to uninstall a prototype, find it's name with kuanzalist.py and remove as follows:
    $> kuanzainstall.py --remove [-p <TARGET_PACKAGE>] <PROTO_NAME>
    