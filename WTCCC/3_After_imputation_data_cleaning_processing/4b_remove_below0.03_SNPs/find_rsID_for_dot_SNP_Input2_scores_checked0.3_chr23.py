#!/usr/bin/env python Daniel Ho

from itertools import cycle
#from sets import Set
#from wikipathways_api_client import WikipathwaysApiClient
import argparse,ast,bisect,configparser,csv,json,multiprocessing,os,pandas,re,requests,shutil,sqlite3,time
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

def load_table(infile, outfile ):
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
	outputfile = open(outfile, 'w')
	inputfile = open(infile, 'r')
	while True:
		input_line = inputfile.readline()
		input_line = input_line[:-1]
#		print ("1")
		if not input_line:
			break
		else:
			items = input_line.split('\t')
			if items[1].strip()  == "." :
				chr = items[0].strip()
				if chr == "23":
					chr = "X"
#				locus = int(items[3])
				locus = int(items[2])
				locus2 = locus - 1
#				print ("2")
#				print (chr)
#				print (locus)
				snp_index.execute("SELECT * FROM snps WHERE chr=? and locus=?",[chr,locus2])
				tag_snp = snp_index.fetchone()
#				print ("3")	
#				if tag_snp == None :
#					snp_index.execute("SELECT * FROM snps WHERE chr=? and locus=?",[chr,locus2])
#					tag_snp = snp_index.fetchone()
#				print ("3-a")		
				if tag_snp == None :
#					rsID = "chr" + chr + ":" + items[3]
					rsID = "chr" + chr + ":" + items[2]
				else:
					rsID = tag_snp[0]
			else:
				rsID = items[1].strip()
			
#			line = items[0] + "\t" + rsID + "\t" + items[2] + "\t" + items[3] + "\t" + items[4] + "\t" + items[5])
			line = items[0] + "\t" + rsID + "\t" + items[2] + "\t" + items[3] + "\t" + items[4] + "\t" + items[5] + "\t" + items[6] + "\t" + items[7] + "\t" + items[8]
#			print ("4")
			outputfile.write(line)
			outputfile.write('\n')
		



	inputfile.close()
	outputfile.close()
#	print "Read Items #: " + str(len(table.keys()))
	


	
	
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

load_table("WTCCCT1D_full_imputed_SNPs_below0.3.txt", "WTCCCT1D_full_imputed_SNPs_below0.3_rsID_chr23.txt")

print ("Finish !!")
#save_items("WTCCC_rsID_position_dbSNP_b151.txt",interlines)
#interlines = []





