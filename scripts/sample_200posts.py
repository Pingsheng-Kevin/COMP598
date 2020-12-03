# This script is used to randomly sample 200 candidate-mentioning posts from a tsv file
# Output file is also a tsv file 
# Assume that the input file has more than 201 lines (1 for the header) 

import argparse as agp
import random as rd 

def main():
    
    parser = agp.ArgumentParser()
    parser.add_argument("rfile", help="a tsv file to be read")
    parser.add_argument("ofile", help="output file (.tsv)")
    parser.add_argument("num", type=int, help="the number of lines in the rfile")

    args = parser.parse_args()
    rfile = open(args.rfile, "r")
    ofile = open(args.ofile, "w+")

    # randomly generate 200 different line numbers
    to_be_selected = rd.sample(range(1, args.num+1), 200)
    
    header = rfile.readline()
    ofile.write(header)

    line_num = 1
    while line_num <= args.num and line_num <= max(to_be_selected):
        
        line = rfile.readline()
        if line_num in to_be_selected:
            ofile.write(line)
        
        line_num += 1
    
    rfile.close()
    ofile.close()

if __name__ == "__main__":
    main()

