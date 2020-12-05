# this script is used for the tfidf calculations in the three different levels: 

# (1) topic level which is required by the project description. That is, the result is a json file which displays 10 words with the highest tfidf score for each topic  

# (2) subreddit level. The result is a json file which displays 10 words with the highest tfidf score for each subbreddit

# (3) candidate-mentioning posts level. The result is a json file which displays 10 words with the highest tfidf score for the two categories "Trump-included" and "Biden-included" posts

# input file should be a tsv file that has been annotated 
# each "post" in the input file has five fields "Subreddit", "Date", "Name", "Title" and "Coding/Topic"

import argparse as agp 
import json 
import math
import pandas as pd
import re 
import matplotlib.pyplot as plt 


def who(title):
    if "Biden" in title and "Trump" in title:
        return "both"
    elif "Biden" in title:
        return "biden"
    elif "Trump" in title:
        return "trump"
    else:
        return "none"

def add(token, tokenset):
    if tokenset is None:    # weird 
        return {tokenset}
    if token in tokenset: 
        return tokenset
    else: 
        return tokenset.add(token)

def addTB(token, tokenset):
    if tokenset is None:    # weird 
        return {token}
    if token == "both":
        return {"biden", "trump"}
    elif token == "none":
        return tokenset
    elif token not in tokenset:
        return tokenset.add(token)
    return tokenset

def count(word, token, tokendict):

    if token in tokendict:
        if word in tokendict[token]:
            tokendict[token][word] += 1
            return
    else:
        tokendict[token] = {}
    tokendict[token][word] = 1 

def countTB(word, token, tokendict):
    
    if token == "both":
        countTB(word, "trump", tokendict)
        countTB(word, "biden", tokendict)
    else:
        count(word, token, tokendict)

def get_data(read_in, topic_count, subRD_count, TB_count):
    
    tt_words = 0
    word_dict = {}
    for i in range(len(read_in)):
        topic = read_in.loc[i, "Coding"]
        subreddit = read_in.loc[i, "Subreddit"]
        title = re.sub("\(\)\[\],-\.?'\"!~:;#&", " ", read_in.loc[i, "Title"])
        TB = who(title)

        words = (title.lower()).split(" ")
        for word in words: 
            if not word.isalpha():
                continue
            print(word)     # testing 
            tt_words += 1
            if word in word_dict:
                word_dict[word]["wc"] += 1
                word_dict[word]["subreddit"] = add(subreddit, word_dict[word]["subreddit"])
                word_dict[word]["topic"] = add(topic, word_dict[word]["topic"])
                word_dict[word]["TB"] = addTB(TB, word_dict[word]["TB"])
            else:
                word_dict[word] = {"wc" : 1, "subreddit":{subreddit}, "TB":set(), "topic":{topic}}
                word_dict[word]["TB"] = addTB(TB, word_dict[word]["TB"])
            count(word, topic, topic_count)
            count(word, subreddit, subRD_count)
            countTB(word, TB, TB_count)
    result = {"tt_words": tt_words, "word_dict": word_dict} 
    return result

def sort_by_value(tokendict):
    
    for token in tokendict:
        tokendict[token] = sorted(tokendict[token].items(), key = lambda x: x[1], reverse=True)
    return tokendict

def tfidf(count_dict, data, method):
    
    result = {}
    tokens = count_dict.keys()

    for token in tokens:
        words = {}
        for word in count_dict[token]:
            tfidf = 0
            freq = count_dict[token][word]
            if method == 1:     # topic
                if data["word_dict"][word]["topic"] is None:
                    continue
                tfidf = freq*(math.log( len(tokens)/len(data["word_dict"][word]["topic"])   ))
            else:   # subreddit or candidate_mentioning posts 
                tfidf = freq*(math.log( data["tt_words"]/data["word_dict"][word]["wc"]  ))
            words[word] = tfidf
        result[token] = words
    
    result = sort_by_value(result)
    return result 

def plotsGenerator(x_result, y_result):
    # the two inputs are of a dict type with keys like topics/subreddits/CMP posts
    plotTitles = {"C": "Corporations", "H": "Human Rights", "I": "International Relationships", "V": "COVID", "E": "Election Result", "T": "Transitions",
            "biden": "Biden", "trump": "Trump", "none": "None", "politic": "Politics", "conservative": "Conservative"}
    plt.rc('xtick', labelsize=8) 
    for token in x_result.keys():
        if token in plotTitles:
            fig = plt.figure()
            x = x_result[token]
            y = y_result[token]
            p = plt.bar(x[:10], y[:10])
            plt.xticks(rotation = 30, horizontalalignment='right')
            plt.title(f'{plotTitles[token]}')
            for i in range(len(y)):
                plt.annotate(str(y[i]), xy=(x[i], y[i]), ha="center", va="bottom", fontsize=8)
            plt.savefig(f'../plots/{str(plotTitles[token]) + ".png"}')
            plt.clf()

def extract_write(temp_result, ofile, stopwords):
    tokens = temp_result.keys()
    
    result ={}
    scores_result = {}
    for token in tokens:
        result[token] = []
        scores_result[token] = []

        num = 0
        i = 0
        while num < 20:         # extract 20 words 
            word = temp_result[token][i][0]
            score = temp_result[token][i][1]
            if word not in stopwords:
                result[token].append(word)
                scores_result[token].append(round(score, 3))
                num += 1
            i += 1

    plotsGenerator(result, scores_result)
    output_str = json.dumps(result, indent=4)
    ofile.write(output_str)
    ofile.close()
            
def main():
    print({"after"})  # testing 
    parser = agp.ArgumentParser()
    parser.add_argument("rfile", help="tsv file that has been annotated")
    parser.add_argument("ofile1", help="result on the topic level")
    parser.add_argument("ofile2", help="result on the subreddit level")
    parser.add_argument("ofile3", help="result on the candidate-mentioning posts level")
    parser.add_argument("stopwords",help="a document listing all the stop words")

    args = parser.parse_args()
    rfile = open(args.rfile, "r")
    read_in = pd.read_csv(rfile, sep='\t', header = 0)

    ofile_topic = open(args.ofile1, "w+")
    ofile_subRD = open(args.ofile2, "w+")
    ofile_TB = open(args.ofile3, "w+")
    
    stopwords = set(open(args.stopwords).read().split())
    
    topic_count = {}
    subRD_count = {}
    TB_count = {}
    
    data = get_data(read_in, topic_count, subRD_count, TB_count)
    # data is of the format :
    # {"tt_words": int, "word_dict": {
    #       "word1": { 
    #               "wc" : int, 
    #               "subreddit": {...}, 
    #               "TB": {...}, 
    #               "topic: {...}
    #               }, 
    #       "word2": {
    #                   ...
    #               }, 
    #           ...
    #                                }
    # }
    
    temp_result = tfidf(topic_count, data, 1)
    extract_write(temp_result, ofile_topic, stopwords)     # ofiles are closed in the method "extract_write"

    temp_result = tfidf(subRD_count, data, 2)
    extract_write(temp_result, ofile_subRD, stopwords)

    temp_result = tfidf(TB_count, data, 3)
    extract_write(temp_result, ofile_TB, stopwords)
    
    rfile.close()

if __name__ == "__main__":
    main()
