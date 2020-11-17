import json
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='the json file you want to read')
    args = parser.parse_args()

    if args.input_file is None:
        print('Input file is missing.')
        return
    names = []
    i = 1
    with open(args.input_file, 'r') as input:
        for line in input:
            if line is None:
                i += 1
                continue
            else:
                try:
                    names.append(json.loads(line)['data']['name'])
                    i += 1
                except json.JSONDecodeError:
                    print(f"invalid json at this line. index: {i}")
                    i += 1
                    continue
    if len(names) == len(set(names)):
        print("No duplicates! OK")
    else:
        print("duplicates exist!")
        print(len(names)-len(set(names)))


if __name__ == '__main__':
    main()
