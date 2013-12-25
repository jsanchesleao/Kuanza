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