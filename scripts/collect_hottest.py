import argparse
import requests
import json


def write_posts_to_file(posts, filename):
    # posts is list of json
    with open(filename, 'w') as outfile:
        for post in posts:
            if post is posts[-1]:
                outfile.write(json.dumps(post))
                break
            outfile.write(json.dumps(post) + '\n')


def get_posts(sub_reddit_name):
    num_posts = 100
    # after = "t3_jnn8bn"
    # TODO: Error Handling
    try:
        data = requests.get(f'http://api.reddit.com/r/{sub_reddit_name}/rising?limit={num_posts}',
                            headers={'User-Agent': 'macos:requests (by /u/Sense_Sen_sibility)'})
    except requests.exceptions:
        print("Request Fails.")
        exit(0)

    posts = data.json()['data']['children']
    """
    print(len(posts))
    print(posts)
    """
    return posts


def get_posts_after(sub_reddit_name, after_name):
    num_posts = 100
    after = after_name
    # TODO: Error Handling
    try:
        data = requests.get(f'http://api.reddit.com/r/{sub_reddit_name}/rising?limit={num_posts}&after={after}',
                            headers={'User-Agent': 'macos:requests (by /u/Sense_Sen_sibility)'})
    except requests.exceptions:
        print("Request Fails.")
        exit(0)

    posts = data.json()['data']['children']
    """
    print(len(posts))
    print(posts)
    """
    return posts


def main():
    parser = argparse.ArgumentParser()


    parser.add_argument('-o <output_file_path>', '--output_file', type=str,
                        help='where the cleaned JSON file you want to output to.')
    parser.add_argument('sub_reddit')

    args = parser.parse_args()
    all_posts = []
    for i in range(11):
        # print(i)
        if i == 0:
            posts = get_posts(args.sub_reddit)
            for post in posts:
                all_posts.append(post)
        else:
            posts = get_posts_after(args.sub_reddit, all_posts[-1]['data']['name'])
            for post in posts:
                all_posts.append(post)
    all_posts = all_posts[:1000]

    write_posts_to_file(all_posts, args.output_file)


if __name__ == '__main__':
    main()
