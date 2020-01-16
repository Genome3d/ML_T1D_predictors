#!/usr/bin/env python Daniel Ho

from itertools import cycle
#from sets import Set
#from wikipathways_api_client import WikipathwaysApiClient
import argparse,ast,bisect,configparser,csv,json,multiprocessing,os,pandas,pybedtools,re,requests,shutil,sqlite3,time
from operator import itemgetter

items = []
table = {}
interlines = []
intralines = []
col = []
PriGene = { }
Geneid = []
MaRfrid = { }
MaRCor = { }

def load_table(datafile):
	items = [ ]
	sitems = [ ]
	titems = [ ]
	fitems = [ ]
	f2items = [ ]
	PriGene = { }
	SNPid = {}
	MaRfrid = { }
	MaRCor = { }
	interlines = []
	count = 0
	SNPs = []
	
	inputfile = open(datafile, 'r')
	while True:
		input_line = inputfile.readline()
		input_line = input_line[:-1]
		if not input_line:
			break
		else:
			items = input_line.split('\t')
			
			
			if items[0].strip() not in SNPs :
				SNPs.append(items[0].strip())
			else:
				
				count += count
			
		



	inputfile.close()
#	print "Read Items #: " + str(len(table.keys()))
	return SNPs

def load_file(datafile, SNPs):
	items = [ ]
	sitems = [ ]
	titems = [ ]
	fitems = [ ]
	f2items = [ ]
	PriGene = { }
	SNPid = {}
	MaRfrid = { }
	MaRCor = { }
	interlines = []
	count = 0
	
	
	inputfile = open(datafile, 'r')
	while True:
		input_line = inputfile.readline()
		input_line = input_line[:-1]
		if not input_line:
			break
		else:
			items = input_line.split('\t')
			
			
			if items[0].strip() in SNPs :
				
				interlines.append(input_line)
			else:
				
				count += count
			
		



	inputfile.close()
#	print "Read Items #: " + str(len(table.keys()))
	return interlines
	
	
def save_items(newfile,lines):
	outputfile = open(newfile, 'w')
#	print "Output Items #: " + str(len(items))
#	lines.sort()
	for x in lines:
		outputfile.write(x)
		outputfile.write('\n')
	outputfile.close()
	

#file_name = raw_input("Input file name: ")





interlines = []

SNPs = load_table("SNPs_neg_strand_Affy500k.txt")
interlines = load_file("WTCCC_SNP_A_and_rsID_table.txt", SNPs)

print ("Write file !!")
save_items("SNPs_neg_strand_Affy500k_rsID.txt",interlines)





