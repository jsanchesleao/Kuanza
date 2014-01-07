#!/usr/bin/env python

import os, optparse

import lib.kuanzaproto as kuanzaproto
import lib.kuanzapackage


def main():
    parser = optparse.OptionParser()
    parser.add_option('--package', '-p', default='Default')
    parser.add_option('--inline', '-i', action='store_true', default=False)
    options, arguments = parser.parse_args()

    if len(arguments) == 0:
        print( 'Usage: kzcreate.py [-p <package>] <prototype> [<project name>] ')
        print( 'For a list of installed packages and their prototypes use kzlist tool')
        return

    packagesData = getPackagesData()

    if not packageExists(options, packagesData):
        return

    if not prototypeExists(options.package, arguments[0], packagesData):
        return
    prototypePath = packagesData[ options.package ]['prototypes'][ arguments[0] ]
    prototype = kuanzaproto.KuanzaProto( prototypePath )
    

    projectname = getProjectName(arguments)    
    if projectname == '':
        print("Project name cannot be empty")
        return

    projectVariables = [
        {'PROJECT_NAME' : projectname}
    ]

    readVariables(prototype, projectVariables)

    doInit = False
    if prototype.getInit():
        print('This prototype uses an initialization script. This operation can be unsafe.')
        print("Should you allow it's execution? y/N")
        response = input()
        if response.upper() == 'Y':
            print('initialization allowed.')
            doInit = True
        else:
            print('initialization skipped')

    
    prototype.extract( projectname, projectVariables, inline=options.inline, doInit=doInit )

def getPackagesData():
    return lib.kuanzapackage.KuanzaPackage.getPackagesData()

def packageExists(options, packagesData):
    if options.package not in packagesData.keys():
        print( 'Package [%s] not found. Aborting.' % options.package)
        return False
    return True

def getPackage(options):
    return kuanzapackage.KuanzaPackage.findByName( options.package )

def prototypeExists(packageName, prototypeName, packagesData):
    if not prototypeName in packagesData[packageName]['prototypes'].keys():
        print('Prototype [%s] of package [%s] cannot be found' % (arguments[0],packageName ) )
        return False
    return True

def getPrototype(package, name):
    return kuanzaproto.KuanzaProto.findByPackageAndName( package, name )

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

def readVariables(prototype, projectVariables):
    for var in prototype.getVariables():
        print( 'Enter value: %s:' % var['desc'] )
        value = input()
        projectVariables.append( {  var['name'] : value } )



if __name__ == '__main__':
    main()