#!/usr/bin/python

"""
Take a CSV file, read it row by row and cell by cell. Convert each cell to
UTF8 with ftfy, and at the end of each row, write the converted row out to
a new file.
"""

import os     # For file inspection
import sys    # For command-line arguments
import csv    # For reading and writing CSV files
import ftfy   # For converting encodings

input_filename = "test.csv"
output_filename = "results.csv"

if len(sys.argv) > 1:
    #print("Arg!")
    if sys.argv[1]:
        input_filename = sys.argv[1]
    if sys.argv[2]:
        if os.path.getsize(sys.argv[2]) > 0:
            print(f"Warning: {sys.argv[2]} exists!")
            print(f"Do you want to overwrite {sys.argv[2]}? (y/n)")
            if input() != "y":
                exit()
        else:
            output_filename = sys.argv[2]
    #print(input_file_size)

def fixAllTheCells(input_filename, output_filename, d_limiter=","):
    with open(input_filename, "r", newline="") as inf, \
         open(output_filename, "w", newline="") as outf:
        inreader = csv.reader(inf, delimiter=d_limiter)
        outwriter = csv.writer(outf)
        for row in inreader:
            newrow = []
            for cell in row:
                #print(cell)
                newrow.append(ftfy.fix_text(cell))
            outwriter.writerow(newrow)

fixAllTheCells(input_filename, output_filename, d_limiter=";")
