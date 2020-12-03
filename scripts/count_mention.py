# This script is used to output the posts that mention "Trump" or "Biden" (case sensitive) in their titles into a tsv file while showing the count of candidate_mentioning posts

# The file to be read is a json file containing 1000 lines. Each line of the file is a dict of the format {"date": date, "post_info": {"approved_at_utc": ...}} 

# there will be two output files: one only contains candidate-mentioning posts, while the other contains all posts and is left for manual annotation 

import argparse as agp
import json

def main():
   
    parser = agp.ArgumentParser()
    parser.add_argument("rfile", help="the json file to be read")
    parser.add_argument("ofile1", help="output file (.tsv)")
    parser.add_argument("ofile2", help="output file (.tsv) containing all posts")

    args = parser.parse_args()

    rfile = open(args.rfile, "r")
    ofile1 = open(args.ofile1, "w+")
    ofile2 = open(args.ofile2, "w+")
    
    ofile1.write("Date \t Name \t Title \t Coding \n")
    ofile2.write("Date \t Name \t Title \t Coding \n")
    
    count = 0
    while True:
        line = rfile.readline()
        if not line:
            break

        read_in = json.loads(line)
        title = read_in["post_info"]["title"]
        output_str = f'{read_in["Date"]} \t {read_in["post_info"]["name"]} \t {title} \t'

        if "Trump" in title or "Biden" in title:
            ofile1.write(f'{output_str} \n')
            ofile2.write(f'{output_str} \n')
            count += 1
        else:
            ofile2.write(f'{output_str} Other \n')
   
    rfile.close()
    ofile1.close()
    ofile2.close()
    
    print(count)

if __name__ == "__main__":
    main()
