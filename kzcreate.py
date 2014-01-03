#!/usr/bin/env python

import os, optparse

import lib.kuanzaproto as kuanzaproto
import lib.kuanzapackage as kuanzapackage


def main():
    parser = optparse.OptionParser()
    parser.add_option('--package', '-p', default='Default')
    parser.add_option('--inline', '-i', action='store_true', default=False)
    options, arguments = parser.parse_args()

    if len(arguments) == 0:
        print( 'Usage: kzcreate.py [-p <package>] <prototype> [<project name>] ')
        print( 'For a list of installed packages and their prototypes use kzlist tool')
        return

    if not kuanzapackage.KuanzaPackage.exists( options.package ):
        print( 'Package [%s] not found. Aborting.' % options.package)
        return

    package = kuanzapackage.KuanzaPackage.findByName( options.package )

    if not kuanzaproto.KuanzaProto.exists(package, arguments[0]) :
        print('Prototype [%s] of package [%s] cannot be found' % (arguments[0], package.getName() ) )
        return

    projectname = getProjectName(arguments)
    print("Creating project %s" % projectname)  

    if projectname == '':
        print("Project name cannot be empty")
        input()
        return

    prototype = kuanzaproto.KuanzaProto.findByPackageAndName( package, arguments[0] )
    projectVariables = [
        {'PROJECT_NAME' : projectname}
    ]

    
    prototype.extract( projectname, projectVariables, inline=options.inline )



def getProjectName(arguments):
    if len(arguments) == 1:
        print('No project name specified. Entering interactive mode')
        print("Enter the project name")
        return input()
    elif len(arguments) == 2:
        return arguments[1]
    else:
        print('More than one project name was passed. Aborting')
        exit(-1)



if __name__ == '__main__':
    main()