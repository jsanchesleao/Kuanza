#!/usr/bin/env python

import re, sys, errno, os, tempfile

import optparse
from lib.interpreter import Interpreter
from lib.filewalker import FileWalker
from lib.kuanzaproto import KuanzaProto
import lib.protoservice as protoservice

def main():
    parser = optparse.OptionParser()
    parser.add_option('--package', '-p', default='Default')
    options, arguments = parser.parse_args()

    if len(arguments) == 0:
        print( 'Usage: kzcreate.py [-p <package>] <prototype> [<project name>] ')
        print( 'For a list of installed packages and their prototypes use kzlist tool')
        sys.exit(-1)

    if not protoservice.checkPrototypeIsInstalled( options.package, arguments[0] ):
        print('Prototype [%s] of package [%s] cannot be found' % (arguments[0], options.package) )
        sys.exit(-1)

    projectname = getProjectName(arguments)
    print("Creating project %s" % projectname)  
    if projectname == '':
        print("Project name cannot be empty")
        input()
        sys.exit(-1)

    copyProject( protoservice.findZipFileByPrototypeName(options.package, arguments[0]), projectname)

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



def copyProject(prototype, projectname):
    proto = KuanzaProto( prototype )
    proto.extract( projectname )



if __name__ == '__main__':
    main()