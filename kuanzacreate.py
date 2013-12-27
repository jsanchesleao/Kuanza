#!/usr/bin/env python

import re, sys, errno, os, tempfile

import optparse
from lib.interpreter import Interpreter
from lib.filewalker import FileWalker
from lib.kuanzaproto import KuanzaProto
import kuanzalist

def main():
    parser = optparse.OptionParser()
    parser.add_option('--prototype', '-p')
    parser.add_option('--name', '-n')
    options, arguments = parser.parse_args()

    if not options.prototype:
        print( 'Enter a prototype with -p <name>')
        print( 'For a list of installed prototypes use kuanzalist tool')
        sys.exit(-1)

    projectname = getProjectName(options)
    print("Creating project %s" % projectname)  
    if projectname == '':
        print("Project name cannot be empty")
        input()
        sys.exit(-1)
    copyProject(kuanzalist.getPrototypePath(options.prototype), projectname)

    projectVariables = [
        {'PROJECT_NAME' : projectname}
    ]

    FileWalker(projectname).each( lambda filename: Interpreter(filename).interpret(projectVariables) )



def getProjectName(options):
    if not options.name:
        print('No project name specified with -n option. Entering interactive mode')
        print("Enter the project name")
        return input()
    return options.name



def copyProject(prototype, projectname):
    proto = KuanzaProto( prototype )
    proto.extract( projectname )



if __name__ == '__main__':
    main()