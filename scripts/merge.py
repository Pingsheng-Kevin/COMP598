# this scirpt is used to merge all the posts in two tsv files of the same format while pointing out that the source of each post (which subreddit generate the post)

import argparse as agp

def add_posts(rfile, ofile, subreddit):
    # the first line of the rfile has been read 

    while True:
        post = rfile.readline()
        if not post:
            break
        ofile.write(f"{subreddit} \t {post}")

def main():

    parser = agp.ArgumentParser()
    parser.add_argument("rfile1", help="a tsv file containing the posts from /r/politics")
    parser.add_argument("rfile2", help="a tsv file containing the posts from /r/conservative")
    parser.add_argument("ofile", help="a tsv file containing all the posts from rfile1 and rfile2")

    args = parser.parse_args()
    rfile1 = open(args.rfile1, "r")
    rfile2 = open(args.rfile2, "r")
    ofile = open(args.ofile, "w+")

    subreddits = {rfile1 : "politics", rfile2 : "conservative"}
    
    header = rfile1.readline()
    rfile2.readline()    # we don't need this line 

    ofile.write(f'Subreddit \t {header}')
    
    add_posts(rfile1, ofile, subreddits[rfile1])
    add_posts(rfile2, ofile, subreddits[rfile2])

    rfile1.close()
    rfile2.close()
        
if __name__ == "__main__":
    main()

