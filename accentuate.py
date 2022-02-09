#!/usr/bin/python

"""
Take a CSV file, check if it is big enough yoink into memory (choosing a 
configurable value for how large that is), or planning to take it in chunks, 
scan it for which character set it is probably in, then convert to UTF8, 
then write it to a new CSV file where all of the data is UTF8, including 
any accented characters, curly quotes, or other weirdness.
"""

import os                   # For file inspection
import sys                  # For command-line arguments
import csv                  # For reading and writing CSV files
import charset_normalizer   # For converting encodings

input_filename = "test.csv"
output_filename = "results.csv"

input_file_size = os.path.getsize(input_filename)

print(input_file_size)

with open(input_filename, "rb") as inf, open(output_filename, "wb") as outf:
    rslts = charset_normalizer.from_fp(inf).best()
    print(rslts)

