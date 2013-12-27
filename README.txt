Prototypes must be zip files inside prototypes dir.

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



create a prototype zip with the kuanzapack util as follows:
    
    $> kuanzapack.py --name <PROTO_NAME> <PROTO_DIR>


to install a prototype zip use the kuanzainstall util as follows:

    $> kuanzainstall.py <PROTO_ZIP>

to uninstall a prototype, find it's name with kuanzalist.py and remove as follows:

    $> kuanzainstall.py --remove <PROTO_NAME>
    