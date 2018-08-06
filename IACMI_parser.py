#IACMI_parser.py

#Libraries
import pandas as pd
import numpy as np

directory = '/Users/malcolmdavidson/Documents/Code/ODI/IACMI/Shear_Rheology/25000_MW'
file = '5_wt%_25k_SS_20C.txt'
keyPhrase = "shear stress	shear rate	viscosity	time	normal stress	torque"

## import_rheology_to_df ##
# Version 1
# Import contents at filepath into a dataframe.
##
def import_rheology_to_df(file_path, data_start):

	return pd.read_csv(file_path, sep='\t', skiprows=data_start, encoding="iso-8859-1")



## build_filepath function ##
# Used to construct a file path from a file name and firectory
##
def build_filepath(directory_path, file_name):

   return str(directory_path + '/' + file_name)


## File I/O ##
# 1. Open file as file object
# 2. scan trhough line by line
#	a. remove newline
#	b. check for key_phrase
#		i. store line number
#	c. return object and number
##
def file_IO(file_path, key_phrase):

	with open(file_path, 'r', encoding="iso-8859-1") as f:

		lines = [line.rstrip('\n') for line in f]
		lines = filter(str.strip, lines)
		data_start = [num for (num, line) in enumerate(lines,0) if key_phrase in line]

	return lines, data_start


# Script #
#test(import_rheology_to_df(build_filepath(directory,file), start_of_data))
filePath = build_filepath(directory, file)
reducedData, startOfData = file_IO(filePath, keyPhrase)

df = import_rheology_to_df(filePath, startOfData[0])
print(df)
#test(df.shape)















