import ATD
import argparse
def main(args=None):
	parser=argparse.ArgumentParser()
	parser.add_argument('textfile',help='filename of the text you want to check.')
	parser.add_argument('--key',help='Your unique API Key')
	args=parser.parse_args()
	fname=args.textfile
	key=args.key
	if key==None:
		ATD.setDefaultKey("your API key")
	else:
		ATD.setDefaultKey(key)
	f=open(fname,'r')
	text=f.read()
	errors = ATD.checkDocument(text)
	for error in errors:
		print "%s error for: %s **%s**" % (error.type, error.precontext, error.string)
		print "some suggestions: %s" % (", ".join(error.suggestions),)

if __name__=="__main__":
	main()