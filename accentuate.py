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
d_limiter = ";"

if len(sys.argv) > 1:
    #print("Arg!")
    try:
        input_filename = sys.argv[1]
    except IndexError:
        print("No arguments!")
        exit()
    try:
        sys.argv[2]
        try:
            os.path.getsize(sys.argv[2])
            print(f"Warning: {sys.argv[2]} exists!")
            print(f"Do you want to overwrite {sys.argv[2]}? (y/n)")
            if input() == "y":
                output_filename = sys.argv[2]
            else:
                exit()
        except FileNotFoundError:
            output_filename = sys.argv[2]
    except IndexError:
        print('No output filename provided, saving as "results.csv", which will overwrite that file if it exists. Continue? (y/n)')
        if input() == "y":
            pass
        else:
            exit()
    try:
        d_limiter = sys.argv[3]
        print(sys.argv[3])
    except IndexError:
        pass


def fixAllTheCells(input_filename, output_filename, d_limiter=","):
    with open(input_filename, "r", newline="") as inf, \
         open(output_filename, "w", newline="", encoding="utf-8") as outf:
        inreader = csv.reader(inf, delimiter=d_limiter)
        outwriter = csv.writer(outf, delimiter=d_limiter)
        for row in inreader:
            #print(row)
            newrow = []
            for cell in row:
                #print(cell)
                newcell = ftfy.fix_text(cell)
                newrow.append(newcell)
            outwriter.writerow(newrow)

if __name__ == "__main__":
    fixAllTheCells(input_filename, output_filename, d_limiter=";")
