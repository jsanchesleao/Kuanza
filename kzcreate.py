#!/usr/bin/env python

import re, sys, errno, os, tempfile

import optparse
from lib.interpreter import Interpreter
from lib.filewalker import FileWalker

import lib.kuanzaproto as kuanzaproto
import lib.kuanzapackage as kuanzapackage


def main():
    parser = optparse.OptionParser()
    parser.add_option('--package', '-p', default='Default')
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
    prototype.extract( projectname )

    projectVariables = [
        {'PROJECT_NAME' : projectname}
    ]

    FileWalker(projectname).each( lambda filename: Interpreter(filename).interpret(projectVariables) )



def getProjectName(arguments):
    if len(arguments) == 1:
        print('No project name specified with -n option. Entering interactive mode')
        print("Enter the project name")
        return input()
    elif len(arguments) == 2:
        return arguments[1]
    else:
        print('More than one project name was passed. Aborting')
        exit(-1)



if __name__ == '__main__':
    main()