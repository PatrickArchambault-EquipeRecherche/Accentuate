#!/usr/bin/python

"""
Take a CSV file, check if it is big enough yoink into memory (choosing a 
configurable value for how large that is), or planning to take it in chunks, 
scan it for which character set it is probably in, then convert to UTF8, 
then write it to a new CSV file where all of the data is UTF8, including 
any accented characters, curly quotes, or other weirdness.
"""

from distutils.dep_util import newer_group
import os                   # For file inspection
import sys                  # For command-line arguments
import csv                  # For reading and writing CSV files
import ftfy   # For converting encodings

input_filename = "test.csv"
output_filename = "results.csv"

input_file_size = os.path.getsize(input_filename)

print(input_file_size)

with open(input_filename, "r", newline="") as inf, \
     open(output_filename, "w", newline="") as outf:
    inreader = csv.reader(inf, delimiter=";")
    outwriter = csv.writer(outf)
    for row in inreader:
        newrow = []
        for cell in row:
            print(cell)
            newrow.append(ftfy.fix_text(cell))
        outwriter.writerow(newrow)


