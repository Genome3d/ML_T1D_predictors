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
	snp_db = sqlite3.connect("/home/ubuntu/MyVolumeStore/dho760_project_raw/Daniel_CodeS3D/lib/snp_index_dbSNP_b151.db")
	snp_db.text_factory = str
	snp_index = snp_db.cursor()
	
	inputfile = open(datafile, 'r')
	while True:
		input_line = inputfile.readline()
		input_line = input_line[:-1]
		if not input_line:
			break
		else:
			items = input_line.split('\t')
			
			snp_index.execute("SELECT * FROM snps WHERE rsID=?",[items[0].strip()])
			tag_snp = snp_index.fetchone()
			if tag_snp == None :
				interlines.append(items[0] + "\t" + "Error")
			else:
				
				interlines.append(items[0] + "\t" + str(tag_snp[2] + 1))
			
		



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

interlines = load_table("WTCCC_rsID.txt")

print ("Write file !!")
save_items("WTCCC_rsID_position_dbSNP_b151.txt",interlines)
interlines = []





