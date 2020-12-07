import pandas as pds
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_tsv')
    args = parser.parse_args()

    input_tsv = args.input_tsv
    df = pds.read_csv(input_tsv, '\t')
    df['Title'] = df['Title'].str.lower()
    # print(df)
    dfg_topic = df.groupby(['Coding'])
    df_general_engagement = df[(df['Coding'] != 'N')]
    # print(df_general_engagement)
    num_T_T = 0
    num_T_B = 0
    num_E_T = 0
    num_E_B = 0
    num_V_T = 0
    num_V_B = 0
    num_I_T = 0
    num_I_B = 0
    num_H_T = 0
    num_H_B = 0
    num_C_T = 0
    num_C_B = 0
    num_O_T = 0
    num_O_B = 0
    for index, post in df_general_engagement.iterrows():
        if post.Coding == 'T':
            # print(post.Title)
            if 'trump' in post.Title:
                num_T_T += 1
            elif 'biden' in post.Title:
                num_T_B += 1
        elif post.Coding == 'E':
            if 'trump' in post.Title:
                num_E_T += 1
            elif 'biden' in post.Title:
                num_E_B += 1
        elif post.Coding == 'V':
            if 'trump' in post.Title:
                num_V_T += 1
            elif 'biden' in post.Title:
                num_V_B += 1
        elif post.Coding == 'I':
            if 'trump' in post.Title:
                num_I_T += 1
            elif 'biden' in post.Title:
                num_I_B += 1
        elif post.Coding == 'H':
            if 'trump' in post.Title:
                num_H_T += 1
            elif 'biden' in post.Title:
                num_H_B += 1
        elif post.Coding == 'C':
            if 'trump' in post.Title:
                num_C_T += 1
            elif 'biden' in post.Title:
                num_C_B += 1
        elif post.Coding == 'O':
            if 'trump' in post.Title:
                num_O_T += 1
            elif 'biden' in post.Title:
                num_O_B += 1
    sum_T = num_H_T + num_T_T + num_O_T + num_V_T + num_C_T + num_E_T + num_I_T
    sum_B = num_H_B + num_T_B + num_O_B + num_V_B + num_C_B + num_E_B + num_I_B
    percentage_T_T = (100.0*num_T_T)/sum_T
    percentage_E_T = (100.0 * num_E_T) / sum_T
    percentage_V_T = (100.0 * num_V_T) / sum_T
    percentage_I_T = (100.0 * num_I_T) / sum_T
    percentage_H_T = (100.0 * num_H_T) / sum_T
    percentage_C_T = (100.0 * num_C_T) / sum_T
    percentage_O_T = 100.0-percentage_C_T-percentage_E_T-percentage_H_T-percentage_I_T-percentage_T_T-percentage_V_T

    percentage_T_B = (100.0 * num_T_B) / sum_B
    percentage_E_B = (100.0 * num_E_B) / sum_B
    percentage_V_B = (100.0 * num_V_B) / sum_B
    percentage_I_B = (100.0 * num_I_B) / sum_B
    percentage_H_B = (100.0 * num_H_B) / sum_B
    percentage_C_B = (100.0 * num_C_B) / sum_B
    percentage_O_B = 100.0-percentage_C_B-percentage_E_B-percentage_H_B-percentage_I_B-percentage_T_B-percentage_V_B

    print(f'T for Trump: {percentage_T_T}%')
    print(f'E for Trump: {percentage_E_T}%')
    print(f'V for Trump: {percentage_V_T}%')
    print(f'I for Trump: {percentage_I_T}%')
    print(f'H for Trump: {percentage_H_T}%')
    print(f'C for Trump: {percentage_C_T}%')
    print(f'O for Trump: {percentage_O_T}%')

    print(f'T for Biden: {percentage_T_B}%')
    print(f'E for Biden: {percentage_E_B}%')
    print(f'V for Biden: {percentage_V_B}%')
    print(f'I for Biden: {percentage_I_B}%')
    print(f'H for Biden: {percentage_H_B}%')
    print(f'C for Biden: {percentage_C_B}%')
    print(f'O for Biden: {percentage_O_B}%')


    """
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
    """


if __name__ == '__main__':
    main()
