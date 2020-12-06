import argparse
import pandas as pds
import warnings
import json


def topic_level_analysis(dfg_category, topic_json):
    print("topic analysis: ")
    print()
    for category, posts in dfg_category:
        posts['Title'] = posts['Title'].str.lower()
        # print(category)
        print(f'For: {category}')
        for word in topic_json.get(category):
            print()
            print('--------')
            print(f'For the word: \'{word}\' in topic: {category}')
            print()
            print('--------')
            for index, post in posts.iterrows():
                # print(post)
                if word in post['Title']:
                    print(post['Title'])
                    print(f'The post above is posted in {post.Subreddit}')
        print('-----------------------------------------------------------')



def subreddit_level_analysis(dfg_sub, subreddit_json):
    print("subreddit analysis: ")
    print()
    for subreddit, posts in dfg_sub:
        print(subreddit)
        posts['Title'] = posts['Title'].str.lower()

        print(f'For: {subreddit}')
        for word in subreddit_json.get(subreddit):
            print()
            print('--------')
            print(f'For the word: \'{word}\' in subreddit: {subreddit}')
            print()
            print('--------')
            for title in posts['Title']:
                if word in title:
                    print(title)
        print('-----------------------------------------------------------')
        # print(posts['Title'])


def main():
    warnings.filterwarnings('ignore')
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    args = parser.parse_args()
    input_file = args.input_file
    with open(input_file, 'r') as input_file:
        df = pds.read_csv(input_file, '\t')
        dfg_sub = df.groupby(['Subreddit'])
        dfg_category = df.groupby(['Coding'])

        subreddit_json = open('../data/subRD.json', 'r')
        subreddit_json = json.load(subreddit_json)

        # print(subreddit_json)
        subreddit_level_analysis(dfg_sub, subreddit_json)

        topic_json = open('../data/topic.json', 'r')
        topic_json = json.load(topic_json)
        # topic_level_analysis(dfg_category, topic_json)


if __name__ == '__main__':
    main()
