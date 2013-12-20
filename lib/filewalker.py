
import re, os

class FileWalker:

	def __init__(self, dirname):
		self.dirname = dirname

	def each( self, action ):
		for file in self.list():
			action(file)

	def list(self):
	    rootdir = self.dirname
	    for root, subFolders, files in os.walk(rootdir):
	        for file in files:
	            fullpath = os.path.join(root, file)
	            if not re.match(r'.*?node_modules.*', fullpath):
	                yield fullpath
