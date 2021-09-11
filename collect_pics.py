import argparse
import requests
import json


def write_posts_to_file(posts, filename):
    # posts is list of json
    with open(filename, 'w') as outfile:
        for post in posts:
            outfile.write(json.dumps(post) + '\n')


def get_posts(sub_reddit_name):
    num_posts = 100
    # TODO: Error Handling
    try:
        data = requests.get(f'http://api.reddit.com/r/{sub_reddit_name}/top?limit={num_posts}',
                            headers={'User-Agent': 'macos:requests (by /u/Sense_Sen_sibility)'})
    except requests.exceptions:
        print("Request Fails.")
        exit(0)

    posts = data.json()['data']['children']
    # print(len(posts))
    # print(posts)

    return posts


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('sub_reddit')

    args = parser.parse_args()

    posts = get_posts(args.sub_reddit)

    pics_url = []
    for post in posts:
        url = post['data']['url_overridden_by_dest']
        pics_url.append(url)
    i = 1
    for url in pics_url:
        image = requests.get(url, allow_redirects=True)
        file = open(f'/Users/kevin/Desktop/pics/pic{i}', 'wb')
        file.write(image.content)
        file.close()
        i = i + 1
    # the following only applys to MacOS

    # write_posts_to_file(posts, '../data/sample1.json')
    # write_posts_to_file(posts, '../data/pics_test.json')


if __name__ == '__main__':
    main()
