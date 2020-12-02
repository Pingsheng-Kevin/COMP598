import argparse
import json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file1')
    parser.add_argument('file2')
    args = parser.parse_args()
    file1 = args.file1
    file2 = args.file2
    titles_list = []
    # titles_set = {}
    with open(file1, 'r') as file1:
        for line in file1:
            post = json.loads(line)
            titles_list.append(post['data']['title'])
    with open(file2, 'r') as file2:
        for line in file2:
            post = json.loads(line)
            titles_list.append(post['data']['title'])
    duplicates = len(titles_list) - len(set(titles_list))
    print(f'# duplicates titles after merging two files: {duplicates} duplicates from {len(titles_list)} posts')
    print('Level of overlapping: ', round(1.0*duplicates/len(titles_list), 3))


if __name__ == '__main__':
    main()
