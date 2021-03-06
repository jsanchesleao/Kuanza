import os, tempfile, shutil
import lib.binaryornot.check as binary

class Interpreter:

    def __init__(self, filename):
        self.filename = filename

    def interpret(self, context):
        if binary.is_binary( self.filename ):
            return

        fh, tempPath = tempfile.mkstemp()
        with open(self.filename) as oldFile:
            with open(tempPath, 'w') as newFile:
                for line in oldFile:
                    newFile.write( self.interpretVariables(line, context) )
        os.close(fh)
        shutil.move(tempPath, self.filename)

    def interpretVariables(self, line, context ):
        finalLine = line
        for variable in context:
            for old, new in variable.items():
                finalLine = finalLine.replace( '[[%' + old + ']]', new )
        return finalLine        
