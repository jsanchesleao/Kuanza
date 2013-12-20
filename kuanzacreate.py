#!/usr/bin/env python

import re, sys, shutil, errno, os, tempfile

import optparse

def main():

    parser = optparse.OptionParser()
    parser.add_option('--prototype', '-p')
    parser.add_option('--name', '-n')
    options, arguments = parser.parse_args()

    if not options.prototype:
        print( 'Enter a prototype with -p <name>')
        print( 'For a list of installed prototypes use kuanzalist.py tool')
        sys.exit(-1)

    projectname = getProjectName(options)
    print("Creating project %s" % projectname)  
    if projectname == '':
        print("Project name cannot be empty")
        input()
        sys.exit(-1)
    copyProject(getPrototypePath(options.prototype), projectname)

    projectVariables = [
        {'PROJECT_NAME' : projectname}
    ]

    for file in listAllFiles( projectname ):
        replaceVars(file, projectVariables)

def getProjectName(options):
    if not options.name:
        print('No project name specified with -n option. Entering interactive mode')
        print("Enter the project name")
        return input()
    return options.name


def getPrototypePath(prototypeName):
    return os.path.join( os.environ['KUANZA_HOME'], 'prototypes', prototypeName )


def copyProject(prototype, projectname):
    shutil.copytree(prototype, projectname)

def listAllFiles(dirname):
    rootdir = dirname
    for root, subFolders, files in os.walk(rootdir):
        for file in files:
            fullpath = os.path.join(root, file)
            if not re.match(r'.*?node_modules.*', fullpath):
                yield fullpath
            

def replaceVars(filename, context):
    fh, tempPath = tempfile.mkstemp()
    with open(filename) as oldFile:
        with open(tempPath, 'w') as newFile:
            for line in oldFile:
                newFile.write( interpretVariables(line, context) )
    os.close(fh)
    shutil.move(tempPath, filename)

def interpretVariables( line, context ):
    finalLine = line
    for variable in context:
        for old, new in variable.items():
            finalLine = finalLine.replace( '[[%' + old + ']]', new )
    return finalLine        


if __name__ == '__main__':
    main()