import pyPdf
import optparse

from pyPdf import PdfFileReader
def printMeta(fileName):
	pdfFile = PdfFileReader(file(fileName, 'rb'))
	docinfo = pdfFile.getDocumentInfo()
	print '[*] pdf MetaData for: ' + str(fileName)
	for metaItem in docinfo:
		print '[*] ' + metaItem + ':' + docinfo[metaItem]

def main():
	parser = optparse.OptionParser('gunakan command ini "+\
		"-F <pdf file name>')
	parser.add_option('-F', dest='fileName', type='string',\
		help='specify pdf fileuser')
	(options, args) = parser.parse_args()

	fileName = options.fileName
	if fileName == None:
		print parser.usage
		exit(0)
	else:
		printMeta(fileName)

if __name__ == '__main__':
	main()