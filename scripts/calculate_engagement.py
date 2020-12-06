import pandas as pds
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_tsv')
    args = parser.parse_args()

    input_tsv = args.input_tsv
    df = pds.read_csv(input_tsv, '\t')
    # print(df)
    dfg_topic = df.groupby(['Coding'])
    for topic, posts in dfg_topic:
        print(f'The topic is: {topic}')
        num_posts_politics = 0
        num_posts_conservative = 0
        for index, post in posts.iterrows():
            if post['Subreddit'] == 'politics':
                num_posts_politics += 1
            else:
                num_posts_conservative += 1
        percentage_politics = round((100.0*num_posts_politics)/(num_posts_politics+num_posts_conservative), 3)
        percentage_conservative = round(100 - percentage_politics, 3)
        print(f'{percentage_politics}% of posts in the topic {topic} is from r/politics')
        print(f'{percentage_conservative}% of posts in the topic {topic} is from r/Conservative')


if __name__ == '__main__':
    main()
