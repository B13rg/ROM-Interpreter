#!/usr/bin/python

import sys, getopt
import nescodes

def openfile(inputfile):
	data = bytearray()
	with open(inputfile, "rb") as f:
		byte = f.read(1)
		while byte:
			data.append(byte)
			byte = f.read(1)
	return data

def main(argv):
	inputfile = ''
	outputfile = ''
	gametype = ''
	try:
		opts, args = getopt.getopt(argv, "hi:o:t:", ["ifile=", "ofile=", "type="])
	except getopt.GetoptError:
		print("test.py -i <inputfile> -o <outputfile> -t <type>")
		sys.exit(2)
	for opt, arg in opts:
		if(opt == '-h'):
			print("test.py -i <inputfile> -o <outputfile> -t <type>")
			sys.exit(2)
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg
		elif opt in ("-t", "--type"):
			gametype = arg
	data = openfile(inputfile)
	#for c in data:
	#	print(hex(c))

if __name__ == "__main__":
	main(sys.argv[1:])
