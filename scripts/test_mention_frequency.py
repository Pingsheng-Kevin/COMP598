# This scripts perform first round analysis to the existing data in order to determine which dataset is
# the most suitable one to analyze
import argparse
import os.path as osp
import json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='the input file to be analyzed')
    args = parser.parse_args()
    input_file = args.input_file
    print(f'Running first round analysis on the file {input_file}')
    if not osp.isabs(input_file):
        input_file = osp.abspath(input_file)
    with open(input_file, 'r') as input_file:
        print('Total # posts\tMention Trump\tMention Biden\tMention Both\tDensity\tDensity of Trump\tDensity of Biden\t'
              + 'Density Difference')
        line_num = 1
        trump_counts = 0
        biden_counts = 0
        mention_both = 0
        for line in input_file:
            post = json.loads(line)
            if 'Trump' in post['data']['title'] and 'Biden' in post['data']['title']:
                trump_counts += 1
                biden_counts += 1
                mention_both += 1
            elif 'Biden' in post['data']['title']:
                biden_counts += 1
            elif 'Trump' in post['data']['title']:
                trump_counts += 1
            # print(line_num, post['data']['title'])
            line_num += 1
        print(
              str(line_num) + '\t' +
              str(trump_counts) + '\t' +
              str(biden_counts) + '\t' +
              str(mention_both) + '\t' +
              str(round(1.0*(trump_counts+biden_counts-mention_both)/(1.0*line_num), 3)) + '\t' +
              str(round(1.0*trump_counts/(1.0*line_num), 3)) + '\t' +
              str(round(1.0*biden_counts/(1.0*line_num), 3)) + '\t' +
              str(round(round(1.0 * trump_counts / (1.0 * line_num), 3)-round(1.0*biden_counts/(1.0*line_num), 3), 3))
              )
        print()


if __name__ == '__main__':
    main()
