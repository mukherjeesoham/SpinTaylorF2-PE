#======================================================================
# Soham M 3/2017
# Code to test and print output from STF2Fisher_SB_parallel.py
#======================================================================

import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Code to test Fisher Matrix computaion')
parser.add_argument('-file','--file', help='FileTag',required=True)
args = parser.parse_args()
file =  args.file

DATA = np.load("%s"%file)
print "SHAPE: ", DATA["FISHER_DET"].shape

count = 0
for slice in DATA["FISHER_DET"]:
	if not np.isnan(slice[3]):
		print slice	
		count = count + 1

print "DATA PTS: ", count