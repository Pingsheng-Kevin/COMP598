# This script is used to randomly select 1000 posts from three json files which are obtained in three consecutive days 

# The output file is a json file. Each line of the file is a dict of the format {"date": date, "post_info": {"approved_at_utc": ...}}

# It is assumed that all the input files have more than 334 posts
import argparse as agp 
import random as rd 
import json 
import datetime as dt 

def list_posts(Rfile):
    
    posts_list = []
    while True:
        line = Rfile.readline()
        if not line:
            break
        posts_list.append(line)

    return posts_list


def sample_posts(Rfile, Wfile, num, date):
    
    # string list 
    posts_list = list_posts(Rfile)
    
    dummy = range(len(posts_list))
    # generate a random sample based on num 
    to_be_selected = rd.sample(dummy, num)

    for i in dummy:
        if i in to_be_selected:
            post_dict = json.loads(posts_list[i])
            post_info = post_dict["data"]
            output_dict = {"Date": date.strftime("%Y-%m-%d"), "post_info": post_info}
            output_str = json.dumps(output_dict)
            Wfile.write(f"{output_str}\n")

def main():
    
    parser = agp.ArgumentParser()
    parser.add_argument("rfile1", help="1st json file to be read (day 1)")
    parser.add_argument("rfile2", help="2nd json file to be read (day 2)")
    parser.add_argument("rfile3", help="3rd json file to be read (day 3)")
    parser.add_argument("day1", help="the date when the data in the rfile1 was collected (yyyy/mm/dd)")
    parser.add_argument("ofile", help="output file (.json)")

    args = parser.parse_args()
    rfile1 = open(args.rfile1, "r")
    rfile2 = open(args.rfile2, "r")
    rfile3 = open(args.rfile3, "r")
    ofile = open(args.ofile, "w+")
    try:
        day1 = dt.datetime.strptime(args.day1, "%Y/%m/%d")
    except:
        print("Enter day1 in the format of yyyy/mm/dd"
                
                )
    # determine where to select 334 posts (rfile1, rfile2 or rfile3)
    select = rd.randint(1, 3)
    file_list = [None, rfile1, rfile2, rfile3]

    for num in range(1,4):

        date = day1 + dt.timedelta(days=num-1)
        if num == select: 
            sample_posts(file_list[num], ofile, 334, date)
        else:
            sample_posts(file_list[num], ofile, 333, date)
    
    rfile1.close()
    rfile2.close()
    rfile3.close()



if __name__ == "__main__":
    main()

