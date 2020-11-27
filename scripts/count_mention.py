# This script is used to output the posts that mention "Trump" or "Biden" (case sensitive) in their titles into a tsv file while showing the count of candidate_mentioning posts

# The file to be read is a json file. Each line of the file is a dict of the format {"date": date, "post_info": {"approved_at_utc": ...}} 

import argparse as agp
import json

def main():
   
    parser = agp.ArgumentParser()
    parser.add_argument("rfile", help="the tsv file to be read")
    parser.add_argument("ofile", help="output file (.tsv)")

    args = parser.parse_args()

    rfile = open(args.rfile, "r")
    ofile = open(args.ofile, "w+")
    
    ofile.write("Date \t Name \t Title \t Coding \n")
    
    count = 0
    while True:
        line = rfile.readline()
        if not line:
            break

        read_in = json.loads(line)
        title = read_in["post_info"]["title"]
        if "Trump" in title or "Biden" in title:
            ofile.write(f'{read_in["Date"]} \t {read_in["post_info"]["name"]} \t {title}\t \n')
            count += 1
   
    rfile.close()
    ofile.close()
    
    print(count)

if __name__ == "__main__":
    main()
