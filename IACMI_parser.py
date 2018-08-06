#IACMI_parser.py

# Version Notes #
# Version: 4.0
# Developmetn Goal: Smartly import each "chunk" of rheology
# data belonging to an individual rheology experiment into its own DF

# Libraries
import pandas as pd
import numpy as np


# Global Variables
DIRECTORY = '/Users/malcolmdavidson/Documents/Code/ODI/IACMI/Shear_Rheology/25000_MW'
FILE = '5_wt%_25k_SS_20C.txt'
KEYPHRASE = "shear stress	shear rate	viscosity	time	normal stress	torque"


## import_rheology_to_df ##
# Version 1
# Import contents at filepath into a dataframe.
##
def import_rheology_to_df(file_path, data_start, chunk_size):

	return pd.read_csv(file_path, sep='\t', skiprows=data_start, encoding="iso-8859-1",nrows=chunk_size)



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
		lines = list(filter(str.strip, lines))
		data_start = [num for (num, line) in enumerate(lines,0) if key_phrase in line]

	return lines, data_start


## calculate_chunk_size ##
# Determines number of rows to import for a single rheology experiment.
# 1. Calculate defference between enumerated_data[1] and enumerated_data[0]
# 2. Subtract the number of filler lines
# 3. Return chunk size for pd as int
##
def calculate_chunk_size(enumerated_data, filler):
	return enumerated_data[1]-enumerated_data[0]-filler




# Script #

filePath = build_filepath(DIRECTORY, FILE)
reducedData, startOfData = file_IO(filePath, KEYPHRASE)
chunkSize = calculate_chunk_size(startOfData,2)

df = import_rheology_to_df(filePath, startOfData[0], chunkSize)

print(chunkSize)
print(df)















